# -*- coding: utf-8 -*-
import json

from flask import Flask,jsonify,request
from flask_cors import CORS
import datetime
import ruz
import asyncio
import websockets
import requests

from datetime import date



# def fun1(fio):
#     r = requests.get("https://ruz.hse.ru/api/search?term=" + fio).json()
#     data_of_names1 = []
#     for i in range(len(r)):
#         data_of_names1.append(r[i]['label'])
#     data_of_names = ((str(data_of_names1).replace("'", "")).replace("[", "")).replace("]", "")
#
# def fun2(fiofortt):
#     fortt = str(fiofortt)
#     rowinf_student = requests.get("https://ruz.hse.ru/api/search?term=" + fortt).json()
#     id = str(rowinf_student[0]['id'])
#     current_date = date.today()
#     date_string1 = current_date.strftime("%Y.%m.%d")
#     next_date = current_date + datetime.timedelta(days=7)
#     date_string2 = next_date.strftime("%Y.%m.%d")
#     timetable = requests.get(
#         "https://ruz.hse.ru/api/schedule/student/" + id + "?start=" + date_string1 + "&finish=" + date_string1 + "&lng=1").json()
#     firstlessons1 = []
#     for i in range(len(timetable)):
#         if i != 3:
#             firstlessons1.append(timetable[i]["beginLesson"])
#             firstlessons1.append(timetable[i]["endLesson"])
#             firstlessons1.append(timetable[i]["discipline"])
#     firstlessons = ((str(firstlessons1).replace("'", "")).replace("[", "")).replace("]", "")
#     print(firstlessons)
#
# def main():
#     fun1("Иванов Илья")
#     fun2("Иванов Илья Романович")
#
# main()





# fio = "Иванов Илья Романович"
# r = requests.get("https://ruz.hse.ru/api/search?term="+fio).json()
# id =str( r[0]['id'])
# current_date = date.today()
# date_string1 = current_date.strftime("%Y.%m.%d")
# next_date = current_date + datetime.timedelta(days=7)
# date_string2 = next_date.strftime("%Y.%m.%d")
# timetable = requests.get("https://ruz.hse.ru/api/schedule/student/"+id+"?start="+date_string1+"&finish="+date_string1+"&lng=1").json()
# firstlessons1=[]
# for i in range(len(timetable)):
#     if i!=3:
#         firstlessons1.append(timetable[i]["beginLesson"])
#         firstlessons1.append(timetable[i]["endLesson"])
#         firstlessons1.append(timetable[i]["discipline"])
# firstlessons = ((str(firstlessons1).replace("'","")).replace("[","")).replace("]","")
#
# print(firstlessons);


# current_date = date.today()
# date_string1 = current_date.strftime("%Y.%m.%d")
# next_date = current_date + datetime.timedelta(days=1)
# date_string2 = next_date.strftime("%Y.%m.%d")
# r = requests.get("https://ruz.hse.ru/api/search?term=Скопин Никита").json()
# r1 = requests.get("https://ruz.hse.ru/api/schedule/student/"+r[0]['id']+ "?start="+date_string1 +"&finish="+date_string1+"&lng=1").json()
# timeobject = []
# for i in range(len(r1)):
#     if i<=2:
#         timeobject.append(r1[i]['beginLesson'])
#         timeobject.append(r1[i]['endLesson'])
#         timeobject.append(r1[i]['discipline'])
#
# print(timeobject)


# s_city = "Moscow,RU"
# city_id = 0
# appid = "6b6165b5f3b150c75f572a0ec7ad1f00"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                  params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
#     data = res.json()
#     cities = ["{} ({})".format(d['name'], d['sys']['country'])
#               for d in data['list']]
#     city_id = data['list'][0]['id']
# except Exception as e:
#     pass
#
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/weather",
#                  params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#     data = res.json()
#     dataweather=[]
#     dataweather.append(data['weather'][0]['description'])
#     dataweather.append(int(data['main']['temp']))
#     dataweather.append(data['weather'][0]['icon'])
# except Exception as e:
#     pass
# print(dataweather)



