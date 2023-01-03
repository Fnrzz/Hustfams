import csv
import os
from .Baterai import *

listObject = []
cwd = os.getcwd()
with open(f'{cwd}/App/data/baterai.csv') as file:
    csvrender = csv.reader(file)
    for item in csvrender:
        listObject.append(Baterai(item[0],item[1],item[2],item[3]))
            
def getData():
    listData = []
    for item in listObject:
        listData.append(item.getItem())
    return listData
