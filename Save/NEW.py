# -*- coding: utf-8 -*-

import SATAN
from SATAN.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib.request import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

#==========================================================================================================

cl = SATAN.LINE()
cl.login(token='ErIilHsa2CBOYcWFGn53.qhYrC9fJKChpsjftiBBIKW.mrHz1EYyQtlmaJVWVCuvk5JhAZCtVp+JrfZjD7OxxQ0= ')

ki = SATAN.LINE()
ki.login(token='Era4eC6sUW8dpHogbwwa.LbxsILM+5RzanHjFSWhD/G.bhCGAdHKVxnw0j65Psffngp5bHPFftMRyDCPbWC01OU=')

ki.loginResult()
cl.loginResult()

#==========================================================================================================

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessageTH = """
╔══════════════════
║       LAST GUN
╠══════════════════
║❂ Me
║☆➣ บอทส่งคอนแทค
║❂ LastGun:SettingView
║☆➣ ดูการตั้งค่า
║❂ LastGun:CommandSetting
║☆➣ ดูการคำสั่งตั้งค่าบอท
║❂ LastGun:Banlist
║☆➣ ดูบัญชีดำ
║❂ LastGun:Reinvite
║☆➣ เรียกบอทกลับ
║❂ LastGun:Check
║☆➣ เช็คบอท
║❂ LastGun:Bye
║☆➣ บอทออก
║❂ COMMING SOON
║☆➣ COMMING SOON
╚══════════════════
"""
helpMessageEN = """
╔══════════════════
║       LAST GUN
╠══════════════════
║❂ Me
║☆➣ Bot send your contact
║❂ LastGun:SettingView
║☆➣ View setting
║❂ LastGun:CommandSetting
║☆➣ View command setting
║❂ LastGun:Banlist
║☆➣ View blacklist
║❂ LastGun:Reinvite
║☆➣ Reinvite bot
║❂ LastGun:Check
║☆➣ Check bot
║❂ LastGun:Bye
║☆➣ Bot exit
║❂ COMMING SOON
║☆➣ COMMING SOON
╚══════════════════
"""
KAC = [cl,ki]
Amid = cl.getProfile().mid
Bmid = ki.getProfile().mid
Creator = "u541bbaba15d68f3a652106a0de5a3e94"
Bots = [Creator,Amid,Bmid]
LastGun1 = {
    "Zxc1":True,
    "Zxc2":True,
    "Zxc3":True,
    }
LastGun2 = {
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    }

LastGun3 = {
    "lang":"TH"
    }

LastGun4 = {
    "lang":"EN"
    }

LastGunComment = {
    "comment":"AUTO LIKE BY @SATAN @NOXTAIN"
    }

banned = LastGun2["blacklist"]
nobanned = LastGun2["whitelist"]

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

Rapid1To = ""

def Rapid1Say(mtosay):
    cl.sendText(Rapid1To,mtosay)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 19:
            if Amid in op.param3:
                LastGun2["blacklist"][op.param2] = True
		if op.type == 25:
			if Amid in op.param3:
				if wait["blacklist"] == True:
					ki.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if Amid in op.param3:
				if wait["blacklist"] == True:
					ki.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if Amid in op.param3:
				if wait["blacklist"] == True:
					ki.kickoutFromGroup(op.param1,[op.param2])
            if Bmid in op.param3:
                LastGun2["blacklist"][op.param2] = True
		if op.type == 25:
			if Bmid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 32:
			if Bmid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
		if op.type == 25:
			if Bmid in op.param3:
				if wait["blacklist"] == True:
					cl.kickoutFromGroup(op.param1,[op.param2])
					
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                try:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        pass
                    except:
                        pass
                    if op.param2 in banned:
                        pass
                    if op.param2 in nobanned:
                        pass
                    else:
                        LastGun2["blacklist"][op.param2] = True
                    G = ki.getGroup
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in baned:
                        pass
                    if op.param2 in nobanned:
                        pass
                    else:
                        LastGun2["blacklist"][op.param2] = True
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                try:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        pass
                    except:
                        pass
                    if op.param2 in banned:
                        pass
                    if op.param2 in nobanned:
                        pass
                    else:
                        LastGun2["blacklist"][op.param2] = True
                    G = ki.getGroup
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if op.param2 in baned:
                        pass
                    if op.param2 in nobanned:
                        pass
                    else:
                        LastGun2["blacklist"][op.param2] = True
                    
        if op.type == 26:
            msg = op.message
            if msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "[ POST URL ]" + msg.contentMetadata["postEndUrl"]
                else:
                    msg.text = "[ POST URL ]" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
        if op.type == 26:
            msg = op.message
            if "Test" in msg.text.lower():
                pass
            elif msg.text is None:
                return
            elif msg.text in ["help","Help","Cmd"]:
                if LastGun3["lang"] == "TH":
                    cl.sendText(msg.to,helpMessageTH)
                else:
                    cl.sendText(msg.to,helpMessageEN)
	    elif msg.text.lower() == 'Me':
                CheckMe = msg.from_
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': CheckMe}
                cl.sendMessage(msg)
            elif "LastGun:Check" == msg.text:
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
            elif "LastGun:Reinvite" in msg.text:
                X = ki.getGroup(msg.to)
                X.preventJoinByTicket = False
                invsend = 0
                Ti = cl.reissueGroupTicket(msg.to)
                cl.acceptGroupInvitationByTicket(msg.to,Ti)
                ki.acceptGroupInvitationByTicket(msg.to,Ti)
                G = ki.getGroup(msg.to)
                G.preventJoinByTicket = True
                Ticket = ki.reissueGroupTicket(msg.to)
                    
        if op.type == 59:
            print(op)

    except Exception as error:
        print(error)
        
def AutoLike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=AutoLike)
thread1.daemon = True
thread1.start()

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
    
def nameUpdate():
    while True:
        try:
            if wait["clock"] == True:
                pass
            time.sleep(10)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
