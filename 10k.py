# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

aditmadzs = LineClient()
#aditmadzs = LineClient(authToken='TOKEN')
aditmadzs.log("Auth Token : " + str(aditmadzs.authToken))
channel = LineChannel(aditmadzs)
aditmadzs.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient()
#ki = LineClient(authToken='TOKEN LU')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient()
#kk = LineClient(authToken='TOKEN LU')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient()
#kc = LineClient(authToken='TOKEN LU')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

kb = LineClient()
#kb = LineClient(authToken='TOKEN LU')
kb.log("Auth Token : " + str(kb.authToken))
channel4 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel4.channelAccessToken))

kd = LineClient()
#kd = LineClient(authToken='TOKEN LU')
kd.log("Auth Token : " + str(kd.authToken))
channel5 = LineChannel(kd)
kd.log("Channel Access Token : " + str(channel5.channelAccessToken))

ke = LineClient()
#ke = LineClient(authToken='TOKEN LU')
ke.log("Auth Token : " + str(ke.authToken))
channel6 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel6.channelAccessToken))

kf = LineClient()
#kf = LineClient(authToken='TOKEN LU')
kf.log("Auth Token : " + str(kf.authToken))
channel7 = LineChannel(kf)
kf.log("Channel Access Token : " + str(channel7.channelAccessToken))

kg = LineClient()
#kg = LineClient(authToken='TOKEN LU')
kg.log("Auth Token : " + str(kg.authToken))
channel8 = LineChannel(kg)
kg.log("Channel Access Token : " + str(channel8.channelAccessToken))

kh = LineClient()
#kh = LineClient(authToken='TOKEN LU')
kh.log("Auth Token : " + str(kh.authToken))
channel9 = LineChannel(kh)
kh.log("Channel Access Token : " + str(channel9.channelAccessToken))

sw = LineClient()
#sw = LineClient(authToken='TOKEN LU')
sw.log("Auth Token : " + str(sw.authToken))
channel1 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel1.channelAccessToken))

poll = LinePoll(aditmadzs)
call = aditmadzs
creator = ["ucd986d9e5c6126e70ed3b1ff06dfbf2d","u4862fe4b182b2fd194a3108e2f3662e8"]
owner = ["ucd986d9e5c6126e70ed3b1ff06dfbf2d"]
admin = ["ucd986d9e5c6126e70ed3b1ff06dfbf2d","u4862fe4b182b2fd194a3108e2f3662e8","uc4e3f36a12aedf1b8835b4697cd8f4ca","uca3853eeb4ec2a86d14ac7e8e359d76d","ub99dd0aea6dea3b40c708f546d3f72e6","u6de346a06258794ff5d52a0189e1a21f","u17e5e2396cdc6004856463758b856c43","uf9a3ed8881f977ac342d483991a3cdd2","ua4705f32b4ec4e1f9802b1ca1e54fee3","uc6793b26f4a4a3d3d82c399d70056d98","u27390643f66508ebbac2190a84682a7b"]
staff = ["ucd986d9e5c6126e70ed3b1ff06dfbf2d"]
mid = aditmadzs.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
Hmid = kg.getProfile().mid
Imid = kh.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [aditmadzs,ki,kk,kc,kb,kd,ke,kf,kg,kh,sw]
ABC = [aditmadzs,ki,kk,kc,kb,kd,ke,kf,kg,kh,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Zmid]
Aditmadzs = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

AditmadzsProfile = aditmadzs.getProfile()
myProfile["displayName"] = AditmadzsProfile.displayName
myProfile["statusMessage"] = AditmadzsProfile.statusMessage
myProfile["pictureStatus"] = AditmadzsProfile.pictureStatus

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName
responsename8 = kg.getProfile().displayName
responsename9 = kh.getProfile().displayName
responsename10 = sw.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items            

def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@SELFBOT-BY:MAX "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    aditmadzs.sendMessage(to, textx, {'AGENT_NAME':'@aditmadzs1 on Instagram', 'AGENT_LINK': 'https://www.instagram.com/aditmadzs1', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + aditmadzs.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessageFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return aditmadzs.sendMessage(to, text, contentMetadata, 0)
    

def sendMessageWithFooter(to, text):
 aditmadzs.reissueUserTicket()
 madzs = aditmadzs.getProfile()
 ticket = "http://line.me/ti/p/"+aditmadzs.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+aditmadzs.pictureStatus
 name = "「 SELFBOT-BY:MAX 」"
 Aditmadzs = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 aditmadzs.sendMessage(to, text, contentMetadata=Aditmadzs)

