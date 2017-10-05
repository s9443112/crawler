#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import HTMLParser
import time
from random import randint
import sys
from IPython.display import clear_output
import http.client
import json
import datetime
import os

IDs=[
#1906,
#1907,
#1909,
#2002,#have question
#2006,
#2007,
#2008,
#2009,
#2010,
#2012,
#2013,
#2014,
#2015,
#2017,
#2020,
#2022,
#2023,
#2024,
#2025,
#2027,
#2028,
#2029,
#2030,
#2031,
#2032,
#2033,
#2034,
#2038,
#2049,#question
#2059,
#2062,
#2069,
#2101,
#2102,
#2103,
#2104,#question
#2105,
#2106,
#2107,
#2108,
#2109,
#2114,
#2115,
#2201,
#2204,
#2206,#question
#2207,
#2208,
#2227,
#2228,
#2231,
#2236,
#2239,
#2301,
#2302,
#2303,#question
#2305,
#2308,
#2311,
#2312,#question
#2313,
#2314,
#2316,#question
#2317,#question
#2321,
#2323,
#2324,
2325,
2327,#question
2328,
2329,
2330,
2331,
2332,
2337,
2338,
2340,#question
2342,
2344,
2345,
2347,
2348,
2349,
2351,#question
2352,
2353,
2354,
2355,
2356,
2357,
2358,
2359,
2360,
2362,
2363,
2365,
2367,
2368,
2369,
2371,#question
2373,
2374,
2375,
2376,
2377,#question
2379,
2380,
2382,





2383,
2385,
2387,
2388,
2390,
2392,
2393,
2395,
2397,
2399,

]

