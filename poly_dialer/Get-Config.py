import os
from dotenv import load_dotenv
import requests
import pandas as pd


load_dotenv()
PhoneUser = os.getenv("PHONEUSER")
Password = os.getenv("PASSWORD")
# Getting this from .csv file now
# Phone = os.getenv("PHONE") 

def GetPhoneConfig(PhoneIPs):
    headers = {
        "Content-Type": "application/json",
    }
    json_data = {
        "data": [
            "SCEP.enable",
        ],
    }
    response = requests.post(
        "https://" + PhoneIPs + "/api/v1/mgmt/config/get",
        headers=headers,
        json=json_data,
        verify=False,
        auth=(PhoneUser, Password),
    )
    return response

PhoneList = pd.read_csv('data/PhoneList.csv')
print(PhoneList)
for index, rows in PhoneList.iterrows():
    print('IP Address is ' + rows['phoneIP'] + ' the type of phone is ' + rows['phoneType'])
# APIResponse = GetPhoneConfig(PhoneIP)
# print(response.text)
