# -*- coding: utf-8 -*-

import SATAN2
from SATAN2.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, urllib, string, codecs, requests, ctypes, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = SATAN2.LINE()
cl.nxtQRLogin()

Kicker = [cl]
OMG = "0.1.2"
Amid = cl.getProfile()
Creator = "u4c9ac515f9763bea5f4bac3e1a00fa22"
Admin = cl.getProfile()
ListList = [Amid,Creator]
wait = {
    "AutoAdd":True,
    "message":"THX FOR ADD ME\n\nline.me/ti/p/~esci_",
    "Protection":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "leaveRoom":True,
    "Like":True,
    "Comment":True,
    "CommentText":"THIS IS AUTO LIKE BY\nSATAN\nline.me/ti/p/~esci_",
    "MemberJoin":"Hi",
    "MemberLeave":"Bye",
    "MemberKick":"Wow",
    "Op1":False,
    "Op2":False,
    "Op3":False,
	"lang":"TH",
    "Tag":False,
}

setting1 = {
    "MemberJoin":"Hi"
}

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    global start_runtime
    try:
        if op.type == 0:
            return
        if op.type == 25:
            msg = op.message
            if msg.text in ["Me","me"]:
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': Admin}
                cl.sendMessage(msg)

            elif msg.text is None:
                return

            elif msg.text in ["Opp1"]:
                cl.sendText(msg.to,"Opp1 is "+wait["MemberJoin"])
            elif "Opp1:" in msg.text:
                SetOpp = msg.text.replace("Opp1:","")
                cl.sendText(msg.to,"Set Opp1 to "+SetOpp)
                wait["MemberJoin"] = SetOpp
            elif msg.text in ["Opp1 on"]:
                if wait["Op1"] == True:
                    cl.sendText(msg.to,"เปิดอยู่แล้ว")
                else:
                    wait["Op1"] = True
                    cl.sendText(msg.to,"เปิดเรียบร้อยแล้ว")
            elif msg.text in ["Opp1 off"]:
                if wait["Op1"] == False:
                    cl.sendText(msg.to,"ปิดอยู่แล้ว")
                else:
                    wait["Op1"] = False
                    cl.sendText(msg.to,"ปิดเรียบร้อยแล้ว")
            elif msg.text in ["Opp2"]:
                cl.sendText(msg.to,"Opp2 is "+wait["MemberJoin"])
            elif "Opp2:" in msg.text:
                SetOpp = msg.text.replace("Opp2:","")
                cl.sendText(msg.to,"Set Opp2 to "+SetOpp)
                wait["MemberKick"] = SetOpp

            elif msg.text in ["Opp2 on"]:
                if wait["Op2"] == True:
                    cl.sendText(msg.to,"เปิดอยู่แล้ว")
                else:
                    wait["Op2"] = True
                    cl.sendText(msg.to,"เปิดเรียบร้อยแล้ว")
            elif msg.text in ["Opp2 off"]:
                if wait["Op2"] == False:
                    cl.sendText(msg.to,"ปิดอยู่แล้ว")
                else:
                    wait["Op2"] = False
                    cl.sendText(msg.to,"ปิดเรียบร้อยแล้ว")

            elif msg.text in ["Opp3"]:
                cl.sendText(msg.to,"Opp3 is "+wait["MemberLeave"])
            elif "Opp3:" in msg.text:
                SetOpp = msg.text.replace("Opp3:","")
                cl.sendText(msg.to,"Set Opp3 to "+SetOpp)
                wait["MemberLeave"] = SetOpp

            elif msg.text in ["Opp3 on"]:
                if wait["Op3"] == True:
                    cl.sendText(msg.to,"เปิดอยู่แล้ว")
                else:
                    wait["Op3"] = True
                    cl.sendText(msg.to,"เปิดเรียบร้อยแล้ว")
            elif msg.text in ["Opp3 off"]:
                if wait["Op3"] == False:
                    cl.sendText(msg.to,"ปิดอยู่แล้ว")
                else:
                    wait["Op3"] = False
                    cl.sendText(msg.to,"ปิดเรียบร้อยแล้ว")

        if op.type == 26:
            msg = op.message
            if msg.text in ["Me","me"]:
                msg.text = None
                msg.contentType = 13
                msg.contentMetadata = {'mid': Admin}
                cl.sendMessage(msg)

            elif msg.text is None:
                return

            elif msg.text in ["Hp","Help","คำสั่ง"]:
                nowTimeis = datetime.now()
                nowH = datetime.strftime(nowTimeis,"%H")
                nowM = datetime.strftime(nowTimeis,"%M")
                nowS = datetime.strftime(nowTimeis,"%S")
                tm = "\nNow : "+nowH+":"+nowM+":"+nowS
                HelpMessage = """
SLC PREMIUM
: BETA
Date : 5/2/2018"""+tm+"""

ใส่ / หน้าคำส่ง

- ps
! search play store
- gos
! search google
- yt
! search youtube
- gl
! search gitlab
- tagall
! แท็กสมาชิกในห้องทั้งหมด
- LinkId
! แอดด้วยลิงก์

 @coming soon

- ตั้งเวลา
! ตั้งจุดอ่าน
- อ่าน
! ดูคนที่อ่าน
- reinvite
! เรียกบอทกลับ
"""
                cl.sendText(msg.to,HelpMessage)
            elif "/ps" in msg.text:
                Title = msg.text.replace("/ps ","")
                Source = "Google Play"
                Link = "https://play.google.com/store/search?q="+Title
                Msgtextt = "Title : "+Title+"\nSource : "+Source+"\nLink : "+Link
                cl.sendText(msg.to,Msgtextt)
            elif "/gos" in msg.text:
                Title = msg.text.replace("/gos ","")
                Link = "https://www.google.co.th/search?q="+Title
                Msgtextt = "Title : "+Title+"\nLink : "+Link
                cl.sendText(msg.to,Msgtextt)
            elif "/yt" in msg.text:
                try:
                    textToSearch = (msg.text).replace('/yt ', "").strip()
                    query = urllib.parse.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib.request.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    Msgtextt = 'Title : '+textToSearch+'\nLink : https://www.youtube.com' + results['href']
                    cl.sendText(msg.to,Msgtextt)
                except:
                    cl.sendText(msg.to,"Could not find it")
            elif "/gl" in msg.text:
                gitlabuser = msg.text.replace("/gl ","")
                Source = gitlabuser
                Link = "https://gitlab.com/"+Source
                cl.sendText(msg.to,"User : "+Source+"\nLink : "+Link)

            elif "/go" in msg.text.lower():
                spl = re.split("/go","")
                if spl[0] == "":
                    if spl[1] != "":
                        try:
                            if msg.toType != 0:
                                cl.sendText(msg.to,"")
                            else:
                                cl.sendText(msg.from_,"")
                            resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                            text = "Result :\n"
                            for el in resp.findAll("h3",attrs={"class":"r"}):
                                try:
                                    tmp = el.a["class"]
                                    continue
                                except:
                                    pass
                                try:
                                    if el.a["href"].startswith("/search?q="):
                                        continue
                                except:
                                    continue
                                text += el.a.text+"\n"
                                text += str(el.a["href"][3:]).split("&sa=U")[0]+"\n\n"
                            text = text[:-2]
                            if msg.toType != 0:
                                cl.sendText(msg.to,str(text))
                            else:
                                cl.sendText(msg.from_,str(text))
                        except Exception as e:
                            print(e)

            elif "/tagall" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in range(k+1):
                    msg = Message(to=msg.to)
                    txt = ''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += '@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)

    except Exception as e:
        print(e)


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