brokers = [1020
,1021
,1022
,1023
,1024
,1025
,1028
,1029
,1030
,1031
,1032
,1033
,1034
,1035
,1036
,1037
,1038
,1039
,1040
,1041
,1042
,1043
,1045
,1090
,1091
,1093
,1095
,1096
,1097
,1110
,1111
,1112
,1113
,1114
,1115
,1116
,1117
,1118
,1119
,1160
,1161
,1162
,1163
,1164
,1165
,1166
,1167
,1168
,1169
,1230
,1232
,1233
,1260
,1261
,1262
,1264
,1360
,1380
,1440
,1470
,1480
,1520
,1530
,1560
,1570
,1590
,1650
,1660
,2180
,2181
,2184
,2185
,2186
,2187
,2188
,2189
,2200
,2210
,5050
,5110
,5112
,5260
,5261
,5262
,5263
,5264
,5265
,5266
,5267
,5268
,5269
,5320
,5321
,5322
,5323
,5380
,5381
,5382
,5383
,5384
,5385
,5386
,5387
,5389
,5460
,5600
,5602
,5603
,5604
,5660
,5850
,5851
,5852
,5853
,5854
,5855
,5856
,5857
,5858
,5859
,5860
,5861
,5862
,5870
,5920
,5921
,5922
,5923
,5925
,5927
,5928
,5926
,5929
,5960
,5961
,5962
,5964
,6012
,6010
,6110
,6114
,6115
,6116
,6117
,6160
,6161
,6163
,6162
,6164
,6165
,6166
,6167
,6168
,6169
,6210
,6380
,6381
,6382
,6383
,6385
,6386
,6450
,6388
,6451
,6452
,6460
,6461
,6463
,6462
,6464
,6465
,6480
,6530
,6531
,6532
,6533
,6536
,6535
,6534
,6537
,6538
,6539
,6620
,6910
,6911
,6912
,6913
,6914
,6915
,6950
,7000
,7001
,7003
,7005
,7006
,7007
,7009
,7008
,7020
,7030
,7031
,7032
,7033
,7034
,7035
,7036
,7038
,7070
,7080
,7671
,7670
,7750
,7790
,7791
,7792
,7795
,7797
,7798
,7900
,8150
,8380
,8381
,8382
,8440
,8450
,8451
,8454
,8455
,8456
,8458
,8459
,8490
,8520
,8560
,8561
,8562
,8563
,8564
,8565
,8580
,8581
,8582
,8583
,8584
,8585
,8586
,8587
,8588
,8660
,8710
,8711
,8712
,8770
,8840
,8841
,8842
,8843
,8844
,8845
,8846
,8847
,8848
,8849
,8850
,8880
,8881
,8882
,8883
,8884
,8885
,8886
,8887
,8890
,8900
,8960
,9100
,9101
,9103
,9105
,9108
,9131
,9133
,9134
,9135
,9136
,9137
,9138
,9183
,9184
,9185
,9186
,9187
,9188
,9189
,9199
,9200
,9202
,9204
,9205
,9206
,9207
,9208
,9209
,9211
,9212
,9215
,9216
,9217
,9218
,9221
,9224
,9223
,9225
,9226
,9227
,9229
,9231
,9232
,9233
,9234
,9235
,9236
,9237
,9238
,9239
,9243
,9252
,9254
,9255
,9256
,9257
,9258
,9259
,9265
,9266
,9268
,9269
,9272
,9273
,9274
,9275
,9276
,9278
,9281
,9283
,9285
,9287
,9288
,9289
,9291
,9294
,9296
,9297
,9298
,9299
,9300
,9302
,9303
,9305
,9306
,9307
,9308
,9309
,9312
,9314
,9315
,9316
,9317
,9319
,9321
,9322
,9323
,9324
,9325
,9326
,9327
,9328
,9329
,9331
,9332
,9333
,9334
,9336
,9337
,9339
,9343
,9347
,9348
,9349
,9352
,9358
,9359
,9362
,9363
,9364
,9365
,9369
,9372
,9377
,9381
,9382
,9386
,9399
,9600
,9602
,9604
,9607
,9608
,9614
,9615
,9616
,9618
,9621
,9622
,9623
,9624
,9625
,9627
,9634
,9636
,9645
,9647
,9648
,9651
,9652
,9653
,9654
,9655
,9656
,9657
,9658
,9659
,9661
,9663
,9664
,9665
,9666
,9667
,9668
,9671
,9672
,9676
,9677
,9678
,9679
,9682
,9686
,9689
,9692
,9693
,9694
,9695
,9697
,9800
,9801
,9812
,9813
,9814
,9815
,9816
,9817
,9819
,9821
,9822
,9824
,9825
,9829
,9831
,9833
,9834
,9835
,9836
,9837
,9838
,9852
,9853
,9854
,9856
,9857
,9858
,9859
,9862
,9863
,9866
,9867
,9868
,9869
,9871
,9872
,9873
,9874
,9875
,9876
,9878
,9879
,9884
,9886
,9888
,9889
,9891
,9892
,9893
,9894
,9896
,9897
,9898
,9899
,"102A"
,"102C"
,"102E"
,"102F"
,"102G"
,"103A"
,"103B"
,"103C"
,"103F"
,"104A"
,"104C"
,"104D"
,"109A"
,"109K"
,"111A"
,"111B"
,"111C"
,"111D"
,"111E"
,"111F"
,"111G"
,"116A"
,"116B"
,"116b"
,"116C"
,"116c"
,"116d"
,"116e"
,"116E"
,"116F"
,"116f"
,"116g"
,"116G"
,"116H"
,"116i"
,"116I"
,"116J"
,"116j"
,"116k"
,"116K"
,"116L"
,"116m"
,"116M"
,"116N"
,"116P"
,"116Q"
,"116r"
,"116s"
,"116S"
,"116U"
,"116v"
,"116W"
,"116V"
,"116w"
,"116x"
,"116X"
,"116Z"
,"126D"
,"126H"
,"126Q"
,"126L"
,"126U"
,"126V"
,"126X"
,"218A"
,"526A"
,"526B"
,"526K"
,"526L"
,"538a"
,"538A"
,"538B"
,"538C"
,"538D"
,"538E"
,"538F"
,"538G"
,"538I"
,"538j"
,"538M"
,"538N"
,"538P"
,"538U"
,"538V"
,"538X"
,"538W"
,"538Y"
,"585A"
,"585B"
,"585b"
,"585C"
,"585c"
,"585D"
,"585d"
,"585E"
,"585e"
,"585f"
,"585F"
,"585g"
,"585h"
,"585G"
,"585H"
,"585I"
,"585J"
,"585L"
,"585m"
,"585M"
,"585N"
,"585P"
,"585Q"
,"585R"
,"585s"
,"585S"
,"585U"
,"585V"
,"585W"
,"585Y"
,"585Z"
,"592a"
,"592A"
,"592B"
,"592b"
,"592c"
,"592C"
,"592D"
,"592d"
,"592e"
,"592E"
,"592f"
,"592g"
,"592G"
,"592H"
,"592i"
,"592I"
,"592j"
,"592L"
,"592l"
,"592M"
,"592m"
,"592n"
,"592N"
,"592o"
,"592P"
,"592Q"
,"592q"
,"592r"
,"592S"
,"592U"
,"592u"
,"592v"
,"592V"
,"592W"
,"592w"
,"592Y"
,"592X"
,"592y"
,"592z"
,"592Z"
,"611A"
,"616A"
,"616K"
,"616X"
,"653B"
,"653C"
,"653D"
,"653E"
,"653J"
,"700a"
,"700B"
,"700b"
,"700C"
,"700c"
,"700D"
,"700d"
,"700E"
,"700f"
,"700F"
,"700G"
,"700g"
,"700H"
,"700h"
,"700I"
,"700i"
,"700j"
,"700J"
,"700k"
,"700K"
,"700L"
,"700m"
,"700M"
,"700N"
,"700P"
,"700p"
,"700q"
,"700r"
,"700R"
,"700s"
,"700S"
,"700U"
,"700V"
,"700W"
,"700w"
,"700X"
,"700Z"
,"703A"
,"703B"
,"779b"
,"779c"
,"779D"
,"779E"
,"779e"
,"779G"
,"779H"
,"779j"
,"779J"
,"779L"
,"779m"
,"779n"
,"779P"
,"779r"
,"779u"
,"779V"
,"779v"
,"779W"
,"779w"
,"779X"
,"779y"
,"779Z"
,"779z"
,"815A"
,"815B"
,"845A"
,"845B"
,"845D"
,"845E"
,"845F"
,"845J"
,"845R"
,"845S"
,"845U"
,"845X"
,"845V"
,"845Y"
,"884A"
,"884B"
,"884C"
,"884D"
,"884E"
,"884F"
,"884G"
,"884H"
,"884I"
,"884J"
,"884L"
,"884K"
,"888A"
,"888K"
,"888Q"
,"910D"
,"913B"
,"913C"
,"913D"
,"913E"
,"913g"
,"913H"
,"913I"
,"913K"
,"913N"
,"913R"
,"913U"
,"913Y"
,"918A"
,"918B"
,"918C"
,"918c"
,"918D"
,"918d"
,"918E"
,"918e"
,"918F"
,"918G"
,"918g"
,"918H"
,"918i"
,"918J"
,"918K"
,"918L"
,"918M"
,"918P"
,"918R"
,"918s"
,"918u"
,"918W"
,"918X"
,"918x"
,"918z"
,"920A"
,"920C"
,"920D"
,"920E"
,"920F"
,"920G"
,"920H"
,"920N"
,"920M"
,"920Z"
,"920V"
,"920W"
,"921A"
,"921C"
,"921E"
,"921F"
,"921G"
,"921H"
,"921J"
,"921M"
,"921S"
,"921Y"
,"922C"
,"922H"
,"960S"
,"965K"
,"965U"
,"966F"
,"969C"
,"980a"
,"980B"
,"980C"
,"980D"
,"980d"
,"980e"
,"980g"
,"980h"
,"980l"
,"980K"
,"980Q"
,"980R"
,"980u"
,"980w"
,"981B"
,"981a"
,"981A"
,"981C"
,"981D"
,"981e"
,"981E"
,"981F"
,"981g"
,"981G"
,"981h"
,"981i"
,"981I"
,"981J"
,"981j"
,"981K"
,"981L"
,"981m"
,"981M"
,"981n"
,"981N"
,"981p"
,"981q"
,"981Q"
,"981r"
,"981R"
,"981S"
,"981U"
,"981V"
,"981X"
,"981y"
,"981Z"
,"981z"
,"982A"
,"982B"
,"982C"
,"982F"
,"983B"
,"983f"
,"983G"
,"983i"
,"983J"
,"983j"
,"983K"
,"983M"
,"983U"
,"983N"
,"983V"
,"983W"
,"983Z"
,"984C"
,"984E"
,"984H"
,"984K"
,"985C"
,"986A"
,"986K"
,"987D"
,"987A"
,"988B"
,"988C"
,"989a"
,"989A"
,"989B"
,"989C"
,"989D"
,"989d"
,"989e"
,"989E"
,"989f"
,"989F"
,"989g"
,"989G"
,"989I"
,"989J"
,"989j"
,"989k"
,"989L"
,"989m"
,"989N"
,"989P"
,"989Q"
,"989S"
,"989U"
,"989V"
,"989W"
,"989X"
,"989Y"
,"989z"
,"989Z"
,"9A00"
,"9A61"
,"9A68"
,"9A69"
,"9A88"
,"9A89"
,"9A8F"
,"9A91"
,"9A92"
,"9A93"
,"9A96"
,"9A97"
,"9A98"
,"9A99"
,"9A9a"
,"9A9A"
,"9A9B"
,"9A9b"
,"9A9C"
,"9A9c"
,"9A9d"
,"9A9D"
,"9A9e"
,"9A9E"
,"9A9F"
,"9A9f"
,"9A9G"
,"9A9g"
,"9A9H"
,"9A9h"
,"9A9i"
,"9A9J"
,"9A9k"
,"9A9j"
,"9A9K"
,"9A9M"
,"9A9L"
,"9A9m"
,"9A9N"
,"9A9p"
,"9A9P"
,"9A9Q"
,"9A9q"
,"9A9R"
,"9A9r"
,"9A9S"
,"9A9s"
,"9A9U"
,"9A9V"
,"9A9v"
,"9A9W"
,"9A9x"
,"9A9X"
,"9A9Y"
,"9A9Z"
]


