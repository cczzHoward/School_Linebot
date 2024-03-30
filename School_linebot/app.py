from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#import Google SHeet
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path='capable-droplet-273505-0ae8d5fe503e.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client=gspread.authorize(credentials)

app = Flask(__name__)


#LINE帳號要選擇Develop trial版本
# 輸入自己的LINE Channel Access Token
line_bot_api = LineBotApi('Cvhclk6pOu6oSUs2panPEv1XqWRPdcoMJg21vJvc0nBu0A7dF9gI2dJJaIYAx2ja+xdQbDxPSN3x4qtqRq5k0NxfNR9Bu2WAcb6Hz9GxnIiEn0zktOJ0HJw5g5pF3I14WF6aNKqgi1tFunf9zaxQCQdB04t89/1O/w1cDnyilFU=')
# 輸入自己的LINE Channel Secret
handler = WebhookHandler('e38ffab0e654ead2114e7410dfa25ae7')

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


#將其他額外功能寫在這，再呼叫此一函數，方便管理
def addfunction():
    a=1
    

    
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #event.message.text是使用者輸入的訊息
    

    
    """
    回復使用者訊息都在這
    
    """
    
    name=event.message.text
    userid = event.source.user_id
    name1=name.split(" ")
    #判斷userid 是否在google sheet上 
    'name = name.split(" ")'
    message = TextSendMessage("預設值")
    
    #開啟Google Sheet資料表
    spreadsheet_key='1QbkuWKrdDysEjZVHqQXxT-ndm7NtCCrHTPxWClavbIA'
    sheet1=gss_client.open_by_key(spreadsheet_key).worksheet('工作表1')
    sheet2=gss_client.open_by_key(spreadsheet_key).worksheet('工作表2')
    sheet3=gss_client.open_by_key(spreadsheet_key).worksheet('工作表3')
    #sheet2=gss_client.open_by_key(spreadsheet_key).sheet2
    
    rowtitle=sheet3.row_values(1)
    n=len(rowtitle)
    listtitle=["職位","傳送對象","傳送訊息","時間"]
    try:
        if name1[0] == "delete":
            j=1
            for i in sheet1.col_values(3) :
                if i == name1[1] :
                    useid=sheet1.cell(j,5).value
                    if userid == useid :
                        sheet1.delete_row(j)
                        message=TextSendMessage("刪除成功")
                        line_bot_api.reply_message(event.reply_token, message)
                j+=1
        elif name1[2] == "teacher":
            j=1
            tcid = event.source.user_id
            
            
            if name1[0] == "班長":
                for i in sheet1.col_values(4) :
                    if i == "班長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "副班長":
                for i in sheet1.col_values(4) :
                    if i == "副班長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "風紀股長":
                for i in sheet1.col_values(4) :
                    if i == "風紀股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "服務股長":
                for i in sheet1.col_values(4) :
                    if i == "服務股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "事務股長":
                for i in sheet1.col_values(4) :
                    if i == "事務股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "班代":
                for i in sheet1.col_values(4) :
                    if i == "班代":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "衛生股長":
                for i in sheet1.col_values(4) :
                    if i == "衛生股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "環保股長":
                for i in sheet1.col_values(4) :
                    if i == "環保股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "輔導股長":
                for i in sheet1.col_values(4) :
                    if i == "輔導股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "體育股長":
                for i in sheet1.col_values(4) :
                    if i == "體育股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
            
            
            if name1[0] == "實習股長":
                for i in sheet1.col_values(4) :
                    if i == "實習股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
                
                
            if name1[0] == "圖資股長":
                for i in sheet1.col_values(4) :
                    if i == "圖資股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)    
                
                
            if name1[0] == "合作股長":
                for i in sheet1.col_values(4) :
                    if i == "合作股長":
                        #message = TextSendMessage("傳送成功")
                        #line_bot_api.reply_message(event.reply_token, message)
                        usename=sheet1.cell(j,2).value
                        useid=sheet1.cell(j,5).value
                        if n==0:
                            sheet3.append_row(listtitle)
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                        else:
                            tcdata=[name1[0],usename,name1[1],str(datetime.datetime.now())]
                            sheet3.append_row(tcdata)
                            message = TextSendMessage(name1[1])
                            
                        line_bot_api.push_message(useid, message)
                    
                    j += 1 
                
                message=TextSendMessage(str(name1[1]) + "--訊息傳送成功")
                line_bot_api.reply_message(event.reply_token, message)
                
                
            else:
                message=TextSendMessage("傳送失敗")
                line_bot_api.reply_message(event.reply_token, message)
    
    #delete (要刪的學號)
        
                
        elif name1[4] == "student":
            
            rowtitle=[]
            rowtitle=sheet1.row_values(1)
            listtitle=["班級","姓名","學號","職位","使用者id"]
            n=len(rowtitle)
            test=False    
                
            for i in sheet2.col_values(1):
                    if i==name1[2]:
                        if n==0:
                            sheet1.append_row(listtitle)
                            stdata=[name1[0],name1[1],name1[2],name1[3],userid]
                            sheet1.append_row(stdata)
                            message=TextSendMessage("註冊完畢")
                            break
                        else:
                            for j in sheet1.col_values(5):
                                if j==userid:
                                    test=True
                                    break
                                else:
                                    test=False
                            if test:
                                message=TextSendMessage("已經註冊")
                                test=False
                                break
                            else:
                                stdata=[name1[0],name1[1],name1[2],name1[3],userid]
                                sheet1.append_row(stdata)
                                message=TextSendMessage("註冊完畢") 
                                break
                    else:
                        message=TextSendMessage("註冊失敗")
                        test=False
                           #裡面是學生端
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message=TextSendMessage("格式錯誤")
            line_bot_api.reply_message(event.reply_token, message)
    except:
        message=TextSendMessage("格式錯誤")
        line_bot_api.reply_message(event.reply_token, message)
    '''
    #message = TextSendMessage(text="請輸入正確格式，(班級)，(空白)")    
    '''
    
    '''
    #自動回覆訊息就用這個
    line_bot_api.reply_message(event.reply_token, message)
    '''
    
    '''
    line_bot_api.reply_message(event.reply_token, message)
    #主動回覆訊息是這個
    line_bot_api.push_message("U836eb76fcc80d1caddcee1e33551a94f", message)
    #line_bot_api.push_message(push_token, message)
    '''
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
