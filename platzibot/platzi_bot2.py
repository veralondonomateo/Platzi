import requests

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=64e96ae8273e0c190d8e4364&org=0d38ddcc-a1ff-4d38-b2a5-f815f0fc527d"
headers = {'Authorization':
			 'Bearer XXXXXXXXXXXXX',
			 'Content-Type': 'application/json'
		}

def query(payload):
 response = requests.post(API_URL, headers=headers, json=payload)
 return response.json()

output = query({"in-0": """Cual es el mejor curso para aprender python?
"""})
print(output)