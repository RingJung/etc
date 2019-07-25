# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 06:14:03 2019

@author: chltj
"""

import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#스프레드시트 설정 및 보안키확인
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("CiDev_CNum").sheet1  # Open the spreadhseet


cell = sheet.find("12가3456")#감지한 번호판 글자를 여기에 <<

print(sheet.cell(cell.row, 2).value)
cell_ph_num = sheet.cell(cell.row, 2).value

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
if __name__ == "__main__":

    # set api key, api secret
    api_key = "NCSZHUQDGXKCEG3U"
    api_secret = "HL2OCOR6KWFTLQA8RNDOJ31IF2W8UN2W"

    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = cell_ph_num # Recipients Number '01000000000,01000000001'
    params['from'] = '01089124880' # Sender number
    params['text'] = 'Test : choiseoyeon' # Message

    cool = Message(api_key, api_secret)
    try:
        print("#########")
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])
        print("#########")

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

    sys.exit()
