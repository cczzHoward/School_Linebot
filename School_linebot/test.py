# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:11:12 2020

@author: 01
"""


import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
auth_json_path='capable-droplet-273505-0ae8d5fe503e.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client=gspread.authorize(credentials)

name="實習股長 張摘凱 哈囉你好 teacher"
userid = 135646646
name1=name.split(" ")
    #判斷userid 是否在google sheet上   

message = "預設"
    
    #開啟Google Sheet資料表
spreadsheet_key='1QbkuWKrdDysEjZVHqQXxT-ndm7NtCCrHTPxWClavbIA'
sheet1=gss_client.open_by_key(spreadsheet_key).sheet1
sheet2=gss_client.open_by_key(spreadsheet_key).worksheet('工作表2')
sheet3=gss_client.open_by_key(spreadsheet_key).worksheet('工作表3')
'''
rowtitle=[]
rowtitle=sheet.row_values(1)
listtitle=["班級","姓名","學號","職位","userid"]
        #Google Sheet資料表
        #sheet.clear()
n=len(rowtitle)
print(len(rowtitle))
if n==0:
    sheet.append_row(listtitle)
    stdata=[name1[0],name1[1],name1[2],name1[3],userid]
    sheet.append_row(stdata)

'''
rowtitle=sheet3.row_values(1)
n=len(rowtitle)
listtitle=["職位","傳送對象","傳送訊息","時間"]
if name1[3] == "teacher":
        j=2
        if name1[0] == "實習股長":
            for i in sheet1.col_values(4) :
                if i == "實習股長":
                    useid=sheet1.cell(j,5).value
                    if n==0:
                        sheet3.append_row(listtitle)
                        tcdata=[name1[0],name1[1],name1[2],str(datetime.datetime.now())]
                        sheet3.append_row(tcdata)
                        message = name1[2]
                    else:
                        tcdata=[name1[0],name1[1],name1[2],str(datetime.datetime.now())]
                        sheet3.append_row(tcdata)
                        message = name1[2]
                    
                    print(message)
                
                j += 1 