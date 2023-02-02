# Poly Physical Phone Dialer for Sandbox environments
# Created by: Keith D'Atrio and Joe Smith
# January 2023 - Updated Feb 2023

import os
from dotenv import load_dotenv
import requests, time, random
import pandas as pd

# ********* Function Declarations **********

def polyPlaceCall(CalledNumber):  # function to place Call with phone number given
    headers = {
        "Content-Type": "application/json",
    }
    json_data = {"data": {"Dest": CalledNumber, "Line": 1, "Type": "TEL"}}
    response = requests.post(
        "https://" + Phone + "/api/v1/callctrl/dial",
        headers=headers,
        json=json_data,
        verify=False,
        auth=(PhoneUser, Password),
    )

def polyCheckCallStatus():  # function to check status of the call and get the responsse into JSON format
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.get(
        "https://" + Phone + "/api/v1/WebCallControl/callStatus",
        headers=headers,
        verify=False,
        auth=(PhoneUser, Password),
    )
    return response.json()

def polyEndCall(
    Handle,
):  # function to end call using Call Handle returned from CheckCallStatus() function
    headers = {
        "Content-Type": "application/json",
    }
    json_data = {"data": {"Ref": Handle}}
    response = requests.post(
        "https://" + Phone + "/api/v1/callctrl/endCall",
        headers=headers,
        json=json_data,
        verify=False,
        auth=(PhoneUser, Password),
    )
    print(response)

# ********** Main Code ***********
# Load Environmental Settings from .env file
load_dotenv()
# Create and load variables from Environment settings
PhoneUser = os.getenv("PHONEUSER")
Password = os.getenv("PASSWORD")
PhoneNumberList = pd.read_csv('data/PhoneNumberList.csv')

# Returns random number from dataframe
PhoneNumber = PhoneNumberList.sample()
print('Calling: ' & PhoneNumber)
polyPlaceCall(PhoneNumber)  # Send phone number to call
time.sleep(random.randint(10,60))
# Get JSON response and place in CallStatus variable
CallStatus = polyCheckCallStatus()
# Get Call Handle from JSON response to Call Status
CallHandle = CallStatus["data"]["CallHandle"]
print(CallHandle)  # Just to display something to screen to troubleshoot when broken
time.sleep(random.randint(5,30))
polyEndCall(CallHandle)  # End call using Call Handle returned above
