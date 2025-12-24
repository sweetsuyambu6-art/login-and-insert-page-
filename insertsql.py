
import mysql.connector
import streamlit as st
import pandas as pd 
import mysql.connector
import datetime

st.sidebar.title('Navigation')
selection = st.sidebar.radio('Go to', ['Insert', 'Team Support']) 
if selection == "Insert":
#sql connection
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='8898969858',
        database="sb25",
    autocommit=True)
    mycursor = mydb.cursor()

st.title("Insert Form")

# Create the form
form = st.form(key='Insert_form')
# Input fields
client_email = form.text_input("Email")
client_mobile = form.text_input("Phone Number")
query_heading = form.text_input("Query Heading")
query_description = form.text_input("Query Description")
# Form submit button
submit_button = form.form_submit_button(label='submission')
# If the form is submitted
if submit_button:
    # Create a dictionary with the form data
    form_data = {
        'client_email': client_email,
        'client_mobile':client_mobile,
        'query_heading':query_heading,
        'query_description':query_description,
        
    }
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([form_data])
    
    # Display a success message
    st.success("Registration Successful!")
    
    # Display the form data as a table
    st.write("Here are your details:")
    st.table(df)
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='8898969858',
        database="sb25",
    autocommit=True)
    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists synthetic_client_queries (email varchar(50), client_mobile int(15), query_heading varchar(100), query_description varchar(500))")
    insert_query = """
    INSERT INTO synthetic_client_queries (client_email, client_mobile, query_heading, query_description)
    VALUES (%s, %s, %s, %s)

    """
    
    data = (client_email,client_mobile,query_heading,query_description)
    mycursor=mydb.cursor()
    mycursor.execute(insert_query,data)

    sql="select * from synthetic_client_queries "
    sql="ALTER table synthetic_client_queries ADD COLUMN query_closed varchar(20)not null default 'N/A'"
    st.success('Data inserted to sql')
    sql = "select * from synthetic_client_queries order by client_mobile desc limit 5"
    mycursor.execute(sql)
    st.table(data)
    import streamlit as st
    current_datetime = datetime.datetime.now()
    st.write("### Current Date and Time")
# Display the datetime object
    st.write(f"The current date and time is: **{current_datetime}**")
# Display a formatted string (e.g., "Dec 23, 2025, 05:48 AM")
    formatted_datetime = current_datetime.strftime("%b %d, %Y, %I:%M %p")
    st.markdown(f"Formatted time: `{formatted_datetime}`")

#team support
if selection == "Team Support":
    st.title("Team Support Form")

    selection = st.selectbox("Select Filter  ",["Opened Queries","Closed Queries"])
    
    if selection == "Opened Queries":
            import mysql.connector
            mydb= mysql.connector.connect(
            host='localhost',
            user='root',
            password='8898969858',
            database="sb25",
            autocommit=True)
            mycursor = mydb.cursor()

            sql = "SELECT * FROM synthetic_client_queries WHERE status = 'Opened'"
            mycursor.execute(sql)
            st.table(mycursor.fetchall())

    #colse query

    elif st.selectbox == "Closed Queries":
        import mysql.connector
        mydb= mysql.connector.connect(
        host='localhost',
        user='root',
        password='8898969858',
        database="sb25",
        autocommit=True)
        mycursor = mydb.cursor()
        sql = "SELECT * FROM synthetic_client_queries WHERE status = 'Closed'"
        mycursor.execute(sql)
        st.table(mycursor.fetchall())
