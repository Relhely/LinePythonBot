from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('WBjq5jKsza23Sj3SEzE5A9S316jvk9vweXs3Uh+DTWGAgxzuaxOa3xDvaDDWIFN4jmzy+K9n448dFOyz351sbKe8Y0wGuM+IFyHKR+uwOpJ3HW9R+yJH9P1mGTig4p0aOKY2CByJk/5/3PTlGqbdeQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fa6caf20fa1aadc77f8a11cad076b874')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
mqtt_broker = "broker.mqtt-dashboard.com"
mqtt_port = 1883
keepalive=60

uid = 'Uc791e422591cfd25826415ce497c0847'
topic = "esp32/te/python"

def on_connect(client,data,flags,rc):
    client.subscribe(topic)

def on_message(client,data,msg):
    line_bot_api.push_message(uid,TextSendMessage(text=str(msg.payload)))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker,mqtt_port,keepalive)

client.loop_forever()   
