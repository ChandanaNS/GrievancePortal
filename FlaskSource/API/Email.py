from flask import render_template, session, request, redirect, Blueprint, flash
from FlaskSource.Model.GrievanceBrief import GrievanceBrief
from FlaskSource.Model.UserDetails import UserDetails
from Database import DBQuery
import json
import ast
from datetime import date
# technojigsprojects@gmail.com
import smtplib,ssl
sender_email = "OGMS.college@gmail.com"
receiver_email = "chandana2594@gmail.com"
message = """\
        Subject: Hi there

        This message is sent from Python."""

# Send email here
print(1)
port = 465  # For SSL
password = "ogms@1234"
print(2)
# Create a secure SSL context
context = ssl.create_default_context()
print(3)
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("OGMS.college@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
