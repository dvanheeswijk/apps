import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import pymsteams
import requests

load_dotenv()

TEAMS_URL = os.getenv("TEAMS_URL")

def send_alert_to_teams(message, webhook_url):
  # Instantiate the connector card object
  teams_message = pymsteams.connectorcard(webhook_url)
  # Set the text of the message
  teams_message.text(message)
  # Publish the message to the MS Teams channel
  teams_message.send()
  return 0

# message = st.write('''
# #Test
# This is testing the streamlit webhook using a url in github secrets.
# ''')

message = "This is a test of streamlit with webhook."

i = 0
if i<1:
  send_alert_to_teams(message, TEAMS_URL)
  i=i+1

print(message)
