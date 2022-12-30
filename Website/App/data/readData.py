import csv
import os

class Baterai():
    rows = []
    item = []
    capacity = []
    time = []
    data = []
    def read():
        cwd = os.getcwd()
        with open(f'{cwd}/App/data/baterai.csv') as file:
            csvrender = csv.reader(file)
            for row in csvrender:
                Baterai.rows.append(row)
    
    def getItem():
        Baterai.read()
        for row in Baterai.rows:
            for item in row:
                Baterai.item.append(item)   

    def getCapacity():
        Baterai.getItem()
        count = 1
        for i in Baterai.item:
            if(count == 4):
                Baterai.capacity.append(i)
                count = 1
            else:
                count += 1

    def getTime():
        Baterai.getCapacity()
        for i in Baterai.capacity:
            count = int(i)/1000/0.85*60
            t = str(round(count))
            Baterai.time.append(t)

    def getData():
        Baterai.getTime()
        for row in Baterai.rows:
            for time in Baterai.time:
                t = int(time)
                for i in range(t):
                    row.append(Baterai.time[i])
                    del Baterai.time[i]
                    break
                break
            Baterai.data.append(row)
    
    def showData():
        if(Baterai.data):
            return Baterai.data
        else:
            Baterai.getData()
            return Baterai.data
