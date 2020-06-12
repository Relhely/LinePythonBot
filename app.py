from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import time
from datetime import datetime
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('9yN0HqYn6HPgvl4XOtlwRNsPqIiivFe4O20kr0cFL1iugM6VKMeG6SwW9IyUBBlsH7TxD0PSN4T0GlXQNCe1fjY7R4v6YLLloz41f/J5b7dzSil1T4GbmsqDXcqzRV3mcagl93XO7Leg4KpeahmBHgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('16f2a338df071ce0e57e8acfecc0e958')

relyID = 'U5050df24d1dde3fba385d42921f07cc8'

def wcat():
    gray = 0
    gold = 0
    ggold = 0
    win = 0
    for i in range(11):
        a = random.randint(0,999999)
        if (a<510000):
            gold = gold + 1
            
            if a < 100000 :
                if a < 28750:
                    win = win+1
                else:
                    ggold = ggold+1  
        else :
            gray = gray + 1
    return str(gold) + "金袍" + str(gray) + "銀袍"  + "\n" + "(" + str(win) + "限 " + str(ggold) + "選拔" + ")"    

def wcata():
    gray = 0
    gold = 0
    ggold = 0
    win = 0
    for i in range(11):
        a = random.randint(0,999999)
        if (a<800000):
            gold = gold + 1
            
            if a < 100000 :
                if a < 50000:
                    win = win+1
                else:
                    ggold = ggold+1  
        else :
            gray = gray + 1
    return str(gold) + "金袍" + str(gray) + "銀袍"  + "\n" + "(" + str(win) + "限 " + str(ggold) + "選拔" + ")"  


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
    text = event.message.text
    
    if(text == "!抽卡"):
        reply_text = wcat()
        if(event.source.user_id == relyID)
            reply_text = wcata()
    elif(text == "123test"):
        reply_text = event.source.user_id
    
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)
                              
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 

                              
                              
