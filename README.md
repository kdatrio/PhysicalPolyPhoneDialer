---

****\***** Poly Physical Phone Dialer ****\*****
****\***** Written: Keith D'Atrio ****\*****
****\***** and Joe Smith ****\*****

---

Requirements (tested versions):

- Python 3.9 (tested)
- python-dotenv==0.21.1
- requests==2.28.2
- urllib3==1.26.14

Setup:

- Create a .env file in the root of the project
- Example:
  PHONEUSER=<Username Admin level>
  PASSWORD=<Phone Admin password>
  PHONE=<Phone IP Address>
- Update phone number in line 58 string

Usage:

- python Put-Dial.py
- No arguments for version 1
- script will send REST API call to dial phone number in function call
- wait 10 seconds
- check CallStatus and retrieve CallHandle
- wait 3 seconds
- Push End Call Rest API
- end script