# mail = "yaaantonova@edu.hse.ru"
# current_date = date.today()
# date_string1 = current_date.strftime("%Y.%m.%d")
# next_date = current_date + datetime.timedelta(days=2)
# date_string2 = next_date.strftime("%Y.%m.%d")
# r = ruz.person_lessons(mail)
# print(type(r))
# print(r)
# FirstLesson1 = 'Нет пары'
# FirstLesson2='время'
# SecondLesson1='Нет пары'
# SecondLesson2='время'
# ThirdLesson1='Нет пары'
# ThirdLesson2='время'
# n=0
# for i in range(len(r)):
#     n = n + 1
#     if (n == 1):
#         FirstLesson1 = r[i]['discipline']
#         FirstLesson2 = r[i]['beginLesson']
#     if (n==2):
#         SecondLesson1 = r[i]['discipline']
#         SecondLesson2 = r[i]['beginLesson']
#     if (n==3):
#         ThirdLesson1= r[i]['discipline']
#         ThirdLesson2= r[i]['beginLesson']
# dataset=[FirstLesson1, FirstLesson2,SecondLesson1,SecondLesson2,ThirdLesson1,ThirdLesson2]
# print(dataset)








async def yourtimetable(websocket):
    while True:
        async for fio in websocket:
            print(fio)
            fiostr = str(fio)
            ch='•'
            if ch in fiostr:

                s_city = "Moscow,RU"
                city_id = 0
                appid = "6b6165b5f3b150c75f572a0ec7ad1f00"
                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
                    data = res.json()
                    cities = ["{} ({})".format(d['name'], d['sys']['country'])
                              for d in data['list']]
                    city_id = data['list'][0]['id']
                except Exception as e:
                    pass

                try:
                    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
                    data = res.json()
                    dataweather = []
                    dataweather.append(data['weather'][0]['description'])
                    dataweather.append(int(data['main']['temp']))
                    dataweather.append(data['weather'][0]['icon'])
                except Exception as e:
                    pass
                foistr1 = fiostr.replace("•","")

                rowinf_student = requests.get("https://ruz.hse.ru/api/search?term=" + foistr1).json()
                id = str(rowinf_student[0]['id'])

                current_date = date.today()
                date_string1 = current_date.strftime("%Y.%m.%d")
                next_date = current_date + datetime.timedelta(days=1)
                date_string2 = next_date.strftime("%Y.%m.%d")

                print(date_string2)

                timetable = requests.get("https://ruz.hse.ru/api/schedule/student/" + id + "?start=" + date_string1 + "&finish=" + date_string1 + "&lng=1").json()

                print(timetable)

                print(len(timetable))

                firstlessons1 = []
                if (len(timetable)==0):
                    for i in range(3):
                        firstlessons1.append("00:00")
                        firstlessons1.append("00:00")
                        firstlessons1.append("Пары нет")
                    firstlessons1.append(dataweather[0])
                    firstlessons1.append(dataweather[1])
                    firstlessons1.append(dataweather[2])
                else:
                    for i in range(0, len(timetable)):
                        if i <= 2:
                            firstlessons1.append(timetable[i]["beginLesson"])
                            firstlessons1.append(timetable[i]["endLesson"])
                            firstlessons1.append(timetable[i]["discipline"])
                            p=i
                    while p!=2:
                        p=p+1
                        firstlessons1.append("00:00")
                        firstlessons1.append("00:00")
                        firstlessons1.append("Пары нет")


                    firstlessons1.append(dataweather[0])
                    firstlessons1.append(dataweather[1])
                    firstlessons1.append(dataweather[2])
                firstlessons = ((str(firstlessons1).replace("'", "")).replace("[", "")).replace("]", "")
                print(firstlessons)
                await websocket.send(str(firstlessons))
            else:

                r = requests.get("https://ruz.hse.ru/api/search?term=" + fio).json()
                data_of_names1 = []
                for i in range(len(r)):
                    data_of_names1.append("•" + r[i]['label'])
                data_of_names = ((str(data_of_names1).replace("'", "")).replace("[", "")).replace("]", "")
                await websocket.send(str(data_of_names))
async def main():
    async with websockets.serve(yourtimetable, "localhost", 8000, compression=None):
        await asyncio.Future()
if __name__ == '__main__':
    asyncio.run(main())
