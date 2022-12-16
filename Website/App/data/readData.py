import csv
import os

class ReadData():
    
    def Read():
        cwd = os.getcwd()
        rows = []
        with open(f'{cwd}/App/data/baterai.csv') as file:
            csvrender = csv.reader(file)
            for row in csvrender:
                rows.append(row)
        return rows
