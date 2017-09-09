# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:22:26 2017

@author: 滕磊
"""

import itchat
from itchat.content import *
import re
import xlrd
import datetime
import threading
from xlutils.copy import copy
import time
import requests
KEY= 'ce71277289cf43aab194c11397fd4208'
def get_response(msg):
    api_url='http://www.tuling123.com/openapi/api'
    data = {
        'key':KEY,
         'info':msg,
         'user_id':'135137'
    }
    try:
        r = requests.post(api_url,data=data).json()
        return r.get('text')
    except:
        return
def load_birthday():
    try:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        print("year:",year)
        print("month",month)
        print("day",day)
        r_data = xlrd.open_workbook('id.xlsx')
        r_table = r_data.sheet_by_index(0)
        print('成功载入id-生日excel文件！')
        for row in range(1,r_table.nrows):
            r_bir = r_table.cell(row,2).value
            print('r_bir',r_bir)
            r_year=r_bir[re.search(r'\d{4}\s*[年\.]',r_bir).span()[0]:re.search(r'\d{4}\s*[年\.]',r_bir).span()[1]-1].strip()
            r_month = r_bir[re.search(r'[年\.]\s*\d{1,2}\s*[月\.]',r_bir).span()[0]+1:re.search(r'[年\.]\s*\d{1,2}\s*[月\.]',r_bir).span()[1]-1].strip()
            r_day = r_bir[re.search(r'\d{1,2}\s*日?$',r_bir).span()[0]:re.search(r'\d{1,2}\s*日?$',r_bir).span()[1]].strip()
            #print('get date')
            if len(r_day)==3:
                print('test:r_day ',r_day[0],' ',r_day[1],' ',r_day[2])
                r_day = r_day[0:2]
                print('after test:r_day ',r_day)
                if r_day[0]=='0':
                    r_day=r_day[1]
            elif len(r_day)==2 and r_day[0]=='0':
                r_day = r_day[1]
            if len(r_month)==2 and r_month[0]=='0':
                r_month=r_month[1]
            print("r_year",r_year)
            print("r_month",r_month)
            print("r_day",r_day)
            print('\n')
            if  str(month) == r_month and str(day) == r_day:
                itchat.send_msg('奥瑞德祝您生日快乐!',str(r_table.cell(row,1).value))
                print(itchat.send_image('pic.jpg',str(r_table.cell(row,1).value)))
                print('send bless to:',r_table.cell(row,1).value)
    except:
        print('找不到excel文件，请确认id-生日excel文件(保证excel名字为id)与程序放在同一目录下！')

def save_to_excel(user_name,usr_id,usr_bir):
    try:
        read_data=xlrd.open_workbook('id.xlsx')
        w_data = copy(read_data)
        w_table = w_data.get_sheet(0)
        print('成功载入id-生日excel文件！')
        r_table = read_data.sheet_by_index(0)
        if(r_table.cell(0,0).value != '用户昵称' or r_table.cell(0,1).value != '用户id'or r_table.cell(0,1).value != '用户生日'): 
          #  print('change')
            w_table.write(0,0,'用户昵称')
            w_table.write(0,1,'用户id')
            w_table.write(0,2,'用户生日')
        for row in range(1,r_table.nrows):
           # print("第%d行",row)
           # print(str(r_table.cell(row,0).value))
            if usr_id==r_table.cell(row,1).value:
                print('write:'+usr_bir)
                w_table.write(row,2,usr_bir)
                w_data.save('id.xlsx')
                return
        w_table.write(r_table.nrows,0,user_name)
        w_table.write(r_table.nrows,1,usr_id)
        w_table.write(r_table.nrows,2,usr_bir)
        w_data.save('id.xlsx')
    except:
        print('找不到excel文件，请确认id-生日excel文件(保证excel名字为id)与程序放在同一目录下！')
@itchat.msg_register(TEXT, isGroupChat = True)
def groupchat_reply(msg):
    if msg['isAt']:
        itchat.send("@"+msg['ActualNickName']+" "+get_response(msg['Content']), msg['FromUserName'])
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    try:
        usr_id = msg['FromUserName']
        print('接收信息:',msg['Content'])
        if re.match(r'\s*生日\s*[:：∶]\s*\d{4}\s*[年\.]\s*\d{1,2}\s*[月\.]\s*\d{1,2}\s*日?\s*',msg['Content']):
            print('格式正确')
            birthday_tmp = re.split(r'[:：∶]',msg['Content'])
            birthday = birthday_tmp[1]
            print('usr_name:'+msg['User']['NickName'])
            print('usr_id:'+usr_id)
            print('birthday:'+birthday)
            save_to_excel(msg['User']['NickName'],usr_id,birthday)
            itchat.send_msg('设置成功',usr_id)
            load_birthday()
            return
        else:
            reply = get_response(msg['Content'])
            msg.text = reply
            print('发送信息',msg.text)
    except:
        msg.text = '出了点小问题'
    return msg.text
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('您好，请输入您的生日，格式为XX年XX月XX日,重置生日请发送 生日:修改后的生日', msg['RecommendInfo']['UserName'])
itchat.auto_login(hotReload=True)
#==============================================================================
# friends = itchat.get_friends(update=True)
# for i in friends:
#     print(i['NickName'])
#==============================================================================
threading.Thread(target=itchat.run).start()
while 1:
    load_birthday()
    time.sleep(21600)
