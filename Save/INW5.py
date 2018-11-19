# -*- coding: utf-8 -*-

import SATAN2
from SATAN2.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, urllib, string, codecs, requests, ctypes, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = SATAN2.LINE()
#cl.nxtQRLogin()
cl.login(token="Era4eC6sUW8dpHogbwwa.LbxsILM+5RzanHjFSWhD/G.bhCGAdHKVxnw0j65Psffngp5bHPFftMRyDCPbWC01OU=")
#ki = SATAN2.LINE()
#ki.nxtQRLogin()

#ki2 = SATAN2.LINE()
#ki2.nxtQRLogin()

helpMsg = """
╔═════════════
║       NOXTAIN
╠═════════════
║ Owner : Satan
║ line://ti/p/~esic_
╠═════════════
║╔════════════
║║  Public Command
║╠═════════════
║║❂➣Time
║╚════════════
║╔════════════
║║      Command
║╠═════════════
║║❂➣Fb (text)
║║❂➣Gos (text)
║║❂➣Ins (username)
║║❂➣Wk (text)
║║❂➣Mus (text)
║║❂➣Idl (text)
║║❂➣Me
║║❂➣Time
║╠❂➣Blacklist
║╠❂➣Ban @
║╠❂➣Unban @
║╠❂➣Clearban
║╠❂➣Banlist
║╠❂➣Contact ban
║╠❂➣Midban
║╚════════════
║╔════════════
║║  Command in Group
║╠═════════════
║║❂➣Ginfo
║║❂➣Gid
║║❂➣Tagall
║╚════════════
║╔════════════
║║  Command Creator
║╠═════════════
║║❂➣Amessage: (text)
║║❂➣Lmessage:
║╚════════════
╚═════════════"""
Mid = cl.getProfile().mid
#Kmid = ki.getProfile().mid
#K2mid = ki2.getProfile().mid
#Bots = [cl,ki,ki2]
Admin = cl.getProfile().mid
Creator = "u4c9ac515f9763bea5f4bac3e1a00fa22"

SaveProfile = [cl]
#SaveProfile2 = [cl,ki,ki2]

#contact = SaveProfile.getProfile()
#backup = SaveProfile.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

wait = {
    "likeOn":False,
    "alwayRead":False,
    "detectMention":True,
    "kickMention":False,
    "steal":True,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""Thx for add me\n»»» http://line.me/ti/p/~esic_ «««""",
    "lang":"JP",
    "comment":"This is Auto Like by\n»»» http://line.me/ti/p/~esic_ «««",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "Wc":False,
    "Lv":False,
    'MENTION':True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Notifed":False,
    }
wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
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

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
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

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print(error)

def SelfBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    KickerR = [ki,ki2]
                    kicker = random.choice(KickerR)
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.kickoutFromGroup(op.param1,[op.param3])
                    kicker.updateGroup(G)
            else:
                cl.sendText(msg.to,"มีการปรับเปลี่ยน URL")

        if op.type == 17:
           if wait["Wc"] == True:
               if op.param2 in Bots:
                 return
               ginfo = cl.getGroup(op.param1)
               cl.sendText(op.param1, "Welcome")

        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1, "GoodBye")

        if op.type == 19:
           if wait["Notifed"] == True:
               if op.param2 in Bots:
                 return
               ginfo = cl.getGroup(op.param1)
               RandomR = ["ไม่น่าจะจุกเท่าไหร่หรอก"]
               RandomY = random.choice(RandomR)
               cl.sendText(op.param1, RandomY)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")

            elif msg.text is None:
                return
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Mid}
                cl.sendMessage(msg)

            elif 'Amessage: ' in msg.text.lower():
                if msg.form_ == Creator:
                    SetMessage = msg.text.replace("Amessage:","")
                    wait['message'] == SetMessage
                    SeeMessage = wait['message']
                    cl.sendText(msg.to,"Add Message : "+SetMessage)
                else:
                    cl.sendText(msg.to,"คุณไม่ใช่ผู้สร้าง")

            elif 'Lmessage: ' in msg.text.lower():
                if msg.form_ == Creator:
                    SetMessage = msg.text.replace("Lmessage:","")
                    wait["comment"] == SetMessage
                    SeeMessage = wait["comment"]
                    cl.sendText(msg.to,"Comment Message :"+SetMessage)
                else:
                    cl.sendText(msg.to,"คุณไม่ใช่ผู้สร้าง")

            elif msg.text in ["help","Help"]:
                cl.sendText(msg.to,helpMsg)
            elif msg.text.lower() == 'Ginfo':
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้ใช้เก่า"
                    md = "[ ชื่อกลุ่ม : " + group.name + "]\n\n[ ID กลุ่ม : " + group.id + "]\n\n[ ผู้สร้างกลุ่ม : " + gCreator + "]\n\n[ รูปกลุ่ม ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nURL : เปิด"
                    else: md += "\n\nURL : ปิด"
                    if group.invitee is None: md += "\n[ สมาชิกกลุ่ม " + str(len(group.members)) + " คน ]" + "\n[ ค้างเชิญ 0 ตน ]"
                    else: md += "\n[ สมาชิกกลุ่ม : " + str(len(group.members)) + " คน ]" + "\n[ ค้างเชิญ " + str(len(group.invitee)) + " ตน ]"
                    cl.sendText(msg.to,md)
            elif msg.text.lower() == 'Gid':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)

            elif "Fb" in msg.text:
                    a = msg.text.replace("Fb ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "ลิงก์ : https://www.facebook.com" + b)
            elif "Tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     cl.sendText(msg.to, "ผู้ใช้เยอะกว่า 500 คน")
                 cnt = Message()
                 cnt.text = "ผู้ใช้ทั้งหมด :\n" + str(jml) +  " คน"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
            elif "Gos" in msg.text:
                    a = msg.text.replace("Gos ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to, "ลิงก์ : https://www.google.com/" + b)

            elif 'Ins ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("Ins ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "ชื่อ : " + text[-2] + "\n"
                    user1 = "ขื่อผู้ใช้ : " + text[-1] + "\n"
                    followers = "ผู้ติดตามทั้งหมด : " + text[0] + "\n"
                    following = "ผู้ติดตามขณะนี้ : " + text[2] + "\n"
                    post = "โพสต์ : " + text[4] + "\n"
                    link = "ลิงก์ : " + "https://www.instagram.com/" + instagram
                    detail = "** ข้อมูล INSTAGRAM **\n"
                    details = "\n** ข้อมูล INSTAGRAM **"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as e:
                	cl.sendText(msg.to, str(e))

            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="หัวข้อ ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="โปรดคลิ้กลิงก์นี้\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif "Mus " in msg.text:
                try:
                    songname = msg.text.lower().replace("Mus ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'ผลจากการค้นหา\n'
                        hasil += 'ชื่อเพลง : ' + song[0]
                        hasil += '\nระยะเวลา : ' + song[1]
                        hasil += '\nลิงก์ดาวน์โหลด : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "โปรดรอคลิปเสียง...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))

            elif "Idl " in msg.text:
                msgg = msg.text.replace('Idl ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)

            elif "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,"เวลาตอนนี้\n"+datetime.today().strftime('%H:%M:%S'))
        if op.type == 26:
            msg = op.message
            if "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,"เวลาตอนนี้\n"+datetime.today().strftime('%H:%M:%S'))
            elif 'Amessage: ' in msg.text.lower():
                if msg.form_ == Creator:
                    SetMessage = msg.text.replace("Amessage:","")
                    wait['message'] == SetMessage
                    SeeMessage = wait['message']
                    cl.sendText(msg.to,"Add Message : "+SetMessage)
                else:
                    cl.sendText(msg.to,"คุณไม่ใช่ผู้สร้าง")

            elif 'Lmessage: ' in msg.text.lower():
                if msg.form_ == Creator:
                    SetMessage = msg.text.replace("Lmessage:","")
                    wait["comment"] == SetMessage
                    SeeMessage = wait["comment"]
                    cl.sendText(msg.to,"Comment Message :"+SetMessage)
                else:
                    cl.sendText(msg.to,"คุณไม่ใช่ผู้สร้าง")

        if op.type == 59:
            print(op)

    except Exception as error:
        print(error)
def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print("Like")
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
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
            SelfBot(Op)
