import requests
import json

url = "http://nokiaai.apps.hztt-oe19-rcp-oe19-1301.dyn.nesc.nokia.net/"

def send_message(prompt, history, max_length=None, top_p=None, temperature=None):
    data = {
        "prompt": prompt,
        "history": history,
        "max_length": max_length,
        "top_p": top_p,
        "temperature": temperature
    }
    headers = {'Content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 示例用法
prompt = "给我讲个故事吧"
history = []
max_length = 8192
top_p = 0.7
temperature = 0.3

if __name__ == "__main__":
    response = send_message(prompt, history, max_length, top_p, temperature)
    if response:
        print("Response:", response["response"])
        print("Updated history:", response["history"])
    else:
        print("Failed to receive response")
