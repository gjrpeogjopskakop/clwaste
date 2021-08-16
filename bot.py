# coding: utf-8 -*-
from linepy import *
from thrift.Thrift import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import concurrent.futures as cf
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse,timeit,atexit,youtube_dl,pafy,shutil,asyncio,pafy
from threading import Thread
####################################################
#↓↓↓↓↓↓↓↓↓json載入↓↓↓↓↓↓↓↓↓↓↓↓↓
read = json.load(codecs.open("read.json","r","utf-8"))
###############################
settings = json.load(codecs.open("temp.json","r","utf-8"))
###############################
warmods = json.load(codecs.open("warmods.json","r","utf-8"))
###############################
red = json.load(codecs.open("red.json","r","utf-8"))
###############################
jg = json.load(codecs.open("jg.json","r","utf-8"))
###############################
ban = json.load(codecs.open("ban.json","r","utf-8"))
###############################
ig = json.load(codecs.open("ig.json","r","utf-8"))
###############################
owner = json.load(codecs.open("owner.json","r","utf-8"))
###############################
ckt = json.load(codecs.open("cktext.json","r","utf-8"))
#↑↑↑↑↑↑↑↑↑json載入↑↑↑↑↑↑↑↑↑↑↑↑↑
#↓↓↓↓↓↓↓↓↓json定義↓↓↓↓↓↓↓↓↓↓↓↓↓
#errorsend = owner["error"]#噴錯回傳
background = owner["dio"]#後台
boomsend = owner["kick"]#炸群發話
gbye = owner["rbye"]#退群指令
botcreator = owner["creator"]#半垢作者
botowner = owner["owner"]#半垢主人
owners = owner["owners"]#半垢主人(友資)
cmdkick = owner["cmdkick"]#炸群指令
jkon = owner["jkon"]#rk指令
jkoff = owner["jkoff"]#rk指令
waron = owner["waron"]#戰爭指令
waroff = owner["waroff"]#戰爭指令
allon = owner["allon"]#全開指令
alloff = owner["alloff"]#全開指令
ivon = owner["ivon"]#回拉指令
ivoff = owner["ivoff"]#回拉指令
kivon = owner["kivon"]#踢回拉指令
kivoff = owner["kivoff"]#踢回拉指令
version = owner["version"]#登入版本
update = owner["update"]#更新內容
account = owner["account"]#帳密
passwd = owner["passwd"]#帳密
Backstage = owner["filename"]#檔案名稱
#↑↑↑↑↑↑↑↑↑json定義↑↑↑↑↑↑↑↑↑↑↑↑↑
#↓↓↓↓↓↓↓↓↓帳密登入↓↓↓↓↓↓↓↓↓↓↓↓↓
print("——————專武垢開始登入—————————")
try:cl = LINE(krl01286@eoopy.com,WERSD123)
except Exception as e:
    print(e)
    sleep(1)
    print("——————專武垢登入介面—————————")
    login = input("\n\n\n\n1.半垢登入\n2.更改後台\n3.更改炸群指令\n4.更改炸群發話\n5.取消登入\n\n\n\n——————沙雕專武垢登入介面—————————\n您想使用的是：")
    if login.lower() == '1':#1-半垢登入選擇
        try:cl = LINE(account,passwd)
        except Exception as e:
            print(e)
            sleep(1)
            print("————————————————————————")
            a = input("\n\n\n\n你想要使用的是:\n\n\n1.電子信箱以及密碼\n2.網址qr登入\n3.取消登入\n\n\n\n\n\n\n————————————————————————\n你想要使用的是:")
            if a.lower() == '1':
                account = input("請輸入要登入的信箱:")
                passwd = input("請輸入要登入的密碼:")
                try:
                    cl = LINE(account,passwd)
                    owner["account"] = account
                    owner["passwd"] = passwd
                    json.dump(owner, codecs.open('./backupData/owner.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
                except Exception as e:
                    print(e)
                    sleep(1)
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
            if a.lower() == '2':
                print("網址登入")
                sleep(0.5)
                cl = LINE()
            if a.lower() == '3':
                print("取消登入")
                os._exit(0)
    if login.lower() == '2':#2-更改後台
        print("更改後台位置")
        b = input("請輸入你要更改的後台位置:")
        owner["dio"] = b
        json.dump(owner, codecs.open('./backupData/owner.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        print("更改完成 將自動重啟檔案")
        sleep(1)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    if login.lower() == '3':#3-更改炸群指令
        print("更改炸群指令")
        b = input("請輸入你要更改的炸群指令:")
        owner["cmdkick"] = b
        json.dump(owner, codecs.open('./backupData/owner.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        print("更改完成 將自動重啟檔案")
        sleep(1)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    if login.lower() == '4':#4-更改炸群發話
        print("更改炸群發話")
        b = input("請輸入你要更改的炸群發話:")
        owner["kick"] = b
        json.dump(owner, codecs.open('./backupData/owner.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        print("更改完成 將自動重啟檔案")
        sleep(1)
        python = sys.executable
        os.execl(python, python, *sys.argv)
    if login.lower() == '5':#5-取消登入
        print("取消登入")
        os._exit(0)
#↑↑↑↑↑↑↑↑↑帳密登入↑↑↑↑↑↑↑↑↑↑↑↑↑
#↓↓↓↓↓↓↓↓↓↓↓↓↓載入↓↓↓↓↓↓↓↓↓↓↓↓↓
ts = time.time()
oepoll = OEPoll(cl)
myProfile = {
    "displayName": "",
    "statusMessage": "",
    "pictureStatus": ""
}
###############################
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
###############################
if clMID not in ban["admin"]:
    ban["admin"].append(clMID)
if botowner not in ban["admin"]:
    ban["admin"].append(botowner)
if botcreator not in ban["admin"]:
    ban["admin"].append(botcreator)
###############################
if clMID not in ig["ig"]:
    ig["ig"].append(clMID)
if botowner not in ig["ig"]:
    ig["ig"].append(botowner)
if botcreator not in ig["ig"]:
    ig["ig"].append(botcreator)
###############################
msg_dict = {}
#↓↓↓↓↓↓↓↓↓wait定義↓↓↓↓↓↓↓↓↓↓↓↓↓
wait = {
    'logout': {},
    'rapidFire': {},
    'group': "",
    'getmid': False,
    'um': False,#收回高速
    'cvp': False,#更換頭貼
    'gbc':{},
    'resset': False,#偵測更新
    'iv': True,#回邀
    'kiv': False,#回邀踢
    'ban': False,#黑單
    'unban': False,#解黑
    'cpi': False,#改頭
    'ctmid': False#友資mid
    }
#↓↓↓↓↓↓↓↓↓wait2定義↓↓↓↓↓↓↓↓↓↓↓↓
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
#↓↓↓↓↓↓↓↓↓廣播系統定義↓↓↓↓↓↓↓↓↓↓
rgb = {
    'pic':False,
    'picsender':{},
    'pictext':{},
    'contact':False,
    'contactsender':{},
    'contacttext':{},
    'post':False,
    'postsender':{}
}
###############################
setTime = {}
setTime = wait2['setTime']
mulai = time.time()
#↓↓↓↓↓↓↓↓↓↓def定義↓↓↓↓↓↓↓↓↓↓↓↓↓
def color():
    color_num1 = ["0", "1"]
    color_num2 = ["31", "32", "33", "34", "35", "36", "37"]
    color_list = [
        "\033[0;32;31m",
        "\033[0;32;32m",
        "\033[0;32;34m",
        "\033["+random.choice(color_num1)+";"+random.choice(color_num2)+"m"]
    return random.choice(color_list)
def Runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '【 %02d天 %02d時 %02d鐘 %02d秒】\n以上為ProMa運行時間' % (days, hours, mins, secs)
def Rtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 天 %02d 時 %02d 鐘 %02d 秒' % (days, hours, mins, secs)
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
def ismid(mid):
    try:
        cl.getContact(mid)
        return True
    except:
        return False
def restartBot():
    print ("重啟中")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        json.dump(read,codecs.open("read.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(settings,codecs.open("temp.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(warmods,codecs.open("warmods.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(red,codecs.open("red.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(jg,codecs.open("jg.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(owner,codecs.open("owner.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
        json.dump(ckt, codecs.open('cktext.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@bianyuanoo "
    if mids == []:
        raise Exception("Invaliod mids")
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
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 
def ytdl(url):
	video = pafy.new(url)
	best = video.getbest() 
	best.download(filepath="cvp.mp4")
#↓↓↓↓↓↓↓↓↓txt指令表↓↓↓↓↓↓↓↓↓↓↓↓↓
def help():#指令總表
    f = open('help.txt','r',encoding="UTF-8")
    return f.read()
def help1():#一般功能
    f = open('help1.txt','r',encoding="UTF-8")
    return f.read()
def help2():#基本功能
    f = open('help2.txt','r',encoding="UTF-8")
    return f.read()
def help3():#踢人/取消
    f = open('help3.txt','r',encoding="UTF-8")
    return f.read()
def help4():#開關
    f = open('help4.txt','r',encoding="UTF-8")
    return f.read()
def help5():#專武
    f = open('help5.txt','r',encoding="UTF-8")
    return f.read()
def help6():#權限設定
    f = open('help6.txt','r',encoding="UTF-8")
    return f.read()
def help7():#專屬指令表
    f = open('help7.txt','r',encoding="UTF-8")
    return f.read()
def help8():#群組指令
    f = open('help8.txt','r',encoding="UTF-8")
    return f.read()
def help9():#其他指令
    f = open('help9.txt','r',encoding="UTF-8")
    return f.read()
def unsend(msgid):
    sleep(1)
    cl.unsendMessage(msgid)
#↓↓↓↓↓↓↓↓↓線程設置↓↓↓↓↓↓↓↓↓↓↓↓↓
#專武登入
def ttk_login_thread(line_token):
    a = LINE(idOrAuthToken=line_token)
    ttk_pool.append(a)
#專武登入
def can_login_thread(line_token):
    a = LINE(idOrAuthToken=line_token)
    can_pool.append(a)
#專武登入
def jk_login_thread(line_token):
    a = LINE(idOrAuthToken=line_token)
    jk_pool.append(a)
#專武登入
def free_login_thread(line_token):
    a = LINE(idOrAuthToken=line_token)
    free_pool.append(a)
#專武踢人
def kick_out_thread(cl, group, who):
    try:
        cl.kickoutFromGroup(group, [who])
    except:
        pass
    if cl in in_ttk_pool:
        in_ttk_pool.remove(cl)
#專武取消
def cancel_thread(cl, group, who):
    try:
        cl.cancelGroupInvitation(group, [who])
    except:
        pass
    if cl in in_can_pool:
        in_can_pool.remove(cl)
#專武取消
def jk_thread(cl, group, who):
    try:
        cl.kickoutFromGroup(group, [who])
    except:
        pass
    if cl in in_jk_pool:
        in_jk_pool.remove(cl)
#專武取消
def free_thread(cl, group, who):
    try:
        cl.kickoutFromGroup(group, [who])
    except:
        cl.cancelGroupInvitation(group, [who])
    if cl in in_free_pool:
        in_free_pool.remove(cl)
#專武執行
def thread_exe(group, targets):
    if targets != []:
        threads = []
        for target in targets:
            find_worker = False
            for char in ttk_pool:
                if char not in in_ttk_pool:
                    find_worker = True
                    in_ttk_pool.append(char)
                    t = threading.Thread(target=kick_out_thread, args= (char, group, target))
                    threads.append(t)
                    break
            if find_worker == False:
                break
        for td in threads:
            td.start()
        all_thread_done = False
        while all_thread_done == False:
            try:
                for td in threads:
                    td.join()
                all_thread_done = True
                break
            except:
                pass
#專武執行
def cancel_exe(group, targets):
    if targets != []:
        threads = []
        for target in targets:
            find_worker = False
            for char in ttk_pool:
                if char not in in_ttk_pool:
                    find_worker = True
                    in_ttk_pool.append(char)
                    t = threading.Thread(target=cancel_thread, args= (char, group, target))
                    threads.append(t)
                    break
            if find_worker == False:
                break
        for td in threads:
            td.start()
        all_thread_done = False
        while all_thread_done == False:
            try:
                for td in threads:
                    td.join()
                all_thread_done = True
                break
            except:
                pass
#專武執行
def joinkick_exe(group, targets):
    if targets != []:
        threads = []
        for target in targets:
            find_worker = False
            for char in jk_pool:
                if char not in in_jk_pool:
                    find_worker = True
                    in_jk_pool.append(char)
                    t = threading.Thread(target=jk_thread, args= (char, group, target))
                    threads.append(t)
                    break
            if find_worker == False:
                break
        for td in threads:
            td.start()
        all_thread_done = False
        while all_thread_done == False:
            try:
                for td in threads:
                    td.join()
                all_thread_done = True
                break
            except:
                pass
#專武執行
def free_exe(group, targets):
    if targets != []:
        threads = []
        for target in targets:
            find_worker = False
            for char in free_pool:
                if char not in in_free_pool:
                    find_worker = True
                    in_free_pool.append(char)
                    t = threading.Thread(target=free_thread, args= (char, group, target))
                    threads.append(t)
                    break
            if find_worker == False:
                break
        for td in threads:
            td.start()
        all_thread_done = False
        while all_thread_done == False:
            try:
                for td in threads:
                    td.join()
                all_thread_done = True
                break
            except:
                pass
#============================踢人專武變數
TOTAL_ttk = int(150)
ttk_pool = []
in_ttk_pool = []
ttk_threads = []
line_token = cl.authToken
#============================取消專武變數
TOTAL_can = int(100)
can_pool = []
in_can_pool = []
can_threads = []
line_token = cl.authToken
#============================JK專武變數
TOTAL_jk = int(40)
jk_pool = []
in_jk_pool = []
jk_threads = []
line_token = cl.authToken
#============================隨機專武變數
TOTAL_free = int(10)
free_pool = []
in_free_pool = []
free_threads = []
line_token = cl.authToken
#============================專武登入
print(color()+"===== 踢人專武系統開始登入 =====")
c=1
for number in range(TOTAL_ttk):
    t = threading.Thread(target=ttk_login_thread, args=(line_token,))
    ttk_threads.append(t)
    print("【登入 "+str(c)+" 線程】-----踢人線程登入完畢")
    c+=1
for td in ttk_threads:
    td.start()
all_thread_done = False
while all_thread_done == False:
    try:
        for td in ttk_threads:
            td.join()
        all_thread_done = True
        break
    except:
        print("線程尚未準備好")
print("===== 踢人專武系統登入完成 =====")
print(color()+"===== 取消專武系統開始登入 =====")
for number in range(TOTAL_can):
    t = threading.Thread(target=can_login_thread, args=(line_token,))
    can_threads.append(t)
    print("【登入 "+str(c)+" 線程】-----取消線程登入完畢")
    c+=1
for td in can_threads:
    td.start()
all_thread_done = False
while all_thread_done == False:
    try:
        for td in can_threads:
            td.join()
        all_thread_done = True
        break
    except:
        print("線程尚未準備好")
print("===== 取消專武系統登入完成 =====")
print(color()+"===== 進群踢專武系統開始登入 =====")
for number in range(TOTAL_jk):
    t = threading.Thread(target=jk_login_thread, args=(line_token,))
    jk_threads.append(t)
    print("【登入 "+str(c)+" 線程】-----進群踢線程登入完畢")
    c+=1
for td in jk_threads:
    td.start()
all_thread_done = False
while all_thread_done == False:
    try:
        for td in jk_threads:
            td.join()
        all_thread_done = True
        break
    except:
        print("線程尚未準備好")
print("===== 進群踢專武系統登入完成 =====")
print(color()+"===== 自由線程系統開始登入 =====")
for number in range(TOTAL_free):
    t = threading.Thread(target=free_login_thread, args=(line_token,))
    free_threads.append(t)
    print("【登入 "+str(c)+" 線程】-----自由線程登入完畢")
    c+=1
for td in free_threads:
    td.start()
all_thread_done = False
while all_thread_done == False:
    try:
        for td in free_threads:
            td.join()
        all_thread_done = True
        break
    except:
        print("線程尚未準備好")
print("===== 自由線程系統登入完成 =====")
print(color()+"登入者名稱:"+clProfile.displayName+"\n登入半垢MID:"+clMID)
print("===== 專武半垢全系統已登入完成 =====")
try:
    cl.sendMessage(background,"【自動發送】\n邊緣專武垢登入成功\n➜版本號:{version}\n➜登錄時間:{time}\n➜踢人線程數:{third}\n➜取消線程數:{cancel}\n➜進群踢線程數:{jk}\n➜額外線程數:{free}\n➜全部登入線程:{allth}".format(version=version,time=(time.time() -ts),third=(TOTAL_ttk),cancel=(TOTAL_can),jk=(TOTAL_jk),free=(TOTAL_free),allth=(TOTAL_ttk+TOTAL_can+TOTAL_jk+TOTAL_free)))
    cl.sendMessage(background,"【半垢更新內容】\n目前版本號:{version}\n更新內容如下\n{update}".format(version=version,update=update))
except:
    cl.sendMessage(botowner,"【自動發送】\n沙雕專武垢登入成功\n➜版本號:{version}\n➜登錄時間:{time}\n➜踢人線程數:{third}\n➜取消線程數:{cancel}\n➜進群踢線程數:{jk}\n➜額外線程數:{free}\n➜全部登入線程:{allth}".format(version=version,time=(time.time() -ts),third=(TOTAL_ttk),cancel=(TOTAL_can),jk=(TOTAL_jk),free=(TOTAL_free),allth=(TOTAL_ttk+TOTAL_can+TOTAL_jk+TOTAL_free)))
    cl.sendMessage(botowner,"【半垢更新內容】\n目前版本號:{version}\n更新內容如下\n{update}".format(version=version,update=update))
    cl.sendMessage(botowner,"請把半垢拉到回傳後台")
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 1:#更新個人資料
            print ("更新配置文件")
        if op.type == 5:#加友
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
        if op.type == 13 or op.type == 124:#邀請13 邀請124
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            if clMID in op.param3:#自動入群
                if settings["autoJoin"] == True:
                    try:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(background,"通知邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
                    except Exception as error:
                        print(error)
            if settings["autoJoin"] == False:#作者自動入群
                if op.param2 in botcreator:
                    if clMID in op.param3:
                        try:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendMessage(background,"通知作者邀請群組:\n" + str(group.name)+"群組 \n"+ str(group.id)+ "\n邀請者:\n" + contact1.displayName + "\nMid:\n" + contact1.mid)
                        except Exception as error:
                            print(error)
            if clMID in op.param3:#進群炸
                if settings["autoJoinkick"] == True:
                    targets = []
                    for g in group.members:
                        if g.mid not in ban["admin"]:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(op.param1,"此群成員皆位於權限名單中")
                        settings["autoJoinkick"] = False
                        cl.sendMessage(op.param1,"已自動關閉進群翻")
                    else:
                        warmods["warmods"][op.param1] = True
                        cl.sendMessage(op.param1,boomsend)
                        thread_exe(op.param1,targets)
                        settings["autoJoinkick"] = False
                        cl.sendMessage(op.param1,"蹦群完成 已自動關閉進群翻")
        if op.type == 15 or op.type == 128:#退群15 退群128
            if settings["seeLeave"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('[提示]\n')
                    arr = []
                    mention = "@yuan "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + "退出了 {} 群組 離我們而去了OAO！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
        if op.type == 60 and op.param1 in jg["JoinGroup"] and op.param2 not in ban["admin"]:#進群踢
            joinkick_exe(op.param1,[op.param2])
        #===========NEW WAR=========#
        if op.type in [11,13,17,19,122,124,130,133]:#戰爭踢人
            if op.param1 in warmods["warmods"]:
                if op.param2 not in ban["admin"]:
                    thread_exe(op.param1,[op.param2])
        if op.type == 11 or op.type == 122:#戰爭網址
            if op.param1 in warmods["warmods"]:
                group = op.param1
                if group.preventedJoinByTicket == True:
                    pass
                else:
                    group.preventedJoinByTicket = True
                    cl.updateGroup(group)
        if op.type == 13 or op.type == 124:#戰爭取消
            if op.param1 in warmods["warmods"]:
                if op.param3 not in ban["admin"]:
                    cancel_exe(op.param1,[op.param3])
        #===========NEW WAR=========#
        if op.type == 17:#入群17 60 入群60 130
            if settings["seeJoin"] == True:
                contact1 = cl.getContact(op.param2)
                group = cl.getGroup(op.param1)
                try:
                    arrData = ""
                    text = "%s "%('歡迎')
                    arr = []
                    mention = "@yuan "
                    slen = str(len(text))
                    elen = str(len(text) + len(mention) - 1)
                    arrData = {'S':slen, 'E':elen, 'M':op.param2}
                    arr.append(arrData)
                    text += mention + " {} 歡迎！".format(str(group.name))
                    cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                except Exception as error:
                    print(error)
            if op.param1 in jg["join"]:
                try:
                    text = jg["join"][op.param1]
                    sendMention(op.param1,text,[op.param2])
                except:
                    pass
        if op.type == 19 or op.type == 133:#踢人19 踢人133
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            cl.sendMessage(background,"有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param3 in ban["admin"]:
                if wait["iv"] == True:#回邀
                    try:
                        #cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if wait["kiv"] == True:#踢回邀
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        cl.sendMessage(op.param1,"規制中ಥ_ಥ")
            if settings["protect"] == True:
                if op.param2 in ban["admin"]:
                    pass
                else:
                    if settings["kickContact"] == True:
                        try:
                            arrData = ""
                            text = "%s " %('[警告]')
                            arr = []
                            mention1 = "@yuan "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention1) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention1 + '踢了 '
                            mention2 = "@yuan "
                            sslen = str(len(text))
                            eelen = str(len(text) + len(mention2) - 1)
                            arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                            arr.append(arrdata)
                            text += mention2
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
            else:
                if settings["kickContact"] == True:
                    try:
                        arrData = ""
                        text = "%s " %('[警告]')
                        arr = []
                        mention1 = "@yuan "
                        slen = str(len(text))
                        elen = str(len(text) + len(mention1) - 1)
                        arrData = {'S':slen, 'E':elen, 'M':op.param2}
                        arr.append(arrData)
                        text += mention1 + '踢了 '
                        mention2 = "@yuan "
                        sslen = str(len(text))
                        eelen = str(len(text) + len(mention2) - 1)
                        arrdata = {'S':sslen, 'E':eelen, 'M':op.param3}
                        arr.append(arrdata)
                        text += mention2
                        cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                    except Exception as error:
                        print(error)
        if op.type == 24 or op.type == 21 or op.type ==22:#自離副本
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25 and wait["um"]: cl.unsendMessage(op.message.id)
        if op.type == 26 or op.type == 25:#網址偵測
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if msg.text is None:
                msg.text = ""
            if msg.contentType == 1:
                if wait["group"] == msg.to and sender in sender:
                    if wait["cvp"] == True:
                        image = cl.downloadObjectMsg(msg_id, saveAs="cvp.jpg")
                        cl.relatedMessage(msg.to, "圖片下載完成 正在更換頭貼(⁎⁍̴̛ᴗ⁍̴̛⁎)",op.message.id)
                        wait["cvp"] = False
                        cl.changeVideoAndPictureProfile('cvp.jpg','cvp.mp4')
                        os.remove("cvp.mp4")
                        os.remove("cvp.jpg")
                        cl.relatedMessage(msg.to, "更改完成(⁎⁍̴̛ᴗ⁍̴̛⁎)",op.message.id)
                        wait["group"] = []
            if msg.contentType == 0:#半垢頭影 專屬名稱
                if text.startswith("yt:"):
                    if sender in botowner:
                        search = text.lower().replace("yt:","")
                        ytdl(search)
                        cl.relatedMessage(msg.to, "影片下載完成 請傳送圖片(⁎⁍̴̛ᴗ⁍̴̛⁎)",op.message.id)
                        wait["cvp"] = True
                        wait["group"] = msg.to
            if msg.contentType == 0:
                if text.lower().startswith("cvp:"):
                    if sender in botowner:
                        search = text.lower().replace("cvp:","")
                        contact = cl.getContact(clMID)
                        cl.sendMessage(msg.to, "影片下載中...")
                        ytdl(search)
                        cl.sendMessage(msg.to, "影片下載成功 正在下載頭貼(⁎⁍̴̛ᴗ⁍̴̛⁎)")
                        pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                        pict = cl.downloadFileURL(pic)
                        cl.sendMessage(msg.to, "頭像下載成功 正在更改⋯")
                        time.sleep(2)
                        cl.changeVideoAndPictureProfile(pict, "cvp.mp4")
                        cl.sendMessage(msg.to, "成功 感謝使用")
                        os.remove("cvp.mp4")
            if "/ti/g/" in msg.text.lower():
                if settings["autoJoinTicket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = cl.findGroupByTicket(ticket_id)
                        if clMID not in group.members:
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.relatedMessage(to,"☰☰☰網址成功進入群組☰☰☰\n加入狀態:成功入群\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\nGID:\n{gid}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id,id=ticket_id),op.message.id)
                            cl.sendMessage(background,"☰☰☰網址成功進入群組☰☰☰\n加入狀態:成功入群\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id))
                            cl.sendMessage(background,group.id)
                        else:
                            cl.relatedMessage(to,"☰☰☰網址通知☰☰☰\n加入狀態:已在群內\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\nGID:\n{gid}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id,id=ticket_id),op.message.id)
                            cl.sendMessage(background,"☰☰☰網址通知☰☰☰\n加入狀態:已在群內\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id))
                            cl.sendMessage(background,group.id)      
                if settings["autoJoinTicketkick"] == True:#網址炸群待檢查
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    targets = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = cl.findGroupByTicket(ticket_id)
                        if clMID not in group.members:
                            cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                            cl.relatedMessage(to,"☰☰☰網址成功進入群組☰☰☰\n加入狀態:成功入群\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\nGID:\n{gid}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id,id=ticket_id),op.message.id)
                            cl.sendMessage(background,"☰☰☰網址成功進入群組☰☰☰\n加入狀態:成功入群\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),id=ticket_id))
                            cl.sendMessage(background,group.id)
                        else:
                            cl.relatedMessage(to,"☰☰☰網址通知☰☰☰\n加入狀態:已在群內\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\nGID:\n{gid}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),gid=group.id,id=ticket_id),op.message.id)
                            cl.sendMessage(background,"☰☰☰網址通知☰☰☰\n加入狀態:已在群內\n群組名稱:\n【{gname}】\n☰☰☰☰☰群組資料☰☰☰☰☰\n群組人數:{people}\n網址ID:{id}\n☰☰☰☰☰☰☰☰☰☰☰☰☰☰".format(gname=group.name,people=len(group.members),id=ticket_id))
                            cl.sendMessage(background,group.id)
                    for g in group.members:
                        if g.mid not in ban["admin"]:
                            targets.append(g.mid)
                            print(g.mid)
                        if targets == []:
                            cl.relatedMessage(msg.to,"群組內沒有人了",op.message.id)
                    else:
                        try:
                            warmods["warmods"][group.id] = True
                            cl.sendMessage(group.id,boomsend)
                            thread_exe(group.id,targets)
                            settings["autoJoinTicketkick"] = False
                            cl.relatedMessage(to, "網址成功進入《{}》群組\n並成功自動炸群\n已自動幫您關閉網址進群翻".format(group.name),op.message.id)
                            cl.sendMessage(background,"網址自動炸群成功\n群組名稱:"+group.name+"\nGID:"+group.id+"\n已自動關閉網址進群翻")
                        except:
                            settings["autoJoinTicketkick"] = False
                            cl.sendMessage(to, "網址成功進入《{}》群組\n但沒有成功自動炸群\n已自動關閉網址進群翻".format(group.name))
                            cl.sendMessage(background,"網址自動炸群失敗\n機器規制ㄌ\n群組名稱:"+group.name+"\nGID:"+group.id+"\n為您關閉進群翻")
        if op.type == 26 or op.type == 25:#25,26發話
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver 
            if sender in ban["admin"]:
                pass 
            else:
                if msg.to in wait["rapidFire"]:
                    if time.time() - wait["rapidFire"][msg.to] < 2:
                        return
                    else:
                        wait["rapidFire"][msg.to] = time.time()
                else:
                    wait["rapidFire"][msg.to] = time.time()       
            if msg.contentType == 0:
                if text.lower() is None:
                    return
                else:
                    cmd = text.lower()
            if msg.contentType == 1:
                if sender in wait['gbc'] and wait['gbc'][sender]['type'] == 'pic':
                    image = cl.downloadObjectMsg(msg.id )
                    n = cl.getGroupIdsJoined()
                    g = 0
                    for manusia in n:
                        group = cl.getGroup(manusia)
                        nama =[contact.mid for contact in group.members]
                        if len(nama) >int(wait['gbc'][sender]['over'] ):
                            cl.sendMessage(manusia,"請注意以下圖片\n" + wait['gbc'][sender]['text'] )
                            cl.sendImage(manusia,image)
                            g+=1
                        else:
                            pass
                    cl.sendMessage(to,"☬☬☬〘群組廣播〙☬☬☬ 分享《{}》個群組".format(str(g)))
                    cl.deleteFile(image)
                    del wait['gbc'][sender]
            if msg.contentType == 7:
                stk_id = msg.contentMetadata['STKID']
                pkg_id = msg.contentMetadata['STKPKGID']
                if sender in ban["admin"]:
                    if sender in ckt['ck'] and pkg_id in ckt['ck']["{}".format(sender)] and stk_id in ckt['ck']["{}".format(sender)][pkg_id]:
                        try:
                            ctext = ckt['ck']["{}".format(sender)][pkg_id][stk_id]
                            cl.sendMessage(to, ctext)
                        except:
                            pass
                    if to in settings["checkSticker"]:
                        try:
                            cl.sendMessage(to, "stkadd {}_{}:".format(pkg_id,stk_id))
                            cl.sendMessage(to, "stkdel {}_{}".format(pkg_id,stk_id))
                        except:
                            cl.sendMessage(to, "執行命令錯誤")
                if text is None:
                    return
            if rgb["contact"] == True and sender in rgb["contactsender"]:#友資廣播
                if msg.contentType == 13:
                    wait["contact"] = False
                    wait["contactsender"] = ""
                    txt = rgb["contacttext"]
                    mid = msg.contentMetadata["mid"]
                    groups = cl.getGroupIdsJoined()
                    g = 0
                    for gid in groups:
                        cl.sendMessage(gid,"請注意以下友資\n" + txt)
                        cl.sendContact(gid,mid)
                        g += 1
                    cl.sendMessage(to,"【群組廣播】\n成功分享了﹝{}﹞個群組".format(g))
                    del rgb["contacttext"]
            if rgb["post"] == True and sender in rgb["postsender"]:#文章廣播
                if msg.contentType == 16:
                    wait["post"] = False
                    wait["postsender"] = ""
                    postid =str(msg.contentMetadata['postEndUrl']).split("&postId=")[1]
                    groups = cl.getGroupIdsJoined()
                    g = 0
                    for gid in groups:
                        cl.sendMessage(gid,"請注意以下文章")
                        cl.sendPostToTalk(gid,postid)
                        g += 1
                    cl.sendMessage(to,"【群組廣播】\n成功分享了﹝{}﹞個群組".format(g))
            if msg.contentType == 13:#友資MID
                if sender in ban["admin"]:
                    if wait["ctmid"] == True:
                        cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                        mid = msg.contentMetadata["mid"]
                    #新增黑單
                    if wait["ban"] == True:
                        if msg.contentMetadata["mid"] in ban["banlist"]:
                            cl.sendMessage(msg.to,"【{}】已在黑名單中".format(cl.getContact(msg.contentMetadata["mid"]).displayName))
                            wait["ban"] = False
                        elif msg.contentMetadata["mid"] in ban["admin"]:
                            cl.sendMessage(msg.to,"【{}】位於權限者名單中\n無法加入黑單！".format(cl.getContact(msg.contentMetadata["mid"]).displayName))
                            wait["ban"] = False
                        else:
                            ban["banlist"][msg.contentMetadata["mid"]] = True
                            wait["ban"] = False
                            cl.sendMessage(msg.to,"【{}】成功加入黑名單".format(cl.getContact(msg.contentMetadata["mid"]).displayName))
                            json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    #移除黑單
                    if wait["unban"] == True:
                        if msg.contentMetadata["mid"] not in ban["banlist"]:
                            cl.sendMessage(msg.to,"【{}】沒在黑名單中".format(cl.getContact(msg.contentMetadata["mid"]).displayName))
                            wait["unban"] = False 
                        else:
                            del ban["banlist"][msg.contentMetadata["mid"]]
                            wait["unban"] = False
                            cl.sendMessage(msg.to,"成功取消【{}】的黑名單".format(cl.getContact(msg.contentMetadata["mid"]).displayName))
                            json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                if text is None:
                    return
            if sender in botowner or sender in botcreator:#半垢主人專屬
                if text.lower().startswith("/inv:"):#GID穿梭
                    gid = text.lower().replace("/inv:","")
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg._from)
                            cl.inviteIntoGroup(gid,[msg._from])
                        except:
                            cl.sendMessage(to, "邀請失敗")
                            pass
                elif text.lower().startswith("邀請:"):#數字穿梭
                    dd = text.lower().replace("邀請:", "")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            invg = cl.getGroupIdsJoined()[(int(x)-1-int(non))]
                            cl.inviteIntoGroup(invg,[sender])
                            gn = cl.getGroup(invg).name
                            cl.sendMessage(to,"已邀請至群組:"+gn)
                        except Exception as e:
                            cl.sendMessage(to,str(e))
                elif text.lower().startswith("炸群:"):#GID炸群
                    gid = text.lower().replace("炸群:","")
                    group = cl.getGroup(gid)
                    if gid == "":
                        cl.sendMessage(to, "請輸入群組ID")
                    else:
                        try:
                            targets = []
                            for a in group.members:
                                if a.mid not in ban["admin"]:
                                    targets.append(a.mid)
                            else:
                                warmods["warmods"][gid] = True
                                cl.sendMessage(gid,boomsend)
                                thread_exe(gid,targets)
                                cl.relatedMessage(to,"遠端gid炸群成功",op.message.id)
                        except:
                            cl.relatedMessage(to,"你輸入的似乎不是gid...",op.message.id)
                elif text.lower().startswith("退出:"):#數字遠端退群
                    dd = text.lower().replace("退出:"," ")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            byeg = cl.getGroupIdsJoined()[(int(x)-1-int(non))]
                            cl.leaveGroup(byeg)
                            gn = cl.getGroup(byeg).name
                            cl.relatedMessage(to,"已退出群組:"+gn,op.message.id)
                            non += 1
                        except Exception as e:
                            cl.sendMessage(to,str(e))
            if sender in botcreator:#作者專屬
                if text.lower().startswith("python:"):
                    sadio = text[7:]
                    try:exec(sadio)
                    except Exception as e:cl.sendMessage(to,str(e))
                #伺服器指令
                elif text.lower().startswith("system:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    res = []
                    p = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE, universal_newlines=True) 
                    p.wait()
                    result_lines = p.stdout.readlines()   # 从子进程 p 的标准输出中读取所有行，并储存在一个list对象中
                    result = ""
                    for line in result_lines:
                        print(line.strip()) 
                        result += line.strip()
                        result += "\n"
                    cl.sendMessage(to, result)
            if sender in botowner:#半垢主人專屬
                if text.lower() == "改頭貼":#更改頭貼
                    wait["cpi"] = True
                    cl.relatedMessage(to,"請發送圖片(´･ω･`)",op.message.id)
                #權限
                elif text.lower() == "清除全部權限":#刪除全部權限
                    ban["admin"] = []
                    ban["admin"].append(clMID)
                    ban["admin"].append(botowner)
                    ban["admin"].append(botcreator)
                    json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    cl.relatedMessage(to,"清除全部權限成功",op.message.id)
                elif text.lower() == "清除全部無視":#刪除全部無視
                    ig["ig"] = []
                    ig["ig"].append(clMID)
                    ig["ig"].append(botowner)
                    ig["ig"].append(botcreator)
                    json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    cl.relatedMessage(to,"清除全部收回無視成功",op.message.id)
                elif text.lower().startswith("加權 "):#標記增加權限
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    MENTION['MENTIONEES'][0]["M"]
                    for x in MENTION['MENTIONEES']:
                        if x["M"] not in ban["admin"]:
                            ban["admin"].append(x["M"])
                            cl.sendMessage(to, "【{}】已獲得權限".format(cl.getContact(x["M"]).displayName))
                            json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                        else:
                            cl.sendMessage(to, "【{}】本來就有權限ㄌ".format(cl.getContact(x["M"]).displayName))
                elif text.lower().startswith("刪權 "):#標記刪除權限
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    MENTION['MENTIONEES'][0]["M"]
                    for x in MENTION['MENTIONEES']:
                        if x["M"] in ban["admin"]:
                            ban["admin"].remove(x["M"])
                            cl.sendMessage(to, "已刪除【{}】權限".format(cl.getContact(x["M"]).displayName))
                            json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                        else:
                            cl.sendMessage(to, "【{}】本來就沒有權限".format(cl.getContact(x["M"]).displayName))
                elif text.lower().startswith("add:"):#MID增加權限
                    txt = op.message.text.replace("add:","")
                    if txt not in ban["admin"]:
                        ban["admin"].append(txt)
                        cl.sendMessage(to, "【{}】已獲得權限".format(cl.getContact(txt).displayName))
                        json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    else:
                        cl.sendMessage(to, "【{}】本來就有權限ㄌ".format(cl.getContact(txt).displayName))
                elif text.lower().startswith("del:"):#MID刪除權限
                    txt = op.message.text.replace("del:","")
                    if txt in ban["admin"]:
                        ban["admin"].remove(txt)
                        cl.sendMessage(to, "已刪除【{}】權限".format(cl.getContact(txt).displayName))
                        json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    else:
                        cl.sendMessage(to, "【{}】本來就沒有權限".format(cl.getContact(txt).displayName))
                elif text.lower().startswith("刪權限:"):#數字刪權限
                    dd = text.lower().replace("刪權限:", " ")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            deladmin = ban["admin"][(int(x)-1-int(non))]
                            ban["admin"].remove(deladmin)
                            kill = cl.getContact(deladmin)
                            cl.relatedMessage(to,"已刪除權限:"+kill.displayName+"\nMID:"+kill.mid,op.message.id)
                            json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                            non += 1
                        except Exception as e:
                            cl.sendMessage(to,str(e))
                elif text.lower().startswith("無視 "):#標記增加無視
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey not in ig["ig"]:
                        ig["ig"].append(str(inkey))
                        cl.relatedMessage(to, "你被無視了 摳連",op.message.id)
                        backupData()
                    else:
                        cl.relatedMessage(to,"你早就被無視了",op.message.id)
                elif text.lower().startswith("刪無視 "):#標記刪除無視
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey in ig["ig"]:
                        ig["ig"].remove(str(inkey))
                        cl.relatedMessage(to, "你沒無視了 摳連",op.message.id)
                        json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    else:
                        cl.relatedMessage(to,"這個人本來就沒被無視阿智障",op.message.id)
                elif text.lower().startswith("刪除無視:"):#數字刪除無視
                    dd = text.lower().replace("刪除無視:", " ")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            delig = ig["ig"][(int(x)-1-int(non))]
                            ig["ig"].remove(delig)
                            kill = cl.getContact(delig)
                            cl.relatedMessage(to,"已刪除收回無視:"+kill.displayName+"\nMID:"+kill.mid,op.message.id)
                            json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                            non += 1
                        except Exception as e:
                            cl.sendMessage(to,str(e))
                elif text.lower().startswith("copy "):#克隆
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    contact = cl.getContact(inkey)
                    p = cl.profile
                    home = cl.getProfileDetail(inkey)
                    pic = cl.downloadFileURL("http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus, saveAs="pic.jpg")
                    objectId = home["result"]["objectId"]
                    cl.updateProfileCoverById(objectId)
                    p.displayName = contact.displayName
                    p.statusMessage = contact.statusMessage
                    cl.updateProfile(p)
                    cl.updateProfileCoverById(cl.getProfileCoverId(inkey))
                    cl.updateProfilePicture(pic)
                    os.remove("pic.jpg")
                    sendMention(to,"已複製為@!",[inkey])
            if sender in ban["admin"]:#權限者
                if text.lower() in ['權限表']:#權限名單
                    if ban["admin"] == []:
                        cl.relatedMessage(msg.to,"沒有權限者",op.message.id) 
                    else:
                        no = 1
                        mc = "權限名單如下："
                        for mi_d in ban["admin"]:
                            try:
                                mc += "\n{no}.{name}\n({mid})".format(no=no,name=cl.getContact(mi_d).displayName,mid=mi_d)
                                no += 1
                            except:
                                mc += "\n{no}.此人砍帳了\n({mid})".format(no=no,mid=mi_d)
                                no += 1
                                ban["admin"].remove(mi_d)
                                json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(background,"砍帳名單刪除完畢")
                        cl.relatedMessage(msg.to,mc,op.message.id)
                elif text.lower() in ['無視表']:#無視名單
                    if ig["ig"] == []:
                        cl.relatedMessage(msg.to,"沒有人被無視",op.message.id) 
                    else:
                        no = 1
                        mc = "無視名單如下："
                        for mi_d in ig["ig"]:
                            try:
                                mc += "\n{no}.{name}\n({mid})".format(no=no,name=cl.getContact(mi_d).displayName,mid=mi_d)
                                no += 1
                            except:
                                mc += "\n{no}.此人砍帳了\n({mid})".format(no=no,mid=mi_d)
                                no += 1
                                ig["ig"].remove(mi_d)
                                json.dump(ig,codecs.open("ig.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(background,"砍帳名單刪除完畢")
                        cl.relatedMessage(msg.to,mc,op.message.id)
                elif text.lower().startswith("admin:"):#數字丟權限者友資
                    dd = text.lower().replace("admin:"," ")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            alladmin = ban["admin"][(int(x)-1-int(non))]
                            cl.sendContact(to,alladmin)
                        except:
                        	pass
                elif text.lower().startswith("igadmin:"):#數字丟無視者友資
                    dd = text.lower().replace("igadmin:"," ")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            ignore = ig["ig"][(int(x)-1-int(non))]
                            cl.sendContact(to,ignore)
                        except:
                            pass
                #指令表txt版本
                if text.lower() == 'help':
                    cl.relatedMessage(to, help(),op.message.id)
                elif text.lower() == 'help1':
                    cl.relatedMessage(to, help1(),op.message.id)
                elif text.lower() == 'help2':
                    cl.relatedMessage(to, help2(),op.message.id)
                elif text.lower() == 'help3':
                    cl.relatedMessage(to, help3(),op.message.id)
                elif text.lower() == 'help4':
                    cl.relatedMessage(to, help4(),op.message.id)
                elif text.lower() == 'help5':
                    cl.relatedMessage(to, help5(),op.message.id)
                elif text.lower() == 'help6':
                    cl.relatedMessage(to, help6(),op.message.id)
                elif text.lower() == 'help7':
                    cl.relatedMessage(to, help7(),op.message.id)
                elif text.lower() == 'help8':
                    cl.relatedMessage(to, help8(),op.message.id)
                elif text.lower() == 'help9':
                    cl.relatedMessage(to, help9(),op.message.id)
                elif text.lower() in ['rg']:
                    G = cl.getGroup(msg.to)
                    group = cl.getGroup(to)
                    contact = cl.getContact(sender)
                    gtime = group.createdTime
                    gtimee = int(round(gtime/1000))
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "創群者已砍帳"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                         gPending = str(len(group.invitee))
                    ret_ ="✦✦✦✦✦群組✦✦✦✦✦"
                    ret_ +="\n成員數量\n【"+(str(len(group.members)))+"】"
                    ret_ +="\n邀請數量\n【"+(gPending)+"】"
                    ret_ +="\n✦✦✦✦✦群組✦✦✦✦✦"
                    ret_ +="\n群組名稱\n【{}】".format(str(group.name))
                    ret_ +="\n✦✦✦✦✦✦✦✦✦✦✦✦"
                    ret_ +="\n群組建立時間\n【{}】".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(gtimee)))
                    ret_ +="\n✦✦✦✦✦說明✦✦✦✦✦"
                    ret_ +="\n群主創建者"
                    ret_ +="\n【"+(str(gCreator))+"】"
                    ret_ +="\n✦✦✦✦✦✦✦✦✦✦✦✦"
                    ret_ +="\n群組Gid"
                    ret_ +="\n【{}】".format(group.id)
                    ret_ +="\n✦✦✦✦✦✦✦✦✦✦✦✦"
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif text == "拉霸" or text.lower() == "rlb":
                    list = []
                    for i in range(15):
                        list.append(random.choice(["０","９","８","７","６","５","４","３","２","２","１"]))
                    mc =  "拉霸機拉霸一次\n"
                    mc += "第一行==>{}  {}  {}<=={}\n".format(list[0],list[1],list[2],int(list[0])+int(list[1])+int(list[2]))
                    mc += "第二行==>{}  {}  {}<=={}\n".format(list[3],list[4],list[5],int(list[3])+int(list[4])+int(list[5]))
                    mc += "第三行==>{}  {}  {}<=={}\n".format(list[6],list[7],list[8],int(list[6])+int(list[7])+int(list[8]))
                    mc += "第四行==>{}  {}  {}<=={}\n".format(list[9],list[10],list[11],int(list[9])+int(list[10])+int(list[11]))
                    mc += "第五行==>{}  {}  {}<=={}".format(list[12],list[13],list[14],int(list[12])+int(list[13])+int(list[14]))
                    cl.relatedMessage(to,mc,op.message.id)
                elif msg.text in ["本日運勢","rls"]:
                    a = random.choice(["大吉！！！運氣旺！ヽ(✿ﾟ▽ﾟ)ノ","中吉！運氣好～(ﾟ∀ﾟ)","小吉〜小有手氣(`・ω・´)","末吉〜還可以(,,・ω・,,)","吉〜普普通通～(´･ω･`)","凶〜有點不好(つд⊂)","大凶〜有點悲劇｡･ﾟ･(ﾉД`)ヽ(ﾟДﾟ )"])
                    slot = "您今天的運氣\n{}<==\n以上是您的測試運氣結果".format(a)
                    cl.relatedMessage(to,slot,op.message.id)
                    cl.relatedMessage(to,"[自動回覆]\n在測試一次吧！ヽ(✿ﾟ▽ﾟ)ノ",op.message.id)
                elif text.lower().startswith("join:"):
                    if msg.toType == 2:
                        _join = text[5:] 
                        try:
                            if msg.to in jg["join"]:
                                del jg["join"][msg.to]
                            jg["join"][msg.to] = _join
                        except:
                            pass
                        json.dump(jg,codecs.open("jg.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.relatedMessage(to, "入群回覆設定成功",op.message.id)
                elif text.lower() == 'joindel':
                    if msg.toType == 2:
                        try:
                            del jg["join"][msg.to]
                        except:
                            pass
                        json.dump(jg,codecs.open("jg.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                        cl.relatedMessage(to, "成功刪除入群回覆",op.message.id)
                elif text.lower() == 'jointest':
                    if msg.toType == 2:
                        if to in jg["join"]:
                            text = jg["join"][to]
                            sendMention(to,text,[sender])
                        else:
                            sendMention(to,"@!\n你還沒有設定入群回覆\n請輸入[join:]來新增",[sender])
                if text.lower().startswith("stkadd "):
                    if sender not in clMID:
                        pkg_id = find_between_r(msg.text, "stkadd ","_")
                        stk_id = find_between_r(msg.text, "_", ":")
                        ctext = find_between_r(msg.text, ":","")
                        if ctext == "" or stk_id == "":
                            cl.sendMessage(to, "請輸入回覆文字")
                            return
                        elif 'byeall' in text.lower() or 'ttkall' in text.lower() or 'tk888' in text.lower() or 'tkn' in text.lower() or 'jk on' in text.lower() or 'rk on' in text.lower() or 'tmd' in text.lower() or "茶茶團隊" in text or "茶茶半垢" in text :
                            cl.sendMessage(to, "觸發關鍵字保護 無法設定")
                        elif sender in ckt['ck']:
                            if pkg_id in ckt['ck']["{}".format(sender)]:
                                ckt['ck']["{}".format(sender)][pkg_id][stk_id] = ctext
                                cl.sendMessage(to, "貼圖回覆新增成功！\n" + ctext)
                            else:
                                ckt['ck']["{}".format(sender)][pkg_id] = {}
                                ckt['ck']["{}".format(sender)][pkg_id][stk_id] = ctext
                                cl.sendMessage(to, "貼圖回覆新增成功！\n" + ctext)
                        else:
                            ckt['ck']["{}".format(sender)] = {}
                            ckt['ck']["{}".format(sender)][pkg_id] = {}
                            ckt['ck']["{}".format(sender)][pkg_id][stk_id] = ctext
                            cl.sendMessage(to, "貼圖回覆新增成功！\n" + ctext)
                        backupData()
                elif text.lower().startswith("stkdel "):
                    if sender not in clMID:
                        pkg_id = find_between_r(msg.text, "stkdel ", "_")
                        stk_id = find_between_r(msg.text, "_", "")
                        try:
                            del ckt['ck']["{}".format(sender)][pkg_id][stk_id]
                            backupData()
                            cl.sendMessage(to, "刪除貼圖回覆成功")
                        except:
                            pass
                elif text.lower().startswith('id:'):
                    try:
                        list_ = msg.text.split(":")
                        msgs = list_[1]     
                        conn = cl.findContactsByUserid(msgs)
                        cl.sendMessage(to, "http://line.me/ti/p/~" + msgs)
                        cl.sendMessage(to, None, contentMetadata={'mid': conn.mid}, contentType=13) 
                    except:
                        cl.sendMessage(to, '目前處於加友規制狀態中')
                elif text.lower().startswith("name "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.relatedMessage(msg.to,"" + cl.getContact(inkey).displayName,op.message.id)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.relatedMessage(to,me.displayName,op.message.id)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.relatedMessage(to,"[個人簽名]\n" + me.statusMessage,op.message.id)
                elif text.lower() == 'mp':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower().startswith("bio "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.relatedMessage(msg.to,"[StatusMessage]\n" + cl.getContact(inkey).statusMessage,op.message.id)
                elif text.lower().startswith("cover "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to, cl.getProfileCoverURL(inkey))
                elif text.lower().startswith("pi "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus)
                elif text.lower().startswith("vp "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + cl.getContact(inkey).pictureStatus + "/vp")
                elif text.lower().startswith("vpc "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        contact = cl.getContact(x["M"])
                        cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus), "PREVIEW_URL": "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)}, contentType = 2)
                elif text.lower().startswith("info "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        contact = cl.getContact(x["M"])
                        cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName +"\n[ 個簽 ]\n" + contact.statusMessage +"\n[ MID ]\n" + contact.mid)
                        cl.sendImageWithURL(msg.to, str("http://dl.profile.line-cdn.net/" + contact.pictureStatus)) 
                        cl.sendImageWithURL(msg.to, str(cl.getProfileCoverURL(x["M"])))
                #定名
                elif text.lower().startswith("ni:"):
                    _name = text[3:]
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to,"沒這個人(´･_･`)")
                    else:
                        try:
                            cl.inviteIntoGroup(to, targets)
                        except:
                            cl.sendMessage(to,"目前處於 帳號規制狀態中")
                elif text.lower().startswith("ac:"):
                    _name = text[3:]
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            if name in g.displayName:
                                targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to,"沒這個人(´･_･`)")
                    else:
                        for target in targets:
                            cl.sendContact(to, target)
                elif text.lower().startswith("tn "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    ga = cl.getAllContactIds()
                    name = text.split(" ",2)
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    if targets == []:
                        pass
                    else:
                        for key1 in targets:
                            if key1 not in ga:
                                cl.findAndAddContactsByMid(key1)
                            cl.renameContact(key1, name[2])
                            cl.sendMessage(msg.to, "更改定名:"+cl.getContact(key1).displayNameOverridden)
                elif text.lower().startswith("di:"):
                    _name = text[3:]
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            try:
                                if name in g.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                    if targets == []:
                        cl.sendMessage(to, "沒這個人(´･_･`)")
                    else:
                        try:
                            cl.inviteIntoGroup(to,targets)
                        except:
                            cl.sendMessage(to, "目前處於 帳號規制狀態中")
                elif text.lower().startswith("adc:"):
                    _name = text[4:]
                    namelist = _name.split()
                    allmid = cl.getAllContactIds()
                    contactlist = cl.getContacts(allmid)
                    targets = []
                    for g in contactlist:
                        for name in namelist:
                            try:
                                if name in g.displayNameOverridden:
                                    targets.append(g.mid)
                            except:
                                pass
                    if targets == []:
                        cl.sendMessage(to, "沒這個人(´･_･`)")
                    else:
                        for target in targets:
                            cl.sendContact(to, target)
                elif text.lower().startswith("dk:"):
                    _name = text[3:]
                    gs = cl.getGroup(to)
                    targets = []
                    try:
                        cl.unsendMessage(msg_id)
                    except:
                        pass
                    for g in gs.members:
                        try:
                            contact = cl.getContact(g.mid)
                            if _name in contact.displayNameOverridden:
                                targets.append(g.mid)
                        except:
                            pass
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif text.lower().startswith("dt:"):
                    _name = text[3:]
                    gs = cl.getGroup(to)
                    txt = u''
                    s=0
                    b=[]
                    for g in gs.members:
                        try:
                            contact = cl.getContact(g.mid)
                            if _name in contact.displayNameOverridden:
                                b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                                s += 7
                                txt += u'@sdsd \n'
                        except:
                            pass
                    if b == []:
                        cl.sendMessage(to,"群組內沒有這個定名的人")
                    else:
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower().startswith("nt:"):
                    _name = text[3:]
                    gs = cl.getGroup(to)
                    txt = u''
                    s=0
                    b=[]
                    for g in gs.members:
                        if _name in g.displayName:
                            b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                            s += 7
                            txt += u'@sdsd \n'
                    if b == []:
                        cl.sendMessage(to, "群組內沒有這個名稱的人")
                    else:
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower().startswith("tgb:"):
                    _bio = text[4:]
                    gs = cl.getGroup(to)
                    txt = u''
                    s=0
                    b=[]
                    for g in gs.members:
                        if _bio in g.statusMessage:
                            b.append({"S":str(s), "E" :str(s+6), "M":g.mid})
                            s += 7
                            txt += u'@sdsd \n'
                    if b == []:
                        cl.sendMessage(to, "群組內沒有這個個簽的人")
                    else:
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'cancel':
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = (contact.mid for contact in X.invitee)
                            ginfo = cl.getGroup(msg.to)
                            sinvitee = str(len(ginfo.invitee))
                            start = time.time()
                            for cancelmod in gInviMids:
                                time.sleep(0.3)
                                cl.cancelGroupInvitation(msg.to, [cancelmod])
                            elapsed_time = time.time() - start
                            cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                            cl.sendMessage(to, "取消人數:" + sinvitee)
                        else:
                            cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower().startswith("cancel:"):
                    _name = text[7:]
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.invitee:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to,"沒有這個人")
                    else:
                        for target in targets:
                            try:
                                cl.cancelGroupInvitation(msg.to,[target])
                            except:
                                pass
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                #少數重要功能
                elif text.lower() == "reb":
                    if sender in botowner:
                        cl.relatedMessage(to, "重新啟動中....",op.message.id)    
                        restartBot()
                elif text.lower().startswith("reb "):
                    contact1 = cl.getContact(sender)
                    group = cl.getGroup(to)
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        if x['M'] == clMID:
                            cl.sendMessage(background, "【" + contact1.displayName + "】重啟了半垢\n群組名稱: " + str(group.name) + "\n群組MID: " + to + "\n重啟者MID: " + sender)
                            cl.relatedMessage(to, "重新啟動中....",op.message.id)    
                            restartBot()
                elif text.lower() == 'ren':
                    eltime = time.time() - mulai
                    cl.relatedMessage(msg.to,str(Runtime(eltime)),op.message.id) 
                elif text.lower() == 'res':
                    backupData()
                    cl.relatedMessage(to,"儲存成功(｡･ω･｡)",op.message.id)
                elif text.lower() == '登入狀態':
                    cl.sendMessage(to, "機器登入狀態(O)")
                elif text.lower() in ['mymid']:
                    cl.relatedMessage(to, sender,op.message.id)
                elif text.lower() == gbye:#退群指令
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        cl.leaveRoom(msg.to)
                        pass
                #elif text.lower().startswith("gbye:"):
                #    owner["rbye"] = text[5:]
                #    json.dump(owner,codecs.open("owner.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                #    cl.relatedMessage(to,"更改成功",op.message.id)
                #elif text.lower().startswith("gbye:"):
                #    owner["rbye"] = text[5:]
                #    json.dump(owner,codecs.open("owner.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                #    cl.relatedMessage(to,"更改成功",op.message.id)
                elif text == "登入版本" or text == "版本號":
                    cl.sendMessage(to,"目前登入版本:" + version)
                elif text.lower() =='後台儲存': 
                        ret_ = "╔═══〖後台儲存量〗"
                        圖片 = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/image'))   
                        ret_ +="\n╠圖片數量：{} ".format(圖片)    
                        語音 = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/sound')) 
                        ret_ +="\n╠語音數量：{} ".format(語音)    
                        檔案 = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/file'))
                        ret_ +="\n╠檔案數量：{} ".format(檔案)    
                        影片 = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/video'))
                        ret_ +="\n╠影片數量：{} ".format(影片)    
                        ret_ +="\n╚═══〖後台儲存量〗"
                        cl.relatedMessage(to, str(ret_),op.message.id)
                elif text.lower().startswith("炸群:"):
                    gg = text.replace("rbye:","")
                    group = cl.getGroup(gg)
                    contact1 = cl.getContact(sender)
                    cl.leaveGroup(gg)
                    cl.sendMessage(to,"機器已全數退出\n{}".format(str(group.name)))
                    cl.sendMessage(background,"機器已全數退出\n群組名稱\n【" + str(group.name)+"】\n群組GID：\n【"+ str(group.id)+ "】\n撤機者\n【" + contact1.displayName + "】\n【" + contact1.mid + "】")
                elif text.lower() in ['friendlist','好友列表']:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"==好友列表==\n"+ap+"好友人數 : "+str(len(anl)))
                #開關
                elif text.lower() == 'raj on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟(｡･ω･｡)")  
                elif text.lower() == 'raj off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉(｡･ω･｡)")  
                elif text.lower() == 'rak on':
                    settings["autoJoinkick"] = True
                    cl.sendMessage(to, "進群翻已開啟(｡･ω･｡)")    
                    cl.sendMessage(background,"【警告】\n進群翻已開啟")
                elif text.lower() == 'rak off':
                    settings["autoJoinkick"] = False
                    cl.sendMessage(to, "入群蹦蹦已關閉(｡･ω･｡)")    
                    cl.sendMessage(background,"【警告】\n進群翻已關閉")
                elif text.lower() == 'ral on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟(｡･ω･｡)")  
                elif text.lower() == 'ral off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉(｡･ω･｡)")  
                elif text.lower() == 'rqj on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "網址入群已開啟(｡･ω･｡)")    
                elif text.lower() == 'rqj off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "網址入群已關閉(｡･ω･｡)")    
                elif text.lower() == 'rqk on':
                    settings["autoJoinTicketkick"] = True
                    cl.sendMessage(to, "網址進群翻已開啟(｡･ω･｡)")  
                    cl.sendMessage(background,"【警告】\n網址進群翻已開啟")
                elif text.lower() == 'rqk off':
                    settings["autoJoinTicketkick"] = False
                    cl.sendMessage(to, "網址入群蹦蹦已關閉(｡･ω･｡)")  
                    cl.sendMessage(background,"【警告】\n網址進群翻已關閉")
                elif text.lower() == 'rdd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟(｡･ω･｡)")  
                elif text.lower() == 'rdd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉(｡･ω･｡)")  
                elif text.lower() == 'red on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟(｡･ω･｡)") 
                elif text.lower() == 'red off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉(｡･ω･｡)") 
                elif text.lower() == 'rd on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟(｡･ω･｡)")    
                elif text.lower() == 'rd off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉(｡･ω･｡)")
                elif text.lower() == 'rt on':
                    wait["resset"] = True
                    cl.sendMessage(to, "幹你娘開三小智障功能")    
                elif text.lower() == 'rt off':
                    wait["resset"] = False
                    cl.sendMessage(to, "你再亂開阿幹")
                elif text.lower() == 'rc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "踢人標註已開啟(｡･ω･｡)")    
                elif text.lower() == 'rc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "踢人標註已關閉(｡･ω･｡)")
                elif text.lower() == 'rj on':
                    settings["seeJoin"] = True
                    cl.sendMessage(to, "入群通知已開啟(｡･ω･｡)")    
                elif text.lower() == 'rj off':
                    settings["seeJoin"] = False
                    cl.sendMessage(to, "入群通知已關閉(｡･ω･｡)")    
                elif text.lower() == 'rl on':
                    settings["seeLeave"] = True
                    cl.sendMessage(to, "退群通知已開啟(｡･ω･｡)")    
                elif text.lower() == 'rl off':
                    settings["seeLeave"] = False
                    cl.sendMessage(to, "退群通知已關閉(｡･ω･｡)")    
                elif text.lower() == 'rm on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註回覆已開啟(｡･ω･｡)")    
                elif text.lower() == 'rm off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註回覆已關閉(｡･ω･｡)")    
                elif text.lower() == 'ru on':
                    wait["um"] = True
                    cl.sendMessage(to, "收回已開啟(｡･ω･｡)")  
                elif text.lower() == 'ru off':
                    wait["um"] = False
                    cl.sendMessage(to, "收回已關閉(｡･ω･｡)")
                elif text.lower() == 'ck on':
                    settings["checkSticker"][to] = True
                    cl.sendMessage(to, "檢查貼圖已開啟(｡･ω･｡)")
                elif text.lower() == 'ck off':
                    del settings["checkSticker"][to]
                    cl.sendMessage(to, "檢查貼圖已關閉(｡･ω･｡)")
                elif text.lower() == 'rop on':
                    settings["protect"] = True
                    cl.sendMessage(to, "群組保護已開啟(｡･ω･｡)")
                elif text.lower() == 'rop off':
                    settings["protect"] = False
                    cl.sendMessage(to, "群組保護已關閉(｡･ω･｡)")
                elif text.lower() == 'rip on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "群組邀請保護已開啟(｡･ω･｡)")
                elif text.lower() == 'rip off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "群組邀請保護已關閉(｡･ω･｡)")
                elif text.lower() == 'rqp on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "群組網址保護已開啟(｡･ω･｡)")
                elif text.lower() == 'rqp off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "群組網址保護已關閉(｡･ω･｡)")
                elif text.lower() == ivon:
                    wait["iv"] = True
                    cl.sendMessage(to, "回邀保護已開啟(｡･ω･｡)")
                elif text.lower() == ivoff:
                    wait["iv"] = False
                    cl.sendMessage(to, "回邀保護已關閉(｡･ω･｡)")
                elif text.lower() == kivon:
                    wait["kiv"] = True
                    cl.sendMessage(to, "踢回邀保護已開啟(｡･ω･｡)")
                elif text.lower() == kivoff:
                    wait["kiv"] = False
                    cl.sendMessage(to, "踢回邀保護已關閉(｡･ω･｡)")
                elif text.lower() == 'mid on':
                    wait["ctmid"] = True
                    cl.sendMessage(to, "友資mid已開啟(｡･ω･｡)")
                elif text.lower() == 'mid off':
                    wait["ctmid"] = False
                    cl.sendMessage(to, "友資mid已關閉(｡･ω･｡)")
                elif text == '關閉廣播' or text == '廣播關閉':
                    rgb['pic'] = False
                    rgb['picsender'] = {}
                    rgb['contact'] = False
                    rgb['contactsender'] = {}
                    rgb['post'] = False
                    rgb['postsender'] = {}
                    cl.relatedMessage(to,"廣播系統全偵測已關閉完成",op.message.id)
                #清空黑名單	
                elif text.lower() == 'cleanban':
                    ban["banlist"] = {}
                    cl.sendMessage(to, "已清空黑單")
				#黑單
                elif text.lower() == 'ban':
                    wait["ban"] = True
                    cl.sendMessage(to,"請給黑單友資")	
                elif text.lower().startswith("ban "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        if x["M"] not in ban["admin"]:
                            ban["banlist"][x["M"]] = True
                            cl.sendMessage(to,"【{}】已加入黑單！".format(cl.getContact(x["M"]).displayName))
                        else:cl.sendMessage(to,"【{}】位於權限者名單中\n無法加入黑單！".format(cl.getContact(x["M"]).displayName))
                elif text.lower().startswith("ban:"):
                    txt = text[4:].split(' ')
                    for mid in txt:
                        if mid not in ban["admin"]:
                            ban["banlist"][mid] = True
                            cl.sendMessage(to,"【{}】已加入黑單！".format(cl.getContact(mid).displayName))
                        else:cl.sendMessage(to,"【{}】位於權限者名單中\n無法加入黑單！".format(cl.getContact(mid).displayName))
                elif text.lower().startswith("unban:"):
                    txt = text[6:].split(' ')
                    for mid in txt:
                        try:
                            del ban["banlist"][mid]
                            cl.sendMessage(to,"已刪除【{}】的黑單！".format(cl.getContact(mid).displayName))
                        except:cl.sendMessage(to,"【{}】不在黑名單中！".format(cl.getContact(mid).displayName))
                elif text.lower() == 'unban':
                    wait["unban"] = True
                    cl.sendMessage(to,"請給黑單友資")
                elif text.lower().startswith("unban "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        if x["M"] in ban["banlist"]:
                            del ban["banlist"][x["M"]]
                            cl.sendMessage(to,"已刪除【{}】的黑單！".format(cl.getContact(x["M"]).displayName))
                        else:cl.sendMessage(to,"【{}】不在黑名單中！".format(cl.getContact(x["M"]).displayName))
                elif text.lower() in jkon:#進群踢指令
                    if msg.toType ==2:
                        jg["JoinGroup"][to] = True
                        cl.sendMessage(to, "已開啟(｡･ω･｡)")
                elif text.lower() in jkoff:
                    if msg.toType ==2 :
                        try:
                            del jg["JoinGroup"][to]
                            cl.sendMessage(to, "已關閉(｡･ω･｡)")
                        except:
                            cl.sendMessage(to, "沒有開啟保護(｡･ω･｡)")
                elif text.lower() == allon:#全保護指令
                    if msg.toType ==2:
                        wait["iv"] = True
                        wait["kiv"] = True
                        jg["JoinGroup"][to] = True
                        warmods["warmods"][to] = True
                        cl.sendMessage(to, "全保護已開啟(｡･ω･｡)")
                elif text.lower() == alloff:
                    if msg.toType ==2:
                        wait["iv"] = True
                        wait["kiv"] = False
                        try:
                            del jg["JoinGroup"][to]
                            del warmods["warmods"][to]
                            cl.sendMessage(to, "全保護已關閉(｡･ω･｡)")
                        except:
                            cl.sendMessage(to, "沒有開啟全保護(｡･ω･｡)")
                elif text.lower() == waron:#戰爭指令
                    if msg.toType ==2:
                        warmods["warmods"][to] = True
                        cl.sendMessage(to, "群組戰爭模式已開啟(｡･ω･｡)")
                elif text.lower() == waroff:
                    if msg.toType ==2 :
                        try:
                            del warmods["warmods"][to]
                            cl.sendMessage(to, "群組戰爭模式已關閉(｡･ω･｡)")
                        except:
                            cl.sendMessage(to,"群組戰爭模式沒有開啟(｡･ω･｡)")
                #機器開關查詢
                elif text.lower() == 'set':
                    ret_ = "╭〖 沙雕專武設定 〗╮"
                    ret_ += "\n├≽ 進群類型 開關"
                    if settings["autoJoin"] == True:ret_ += "\n├≽ 自動入群 ✅"
                    else:ret_ += "\n├≽ 自動入群 ❌"
                    if settings["autoJoinkick"] == True:ret_ += "\n├≽ 自動入群蹦蹦 ✅"
                    else:ret_ += "\n├≽ 自動入群蹦蹦 ❌"
                    if settings["autoJoinTicket"] == True:ret_ += "\n├≽ 網址入群 ✅"
                    else:ret_ += "\n├≽ 網址入群 ❌"
                    if settings["autoJoinTicketkick"] == True:ret_ += "\n├≽ 網址炸群 ✅"
                    else:ret_ += "\n├≽ 網址炸群 ❌"
                    if settings["autoLeave"] == True:ret_ += "\n├≽ 自離副本 ✅"
                    else:ret_ += "\n├≽ 自離副本 ❌"
                    ret_ += "\n├≽ 其餘功能 開關"
                    if settings["autoAdd"] == True:ret_ += "\n├≽ 自動加友 ✅"
                    else:ret_ += "\n├≽ 自動加友 ❌"
                    if settings["autoRead"] == True:ret_ += "\n├≽ 自動已讀 ✅"
                    else:ret_ += "\n├≽ 自動已讀 ❌"
                    if settings["reread"] == True:ret_ += "\n├≽ 查詢收回 ✅"
                    else:ret_ += "\n├≽ 查詢收回 ❌"
                    if wait["resset"] == True:ret_ += "\n├≽ 偵測更改 ✅"
                    else:ret_ += "\n├≽ 偵測更改 ❌"
                    ret_ += "\n├≽ 保護類型 開關"
                    if settings["protect"] == True:ret_ += "\n├≽ 群組保護 ✅"
                    else:ret_ += "\n├≽ 群組保護 ❌"
                    if settings["inviteprotect"] == True:ret_ += "\n├≽ 邀請保護 ✅"
                    else:ret_ += "\n├≽ 邀請保護 ❌"
                    if settings["qrprotect"] == True:ret_ += "\n├≽ 網址保護 ✅"
                    else:ret_ += "\n├≽ 網址保護 ❌"
                    ret_ += "\n├≽ 通知類型 開關"
                    if settings["seeJoin"] == True:ret_ += "\n├≽ 入群通知開啟 ✅"
                    else:ret_ += "\n├≽ 入群通知關閉 ❌"
                    if settings["seeLeave"] == True:ret_ += "\n├≽ 退群通知開啟 ✅"
                    else:ret_ += "\n├≽ 退群通知關閉 ❌"
                    if wait["iv"] == True:ret_ += "\n├≽ 回邀保護開啟 ✅"
                    else:ret_ += "\n├≽ 回邀保護關閉 ❌"
                    if wait["kiv"] == True:ret_ += "\n├≽ 踢回邀保護開啟 ✅"
                    else:ret_ += "\n├≽ 踢回邀保護關閉 ❌"
                    ret_ += "\n├≽ 《以下為單群設定》"
                    G = cl.getGroup(to)
                    ret_ += "\n├≽ 群組名稱：<{}>".format(G.name)
                    ret_ += "\n├≽ 進群保護 開關"
                    if to in jg["JoinGroup"]:ret_+="\n├≽ 進群保護 ✅"
                    else:ret_ += "\n├≽進群保護 ❌"
                    ret_ += "\n├≽ 群組戰爭 開關"
                    if to in warmods["warmods"]:ret_+="\n├≽ 群組戰爭 ✅"
                    else:ret_ += "\n├≽ 群組戰爭 ❌"
                    if to in jg["join"]:
                        try:
                            text = jg["join"][to]
                            ret_ += "\n├≽ 入群回覆設置成功 ✅"
                            ret_ += "\n├≽ 以下為入群回覆文字"
                            ret_ += "\n├≽ " + text
                        except:
                            pass
                    else:
                        ret_ += "\n├≽ 入群回覆尚未設置 ❌"
                    ret_ += "\n╰〖 沙雕專武設定 〗╯"
                    cl.sendMessage(to,ret_)
                #機器簡介
                elif text.lower() == 'about':
                    try:
                        cl.kickoutFromGroup(to,["fuck"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            aa = "無法執行(規制)"
                        else:
                            aa = "可以執行(無規制)"
                        arr = []
                        t1 = time.time()
                        loop = asyncio.get_event_loop()
                        loop.close
                        t2 = (time.time() -t1)
                        owner = botowner
                        creator = botcreator
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        eltime = time.time() - mulai
                        bot = Rtime(eltime)
                        ret_ = "《關於自己》"
                        ret_ += "\n➲群組數量: {}".format(str(len(grouplist)))
                        ret_ += "\n➲好友人數: {}".format(str(len(contactlist)))
                        ret_ += "\n➲封鎖人數: {}".format(str(len(blockedlist)))
                        ret_ += "\n➲個簽字數: {}".format(str(len(clProfile.statusMessage)))
                        ret_ += "\n➲最愛人數: {}".format(str(len(cl.getFavoriteMids())))
                        ret_ += "\n➲封鎖好友: {}".format(str(len(cl.getBlockedContactIds())))
                        ret_ += "\n➲邀請群組: {}".format(str(len(cl.getGroupIdsInvited())))
                        ret_ += "\n➲Line帳號ID:\n➲{}".format(clProfile.userid)
                        ret_ += "\n➲個人名稱:\n➲{}".format(str(clProfile.displayName))
                        ret_ += "\n➲個人網址(一):\n➲http://line.me/ti/p/{}".format(str(clProfile.userid))
                        ret_ += "\n➲識別碼:\n➲{}".format(str(clProfile.mid))
                        ret_ += "\n《狀態規制》"
                        ret_ += "\n➲踢人狀態: {}".format(aa)
                        ret_ += "\n➲邀請狀態: {}".format(aa)
                        #ret_ += "\n➲加友狀態: {}".format(bb)
                        ret_ += "\n➲取消狀態: 可以執行(無規制)"
                        ret_ += "\n《個人開關》"
                        if settings["autoJoin"] == True: ret_ += "\n➲自動入群 ✅"
                        else: ret_ += "\n➲自動入群 ❌"
                        if settings["autoJoinkick"] == True: ret_ += "\n➲自動入群蹦蹦 ✅"
                        else: ret_ += "\n➲自動入群蹦蹦 ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n➲網址入群 ✅"
                        else: ret_ += "\n➲網址入群 ❌"
                        if settings["autoJoinTicketkick"] == True: ret_ += "\n➲網址炸群 ✅"
                        else: ret_ += "\n➲網址炸群 ❌"
                        if settings["reread"] == True: ret_ += "\n➲防止收回 ✅"
                        else: ret_ += "\n➲防止收回 ❌"
                        if settings["autoRead"] == True: ret_ += "\n➲自動已讀 ✅"
                        else: ret_ += "\n➲自動已讀 ❌"
                        ret_ += "\n《關於半垢》"
                        ret_ += "\n➲半垢作者:沙雕"
                        ret_ += "\n➲專武極限速度:\n➲{}".format(str("%.18fs" %t2))
                        ret_ += "\n➲半垢運行時間:\n➲l───────●──────l\n➲{}\n➲⇆ ㅤ ㅤ◁  ㅤ❚ ❚  ㅤ▷  ㅤ↻".format(bot)
                        cl.relatedMessage(to, str(ret_),op.message.id)
                    except Exception as e:
                        cl.sendMessage(to,str(e))
                #線程數
                elif text.lower() == '.set':
                    ret_ = "=====專武垢設定====="
                    ret_ += "\n➽登入版本:{}".format(version)
                    ret_ += "\n➽已運行踢人線程數:{}".format(TOTAL_ttk)
                    ret_ += "\n➽已運行取消線程數:{}".format(TOTAL_can)
                    ret_ += "\n➽已運行進群踢線程數:{}".format(TOTAL_jk)
                    ret_ += "\n➽已運行自由線程數:{}".format(TOTAL_free)
                    ret_ += "\n➽已運行總線程數:{}".format(TOTAL_ttk+TOTAL_can+TOTAL_jk+TOTAL_free)
                    ret_ += "\n=====專武垢設定====="
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif text.lower() == 'gid':#群組GID 副本RID
                    try:
                        cl.relatedMessage(msg.to,msg.to,op.message.id)
                    except:
                        cl.relatedMessage(msg.to,op.param1,op.message.id)
                #網址開關
                elif text.lower() == 'ru':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.relatedMessage(to, "[ 群組網址 ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)),op.message.id)
                        else:
                            cl.relatedMessage(to, "群組沒有開啟網址",op.message.id)
                elif text.lower() == 'ro':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.relatedMessage(to, "群組網址已開",op.message.id)
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "開啟成功",op.message.id)
                elif text.lower() == 'rc':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.relatedMessage(to, "群組網址已關",op.message.id)
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.relatedMessage(to, "關閉成功",op.message.id)
                #廣播
                elif text.lower().startswith("文章廣播:"):#文章廣播
                    id = text[5:].split(':')
                    for x in range(int(id[1])):
                        cl.sendPostToTalk(to,id[0])
                    cl.relatedMessage(to, "文章分享完畢",op.message.id)
                elif text.lower() == "圖片廣播" or text.lower().startswith("圖片廣播:"):
                    if "圖片廣播:" in text:
                        txt = text[5:]
                        rgb["pictext"] = txt
                    rgb["pic"] = True
                    rgb["picsender"] = sender
                    cl.relatedMessage(to,"請發送圖片",op.message.id)
                elif text.lower() == "友資廣播" or text.lower().startswith("友資廣播:"):
                    if "友資廣播:" in text:
                        txt = text[5:]
                        rgb["contacttext"] = txt
                    rgb["contact"] = True
                    rgb["contactsender"] = sender
                    cl.relatedMessage(to,"請發送欲廣播友資",op.message.id)
                elif text.lower().startswith("文字廣播:"):
                    txt = text.lower().replace("文字廣播:","")
                    gids = cl.getGroupIdsJoined()
                    n = 0
                    for g in gids:
                        cl.sendMessage(g,"請注意以下廣播內容\n" + txt)
                        n += 1
                    cl.sendMessage(to,"【群組廣播】\n成功分享了﹝{}﹞個群組".format(n))
                elif text.lower().startswith("rgb:"):
                    data = text[4:].lower().split(':')
                    if len(data) == 2:data.append("0")
                    elif len(data) >3 or len(data) <2:return
                    try:int(data[2])
                    except:return
                    if data[0] == 'text':
                        n = cl.getGroupIdsJoined()
                        g = 0
                        for manusia in n:
                            group = cl.getGroup(manusia)
                            nama =[contact.mid for contact in group.members]
                            if len(nama) >int(data[2]):
                                cl.sendMessage(manusia,"➲➲➲群組廣播➲➲➲➲ 《文字》\n" + data[1])
                                g+=1
                            else:
                                pass
                        cl.sendMessage(to,"➲➲➲群組廣播➲➲➲➲ 分享《{}》個群組".format(str(g)))
                    elif data[0] in ['pic', 'contact', 'post']:
                        wait['gbc'][sender] = {'type':data[0],'text':data[1],'over':data[2]}
                        cl.relatedMessage(to,'請發送你要廣播的東西~',op.message.id)
                #測速功能
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(background, "檢查中......")
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,format(str(elapsed_time)) + "秒",op.message.id)
                elif text.lower() == 'speed':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.relatedMessage(to,'處理速度\n' + str1 + '秒',op.message.id)
                    elapsed_time = time.time() - start
                    cl.relatedMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒',op.message.id)
                elif msg.text in ["/sp","/speed"]:
                    t1 = time.time()
                    cl.sendMessage(background, "第1次速度")
                    t2 = time.time() - t1
                    time.sleep(0.01)
                    t3 = time.time()
                    cl.sendMessage(background, "第2次速度")
                    t4 = time.time() - t3
                    time.sleep(0.01)
                    t5 = time.time()
                    cl.sendMessage(background, "第3次速度")
                    t6 = time.time() - t5
                    time.sleep(0.01)
                    t7 = time.time()
                    cl.sendMessage(background, "第4次速度")
                    t8 = time.time() - t7
                    time.sleep(0.01)
                    t9 = time.time()
                    cl.sendMessage(background, "第5次速度")
                    t10 = time.time() - t9
                    time.sleep(0.01)
                    a1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b1 = str(a1)
                    a2 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b2 = str(a2)
                    a3 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b3 = str(a3)
                    a4 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b4 = str(a4)
                    a5 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    b5 = str(a5)
                    ret_ = "     [反應速度]\n"
                    ret_ += "第一次:{}秒\n".format(str(t2))
                    ret_ += "第二次:{}秒\n".format(str(t4))
                    ret_ += "第三次:{}秒\n".format(str(t6))
                    ret_ += "第四次:{}秒\n".format(str(t8))
                    ret_ += "第五次:{}秒\n     [處理速度]\n".format(str(t10))
                    ret_ += "第一次:{}秒\n".format(str(b1))
                    ret_ += "第二次:{}秒\n".format(str(b2))
                    ret_ += "第三次:{}秒\n".format(str(b3))
                    ret_ += "第四次:{}秒\n".format(str(b4))
                    ret_ += "第五次:{}秒\n".format(str(b5))
                    ret_ += "     [速度測試]"
                    cl.relatedMessage(to, str(ret_),op.message.id)
                elif msg.text in ["$sp"]:   
                    speed1=cl.relatedMessage(to, "正在檢查整體讀取速度",op.message.id)                        
                    kickerMid = cl.profile.mid      
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                    str1 = str(time0)
                    start = timeit.default_timer()      
                    xtime = (timeit.default_timer()- start)
                    for i in range(1):print ("Test Speed")
                    loadtime = (timeit.default_timer() - start) * 10
                    speed = time.time()
                    time.sleep(1)
                    for x in range(1000):x +=1
                    tend = time.time()  
                    get_profile_time_start = time.time()
                    get_profile = cl.getProfile()
                    get_profile_time = time.time() - get_profile_time_start
                    get_allgroup_time_start = time.time()
                    get_allgroup = cl.getGroupIdsJoined()
                    get_allgroup_time = time.time() - get_allgroup_time_start
                    get_contact_time_start = time.time()                    
                    get_contact = cl.getContact(kickerMid)
                    get_contact_time = time.time() - get_contact_time_start
                    get_friend_time_start = time.time()
                    get_friend = cl.getAllContactIds()
                    get_friend_time = time.time() - get_friend_time_start
                    get_group_time_start = time.time()
                    get_group = cl.getGroup(to)
                    get_group_time = time.time() - get_group_time_start
                    cl.relatedMessage(to, '◈╾ 程序處理速度\n{}秒\n◈╾ 指令反應\n{}秒\n◈╾ 處理速度\n{}秒\n◈╾ 程式反應\n{}秒\n◈╾ 資料讀取速度\n    ◈╾ 讀取自己\n     %a秒\n    ◈╾ 讀取群組\n     %.10f秒\n    ◈╾ 讀取友資\n     %.10f秒\n    ◈╾ 讀取全部群組\n     %.10f秒\n    ◈╾ 讀取全部好友\n     %.10f秒'.format(str(loadtime), str(str1), str(xtime), str(tend -speed )) %(get_profile_time, get_group_time, get_contact_time, get_allgroup_time, get_friend_time),op.message.id)
                #踢人指令
                elif text.lower().startswith("ri:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("ti:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif text.lower().startswith("vk:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif text.lower().startswith("轟幹 "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.relatedMessage(to,"規制中(｡･ω･｡)",op.message.id)
                elif text.lower().startswith("tnk:"):
                    separate = text.split(":")
                    _name = text.replace(separate[0] + ":","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.relatedMessage(msg.to,"群組內沒有這個名字",op.message.id)
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                            except:
                                cl.relatedMessage(to,"規制中(｡･ω･｡)",op.message.id)
                elif text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.relatedMessage(to,"規制中(｡･ω･｡)",op.message.id)
                elif text.lower().startswith("ti "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.relatedMessage(to,"規制中(｡･ω･｡)",op.message.id)
                elif text.lower().startswith("ad "):
                    MENTION = eval(msg.contentMetadata['MENTION']) 
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.findAndAddContactsByMid(inkey)
                    cl.relatedMessage(to,"成功加入好友",op.message.id)
                elif text.lower().startswith("vk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                        except:
                            cl.relatedMessage(to,"規制中(｡･ω･｡)",op.message.id)
                elif text.lower() == 'mine':
                    ret_="【規制查詢】"
                    try:
                        cl.kickoutFromGroup(msg.to, ["Fuck you"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            ret_ += "\n• 踢人狀態 : 規制中\n• 邀請狀態 : 規制中"
                        else:
                            ret_ += "\n• 踢人狀態 : 可以執行\n• 邀請狀態 : 可以執行"
                    try:
                        cl.cancelGroupInvitation(msg.to, ["Fuck you"])
                    except Exception as e:
                        if e.reason == "request blocked":
                            ret_ += "\n• 取消狀態 : 規制中"
                        else:
                            ret_ += "\n• 取消狀態 : 可以執行"
                    try:
                        cl.findAndAddContactsByMid("u4c5ecf983316a9ebd253f3c567a9e9c2")
                        ret_ += "\n• 加友狀態 : 可以執行"
                    except Exception as e:
                        if e.reason == "request blocked":
                            ret_ += "\n• 加友狀態 : 規制中"
                    cl.relatedMessage(msg.to, ret_,op.message.id)
                elif text.lower().startswith("mid "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        cl.relatedMessage(to,x["M"],op.message.id)
                elif text == "半垢主人":
                    cl.sendContact(to,owners)
                elif text.lower().startswith("ct "):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        cl.sendContact(to,x["M"])
                elif text.lower().startswith("mc:"):
                    a = text[3:].split(" ")
                    for mid in a:
                        cl.sendContact(to,mid)
                elif text.lower().startswith("picmc:"):
                    separate = text.split(":")
                    mmid = text.replace(separate[0] + ":","")
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + cl.getContact(mmid).pictureStatus)
                elif text.lower().startswith("glink:"):
                    GTG = text.replace("glink:","")
                    GR = cl.getGroup(GTG)
                    cl.updateGroup(GR)
                    GR.preventedJoinByTicket = False
                    group = cl.getGroup(GTG)
                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    cl.sendMessage(to, "{}".format(gTicket))
                #mid或其餘方式功能
                elif text.lower().startswith("inv:"):
                    separate = text.split(":")
                    midd = text.replace(separate[0] + ":","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.relatedMessage(to,"已經幫您邀請\n"+midd+"\n邀請完畢\n或可能此人已經在群組",op.message.id)
                elif text.lower().startswith("ce:"):
                    separate = text.split(":")
                    txt = text.replace(separate[0] + ":","")
                    cl.createPost(txt)
                    cl.relatedMessage(to,"正在幫您生成貼文\n貼文創建內容:\n" + txt + "\n貼文創建完畢",op.message.id)
                elif text.lower().startswith("pn:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.relatedMessage(to,"名稱已更改為\n=>" + string + "",op.message.id)
                elif text.startswith("Ytmp3:"):
                    sep = text.lower().replace("Ytmp3:","")
                    search = text.lower().replace("Ytmp3:","")
                    ytdl(search)
                    cl.sendAudio(msg.to, "cvp.mp4")
                    os.remove("cvp.mp4")
                elif text.startswith("Ytmp4:"):
                    search = text.lower().replace("Ytmp4:","")
                    ytdl(search)
                    picture = "https://obs-jp.line-apps.com/"+cl.getProfile().pictureStatus
                    #cl.sendVideo(to, picture, ytdl) 
                    contact = cl.getProfile()
                    cl.sendMessage(to, " 傳送了影片", contentMetadata={"DOWNLOAD_URL": "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus), "PREVIEW_URL": "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)}, contentType = 2)
                elif text.lower() == 'sr':
                    cl.relatedMessage(msg.to, "設置已讀點 ✔",op.message.id)
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif text.lower() == 'cr':
                    cl.relatedMessage(to, "刪除已讀點 ✘",op.message.id)
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif text.lower() == 'lr':
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.relatedMessage(msg.to, "[已讀的人/順序]:%s\n\n查詢時間:[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]),op.message.id)
                    else:
                        cl.relatedMessage(msggbc.to, "請輸入SR設置已讀點",op.message.id)               
                #後台指令
                elif text.lower() == 'us':
                    try:
                        cl.unsendMessage(msg.relatedMessageId)
                    except Exception as e:
                        cl.sendMessage(to, "")
                #GID查成員
                elif text.lower().startswith("tg:"):
                    gid = text.lower().replace("tg:","")
                    a = cl.getGroup(gid)
                    gmb = a.members
                    count=0
                    no=0
                    d = "【群組成員】\n"
                    d += "群組名稱:\n{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            no+=1
                            d += str(no)+"."+mn+"\n"
                            count+=1
                            if count == 150:
                                cl.sendMessage(to,d)
                                d=""
                                count=0
                        except:
                            pass
                    d += "【成員清單生成完畢】"
                    cl.relatedMessage(to,d,op.message.id)
                elif text.lower().startswith("tgm:"):
                    gid = text.lower().replace("tgm:","")
                    a = cl.getGroup(gid)
                    gmb = a.members
                    count=0
                    no=0
                    d = "【群組成員】\n"
                    d += "群組名稱:\n{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            no+=1
                            mi = cl.getContact(i.mid).mid
                            d += str(no)+"."+mn+"\n"+mi+"\n"
                            count+=1
                            if count == 150:
                                cl.sendMessage(to,d)
                                d=""
                                count=0
                        except:
                            pass
                    d += "【成員清單生成完畢】"
                    cl.relatedMessage(to,d,op.message.id)
                elif text.lower().startswith("te:"):
                    gid = text.lower().replace("te:","")
                    a = cl.getGroup(gid)
                    gmb = a.invitee
                    count=0
                    no=0
                    d = "【邀請清單】\n"
                    d += "群組名稱:\n{}\n".format(str(a.name))
                    for i in gmb:
                        try:
                            mn = cl.getContact(i.mid).displayName
                            no+=1
                            mi = cl.getContact(i.mid).mid
                            d += str(no)+"."+mn+"\n成員Mid:"+mi+"\n"
                            count+=1
                            if count == 150:
                                cl.sendMessage(to,d)
                                d=""
                                count=0
                        except:
                        	d += "無邀請中成員\n"
                    else:
                        d += "【邀請清單生成完畢】"
                    cl.relatedMessage(to,d,op.message.id)
                elif text.lower().startswith('gmb:'):
                    for b in text[4:].split(" "):
                        if b <= len(cl.getGroupIdsJoined()):
                            diooo = cl.getGroupIdsJoined()[int(b)-1]
                            cl.relatedMessage(to,"【群組成員】\n群組名稱:\n{}".format(str(a.name)),op.message.id)
                            gmb = cl.getGroup(diooo).members
                            count = 0
                            ret_ = "╔══[ 成員名單 ]"
                            for i,elements in enumerate(gmb):
                                ret_ += "\n╠ {}. {}".format(i+1, elements.displayName)
                                count +=1
                                if count > 150:
                                    cl.sendMessage(to,ret_)
                                    ret_ = "╔══[ 成員名單 ]"
                                    count = 0
                            cl.sendMessage(to,ret_ +"\n╚══[ 全部成員共 {} 人]".format(i+1))
                elif text.lower() == 'il':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gil = group.invitee
                        if gil != None:
                            ret_ = "[ 邀請區名單 ]"
                            no = 0 + 1
                            for mem in gil:
                                try:
                                    ret_ += "\n➽{}. 名稱：{}".format(str(no), str(mem.displayName))
                                    no += 1
                                except:
                                    pass
                            ret_ += "\n[ 邀請區成員共 {} 人]".format(str(len(gil)))
                        else:
                            ret_ = "沒有任何人在邀請區中!!!"
                        cl.sendReplyMessage(msg.id, to, str(ret_))
                elif text.lower() in ['gmb']:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ 成員名單 ]"
                        no = 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ 全部成員共 {} 人]".format(str(no-1))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() in ['群組頭貼','gpicture']:
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() in ['創群者','gcreator']:
                    group = cl.getGroup(to)
                    gc = group.creator.mid
                    sendMention(to,"此群創群者為:@!",[gc])
                    cl.sendContact(to,gc)
                elif text.lower() in ['群組資訊','ginfo']:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ 群組資料 ]"
                    ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組 Id : {}".format(group.id)
                    ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請中 : {}".format(gPending)
                    ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.startswith("ginfo:"):
                    gfo = text[6:]
                    group = cl.getGroup(gfo)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower().startswith('gn '):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = text[3:]
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif text.lower().startswith('gc:'):
                    group = cl.getGroup(text[3:])
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                    else:
                        gQr = "開啟"
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔═══[群組查詢]"
                    ret_ += "\n╠群組名稱 : {}".format(str(group.name))
                    ret_ += "\n╠群組 Id : {}".format(group.id)
                    ret_ += "\n╠創建者 : {}".format(str(gCreator))
                    ret_ += "\n╠群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n╠邀請中 : {}".format(gPending)
                    ret_ += "\n╠網址狀態 : {}".format(gQr)
                    ret_ += "\n╚═══[查詢完畢]"
                    cl.sendReplyMessage(msg.id,to, str(ret_))
                    cl.sendImageWithURL(to, path)
                #群組列表
                elif text.lower() == 'lg':
                    groups = cl.getGroupIdsJoined()
                    no = 0 + 1
                    k = len(groups)//100
                    ret_ = "以下為群組列表"
                    cl.relatedMessage(to, str(ret_),op.message.id)
                    for a in range(k+1):
                        ret_ = "╔══[群組列表]"
                        for gid in groups[a*100 : (a+1)*100]:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[總共{}個群組]".format(str(len(groups)))
                        cl.relatedMessage(to, str(ret_),op.message.id)
                elif text.lower().startswith('查群:'):
                    dd = text.lower().replace("查群:", "")
                    sep = dd.split(" ")
                    non = 0
                    dio = sorted(sep)
                    for x in dio:
                        try:
                            diooo = cl.getGroupIdsJoined()[(int(x)-1-int(non))]
                            group = cl.getGroup(diooo)
                            try:
                                gCreator = group.creator.displayName
                            except:
                                gCreator = "已經砍帳ㄌ"
                            if group.invitee is None:
                                gPending = "0"
                            else:
                                gPending = str(len(group.invitee))
                            if group.preventedJoinByTicket == True:
                                gQr = "關閉"
                            else:
                                gQr = "開啟"
                            ret_ = "╔══[ 群組資料 ]"
                            ret_ += "\n╠ 群組名稱 : {}".format(str(group.name))
                            ret_ += "\n╠ 群組 Id : {}".format(group.id)
                            ret_ += "\n╠ 創建者 : {}".format(str(gCreator))
                            ret_ += "\n╠ 群組人數 : {}".format(str(len(group.members)))
                            ret_ += "\n╠ 邀請中 : {}".format(gPending)
                            ret_ += "\n╠ 網址狀態 : {}".format(gQr)
                            ret_ += "\n╚══[ 完 ]"
                            cl.sendMessage(to, str(ret_))
                            #non += 1
                        except Exception as e:
                            cl.sendMessage(to,str(e))
                elif text.lower().startswith('un'): #收回指定數量訊息
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    try:
                        args = text.split(' ')
                        mes = 0
                        try:
                            mes = int(args[1])
                        except:
                            mes = 1
                        M = cl.getRecentMessagesV2(to, 1001)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == clMID:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            cl.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                    except:
                        pass
                #發送文字指令
                elif text.lower().startswith("sy "):
                    x = text.split(' ')
                    if len(x) == 2:
                        cl.relatedMessage(to,x[1],op.message.id)
                    elif len(x) == 3:
                        try:
                            c = int(x[2])
                            for c in range(c):
                                cl.relatedMessage(to,x[1],op.message.id)
                        except:
                            cl.relatedMessage(to,"無法正確執行此指令",op.message.id)
                elif msg.text.startswith("Rex "):
                    txt = msg.text.split(" ")
                    text = msg.text.replace("Rex "+txt[1]+" ","")
                    if text != "":
                        for x in range(int(txt[1])):
                            if "MENTION" in msg.contentMetadata.keys()!= None:
                                datalist = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                                taglist = []
                                for data in datalist:
                                    tags = int(data["S"]) - 5 - len(txt[1])
                                    tage = int(data["E"]) - 5 - len(txt[1])
                                    tagm = data["M"]
                                    taglist.append({"S":str(tags), "E" :str(tage), "M":tagm})
                                cl.sendMessage(msg.to, text, contentMetadata={u"MENTION": json.dumps({"MENTIONEES":taglist})})
                            else:
                                cl.sendMessage(msg.to, text)
                #標註指令
                elif text.lower().startswith('tg '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    for var in range(0,num):
                        sendMention(to,"@!",[inkey])
                    cl.relatedMessage(to, "標註完畢\n共標註了{}次".format(number),op.message.id)
                elif text.lower().startswith('ty '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    list_ = msg.text.split(" ")
                    number = list_[2]
                    num = int(number)
                    cl.relatedMessage(to,"開始私訊標註",op.message.id)
                    for var in range(0,num):
                        sendMention(inkey,"@!",[inkey])
                    cl.relatedMessage(to, "標註完畢 共標註了{}次".format(number),op.message.id)
                elif text.lower().startswith('talk:'):
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        text = text[5:]
                        for mem in group.members:
                            cl.sendMessage(to, text)
                elif text.lower() == 'rgall':
                    group = cl.getGroup(msg.to)
                    tagall=[]
                    for mem in group.members:
                        tagall.append(mem)
                    k = len(tagall)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in tagall[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@sdsd \n'
                        if tagall == []:
                            cl.sendMessage(to,"error")
                        else:
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                #更改個簽指令
                elif text.lower().startswith("cb:"):
                    separate = text.split(":")
                    string = text.replace(separate[0] + ":","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.relatedMessage(to,"個簽狀態已更改為 :  \n" + string,op.message.id)
                #登出指令
                elif text.lower() in ["logout"]:
                    cl.relatedMessage(msg.to, "直接登出請輸入[登出][Y]\n手動登出請輸入[手動][N]",op.message.id)   
                    wait['logout'][msg.to] = sender
                elif text.lower() in ["y","Y","N","n",]:
                    if msg.to in wait['logout'] and msg._from== wait['logout'][msg.to]:
                        if text.lower() in ["登出","y","Y"]:
                            cl.relatedMessage(msg.to, "將自動幫您登出機器",op.message.id)    
                            cl.relatedMessage(to,"[提示]\n已經自動登出後台伺服器",op.message.id) 
                            os._exit(0) 
                            del wait['logout'][msg.to]
                        elif text.lower() in ["N","n","手動"]:
                            cl.relatedMessage(msg.to, "請點擊以下網址\nline://nv/connectedDevices/\n進行手動登出",op.message.id) 
                            del wait['logout'][msg.to]
                    else:
                        pass
                #掃人
                elif text.lower().startswith("mak:"):
                    txt = text[4:].split(' ')
                    contact1 = cl.getContact(sender)
                    if txt == botowner or txt == botcreator:
                        cl.relatedMessage(to,"無法掃除最大權限者",op.message.id)
                    else:
                        ret_ = "[掃人完成]"
                        a = 0
                        for mid in txt:
                            gid = cl.getGroupIdsJoined() 
                            cl.relatedMessage(to, "MID搜尋中…\n搜尋完成\n被掃人員：" + cl.getContact(mid).displayName + "\n開始執行(,,・ω・,,)",op.message.id)
                            for i in gid:
                                group = cl.getGroup(i)
                                gMembMids = [contact.mid for contact in group.members]
                                matched_list = []
                                for tag in txt:
                                    matched_list+=filter(lambda str: str == tag, gMembMids)
                                if matched_list == []:
                                    pass
                                else:
                                    for jj in matched_list:
                                        cl.kickoutFromGroup(i,[jj])
                                        a += 1
                                    cl.sendMessage(i, "掃人目標已踢除")
                            ret_ += "\n搜索 {} 個群組".format(str(len(gid)))
                            ret_ += "\n掃到 {} 個群組".format(str(a))
                            cl.relatedMessage(to, str(ret_),op.message.id)
                            mgroup = cl.getGroup(to)
                            cl.sendMessage(botcreator,"【"+contact1.displayName + "】掃了【" + cl.getContact(mid).displayName + "】\n群組名稱: " + str(mgroup.name) + "\n群組GID: " + str(mgroup.id) + "\n掃人者MID: " + contact1.mid + "\n被掃者MID：" + mid )
                            cl.sendMessage(background,"【"+contact1.displayName + "】掃了【" + cl.getContact(mid).displayName + "】\n群組名稱: " + str(mgroup.name) + "\n群組GID: " + str(mgroup.id) + "\n掃人者MID: " + contact1.mid + "\n被掃者MID：" + mid )
                elif text.startswith("Tak "):
                    contact1 = cl.getContact(sender)
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    if inkey == botowner or inkey == botcreator:
                        cl.relatedMessage(to,"無法掃除最大權限者",op.message.id)
                    else:
                        orang = cl.getGroupIdsJoined()
                        nam = cl.getContact(inkey)
                        cl.sendMessage(msg.to,"名稱:"+nam.displayName)
                        targets = []
                        a = 0
                        for manusia in orang:
                            gs = cl.getGroup(manusia)
                            for g in gs.members:
                                if inkey == g.mid:
                                    targets.append(manusia)
                        cl.sendMessage(msg.to,"搜尋完成 開始踢人")
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(target, [inkey])
                                cl.sendMessage(target,"掃人目標已踢除")
                                a +=1
                            except:
                                pass
                        cl.sendMessage(msg.to,"成功")
                        cl.sendMessage(msg.to,"共踢出{}個群組".format(str(a)))
                        mgroup = cl.getGroup(to)
                        cl.sendMessage(botcreator,"【"+contact1.displayName + "】掃了【" + nam.displayName + "】\n群組名稱: " + str(mgroup.name) + "\n群組GID: " + str(mgroup.id) + "\n掃人者MID: " + contact1.mid + "\n被掃者MID：" + str(inkey) )
                        cl.sendMessage(background,"【"+contact1.displayName + "】掃了【" + nam.displayName + "】\n群組名稱: " + str(mgroup.name) + "\n群組GID: " + str(mgroup.id) + "\n掃人者MID: " + contact1.mid + "\n被掃者MID：" + str(inkey) )
                #共同群組
                elif text.lower().startswith("sg:"):
                    txt = text[3:].split(' ')
                    ret_ = "[共同群組]"
                    a = 0
                    for mid in txt:
                        gid = cl.getGroupIdsJoined() 
                        cl.relatedMessage(to, "MID搜尋中…\n搜尋完成\n被查人員：" + cl.getContact(mid).displayName + "\n開始執行(,,・ω・,,)",op.message.id)
                        for i in gid:
                            group = cl.getGroup(i)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in txt:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                pass
                            else:
                                for jj in matched_list:
                                    a += 1
                                    ret_ += "\n {}. {} | {}\nGid➲{}".format(str(a), str(group.name), str(len(group.members)),str(group.id))
                        ret_ += "\n共同 {} 個群組".format(str(a))
                        cl.relatedMessage(to, str(ret_),op.message.id)
                elif msg.text.startswith("Sa "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    num=1
                    gid = cl.getGroupIdsJoined()
                    gidl = []
                    for id in gid:
                        ids = cl.getGroup(id)
                        nama = [contact.mid for contact in ids.members]
                        if inkey in nama:
                            gidl.append(id)
                    msgs="=====共同群組名單====="
                    for x in gidl:
                        ins = cl.getGroup(x)
                        msgs+="\n[%i] %s" % (num, ins.name)
                        msgs+="\nGid:%s" % (x)
                        num=(num+1)
                    msgs+="\n=====共同群組名單=====\n\n群組數量:%i" % len(gidl)
                    cl.sendMessage(to, msgs)
                #專武線程
                elif text.lower().startswith("K "):
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                    	thread_exe(to,x["M"])
                    cl.sendMessage(op.message.to, "已踢除(｡･ω･｡)")
                elif text.lower().startswith("Ttk "):
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    n = 0
                    for x in key["MENTIONEES"]:
                    	thread_exe(to,x["M"])
                    cl.sendMessage(op.message.to, "已踢除")
                elif "spt" == op.message.text.lower(): 
                    t1 = time.time()
                    loop = asyncio.get_event_loop()
                    t2 = (time.time() - t1)
                    loop.close
                    return cl.relatedMessage(op.message.to, "【%.18f秒】" %t2,op.message.id)
                elif text.lower().startswith("sp3"):
                    t1 = time.time()
                    threading.Thread(target=cl.sendMessage, args=(to, "【Test Speed By Threading】",)).start()
                    t2 = time.time() - t1
                    time.sleep(0.10)
                    return cl.sendMessage(to, "【%s】" %t2) 
                elif text.lower() == cmdkick:
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    for g in gs.members:
                        if g.mid not in ban["admin"]:
                            targets.append(g.mid)
                    else:
                        cl.sendMessage(to,boomsend)
                        thread_exe(to,targets)
                elif text.lower().startswith(".Nk:"):
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    _name = op.message.text.replace(".Nk:","")
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.relatedMessage(msg.to,"群組沒有這個名字",op.message.id)
                    else:
                        thread_exe(to,targets)
                elif text.lower().startswith("tbk:"):
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    _bio = op.message.text.replace("tbk:","")
                    targets = []
                    gs = cl.getGroup(op.message.to)
                    try:
                        cl.unsendMessage(msg_id)
                    except:
                        pass
                    for g in gs.members:
                        try:
                            contact = cl.getContact(g.mid)
                            if _bio in contact.statusMessage:
                                targets.append(g.mid)
                        except:
                            pass
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif text.lower().startswith("cbk:"):
                    try:
                        cl.unsendMessage(msg.id)
                    except:
                        pass
                    _bio = op.message.text.replace("cbk:","")
                    targets = []
                    gs = cl.getGroup(op.message.to)
                    try:
                        cl.unsendMessage(msg_id)
                    except:
                        pass
                    for g in gs.invitee:
                        try:
                            contact = cl.getContact(g.mid)
                            if _bio in contact.statusMessage:
                                targets.append(g.mid)
                        except:
                            pass
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    cl.cancelGroupInvitation(to,[target])
                                except:
                                    pass
                elif text.lower() == '踢名單':
                    if msg.toType == 2:
                        group = cl.getGroup(op.message.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in ban["tlist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(op.message.to, "沒人(｡･ω･｡)")
                        else:
                            thread_exe(to,matched_list)
                elif text.lower() == '特殊拆':#特殊拆
                    if msg.toType == 2:
                        group = cl.getGroup(op.message.to)
                        gMembMids = [contact.mid for contact in group.members]
                        gInvMids = [contact.mid for contact in group.invitee]
                        matched_list = []
                        matched_list2 = []
                        for tag in ban["klist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        for can in ban["clist"]:
                            matched_list2+=filter(lambda str: str == can, gInvMids)
                        if matched_list and matched_list2 == []:
                            cl.sendMessage(op.message.to, "列表沒人")
                        else:
                            jg["JoinGroup"][to] = True
                            thread_exe(to,matched_list)
                            cancel_exe(to,matched_list2)
                elif text.lower() == '特殊拆2':#特殊拆
                    if msg.toType == 2:
                        group = cl.getGroup(op.message.to)
                        gMembMids = [contact.mid for contact in group.members]
                        gInvMids = [contact.mid for contact in group.invitee]
                        matched_list = []
                        matched_list2 = []
                        for tag in ban["tlist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        for can in ban["clist"]:
                            matched_list2+=filter(lambda str: str == can, gInvMids)
                        if matched_list and matched_list2 == []:
                            cl.sendMessage(op.message.to, "沒人(｡･ω･｡)")
                        else:
                            warmods["warmods"][to] = True
                            thread_exe(to,matched_list)
                            cancel_exe(to,matched_list2)
                elif text == "名單":
                    mc = "☵☵☵☵特殊名單☵☵☵☵"
                    for i,mi_d in enumerate(ban["tlist"]):
                        mc += "\n{}.{}".format(i+1,cl.getContact(mi_d).displayName)
                    mc += "\n☵☵☵☵共 {} 人☵☵☵☵".format(len(ban["klist"]))
                    mc += "\n☵☵☵☵取消名單☵☵☵☵"
                    for i,mi_d in enumerate(ban["clist"]):
                        mc += "\n{}.|{}".format(i+1,cl.getContact(mi_d).displayName)
                    mc += "\n☵☵☵☵共 {} 人☵☵☵☵".format(len(ban["clist"]))
                    if md != 0:
                            mc += "\n☵☵☵☵意外處理☵☵☵☵\n清理 %s 位不存在的帳號" % (md)
                    backupData() 
                    cl.sendMessage(to,mc)
                elif text.lower().startswith("tta ") or text.lower().startswith("Tta "):
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["tlist"][target] = True
                        except:
                            break
                    cl.sendMessage(op.message.to,"成功(｡･ω･｡)")
                elif text.lower().startswith("ttd ") or text.lower().startswith("Ttd "):
                    targets = []
                    key = eval(op.message.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["tlist"][target]
                            cl.sendMessage(op.message.to,"刪除踢人名單成功(｡･ω･｡)")
                            break
                        except:
                            cl.relatedMessage(op.message.to,"刪除踢人名單失敗(｡･ω･｡)")
                            break
                elif text.lower().startswith("Tma:") or text.lower().startswith("tma:"):
                    txt = text[4:]
                    try:
                        ban["tlist"][txt] = True
                        cl.sendMessage(op.message.to,"已踢人名單(｡･ω･｡)")
                    except:
                        cl.sendMessage(op.messageto,"添加名單失敗(｡･ω･｡)" +txt)
                elif text.lower().startswith("Tmd:") or text.lower().startswith("tmd"):
                    txt = text[4:]
                    try:
                        del ban["tlist"][txt]
                    except:
                        cl.sendMessage(op.message.to,"刪除" + str(txt) + "失敗(｡･ω･｡)")
                    cl.sendMessage(op.message.to,"已刪除名單(｡･ω･｡)")
                elif text.lower().startswith("Cma:") or text.lower().startswith("cma:"):
                    txt = text[4:]
                    try:
                        ban["clist"][txt] = True
                        cl.sendMessage(op.message.to,"已踢人名單(｡･ω･｡)")
                    except:
                        cl.sendMessage(op.messageto,"添加名單失敗(｡･ω･｡)" +txt)
                elif text.lower().startswith("Cmd:") or text.lower().startswith("cmd"):
                    txt = text[4:]
                    try:
                        del ban["clist"][txt]
                    except:
                        cl.sendMessage(op.message.to,"刪除" + str(txt) + "失敗(｡･ω･｡)")
                    cl.sendMessage(op.message.to,"已刪除名單(｡･ω･｡)")
                elif text.lower().startswith("tna ") or text.lower().startswith("Tna "):
                    _name = text[4:]
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a = 0
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    ban["tlist"][target] = True
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"加入名單失敗(｡･ω･｡)")
                        cl.sendMessage(op.message.to,"已增加名單共" + str(a) + "人(｡･ω･｡)")
                elif text.lower().startswith("tnd ") or text.lower().startswith("Tnd "):
                    _name = text[4:]
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a=0
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    del ban["tlist"][target]
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"刪除名單失敗(｡･ω･｡)")
                        cl.sendMessage(op.message.to,"已刪除名單共" + str(a) + "人(｡･ω･｡)")
                elif text.lower().startswith("cna ") or text.lower().startswith("Cna "):
                    _name = text[4:]
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a = 0
                    for g in gs.invitee:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    ban["clist"][target] = True
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"加入名單失敗(｡･ω･｡)")
                        cl.sendMessage(op.message.to,"已增加名單共" + str(a) + "人(｡･ω･｡)")
                elif text.lower().startswith("cnd ") or text.lower().startswith("Cnd "):
                    _name = text[4:]
                    gs = cl.getGroup(op.message.to)
                    targets = []
                    a=0
                    for g in gs.invitee:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in ban["admin"]:
                                pass
                            else:
                                try:
                                    del ban["clist"][target]
                                    a+=1
                                except:
                                    cl.sendMessage(op.message.to,"刪除名單失敗(｡･ω･｡)")
                        cl.sendMessage(op.message.to,"已刪除名單共" + str(a) + "人(｡･ω･｡)")
                elif text.lower().startswith("ai ") or text.lower().startswith("Ai "):
                    txt = text.split( )
                    st = text.replace(txt[0]+" ","")
                    a = []
                    group = cl.getGroup(to)
                    targets = []
                    text = "已加入取消名單"
                    num = 0
                    nama =[contact.mid for contact in group.invitee]
                    for x in st.split( ):a.append(x)
                    for xi in a:
                        gorue =nama[int(xi)-1]
                        targets.append(gorue)
                    for x in targets:
                        if x in ban["admin"]:
                            pass
                        else:
                            try:
                                num+=1
                                ban["clist"][x] = True
                                text += "\n"+str(num)+"."+str(cl.getContact(x).displayName)+"✔"
                            except:pass
                    text += "\n成功加入取消名單"
                    cl.relatedMessage(to, text,op.message.id)
                elif text.lower() == '清名單':
                    ban["tlist"] = {}
                    ban["clist"] = {}
                    json.dump(ban,codecs.open("ban.json","w","utf-8"), sort_keys=True, indent=4, ensure_ascii=False)
                    cl.sendMessage(op.message.to, "已清空(｡･ω･｡)")
        if op.type == 26:
            try:
                msg = op.message
                msg_id = msg.id
                sender = msg._from
                if msg.toType == 0:
                    cl.log("[%s]"%(msg._from)+msg.text)
                else:
                    if msg.contentType == 0: #文字
                        cl.log("[%s]"%(msg.to)+msg.text)
                    elif msg.contentType == 7: #貼圖
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata['STKID'])
                    elif msg.contentType == 13: #友資
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["mid"]+' '+msg.contentMetadata["displayName"])
                    elif msg.contentType == 14: #檔案
                        cl.log("[%s]"%(msg.to)+msg.contentMetadata["FILE_NAME"]+'檔案下載完成')
                    else: #若是都沒有則是錯誤
                        cl.log("[%s] [E]"%(msg.to)+msg.text)
                if msg.contentType == 0: #文字
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime, "optype":msg.toType}
                elif msg.contentType == 1: #圖片
                    image = cl.downloadObjectMsg(msg_id, saveAs="file/image/{}-jpg.jpg".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"image":image,"createdTime":msg.createdTime, "optype":msg.toType}
                    imagesave = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/image'))
                    if (imagesave > 3000):
                        cl.sendMessage(background,"清理圖片後台中....")
                        shutil.rmtree('/root/'+Backstage+'/file/image')
                        os.makedirs("/root/"+Backstage+"/file/image")
                        cl.sendMessage(background,"圖片後台清理完畢")
                    if wait["cpi"] == True:
                        if sender in botowner:
                            image = cl.downloadObjectMsg(msg_id, saveAs="cpi.jpg")
                            cl.sendMessage(msg.to, "圖片下載完成 正在更換頭貼(｡･ω･｡)")
                            wait["cpi"] = False
                            cl.updateProfilePicture(image)
                            os.remove("cpi.jpg")
                            cl.sendMessage(msg.to, "更改完成(｡･ω･｡)")
                elif msg.contentType == 2: #影片
                    createdTime=msg.createdTime
                    msg_idto=msg_id
                    def videowww(msg_idto,createdTime):
                        print("開始下載影片")
                        Video = cl.downloadObjectMsg(msg_id, saveAs="file/video/{}-Video.mp4".format(createdTime))
                        msg_dict[msg.id] = {"from":msg._from,"Video":Video,"createdTime":createdTime, "optype":msg.toType}
                    threading.Thread(target=videowww, args=(to,createdTime,)).start()
                    videosave = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/video'))
                    if (videosave > 300):
                        cl.sendMessage(background,"清理影片後台中....")
                        shutil.rmtree('/root/'+Backstage+'/file/video')
                        os.makedirs("/root/"+Backstage+"/file/video")
                        cl.sendMessage(background,"影片後台清理完畢")
                elif msg.contentType == 3: #錄音檔
                    sound = cl.downloadObjectMsg(msg_id, saveAs="file/sound/{}-sound.mp3".format(msg.createdTime))
                    msg_dict[msg.id] = {"from":msg._from,"sound":sound,"createdTime":msg.createdTime, "optype":msg.toType}
                    soundsave = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/sound'))
                    if (soundsave > 100):
                        cl.sendMessage(background,"清理語音後台中....")
                        shutil.rmtree('/root/'+Backstage+'/file/sound')
                        os.makedirs("/root/"+Backstage+"/file/sound")
                        cl.sendMessage(background,"語音後台清理完畢")
                elif msg.contentType == 7: #貼圖
                    msg_dict[msg.id] = {"from":msg._from,"id":msg.contentMetadata['STKID'],"createdTime":msg.createdTime, "optype":msg.toType}
                elif msg.contentType == 13: #友資
                    msg_dict[msg.id] = {"from":msg._from,"mid":msg.contentMetadata["mid"],"createdTime":msg.createdTime, "optype":msg.toType}
                elif msg.contentType == 14: #檔案
                    file = cl.downloadObjectMsg(msg_id, saveAs="file/file/{}-".format(msg.createdTime)+msg.contentMetadata['FILE_NAME'])
                    msg_dict[msg.id] = {"from":msg._from,"file":file,"createdTime":msg.createdTime, "optype":msg.toType}
                    filesave = sum(len(files) for _, _, files in os.walk(r'/root/'+Backstage+'/file/file'))
                    if (filesave > 100):
                        cl.sendMessage(background,"清理檔案後台中....")
                        shutil.rmtree('/root/'+Backstage+'/file/file')
                        os.makedirs("/root/"+Backstage+"/file/file")
                        cl.sendMessage(background,"檔案後台清理完畢")
                else: #若是都沒有則是錯誤
                    msg_dict[msg.id] = {"from":msg._from,"createdTime":msg.createdTime, "optype":msg.toType}
            except Exception as e:
                print(e)
        if op.type == 65:
            at = background
            msg_id = op.param2
            try:
                abc = cl.getContact(msg_dict[msg_id]["from"])
            except:
                pass
            if msg_id in msg_dict:
                if msg_dict[msg_id]["from"] not in ig["ig"]:
                    if msg_dict[msg_id]["from"] not in red["rereadMID"]:
                        if at not in red["rereadGID"]:
                            if at not in red["reread"]:
                                rereadtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(round(msg_dict[msg_id]["createdTime"]/1000))))
                                newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                                if 'text' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    if "ণاعနัゆीՁşัढे囟ֆ₤❂Ǥª₦🔝" in msg_dict[msg_id]["text"] or ".1.2.3.4.5.6.7.8.9.0.A.1.B.2.D.3.E.4.F.5.G.6.H.7.I.8.J.9.K.0." in msg_dict[msg_id]["text"] or "జ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞాజ్ఞా" in msg_dict[msg_id]["text"]:txr = '\n[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%("<他收回了一個當機文>",rereadtime,newtime)
                                    else:txr = '\n[收回訊息]\n%s\n[發送時間]\n%s\n[收回時間]\n%s'%(msg_dict[msg_id]["text"],rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_ , contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    del msg_dict[msg_id]
                                elif 'id' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一張貼圖]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    yesno = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/IOS/sticker_animation.png'
                                    ok = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + msg_dict[msg_id]["id"] + '/ANDROID/sticker.png'
                                    cl.sendImageWithURL(at, ok)
                                    del msg_dict[msg_id]
                                elif 'mid' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一個友資]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendContact(at,msg_dict[msg_id]["mid"])
                                    del msg_dict[msg_id]
                                elif 'sound' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一個錄音檔]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendAudio(at, msg_dict[msg_id]["sound"])
                                    del msg_dict[msg_id]
                                elif 'file' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一個檔案]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendFile(at, msg_dict[msg_id]["file"])
                                    del msg_dict[msg_id]
                                elif 'image' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一張圖片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    cl.sendImage(at, msg_dict[msg_id]["image"])
                                    del msg_dict[msg_id]
                                elif 'Video' in msg_dict[msg_id]:
                                    aa = '{"S":"0","E":"3","M":'+json.dumps(msg_dict[msg_id]["from"])+'}'
                                    txr = '\n[收回了一部影片]\n在下面\n[發送時間]\n%s\n[收回時間]\n%s'%(rereadtime,newtime)
                                    msgop = msg_dict[msg_id]["optype"]
                                    pesan = '@c \n'
                                    if msgop == 0:
                                        rat_ = "收回位置：私訊"
                                    elif msgop == 1:
                                        rat_ = "收回位置：副本"
                                    elif msgop == 2:
                                        gn = cl.getGroup(op.param1).name
                                        rat_ = "群組名稱:\n{}".format(gn)
                                        rat_ += "\n群組識別:\n{}".format(op.param1)
                                    text_ =  pesan + rat_
                                    text_ += "\n收回人員名稱："+ abc.displayName
                                    text_ += "\n收回人員MID："+ abc.mid
                                    text_ += txr
                                    cl.sendMessage(at, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                                    #cl.sendMessage(at, msg_dict[msg_id]["Video"])
                                    cl.sendVideo(at, msg_dict[msg_id]["Video"])
                                    del msg_dict[msg_id]
                                else:
                                    pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[★]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[★]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
#==============================================================================#
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
#==============================================================================#
