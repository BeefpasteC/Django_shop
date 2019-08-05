import json
import requests

url = 'https://oapi.dingtalk.com/robot/send?access_token=ab6d36689780c02fc9b82a12b5e04f445e188379fcc569e8e460173b044a3432'

headers = {
    "Content-Type": "application/json",
    "Chartset": "utf-8"
}

requests_data = {
    "msgtype": "text",
    "text":{
        "content": "未认证"
    },
    "at":{
        "atMobiles":[
        ],
    },
    "isAtAll": True
}

sendData = json.dumps(requests_data)
response = requests.post(url,headers = headers,data=sendData)
content = response.json()
print(content)