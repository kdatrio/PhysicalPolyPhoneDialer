import os
from dotenv import load_dotenv
import requests
import pandas as pd


load_dotenv()
PhoneUser = os.getenv("PHONEUSER")
Password = os.getenv("PASSWORD")
Phone = os.getenv("PHONE")

headers = {
    "Content-Type": "application/json",
}

json_data = {
    "data": [
        "SCEP.enable",
    ],
}

response = requests.post(
    "https://" + Phone + "/api/v1/mgmt/config/get",
    headers=headers,
    json=json_data,
    verify=False,
    auth=(PhoneUser, Password),
)

print(response.text)
