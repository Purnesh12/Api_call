import requests

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "John Doe" ,
        "regNo": "REG12347" ,
        "email": "john@example.com"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        data = response.json()
        print("Webhook URL:", data.get('webhook'))
        print("Access Token:", data.get('accessToken'))
    except Exception as e:
        print("Error:", e)

generate_webhook()


