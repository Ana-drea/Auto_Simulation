import json

import requests

url = "https://test-projects.moravia.com/api/v5/TaskAmounts(-62710401)"

payload = json.dumps({
  "Id": 3720657
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 5c7ce072546a717d1033aba993d9b64e'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
