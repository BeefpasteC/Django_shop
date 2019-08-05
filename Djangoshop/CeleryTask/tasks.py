from __future__ import absolute_import
from Djangoshop.celery import app #在成功安装celery框架之后，django新生成的模块
import json
import requests
@app.task # 将taskExample 转换为一个任务
def taskExample():
    print('send email ok!')
    return 'send email ok!'

@app.task
def add(x=1,y=2):
    return x+y

@app.task
def dingTalk():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=ab6d36689780c02fc9b82a12b5e04f445e188379fcc569e8e460173b044a3432'

    headers = {
        "Content-Type": "application/json",
        "Chartset": "utf-8"
    }

    requests_data = {
        "msgtype": "text",
        "text": {
            "content": "未认证"
        },
        "at": {
            "atMobiles": [
            ],
        },
        "isAtAll": True
    }

    sendData = json.dumps(requests_data)
    response = requests.post(url, headers=headers, data=sendData)
    content = response.json()
    print(content)