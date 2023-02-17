import streamlit as st
from sendEmail import sendEmail
import re

# Regular expression for general email syntax
regex = re.compile(r'([A-Za-z0-9]+[.-_-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

st.title('Contact Me', anchor='center')

with st.form(key='emailForm'):
    userEmail = st.text_input('Your email address', key='userEmail')
    message = st.text_area('Your message')
    button = st.form_submit_button()
    if button:
        if message == '':
            st.info("Please enter a message")
            print('Empty message')
        elif re.fullmatch(regex, userEmail):  # email address has correct syntax
            message = f"""Subject: New email from {userEmail}

From: {userEmail}
{message
            }"""
            sendEmail(message=message)
            st.info("Your message was sent")

        else:
            st.info("Please enter a valid email address")
