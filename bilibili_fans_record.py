# coding: utf-8
import requests
import json
from datetime import datetime
import time
import os.path

#jump = int(input('时间间隔：') or 43200)
jump = int(30)

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "")



fanss = []
names = []
names1 = {}
fanss2 = {}
names2 = {}
#uid = input('uid:') or 2100679
uids = [2100679,508963009,1838190318,1749046,541696090]
i = 0
for uid in uids:
    web = 'https://api.bilibili.com/x/web-interface/card?mid=' + str(uid)
    data = requests.get(web)
    info = json.loads(data.text)
    fanss.append(info['data']['card']['fans'])
    names.append(info['data']['card']['name'])
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(names[i]+" 的粉丝数量为："+str(fanss[i]))
    print('变化量：-')

    filename = path+"/文档/" + str(uid) + "  " + str(names[i]) + '.txt'

    if not os.path.exists(filename):
        def text_create(name, msg):
            desktop_path = path+"/文档/"  # 新创建的txt文件的存放路径
            full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
            file = open(full_path, 'w')
            file.write(msg)  # msg也就是下面的Hello world!
            # file.close()

        text_create(str(uid) + "  " + str(names[i]), '')

    file_handle=open(path+"/文档/" + str(uid) + "  " + str(names[i]) + '.txt', mode='a')
    file_handle.write('|-'+'\n'+'|'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'  ' + "||"+str(fanss[i])+' || '+'0'+'\n')
    file_handle.close()
    i = i+1

def timer(n):
    ifif = 0
    while True:
        for index in range(len(uids)):
            f = open(path+"/文档/" + str(uids[index]) + "  " + str(names[index]) + '.txt', mode='a')

            if (ifif == 0):
                web = 'https://api.bilibili.com/x/web-interface/card?mid=' + str(uids[index])
                data = requests.get(web)
                info = json.loads(data.text)
                fanss[index] = info['data']['card']['fans']
                names[index] = info['data']['card']['name']
            else:
                fanss[index] = fanss2[index]
                names[index] = names2[index]

        ifif = 1
        time.sleep(n)
        for index in range(len(uids)):
            web = 'https://api.bilibili.com/x/web-interface/card?mid=' + str(uids[index])
            data2 = requests.get(web)
            info2 = json.loads(data2.text)
            fanss2[index] = info2['data']['card']['fans']
            names2[index] = info2['data']['card']['name']
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print(names[index]+" 的粉丝数量为："+str(fanss2[index]))
            print('变化量：'+str(fanss2[index]-fanss[index]))

            str2 = '|-'+'\n'+'|'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'  ' + "||"+str(fanss2[index])+' || '+str(fanss2[index]-fanss[index])+'\n'
            # str2 = bytes(str2, encoding = "utf8")
            ff = open(path + "/文档/" + str(uids[index]) + "  " + str(names[index]) + '.txt', mode='a')
            ff.write(str2)
            ff.close()

timer(jump)