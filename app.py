from flask import Flask, request, abort
from flask_mqtt import Mqtt

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
    asd = event.message.text
    if(asd == "/查詢"):
        
    
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


uid = 'Uc791e422591cfd25826415ce497c0847'


                              
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 

                              
                              
