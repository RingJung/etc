import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import socket
import fcntl
import struct
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("lse")


def on_message(client, userdata, msg):
    print( msg.topic+" "+str(msg.payload))
    sangeun=str(msg.payload)
    print(sangeun)
    return sangeun

def get_ipaddress(network):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', network[:15].encode('utf-8'))
    )[20:24])


client = mqtt.Client('RaspberryPI')
client.on_connect = on_connect
client.on_message = on_message

client.connect(get_ipaddress('wlan0'), 1883, 60)
#client.loop(2)
print(msg.client())
print(msg.payload())

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) #spread json lock key
client = gspread.authorize(creds)
sheet = client.open("FD_Pn").sheet1  # Open the spreadhseet
#data = sheet.get_all_records()  # Get a list of all recordsw

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
if __name__ == "__main__":

    # set api key, api secret
    api_key = "NCSZHUQDGXKCEG3U"
    api_secret = "HL2OCOR6KWFTLQA8RNDOJ31IFW8UN2W"

    i = 1

    while(1) :
        i = i + 1
        print(i)
        phNumData = sheet.cell(i, 2).value
        pprint(phNumData)
        if phNumData == '': break
        else :
            usedCheck = sheet.cell(i, 3).value
            if(usedCheck == '') :
                ## 4 params(to, from, type, text) are mandatory. must be filled
                params = dict()
                params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
                params['to'] = phNumData # Recipients Number '01000000000,01000000001'
                params['from'] = '01089124880' # Sender number
                params['text'] = (msg.payload) # Message
                print("send ")
                sheet.update_cell(i, 3, "used")

                cool = Message(api_key, api_secret)
                try:
                    response = cool.send(params)
                    print("Success Count : %s" % response['success_count'])
                    print("Error Count : %s" % response['error_count'])

                    if "error_list" in response:
                        print("Error List : %s" % response['error_list'])

                except CoolsmsException as e:
                    print("Error Code : %s" % e.code)
                    print("Error Message : %s" % e.msg)

    #sys.exit()
