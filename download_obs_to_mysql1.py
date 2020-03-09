#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
 This sample demonstrates how to upload multiparts to OBS
 using the OBS SDK for Python.
'''
import os
import csv
import time
import pymysql
from obs import ObsClient


def insertMysql(filename):
    filen_data = []


    if "podserver_ip" in filename:
        i = 0
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1", 'root', 'root', 'reptile', 3306)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        print("开始写入数据库")
        with open("D:\\python\\1\\"+filename) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                username=row[0]
                domain_id=row[1]
                public_ip=row[2]
                status=row[3]
                # create_time=row[4]
                create_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                try:
                    try:
                        sql = '''insert into t_ad_pod_server set username='{0}',domain_id='{1}', public_ip='{2}',status='{3}',time='{4}',detection='{5}' '''
                        sql = sql.format(username,domain_id,public_ip,status,create_time.replace("T"," ").replace("Z",""),username+public_ip)
                        cursor.execute(sql)
                        i=i+1
                    except:
                        sql = "UPDATE t_ad_pod_server  SET create_time='" + str(
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + "' where detection='" + (
                                          username + public_ip) + "'"
                        cursor.execute(sql)
                        # print("重复了", i)

                except:
                    continue
        db.commit()
        # 关闭数据库连接
        db.close()
        csvfile.close()
        print("写完了", i)

    else:
        time_string=str(time.strftime("%Y%m%d", time.localtime())) + ".csv"
        i = 0
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1", 'root', 'root', 'reptile', 3306)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        print("开始写入数据库")
        with open("D:\\python\\1\\" + filename,encoding ='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                username = filename.replace(time_string,"")
                domain_id = filename.replace(time_string,"")
                public_ip = row[0]
                status = ""
                create_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                try:
                    try:
                        sql = '''insert into t_ad_pod_server set username='{0}',domain_id='{1}', public_ip='{2}',status='{3}',time='{4}',detection='{5}' '''
                        sql = sql.format(username, domain_id, public_ip, status, create_time, username + public_ip)
                        cursor.execute(sql)
                        i = i + 1
                    except:
                        sql="UPDATE t_ad_pod_server  SET create_time='"+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"' where detection='"+(username + public_ip)+"'"
                        cursor.execute(sql)
                        # print("重复了", i)


                except:
                    continue
        db.commit()
        # 关闭数据库连接
        db.close()
        csvfile.close()
        print("写完了", i)

if __name__ == '__main__':

    while 1:
        if str(time.strftime("%H%M", time.localtime())) =="1200":
        # if 1:
            filename1 = "podserver_ip.csv"
            filename2 = "platform_ip.csv"
            filename3 = "cdn_ip.csv"
            for filename in [filename1,filename2,filename3]:
                try:
                    try:
                        print(filename)
                        # 创建ObsClient实例
                        obsClient = ObsClient(
                            access_key_id='',
                            secret_access_key='',
                            server='https://obs.cn-north-4.myhuaweicloud.com'
                        )

                        resp = obsClient.getObject('1',"basedata/"+filename.replace(".csv","")+"/"+filename, downloadPath="1/"+filename)
                        if resp.status < 300:
                            print('requestId:', resp.requestId)
                            print('url:', resp.body.url)
                            insertMysql(filename)
                        else:
                            print('errorCode:', resp.errorCode)
                            print('errorMessage:', resp.errorMessage)
                        os.remove("D:\\python\\1\\"+filename)
                    except:
                        time.sleep(10)
                        print(filename)
                        # 创建ObsClient实例
                        obsClient = ObsClient(
                            access_key_id='1',
                            secret_access_key='1',
                            server='https://obs.cn-north-4.myhuaweicloud.com'
                        )

                        resp = obsClient.getObject('1',
                                                   "basedata/" + filename.replace(".csv", "") + "/" + filename,
                                                   downloadPath="1/" + filename)
                        if resp.status < 300:
                            print('requestId:', resp.requestId)
                            print('url:', resp.body.url)
                            insertMysql(filename)
                        else:
                            print('errorCode:', resp.errorCode)
                            print('errorMessage:', resp.errorMessage)
                        os.remove("D:\\python\\1\\" + filename)
                except:
                    print("error download")
        time.sleep(60)