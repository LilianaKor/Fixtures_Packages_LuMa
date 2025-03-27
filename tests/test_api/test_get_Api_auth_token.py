import requests

url = "https://magento.softwaretestingboard.com/rest/V1/integration/customer/token"
payload = {
    "email": "Kcoco@gmail.com",  # Use your Magento account email
    "password": "Passwo1!"            # Use your Magento account password
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    token = response.text.strip('"')  # The API returns the token inside double quotes
    print(f"Access Token: {token}")
else:
    print(f"Failed to get token: {response.status_code}, {response.text}")
