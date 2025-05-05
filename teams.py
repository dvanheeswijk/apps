pip install dotenv

import streamlit
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

TEAMS_URL = os.getenv("TEAMS_URL")

print("Hello, world!")
