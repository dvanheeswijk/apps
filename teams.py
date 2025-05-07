import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import pymsteams
import asyncio
import requests
import httpx

load_dotenv()

TEAMS_URL = os.getenv("TEAMS_URL")

def send_alert_to_teams(message, webhook_url):
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  # Instantiate the connector card object
  # teams_message = pymsteams.connectorcard(webhook_url)
  # the async_connectorcard object is used instead of the normal one.
  teams_message = pymsteams.async_connectorcard(webhook_url)
  # Set the text of the message
  teams_message.text(message)
  # Publish the message to the MS Teams channel
  loop.run_until_complete(teams_message.send())

st.write("""
#Test
New Message.
""")


send_alert_to_teams(st, TEAMS_URL)


print("Done!")
