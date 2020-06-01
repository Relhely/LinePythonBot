from flask import Flask, request, abort
from flask_mqtt import Mqtt

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
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('WBjq5jKsza23Sj3SEzE5A9S316jvk9vweXs3Uh+DTWGAgxzuaxOa3xDvaDDWIFN4jmzy+K9n448dFOyz351sbKe8Y0wGuM+IFyHKR+uwOpJ3HW9R+yJH9P1mGTig4p0aOKY2CByJk/5/3PTlGqbdeQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fa6caf20fa1aadc77f8a11cad076b874')

def serach_temp_data():
    auth_json_path = 'mykey.json'
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
    gss_client = gspread.authorize(credentials)

    #開啟 Google Sheet 資料表
    spreadsheet_key = '1llgK0kQM7wWoAJ3DlR3l5adk-jiWT4z1u7RS-3PFuSw'
    sheet = gss_client.open_by_key(spreadsheet_key).sheet1
    data = sheet.acell('A2').value
    now = sheet.acell('C2').value
    qwe = "溫度 : " + data + " °C" + "\n\n" + "資料更新時間 : " + str(now)
    
    return qwe

def serach_humid_data():
    auth_json_path = 'mykey.json'
    gss_scopes = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
    gss_client = gspread.authorize(credentials)

    #開啟 Google Sheet 資料表
    spreadsheet_key = '1llgK0kQM7wWoAJ3DlR3l5adk-jiWT4z1u7RS-3PFuSw'
    sheet = gss_client.open_by_key(spreadsheet_key).sheet1
    data = sheet.acell('B2').value
    now = sheet.acell('C2').value
    qwe = "濕度 : " + data + " %" + "\n\n" + "資料更新時間 : " + str(now)
    return qwe

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
    if(text == "查詢溫度"):
        reply_text = serach_temp_data()
    elif(text == "查詢濕度"):
        reply_text = serach_humid_data()
    elif(text == "抽卡"):
        reply_text = serach_temp_data()
    else:
        reply_text = text
        
    
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)


uid = 'Uc791e422591cfd25826415ce497c0847'


                              
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 

                              
                              
