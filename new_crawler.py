#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import HTMLParser
import http.client
import json
import os
import datetime
from datetime import datetime as dt
import threading
import queue
import time
import sys
import csv

brokers = []
IDs=[]

class Worker(threading.Thread):
    def __init__(self, queue,num):
        threading.Thread.__init__(self)
        self.num = num
        self.queue = queue
        # self.broker = queue.get()[0]
        # self.ID = queue.get()[1]
    def run(self):
        buffer = self.queue.get()
        self.broker = buffer[0]
        self.ID = buffer[1]
        shop_list = open(self.ID+'.csv',encoding = "utf-8",mode = 'w',newline='')
        print("被打開來")
        while not self.queue.empty():

            get_html = open(self.ID+'/'+self.broker+'.txt',encoding = "utf-8",mode = 'w')
            conn = http.client.HTTPSConnection("www.nvesto.com",timeout=10)
            payload = "fromdate=2015-05-01&todate=2016-10-06&broker="+str(self.broker)
            headers = {
                'content-type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache",
                'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"
                }
            conn.request("POST", "/brokeranalysis/ajaxGetData/sotckType/tpe/stockId/"+self.ID, payload, headers)
            res = conn.getresponse()    
            data = res.read()
            get_html.write(data.decode("utf-8"))
            get_html.close()
            
            # 解析
           
            shop_list.write('Date'+','+'券商'+','+'buy'+','+'sell'+','+'buyPer'+','+'sellPer'+','+'netPer'+','+'buyWeek'+','+'sellWeek'+','+'netWeek'+','+'buyWeekPer'+','+'sellWeekPer'+','+'last_price'+','+'netWeekPer')
            
            try:
                data = data.decode("utf-8")
                res_data = json.loads(data)
                shop_list.write('\n')
                StartDate = time.strptime("2015/05/01", "%Y/%m/%d")
                EndDate = time.strptime("2016/10/06", "%Y/%m/%d")
                StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
                EndDate = datetime.date(EndDate[0], EndDate[1], EndDate[2])
                # EndDate =  datetime.date(EndDate[0], EndDate[1], EndDate[2])
                RangeDate = datetime.timedelta(days = 1)
                while StartDate <= EndDate:
                    z = StartDate + RangeDate
                    yearmonthday = str(z)
                    try:
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['date'])+',')
                        shop_list.write(str(self.broker)+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['buy'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['sell'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['buyPer'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['sellPer'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['netPer'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['buyWeek'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['sellWeek'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['netWeek'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['buyWeekPer'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['sellWeekPer'])+',')
                        shop_list.write(str(res_data['stockpriceData']['stockprice'][yearmonthday]['last_price'])+',')
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['netWeekPer'])+',')
                        shop_list.write('\n')
                    except Exception as e:
                        pass
                        
                    StartDate = StartDate + RangeDate

                shop_list.write('\n')
                print("complete ID: "+str(self.ID)+" broker: "+str(self.broker)+" Worker %d" % (self.num))
                sys.stdout.flush()
            except Exception as e:
                print(e)
                print("out of range")
            #time.sleep(1)


# 建立佇列
my_queue = queue.Queue()

with open('123.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile)
  for row in spamreader:
    if row[0] != '':
        brokers.append(row[0])
    
    if row[1] != '':
        IDs.append(row[1])
    

for ID in IDs: # 證券代碼

    ID = str(ID)
    try:
        os.mkdir(ID) #創見目錄
    except Exception as e:
        print(e)
        print("File have exist "+ID)

    for broker in brokers: #卷商

        broker = str(broker)
        x = [broker,ID]
        my_queue.put(x)
    #print("All complete "+str(ID))

starttime = dt.now()
print("開始 "+str(starttime))
# 建立兩個 Worker
my_worker1 = Worker(my_queue, 1)
my_worker2 = Worker(my_queue, 2)
my_worker3 = Worker(my_queue, 3)
my_worker4 = Worker(my_queue, 4)
my_worker5 = Worker(my_queue, 5)
my_worker6 = Worker(my_queue, 6)
my_worker7 = Worker(my_queue, 7)
my_worker8 = Worker(my_queue, 8)

# 讓 Worker 開始處理資料
my_worker1.start()
my_worker2.start()
my_worker3.start()
my_worker4.start()
my_worker5.start()
my_worker6.start()
my_worker7.start()
my_worker8.start()

# 等待所有 Worker 結束
my_worker1.join()
my_worker2.join()
my_worker3.join()
my_worker4.join()
my_worker5.join()
my_worker6.join()
my_worker7.join()
my_worker8.join()


print("全部結束 "+str(dt.now()-starttime))

    


