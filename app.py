import streamlit as st
import database
import model
import pandas as pd
import plotly.express as px
import report
if "start" not in st.session_state:
    st.session_state.start=False


# your existing code continues
st.set_page_config(
page_title="AI Health Predictor",
layout="wide"
)
st.set_page_config(
page_title="AI Health Predictor",
layout="wide"
)

# SESSION
if "user" not in st.session_state:
    st.session_state.user=None

# SIDEBAR
st.sidebar.title("AI Health System")

theme=st.sidebar.radio(
"Theme",
["Dark","Light"]
)

# DARK MODE
if theme=="Dark":

    st.markdown("""

    <style>

    .stApp{
    background:linear-gradient(135deg,#141e30,#243b55);
    color:white;
    }

    label{
    color:white !important;
    font-weight:bold;
    }

    .stTextInput input{
    background:#1f2c3d;
    color:white;
    }

    </style>

    """,unsafe_allow_html=True)

# LIGHT MODE
else:

    st.markdown("""

    <style>

    .stApp{
    background:#f5f7fb;
    color:black;
    }

    label{
    color:black !important;
    font-weight:bold;
    }

    .stTextInput input{
    background:white;
    color:black;
    }

    </style>

    """,unsafe_allow_html=True)

# MENU
if st.session_state.user:

    page=st.sidebar.selectbox(

    "Menu",

    ["Prediction","Profile","History","Logout"]

    )

else:

    page=st.sidebar.selectbox(

    "Menu",

    ["Login","Signup"]

    )

# LOGIN
if page=="Login":

    st.title("Login")

    email=st.text_input("Email")

    password=st.text_input(
    "Password",
    type="password"
    )

    if st.button("Login"):

        user=database.login_user(
        email,
        password
        )

        if user:

            st.session_state.user=user

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Credentials")

# SIGNUP
if page=="Signup":

    st.title("Create Account")

    name=st.text_input("Full Name")

    email=st.text_input("Email Address")

    mobile=st.text_input("Mobile Number")

    password=st.text_input(
    "Password",
    type="password"
    )

    if st.button("Create Account"):

        success=database.add_user(

        name,
        email,
        mobile,
        password

        )

        if success:

            st.success("Account Created")

        else:

            st.error("Email already exists")

# PROFILE
if page=="Profile":

    st.title("User Profile")

    st.write("Name :",st.session_state.user[1])

    st.write("Email :",st.session_state.user[2])

    st.write("Mobile :",st.session_state.user[3])

# PREDICTION
if page=="Prediction":

    st.title("AI Health Prediction")

    disease=st.selectbox(

    "Select Disease",

    ["Diabetes","Heart Disease"]

    )

    col1,col2=st.columns(2)

    with col1:

        age=st.number_input(
        "Age",
        10,
        100
        )

        gender=st.radio(

        "Gender",

        ["Male","Female"]

        )

        weight_unit=st.selectbox(

        "Weight Unit",

        ["kg","lbs"]

        )

        weight=st.number_input(

        "Weight",

        30,
        200

        )

        if weight_unit=="lbs":

            weight=weight*0.453

        height=st.number_input(

        "Height (cm)",

        120,
        220

        )

        bmi=weight/((height/100)**2)

        st.write("BMI :",round(bmi,2))

    with col2:

        glucose=st.number_input(

        "Glucose Level",

        50,
        300

        )

        bp=st.number_input(

        "Blood Pressure",

        60,
        200

        )

        cholesterol=st.number_input(

        "Cholesterol",

        100,
        400

        )

        pregnancies=st.number_input(

        "Pregnancies (0 if male)",

        0,
        10

        )

    if st.button("Predict Risk"):

        if disease=="Diabetes":

            risk=model.predict_diabetes(

            pregnancies,
            glucose,
            bp,
            bmi,
            age

            )

        else:

            risk=model.predict_heart(

            age,
            cholesterol,
            bp,
            bmi

            )

        st.metric(
        "Risk Percentage",
        str(risk)+"%"
        )

        if risk>50:

            result="High Risk"

            st.error(result)

        else:

            result="Low Risk"

            st.success(result)

        database.add_prediction(

        st.session_state.user[0],

        disease,

        risk

        )

        if st.button("Generate Report"):

            report.create_report(

            st.session_state.user[1],

            disease,

            result,

            risk

            )

            st.success("Report Generated")

# HISTORY
if page=="History":

    st.title("Prediction History")

    data=database.get_history(

    st.session_state.user[0]

    )

    if data:

        df=pd.DataFrame(

        data,

        columns=[

        "Disease",
        "Risk %",
        "Date"

        ]

        )

        st.dataframe(df)

        fig=px.line(

        df,

        x="Date",

        y="Risk %",

        color="Disease",

        markers=True

        )

        st.plotly_chart(fig)

    else:

        st.info("No history found")

# LOGOUT
if page=="Logout":

    st.session_state.user=None

    st.rerun()