class Baterai(object):
    def __init__(self,id,brand,type,capacity):
        self.id = id
        self.brand = brand
        self.type = type
        self.capacity = capacity

    def getItem(self):
        listItem = [self.id,self.brand,self.type,self.capacity,self.getTime()]
        return listItem

    def getTime(self):
        time = str(round(int(self.capacity) /1000/0.85*60))
        return time