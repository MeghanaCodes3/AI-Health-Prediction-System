import streamlit as st
import database
import pandas as pd

def admin_panel():

    st.title("Admin Dashboard")

    users=database.get_all_users()

    df=pd.DataFrame(

    users,

    columns=["ID","Name","Email"]

    )

    st.subheader("Users")

    st.dataframe(df)

    pred=database.get_all_predictions()

    df2=pd.DataFrame(

    pred,

    columns=[

    "ID",

    "User",

    "Disease",

    "Risk",

    "Date"

    ]

    )

    st.subheader("Predictions")

    st.dataframe(df2)