def sendMentionV10(to, text,name, url, iconlink):
    aditmadzs.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def mentionMembers(to, mid,name,url,iconlink):
    try:
        arrData = ""
        ginfo = aditmadzs.getGroup(to)
        textx = "    ⊰❂⊱Mention Members⊰❂⊱\n\n•1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "•{}. ".format(str(no))
            else:
                textx += "\nTotal: {} members".format(str(len(mid)))
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ╰══[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n  ╰══[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = aditmadzs.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ╰══[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n  ╰══[ Success ]"
        aditmadzs.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = aditmadzs.getAllContactIds()
        gid = aditmadzs.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"┃┃Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n┃┃Group : "+str(len(gid))+"\n┃┃Teman : "+str(len(teman))+"\n┃┃Version : SELFBOT-BY:MAX\n┃┃Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃┃Runtime :\n "+bot
        aditmadzs.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        aditmadzs.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "             😈 HELP 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "Cctv「on/off」\n" + \
				  "│ ≫ " + key + "Cyduk\n" + \
				  "│ ≫ " + key + "Creator\n" + \
				  "│ ≫ " + key + "Help2\n" + \
				  "│ ≫ " + key + "Help3\n" + \
				  "│ ≫ " + key + "Help4\n" + \
                                  "│ ≫ " + key + "Help5\n" + \
                  "│ ≫ " + key + "Help6\n" + \
				  "│ ≫ " + key + "Help7\n" + \
                  "│ ≫ " + key + "Listbot\n" + \
                  "│ ≫ " + key + "Listadmin\n" + \
				  "│ ≫ " + key + "Status\n" + \
				  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage

def helpcreator():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "    😈 HELP CREATOR 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "Cek spam\n" + \
                  "│ ≫ " + key + "Cek pesan\n" + \
                  "│ ≫ " + key + "Cek respon\n" + \
                  "│ ≫ " + key + "Cek welcome\n" + \
                  "│ ≫ " + key + "Cek leave\n" + \
                  "│ ≫ " + key + "Set spam:「Text」\n" + \
                  "│ ≫ " + key + "Set pesan:「Text」\n" + \
                  "│ ≫ " + key + "Set respon:「Text」\n" + \
                  "│ ≫ " + key + "Set welcome:「Text」\n" + \
                  "│ ≫ " + key + "Set leave:「Text」\n" + \
                  "│ ≫ " + key + "Bot1\n" + \
                  "│ ≫ " + key + "Bot2\n" + \
                  "│ ≫ " + key + "Bot3\n" + \
                  "│ ≫ " + key + "Bot4\n" + \
                  "│ ≫ " + key + "Bot5\n" + \
                  "│ ≫ " + key + "Bot6\n" + \
                  "│ ≫ " + key + "Bot7\n" + \
                  "│ ≫ " + key + "Bot8\n" + \
                  "│ ≫ " + key + "Bot9\n" + \
                  "│ ≫ " + key + "B1bye\n" + \
                  "│ ≫ " + key + "B2bye\n" + \
                  "│ ≫ " + key + "B3bye\n" + \
                  "│ ≫ " + key + "B4bye\n" + \
                  "│ ≫ " + key + "B5bye\n" + \
                  "│ ≫ " + key + "B6bye\n" + \
                  "│ ≫ " + key + "B7bye\n" + \
                  "│ ≫ " + key + "B8bye\n" + \
                  "│ ≫ " + key + "B9bye\n" + \
                  "│ ≫ " + key + "Myname:「Name」\n" + \
                  "│ ≫ " + key + "B1name:「Name」\n" + \
                  "│ ≫ " + key + "B2name:「Name」\n" + \
                  "│ ≫ " + key + "B3name:「Name」\n" + \
                  "│ ≫ " + key + "B4name:「Name」\n" + \
                  "│ ≫ " + key + "B5name:「Name」\n" + \
                  "│ ≫ " + key + "B6name:「Name」\n" + \
                  "│ ≫ " + key + "B7name:「Name」\n" + \
                  "│ ≫ " + key + "B8name:「Name」\n" + \
                  "│ ≫ " + key + "B9name:「Name」\n" + \
				  "│ ≫ " + key + "B10name:「Name」\n" + \
                  "│ ≫ " + key + "Uppro:「Foto」\n" + \
                  "│ ≫ " + key + "B1up「Foto」\n" + \
                  "│ ≫ " + key + "B2up「Foto」\n" + \
                  "│ ≫ " + key + "B3up「Foto」\n" + \
                  "│ ≫ " + key + "B4up「Foto」\n" + \
                  "│ ≫ " + key + "B5up「Foto」\n" + \
                  "│ ≫ " + key + "B6up「Foto」\n" + \
                  "│ ≫ " + key + "B7up「Foto」\n" + \
                  "│ ≫ " + key + "B8up「Foto」\n" + \
                  "│ ≫ " + key + "B9up「Foto」\n" + \
				  "│ ≫ " + key + "B10up「Foto」\n" + \
                  "│ ≫ " + key + "Run:「Mid」「Jumlah」\n" + \
                  "│ ≫ " + key + "Spam:「Mid」「Jumlah」\n" + \
				  "│ ≫ " + key + "Spamtag:「jumlahnya」\n" + \
                  "│ ≫ " + key + "Spamtag「@」\n" + \
                  "│ ≫ " + key + "Spamcall:「jumlahnya」\n" + \
                  "│ ≫ " + key + "Spamcall\n" + \
                  "│ ≫ " + key + "Broadcast:「Text」\n" + \
                  "│ ≫ " + key + "Setkey「New Key」\n" + \
                  "│ ≫ " + key + "Mykey\n" + \
                  "│ ≫ " + key + "Resetkey\n" + \
				  "│ ≫ " + key + "Self「on/off」\n" + \
                  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage1

def helpblacklist():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "       😈 Help Blacklist 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "Banlist\n" + \
				  "│ ≫ " + key + "Ban:on\n" + \
                  "│ ≫ " + key + "Blc\n" + \
				  "│ ≫ " + key + "Clearban\n" + \
				  "│ ≫ " + key + "Refresh\n" + \
				  "│ ≫ " + key + "Unban「@」\n" + \
				  "│ ≫ " + key + "Unban:on\n" + \
				  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage3

def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "        😈 Help Admin 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "Admin:on\n" + \
                  "│ ≫ " + key + "Admin:repeat\n" + \
                  "│ ≫ " + key + "Adminadd「@」\n" + \
                  "│ ≫ " + key + "Admindell「@」\n" + \
				  "│ ≫ " + key + "Bot:on\n" + \
                  "│ ≫ " + key + "Bot:repeat\n" + \
				  "│ ≫ " + key + "Botadd「@」\n" + \
                  "│ ≫ " + key + "Botdell「@」\n" + \
				  "│ ≫ " + key + "Refresh\n" + \
				  "│ ≫ " + key + "Staff:on\n" + \
                  "│ ≫ " + key + "Staff:repeat\n" + \
                  "│ ≫ " + key + "Staffadd「@」\n" + \
                  "│ ≫ " + key + "Staffdell「@」\n" + \
                  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage4
    	
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "       😈 Help Setting 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "Autoadd「on/off」\n" + \
				  "│ ≫ " + key + "Autojoin「on/off」\n" + \
				  "│ ≫ " + key + "Autoleave「on/off」\n" + \
				  "│ ≫ " + key + "Contact「on/off」\n" + \
				  "│ ≫ " + key + "Jointicket「on/off」\n" + \
				  "│ ≫ " + key + "Respon「on/off」\n" + \
				  "│ ≫ " + key + "Unsend「on/off」\n" + \
                  "│ ≫ " + key + "Welcome「on/off」\n" + \
                  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage5
    
def helpprotect():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "        😈 Help Protect 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
				  "│ ≫ " + key + "Join all\n" + \
                                  "│ ≫ " + key + "Bye all\n" + \
                                  "│ ≫ " + key + "Bye me\n" + \
				  "│ ≫ " + key + "Allpro 「on/off」\n" + \
                  "│ ≫ " + key + "Notag「on/off」\n" + \
                  "│ ≫ " + key + "Protecturl「on/off」\n" + \
                  "│ ≫ " + key + "Protectjoin「on/off」\n" + \
                  "│ ≫ " + key + "Protectkick「on/off」\n" + \
                  "│ ≫ " + key + "Protectcancel「on/off」\n" + \
                  "│ ≫ " + key + "Protectinvite「on/off」\n" + \
                  "│ ≫ " + key + "Blockjs「on/off」\n" + \
                  "│ ≫ " + key + "Js stay\n" + \
                  "│ ≫ " + key + "Ghost「on/off」\n" + \
				  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage6
	
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage8 = "╭──────────╮" + "\n" + \
                  "│【さัএπัஞ✵ບิथℓℓҨतΩ】" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│  ☯ sᴇʟғʙᴏᴛ ʙʏ ᴍᴀx ☯" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "         😈 Help SELF 😈" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "│ ≫ " + key + "About\n" + \
				  "│ ≫ " + key + "Close\n" + \
				  "│ ≫ " + key + "Ginfo\n" + \
				  "│ ≫ " + key + "Gruplist\n" + \
				  "│ ≫ " + key + "Info 「@」\n" + \
                                  "│ ≫ " + key + "Nk「@」\n" + \
                                  "│ ≫ " + key + "Fuck「@」\n" + \
				  "│ ≫ " + key + "S u p e r\n" + \
				  "│ ≫ " + key + "Me\n" + \
                  "│ ≫ " + key + "Mid「@」\n" + \
				  "│ ≫ " + key + "Mybot\n" + \
                  "│ ≫ " + key + "Mid\n" + \
				  "│ ≫ " + key + "Open\n" + \
				  "│ ≫ " + key + "Respon\n" + \
				  "│ ≫ " + key + "Restart\n" + \
				  "│ ≫ " + key + "Runtime\n" + \
				  "│ ≫ " + key + "Speed/Sp\n" + \
                                  "│ ≫ " + key + "Spbot/Spb\n" + \
                                  "│ ≫ " + key + "My token\n" + \
                  "│ ≫ " + key + "Spbot\n" + \
				  "│ ≫ " + key + "Stealname「@」\n" + \
                  "│ ≫ " + key + "Stealbio「@」\n" + \
                  "│ ≫ " + key + "Stealcover「@」\n" + \
				  "│ ≫ " + key + "Stealpicture「@」\n" + \
                  "│ ≫ " + key + "Stealvideoprofile「@」\n" + \
                  "│ ≫ " + key + "Tag\n" + \
                  "╰──────────╯" + "\n" + \
                  " " + "\n" + \
                  "😈「SELFBOT-BY:MAX」😈"
    return helpMessage8

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            aditmadzs.reissueGroupTicket(op.param1)
                            X = aditmadzs.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            aditmadzs.updateGroup(X)
                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if aditmadzs.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            aditmadzs.reissueGroupTicket(op.param1)
                                            X = aditmadzs.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            aditmadzs.updateGroup(X)
                                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    kb.reissueGroupTicket(op.param1)
                                                    X = kb.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    kb.updateGroup(X)
                                                    aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                        except:
                                            try:
                                                if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kd.reissueGroupTicket(op.param1)
                                                        X = kd.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kd.updateGroup(X)
                                                        aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                            except:
                                                try:
                                                    if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            ke.reissueGroupTicket(op.param1)
                                                            X = ke.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            ke.updateGroup(X)
                                                            aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                except:
                                                    try:
                                                        if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                kf.reissueGroupTicket(op.param1)
                                                                X = kf.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                kf.updateGroup(X)
                                                                aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                    except:
                                                        try:
                                                            if kg.getGroup(op.param1).preventedJoinByTicket == False:
                                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                    kg.reissueGroupTicket(op.param1)
                                                                    X = kg.getGroup(op.param1)
                                                                    X.preventedJoinByTicket = True
                                                                    kg.updateGroup(X)
                                                                    aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                        except:
                                                            try:
                                                                if kh.getGroup(op.param1).preventedJoinByTicket == False:
                                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                        kh.reissueGroupTicket(op.param1)
                                                                        X = kh.getGroup(op.param1)
                                                                        X.preventedJoinByTicket = True
                                                                        kh.updateGroup(X)
                                                                        aditmadzs.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                                            except:
                                                                pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        aditmadzs.leaveGroup(op.param1)
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Haii, salken yaa ^^")
                    else:
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ginfo = aditmadzs.getGroup(op.param1)
                        aditmadzs.sendMessage(op.param1,"Hello baby 🐺")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kg.leaveGroup(op.param1)
                    else:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kh.leaveGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = aditmadzs.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = ke.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                            except:
                                                try:
                                                    group = kf.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                except:
                                                    try:
                                                        group = kg.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                    except:
                                                        try:
                                                            group = kh.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for _mid in gMembMids:
                                                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                                        except:
                                                            pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = aditmadzs.getGroup(op.param1)
                contact = aditmadzs.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                aditmadzs.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in wait["blacklist"]:
                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        aditmadzs.sendText(op.param1, wait["message"])
                        aditmadzs.sendContact(op.param1, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                        aditmadzs.blockContact(op.param1)
#================================================================================
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass             

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = aditmadzs.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        aditmadzs.updateGroup(G)
                        invsend = 0
                        Ticket = aditmadzs.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = aditmadzs.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        aditmadzs.updateGroup(X)
            except:
                pass             
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenARoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenARoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                        aditmadzs.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.findAndAddContactsByMid(op.param3)
                        aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                        aditmadzs.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        aditmadzs.findAndAddContactsByMid(op.param3)
                        aditmadzs.inviteIntoGroup(op.param1,[Zmid])
                        aditmadzs.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                            aditmadzs.findAndAddContactsByMid(op.param3)
                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                            aditmadzs.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                            except:
                                                try:
                                                    if op.param3 not in wait["blacklist"]:
                                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                                except:
                                                    try:
                                                        if op.param3 not in wait["blacklist"]:
                                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                                            random.choice(ABC).inviteIntoGroup(op.param1,[Zmid])
                                                    except:
                                                        pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        aditmadzs.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            aditmadzs.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                aditmadzs.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    aditmadzs.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        aditmadzs.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            aditmadzs.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                aditmadzs.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    aditmadzs.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        aditmadzs.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = ki.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            ki.updateGroup(G)
                                                            Ticket = ki.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = ki.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            ki.updateGroup(G)
                                                            Ticket = ki.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                aditmadzs.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    aditmadzs.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        aditmadzs.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            aditmadzs.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                aditmadzs.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    aditmadzs.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        aditmadzs.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            aditmadzs.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                aditmadzs.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kk.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kk.updateGroup(G)
                                                            Ticket = kk.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kk.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kk.updateGroup(G)
                                                            Ticket = kk.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                                ki.acceptGroupInvitation(op.param1)
                                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki.acceptGroupInvitation(op.param1)
                                                                    aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        ki.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            ki.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                ki.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ki.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ki.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ki.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ki.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kc.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kc.updateGroup(G)
                                                            Ticket = kc.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kc.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kc.updateGroup(G)
                                                            Ticket = kc.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kk.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                    kk.acceptGroupInvitation(op.param1)
                                                                    aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kk.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kk.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kk.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kk.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kk.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kk.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kk.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kb.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kb.updateGroup(G)
                                                            Ticket = kb.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kb.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kb.updateGroup(G)
                                                            Ticket = kb.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kc.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kc.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                        kc.acceptGroupInvitation(op.param1)
                                                                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kc.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kc.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kc.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kc.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kc.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kc.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                    aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kd.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kd.updateGroup(G)
                                                            Ticket = kd.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kd.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kd.updateGroup(G)
                                                            Ticket = kd.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kb.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kb.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kb.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                            kb.acceptGroupInvitation(op.param1)
                                                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kb.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kb.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kb.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kb.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kb.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = ke.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            ke.updateGroup(G)
                                                            Ticket = ke.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = ke.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            ke.updateGroup(G)
                                                            Ticket = ke.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kd.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kd.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kd.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kd.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                                kd.acceptGroupInvitation(op.param1)
                                                                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kd.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kd.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kd.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kd.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kf.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kf.updateGroup(G)
                                                            Ticket = kf.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kf.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kf.updateGroup(G)
                                                            Ticket = kf.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                ke.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    ke.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        ke.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            ke.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                ke.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                                    ke.acceptGroupInvitation(op.param1)
                                                                                    aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        ke.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            ke.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                ke.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kf.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kg.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kg.updateGroup(G)
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kg.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kg.updateGroup(G)
                                                            Ticket = kg.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kf.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kf.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kf.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kf.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kf.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kf.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kf.acceptGroupInvitation(op.param1)
                                                                                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kf.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kf.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kg.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kg.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kg.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                    kg.acceptGroupInvitation(op.param1)
                                                    aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        kg.acceptGroupInvitation(op.param1)
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = kh.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            kh.updateGroup(G)
                                                            Ticket = kh.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = kh.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            kh.updateGroup(G)
                                                            Ticket = kh.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kg.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kg.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kg.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kg.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kg.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kg.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kg.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kg.acceptGroupInvitation(op.param1)
                                                                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kg.acceptGroupInvitation(op.param1)
                                                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kh.acceptGroupInvitation(op.param1)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            kh.acceptGroupInvitation(op.param1)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                kh.acceptGroupInvitation(op.param1)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    kh.acceptGroupInvitation(op.param1)
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                        kh.acceptGroupInvitation(op.param1)
                                                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            G = aditmadzs.getGroup(op.param1)
                                                            G.preventedJoinByTicket = False
                                                            aditmadzs.updateGroup(G)
                                                            Ticket = aditmadzs.reissueGroupTicket(op.param1)
                                                            aditmadzs.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            aditmadzs.kickoutFromGroup(op.param1,[op.param2])                                    
                                                            G = aditmadzs.getGroup(op.param1)
                                                            G.preventedJoinByTicket = True
                                                            aditmadzs.updateGroup(G)
                                                            Ticket = aditmadzs.reissueGroupTicket(op.param1)
                                                        except:
                                                            try:
                                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                                kh.acceptGroupInvitation(op.param1)
                                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                                    kh.acceptGroupInvitation(op.param1)
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                                except:
                                                                    try:
                                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                                        kh.acceptGroupInvitation(op.param1)
                                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                                    except:
                                                                        try:
                                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                                            kh.acceptGroupInvitation(op.param1)
                                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                                        except:
                                                                            try:
                                                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                                                kh.acceptGroupInvitation(op.param1)
                                                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                                            except:
                                                                                try:
                                                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                                                    kh.acceptGroupInvitation(op.param1)
                                                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                                                except:
                                                                                    try:
                                                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                                                        kh.acceptGroupInvitation(op.param1)
                                                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                                                    except:
                                                                                        try:
                                                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                                                            kh.acceptGroupInvitation(op.param1)
                                                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                                                        except:
                                                                                            try:
                                                                                                aditmadzs.inviteIntoGroup(op.param1,[op.param3])
                                                                                                kh.acceptGroupInvitation(op.param1)
                                                                                                aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                                                                                            except:
                                                                                                pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        aditmadzs.findAndAddContactsByMid(op.param1,admin)
                        aditmadzs.inviteIntoGroup(op.param1,admin)
                        aditmadzs.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.inviteIntoGroup(op.param1,admin)
                                        except:
                                             try:
                                                 ke.kickoutFromGroup(op.param1,[op.param2])
                                                 ke.findAndAddContactsByMid(op.param1,admin)
                                                 ke.inviteIntoGroup(op.param1,admin)
                                             except:
                                                 try:
                                                     kf.kickoutFromGroup(op.param1,[op.param2])
                                                     kf.findAndAddContactsByMid(op.param1,admin)
                                                     kf.inviteIntoGroup(op.param1,admin)
                                                 except:
                                                     try:
                                                         kg.kickoutFromGroup(op.param1,[op.param2])
                                                         kg.findAndAddContactsByMid(op.param1,admin)
                                                         kg.inviteIntoGroup(op.param1,admin)
                                                     except:
                                                         try:
                                                             kh.kickoutFromGroup(op.param1,[op.param2])
                                                             kh.findAndAddContactsByMid(op.param1,admin)
                                                             kh.inviteIntoGroup(op.param1,admin)
                                                         except:
                                                             pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param1,admin)
                                    kb.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.findAndAddContactsByMid(op.param1,admin)
                                        kd.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param1,admin)
                                            ke.inviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.findAndAddContactsByMid(op.param1,admin)
                                                kf.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                    kg.findAndAddContactsByMid(op.param1,admin)
                                                    kg.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                        kh.findAndAddContactsByMid(op.param1,admin)
                                                        kh.inviteIntoGroup(op.param1,admin)
                                                    except:
                                                        pass


                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ADITMADZSreadPoint"]:
                   if op.param2 in Setmain["ADITMADZSreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ADITMADZSreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = aditmadzs.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = aditmadzs.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        aditmadzs.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(Aditmadzs.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':Aditmadzs.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                aditmadzs.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                aditmadzs.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = aditmadzs.getGroup(at)
                                Aditmadzs = aditmadzs.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(Aditmadzs.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                aditmadzs.sendMessage(at, str(ret_))
                                aditmadzs.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26 or op.type == 25:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = aditmadzs.getContact(msg._from)
                   cName = contact.displayName
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendImageWithURL(msg.to, image)
                           aditmadzs.sendMessage(msg.to, wait["Respontag"])
                           aditmadzs.sendMessage(msg.to, None, contentMetadata={"STKID":"52114143","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           aditmadzs.sendMessage(msg.to, "Ye ngetag ngetag, lu minta digift ya? cek PersonalChat bos, udah gue gift tuh. Jangan lupa bilang makasih yak!")
                           aditmadzs.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           aditmadzs.sendMessage(msg.to, "Jangan tag saya....")
                           aditmadzs.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"「Cek ID Sticker」\n🐚 STKID : " + msg.contentMetadata["STKID"] + "\n🐚 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🐚 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"💀 Nama: " + msg.contentMetadata["displayName"] + "\n💀 MID: " + msg.contentMetadata["mid"] + "\n💀 Status: " + contact.statusMessage + "\n💀 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = aditmadzs.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = aditmadzs.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    aditmadzs.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = aditmadzs.getContact(msg.contentMetadata["mid"])
                        path = aditmadzs.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        aditmadzs.sendMessage(msg.to,"»» Nama : " + msg.contentMetadata["displayName"] + "\n»» MID : " + msg.contentMetadata["mid"] + "\n»» Status Msg : " + contact.statusMessage + "\n»» Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        aditmadzs.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan anggota bot Aditmadzs")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        aditmadzs.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        aditmadzs.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        aditmadzs.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = aditmadzs.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            aditmadzs.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = aditmadzs.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     aditmadzs.updateGroupPicture(msg.to, path)
                     aditmadzs.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ADITMADZSfoto"]:
                            path = aditmadzs.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][mid]
                            aditmadzs.updateProfilePicture(path)
                            aditmadzs.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ADITMADZSfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ADITMADZSfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ADITMADZSfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ADITMADZSfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ADITMADZSfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Emid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["ADITMADZSfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Fmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["ADITMADZSfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Gmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["ADITMADZSfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Hmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["ADITMADZSfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Imid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ADITMADZSfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ADITMADZSfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = kd.downloadObjectMsg(msg_id)
                     path6 = ke.downloadObjectMsg(msg_id)
                     path7 = kf.downloadObjectMsg(msg_id)
                     path8 = kg.downloadObjectMsg(msg_id)
                     path9 = kh.downloadObjectMsg(msg_id)
                     path10 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path4)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path5)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path6)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path7)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path8)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kh.updateProfilePicture(path9)
                     kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path10)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        aditmadzs.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)
                        kd.sendChatChecked(msg.to, msg_id)
                        ke.sendChatChecked(msg.to, msg_id)
                        kf.sendChatChecked(msg.to, msg_id)
                        kg.sendChatChecked(msg.to, msg_id)
                        kh.sendChatChecked(msg.to, msg_id)
                        sw.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               aditmadzs.sendMessage(msg.to, str(helpMessage))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                aditmadzs.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                aditmadzs.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpcreator()
                               aditmadzs.sendMessage(msg.to, str(helpMessage1))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        elif cmd == "help3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpadmin()
                               aditmadzs.sendMessage(msg.to, str(helpMessage4))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        elif cmd == "help4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpsetting()
                               aditmadzs.sendMessage(msg.to, str(helpMessage5))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        elif cmd == "help5":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpprotect()
                               aditmadzs.sendMessage(msg.to, str(helpMessage6))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        elif cmd == "help6":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage8 = helpbot()
                               aditmadzs.sendMessage(msg.to, str(helpMessage8))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        elif cmd == "help7":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpblacklist()
                               aditmadzs.sendMessage(msg.to, str(helpMessage3))
                               aditmadzs.sendContact(to, "ucd986d9e5c6126e70ed3b1ff06dfbf2d")
                               
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                aditmadzs.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "-▬▬▬▬▬▬▬▬▬▬▬▬\n         🇦🇱 S T A T U S 🇦🇱\n-▬▬▬▬▬▬▬▬▬▬▬▬\n"
                                if wait["unsend"] == True: md+="┃🇦🇱┃ ✔️ Unsend「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Unsend「OFF」\n"                                
                                if wait["Mentionkick"] == True: md+="┃🇦🇱┃ ✔️ Notag「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃🇦🇱┃ ✔️ Respon「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Respon「OFF」\n"                   
                                if wait["autoJoin"] == True: md+="┃🇦🇱┃ ✔️ Autojoin「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Autojoin「OFF」\n"
                                if settings["autoJoinTicket"] == True: md+="┃🇦🇱┃ ✔️ Jointicket「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Jointicket「OFF」\n"                                
                                if wait["autoAdd"] == True: md+="┃🇦🇱┃ ✔️ Autoadd「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃🇦🇱┃ ✔️ Welcome「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Welcome「OFF」\n"                 
                                if wait["autoLeave"] == True: md+="┃🇦🇱┃ ✔️ Autoleave「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃🇦🇱┃ ✔️ Protecturl「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃🇦🇱┃ ✔️ ProtectJoin「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ ProtectJoin「OFF」\n"
                                if msg.to in protectkick: md+="┃🇦🇱┃ ✔️ Protectkick「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃🇦🇱┃ ✔️ Protectcancel「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Protectcancel「OFF」\n"
                                if msg.to in protectinvite: md+="┃🇦🇱┃ ✔️ Protectinvite「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Protectinvite「OFF」\n"
                                if msg.to in protectantijs: md+="┃🇦🇱┃ ✔️ Blockjs「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Blockjs「OFF」\n"  
                                if msg.to in ghost: md+="┃🇦🇱┃ ✔️ Ghost「ON」\n"
                                else: md+="┃🇦🇱┃ ✖ Ghost「OFF」\n"
                                aditmadzs.sendMessage(msg.to, md+"-▬▬▬▬▬▬▬▬▬▬▬▬\n┃☬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃☬ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n-▬▬▬▬▬▬▬▬▬▬▬▬")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                aditmadzs.sendMessage(msg.to,"Creator Bot") 
                                ma = ""
                                for i in creator:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "About":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "┏━━[ SELFBOT-BY:MAX ]\n")
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'mek':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "mid":
                               aditmadzs.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = aditmadzs.getContact(key1)
                               aditmadzs.sendMessage(msg.to, "💀 Nama : "+str(mi.displayName)+"\n💀 Mid : " +key1+"\n💀 Status Message"+str(mi.statusMessage))
                               aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(aditmadzs.getContact(key1)):
                                   aditmadzs.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               msg.contentType = 13
                               aditmadzs.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Emid}
                               msg.contentType = 13
                               aditmadzs.sendMessage1(msg)
                               msg.contentMetadata = {'mid': Fmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               aditmadzs.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               aditmadzs.sendMessage1(msg)

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   ki.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kk.removeAllMessages(op.param2)
                                   kk.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kf.removeAllMessages(op.param2)
                                   kf.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kg.removeAllMessages(op.param2)
                                   kg.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   kh.removeAllMessages(op.param2)
                                   kh.sendMessage(msg.to, "ลบแชท เรียบร้อย ✔")
                                   aditmadzs.sendMessage(msg.to,"ลบแชทคิกเรียบร้อย ✔")
                               except:
                                   pass

                        elif cmd.startswith("stealname "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = aditmadzs.getContact(ls)
                                      aditmadzs.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                        elif cmd.startswith("stealbio "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = aditmadzs.getContact(ls)
                                      aditmadzs.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                        elif cmd.startswith("stealpicture "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + aditmadzs.getContact(ls).pictureStatus
                                        aditmadzs.sendImageWithURL(msg.to, str(path))
                            
                        elif cmd.startswith("stealcover "):
                            if msg._from in admin:
                                if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = aditmadzs.getProfileCoverURL(ls)
                                            aditmadzs.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("stealvideoprofile "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = aditmadzs.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            aditmadzs.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass                                            

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = aditmadzs.getGroupIdsJoined()
                               for group in saya:
                                   aditmadzs.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   aditmadzs.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               aditmadzs.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               aditmadzs.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               aditmadzs.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = aditmadzs.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                aditmadzs.sendMessage(msg.to, "┏━━[ BOT Grup Info]\n┃┃ Nama Group : {}".format(G.name)+ "\n┃┃ ID Group : {}".format(G.id)+ "\n┃┃ Pembuat : {}".format(G.creator.displayName)+ "\n┃┃ Waktu Dibuat : {}".format(str(timeCreated))+ "\n┃┃ Jumlah Member : {}".format(str(len(G.members)))+ "\n┃┃ Jumlah Pending : {}".format(gPending)+ "\n┃┃ Group Qr : {}".format(gQr)+ "\n┃┃ Group Ticket : {}".format(gTicket))
                                aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                aditmadzs.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                aditmadzs.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = aditmadzs.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = aditmadzs.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(aditmadzs.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "┏━━[ BOT Grup Info]\n"
                                ret_ += "\n┃┃ Nama Group : {}".format(G.name)
                                ret_ += "\n┃┃ ID Group : {}".format(G.id)
                                ret_ += "\n┃┃ Pembuat : {}".format(gCreator)
                                ret_ += "\n┃┃ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┃┃ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┃┃ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┃┃ Group Qr : {}".format(gQr)
                                ret_ += "\n┃┃ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                aditmadzs.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = aditmadzs.getGroupIdsJoined()
                               for i in gid:
                                   G = aditmadzs.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃☬ " + str(a) + ". " +G.name+ "\n"
                               aditmadzs.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n┃☬\n"+ma+"┃☬\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃☬ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n┃☬\n"+ma+"┃☬\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃☬ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n┃☬\n"+ma+"┃☬\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃☬ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╭════════[ GROUP LIST ]\n┃☬\n"+ma+"┃☬\n  ╰═══════[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "QR telah dibuka")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = aditmadzs.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   aditmadzs.updateGroup(X)
                                   aditmadzs.sendMessage(msg.to, "QR telah ditutup")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = aditmadzs.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      aditmadzs.updateGroup(x)
                                   gurl = aditmadzs.reissueGroupTicket(msg.to)
                                   aditmadzs.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "uppro":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][mid] = True
                                aditmadzs.sendMessage(msg.to,"Kirim fotonya.....")
 
                        elif cmd == "b1up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "b2up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "b3up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b4up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b5up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Emid] = True
                                kd.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b6up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Fmid] = True
                                ke.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b7up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Gmid] = True
                                kf.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b8up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Hmid] = True
                                kg.sendMessage(msg.to,"Kirim fotonya.....")
                        elif cmd == "b9up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Imid] = True
                                kh.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "b10up":
                            if msg._from in admin:
                                Setmain["ADITMADZSfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Kirim fotonya.....")
                        
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = aditmadzs.getProfile()
                                profile.displayName = string
                                aditmadzs.updateProfile(profile)
                                aditmadzs.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("b10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd == "ลบรัน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = aditmadzs.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      aditmadzs.rejectGroupInvitation(gid)
                                  aditmadzs.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  aditmadzs.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'hai':
                          if wait["selfbot"] == True:
                               group = aditmadzs.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "tag":
                          if wait["selfbot"] == True:
                            group = aditmadzs.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Alin \n'
                                aditmadzs.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                aditmadzs.sendMessage(to, "Hello {} Mention".format(str(len(nama)))) 

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"┏━━[ BOT ]\n\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"┏━━[ BOT admin ]\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +aditmadzs.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +aditmadzs.getGroup(group).name + "\n"                                    
                                aditmadzs.sendMessage(msg.to,"┏━━[ MAX Protect ]\n\n»» PROTECT URL :\n"+ma+"\n»» PROTECT KICK :\n"+mb+"\n»» PROTECT JOIN :\n"+md+"\n»» PROTECT CANCEL:\n"+mc+"\n»» PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kb.sendMessage(msg.to,responsename4)
                                kd.sendMessage(msg.to,responsename5)
                                ke.sendMessage(msg.to,responsename6)
                                kf.sendMessage(msg.to,responsename7)
                                kg.sendMessage(msg.to,responsename8)
                                kh.sendMessage(msg.to,responsename9)
                                sw.sendMessage(msg.to,responsename10)
                        
                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    aditmadzs.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "js stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = aditmadzs.getGroup(msg.to)
                                    aditmadzs.inviteIntoGroup(msg.to, [Zmid])
                                    aditmadzs.sendMessage(msg.to,"Grup 「"+str(ginfo.name)+"」 Amax Dari JS")
                                except:
                                    pass

                        elif cmd == "reinvite":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                ki.updateGroup(G)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kc.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kb.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kd.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)
                                G.preventedJoinByTicket = False
                                ke.updateGroup(G)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kf.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kg.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)
                                G.preventedJoinByTicket = False
                                kh.updateGroup(G)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)
                                
                        elif cmd == "join all":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "bye all":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ki.sendMessage(msg.to, "dadah group "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)

                        elif cmd == "bot1":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "bot2":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "bot3":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "bot4":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "bot5":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "bot6":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "bot7":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kf.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)

                        elif cmd == "bot8":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)

                        elif cmd == "bot9":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)

                        
                        elif cmd == "kicker join":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ginfo = aditmadzs.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                aditmadzs.updateGroup(G)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kicker bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                sw.sendText(msg.to, "Bye fams "+str(G.name))
                                sw.leaveGroup(msg.to)

                        elif cmd == "b1bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ki.sendText(msg.to, "Bye fams "+str(G.name))
                                ki.leaveGroup(msg.to)

                        elif cmd == "b2bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kk.sendText(msg.to, "Bye fams "+str(G.name))
                                kk.leaveGroup(msg.to)

                        elif cmd == "b3bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kc.sendText(msg.to, "Bye fams "+str(G.name))
                                kc.leaveGroup(msg.to)

                        elif cmd == "b4bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kb.sendText(msg.to, "Bye fams "+str(G.name))
                                kb.leaveGroup(msg.to)

                        elif cmd == "b5bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kd.sendText(msg.to, "Bye fams "+str(G.name))
                                kd.leaveGroup(msg.to)

                        elif cmd == "b6bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                ke.sendText(msg.to, "Bye fams "+str(G.name))
                                ke.leaveGroup(msg.to)

                        elif cmd == "b7bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kf.sendText(msg.to, "Bye fams "+str(G.name))
                                kf.leaveGroup(msg.to)

                        elif cmd == "b8bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kg.sendText(msg.to, "Bye fams "+str(G.name))
                                kg.leaveGroup(msg.to)

                        elif cmd == "b9bye":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                kh.sendText(msg.to, "Bye fams "+str(G.name))
                                kh.leaveGroup(msg.to)

                        elif cmd == "bye me":
                            if msg._from in admin:
                                G = aditmadzs.getGroup(msg.to)
                                aditmadzs.sendText(msg.to, "Bye fams "+str(G.name))
                                aditmadzs.leaveGroup(msg.to)

                        elif cmd == "สปีด" or cmd == "สปีท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = aditmadzs.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                aditmadzs.sendMessage(msg.to, "Waiting...")
                                aditmadzs.sendMessage(msg.to, "%.10f detik" % (get_profile_time/3))
                        
                        elif cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = ki.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ki.sendMessage(msg.to, "➲ BOT 1 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kk.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kk.sendMessage(msg.to, "➲ BOT 2 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kc.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kc.sendMessage(msg.to, "➲ BOT 3 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kb.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kb.sendMessage(msg.to, "➲ BOT 4 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kd.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kd.sendMessage(msg.to, "➲ BOT 5 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = ke.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ke.sendMessage(msg.to, "➲ BOT 6 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kf.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kf.sendMessage(msg.to, "➲ BOT 7 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kg.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kg.sendMessage(msg.to, "➲ BOT 8 Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = kh.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kh.sendMessage(msg.to, "➲ BOT 9 Speed\n%.10f detik" % (get_profile_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               aditmadzs.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               aditmadzs.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
 
                        elif cmd == "speedbot" or cmd == "spbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               ki.sendMessage(msg.to, "Waiting...")
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kd.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kf.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kg.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kh.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               
                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ADITMADZSreadPoint'][msg.to] = msg_id
                                 Setmain['ADITMADZSreadMember'][msg.to] = {}
                                 aditmadzs.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ADITMADZSreadPoint'][msg.to]
                                 del Setmain['ADITMADZSreadMember'][msg.to]
                                 aditmadzs.sendMessage(msg.to, "CCTV berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cyduk":
                            if msg.to in Setmain['ADITMADZSreadPoint']:
                                if Setmain['ADITMADZSreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ADITMADZSreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Read Member ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(aditmadzs.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        aditmadzs.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ADITMADZSreadPoint'][msg.to]
                                        del Setmain['ADITMADZSreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ADITMADZSreadPoint'][msg.to] = msg.id
                                    Setmain['ADITMADZSreadMember'][msg.to] = {}
                                else:
                                    aditmadzs.sendMessage(msg.to, "User kosong...")
                            else:
                                aditmadzs.sendMessage(msg.to, "Ketik cctv on dulu")

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ADITMADZSlimit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                aditmadzs.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ADITMADZSlimit"])
                                    if jmlh <= 1000000:
                                        for x in range(jmlh):
                                            try:
                                                aditmadzs.sendMessage1(msg)
                                            except Exception as e:
                                                aditmadzs.sendMessage(msg.to,str(e))
                                    else:
                                        aditmadzs.sendMessage(msg.to,"KEBANYAKAN GOBLOK!")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = aditmadzs.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                aditmadzs.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        aditmadzs.sendMessage(msg.to,str(e))
                                else:
                                    aditmadzs.sendMessage(msg.to,"KEBANYAKAN BANGSAT!")

                        elif 'Run: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Run: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kd.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kf.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kg.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kh.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      sw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000000:
                                  for var in range(0,jumlah):
                                      aditmadzs.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      ki.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kk.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kc.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kb.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kd.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      ke.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kf.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kg.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      kh.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      sw.sendMessage(midd, str(Setmain["ADITMADZSmessage"]))
                                      
                        elif 'Mytoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX\n"+aditmadzs.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 1\n"+ki.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 2\n"+kk.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 3\n"+kc.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 4\n"+kb.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 5\n"+kd.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 6\n"+ke.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 7\n"+kf.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 8\n"+kg.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 9\n"+kh.authToken)
                               aditmadzs.sendMessage(msg.to,"SELFBOT-BY:MAX 10\n"+sw.authToken)
 
#===========Settings============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                 

                        elif 'Blockjs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Blockjs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Pro JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Pro JS diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Pro JS dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Pro JS sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                 

                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = aditmadzs.getGroup(msg.to)
                                       msgs = "Ghost diaktifkan\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Ghost dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost sudah tidak aktif"
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                                 

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "ALL protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = aditmadzs.getGroup(msg.to)
                                      msgs = "Sudah mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  aditmadzs.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "ALL protect sudah off\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = aditmadzs.getGroup(msg.to)
                                         msgs = "Sudah menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    aditmadzs.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = aditmadzs.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           aditmadzs.updateGroup(G)
                                           invsend = 0
                                           Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = aditmadzs.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           aditmadzs.updateGroup(X)
                                       except:
                                           pass

                        elif ("Fuck " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif text.lower() == 'super':
                            if msg._from in admin:
                                if msg.toType == 2:
                                    gs = aditmadzs.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                aditmadzs.updateGroup(gs)
                                invsend = 0
                                Ticket = aditmadzs.reissueGroupTicket(msg.to)
                                aditmadzs.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    aditmadzs.sendText(msg.to,"MAX KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[aditmadzs,ki,kk,kc,kb,kd,ke,kf,kg,kh]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                             
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           staff.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus Staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           Bots.remove(target)
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                aditmadzs.sendMessage(msg.to,"Refresh Done!")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = aditmadzs.getContact(i)
                                    aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                aditmadzs.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                aditmadzs.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                aditmadzs.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                aditmadzs.sendMessage(msg.to,"Auto respon dinonaktifkan")                   

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                aditmadzs.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                aditmadzs.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                aditmadzs.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                aditmadzs.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                aditmadzs.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                aditmadzs.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                aditmadzs.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                aditmadzs.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                aditmadzs.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                aditmadzs.sendMessage(msg.to,"Join Ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           aditmadzs.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           aditmadzs.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                aditmadzs.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +aditmadzs.getContact(m_id).displayName + "\n"
                                aditmadzs.sendMessage(msg.to,"»» Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    aditmadzs.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = aditmadzs.getContact(i)
                                        aditmadzs.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = aditmadzs.getContacts(wait["blacklist"])
                              mc = "[%i]User Blacklist" % len(ragets)
                              aditmadzs.sendMessage(msg.to,"Kalian di maafkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Leave Msg」\nLeave Msg diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  aditmadzs.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ADITMADZSmessage"] = spl
                                  aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               aditmadzs.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ADITMADZSmessage"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = aditmadzs.findGroupByTicket(ticket_id)
                                     aditmadzs.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     aditmadzs.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group4 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     kb.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group5 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     kd.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group6 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     ke.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group7 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     kf.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group8 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     kg.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))
                                     group9 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     kh.sendMessage(msg.to, "SELFBOT-BY:MAX JOIN GROUP : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
