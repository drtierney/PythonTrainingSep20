import requests
import getpass


instance = input("Enter instance: ")
name = input("Enter username: ")
pwd = getpass.getpass("Enter password: ")

url = 'https://{0}.service-now.com/api/now/table/incident?sysparm_query=state%3D1&sysparm_limit=1'.format(instance)

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
incident_no = data["result"][0]["number"]
description = data["result"][0]["description"]
sys_id = data["result"][0]["sys_id"]

print("---current request---\nIncident No: {0}\nSys_Id: {1}\nDescription: {2}".format(incident_no, sys_id, description))
work_note = r'{{"work_notes":"{0}"}}'.format(input("Please enter new work notes:\n"))
url = 'https://{0}.service-now.com/api/now/table/incident/{1}?sysparm_limit=1'.format(instance, sys_id)
response = requests.patch(url, auth=(user, pwd), headers=headers ,data=work_note)

if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

data = response.json()
print(data)
