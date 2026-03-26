import sqlite3
import bcrypt

def connect():
    return sqlite3.connect("users.db",check_same_thread=False)

def create_tables():

    conn=connect()
    c=conn.cursor()

    c.execute("""

    CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    mobile TEXT,
    password TEXT

    )

    """)

    c.execute("""

    CREATE TABLE IF NOT EXISTS predictions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    disease TEXT,
    risk INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

create_tables()

def add_user(name,email,mobile,password):

    conn=connect()
    c=conn.cursor()

    hashed=bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
    )

    c.execute("""

    INSERT INTO users
    (name,email,mobile,password)

    VALUES(?,?,?,?)

    """,(name,email,mobile,hashed))

    conn.commit()

def login_user(email,password):

    conn=connect()
    c=conn.cursor()

    c.execute(
    "SELECT * FROM users WHERE email=?",
    (email,)
    )

    user=c.fetchone()

    if user:

        if bcrypt.checkpw(
        password.encode(),
        user[4]
        ):
            return user

    return None

def add_prediction(user,disease,risk):

    conn=connect()
    c=conn.cursor()

    c.execute("""

    INSERT INTO predictions
    (user_id,disease,risk)

    VALUES(?,?,?)

    """,(user,disease,risk))

    conn.commit()

def get_history(user):

    conn=connect()
    c=conn.cursor()

    c.execute("""

    SELECT disease,risk,date
    FROM predictions

    WHERE user_id=?

    ORDER BY id DESC

    """,(user,))

    return c.fetchall()