import time
for ID in IDs:

    ID = str(ID)
    shop_list = open(ID+'.csv',encoding = "utf-8",mode = 'w',newline='')
    shop_list.write('Date'+','+'broker'+','+'buy'+','+'sell'+','+'buyPer'+','+'sellPer'+','+'netPer'+','+'buyWeek'+','+'sellWeek'+','+'netWeek'+','+'buyWeekPer'+','+'sellWeekPer'+','+'last_price'+','+'netWeekPer')

    for broker in brokers:
        broker = str(broker)

        #print(data.decode("utf-8"))
        try:
            filea = open(ID+'/'+broker+'.txt', "r+",encoding='utf-8')
            fileaStrings = filea.read()

            try:

                res_data = json.loads(fileaStrings)
                shop_list.write('\n')

                StartDate = time.strptime("2015/06/07", "%Y/%m/%d")
                EndDate = time.strptime("2016/10/05", "%Y/%m/%d")
                StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
                EndDate =  datetime.date(EndDate[0], EndDate[1], EndDate[2])
                RangeDate = datetime.timedelta(days = 1)
                while StartDate <= EndDate:
                    z = StartDate + RangeDate
                    yearmonthday = str(z)
                    print (z)
                    try:
                        shop_list.write(str(res_data['chartData']['ba'][yearmonthday]['date'])+',')
                        shop_list.write(str(broker)+',')
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
                        print("out of range")


                    StartDate = StartDate + RangeDate

                shop_list.write('\n')
                print("complete "+" broker "+str(broker))
                sys.stdout.flush()
            except Exception as e:
                print("out of range")
        except Exception as e:
            print("out of range")
    print("All complete")
    shop_list.close()
