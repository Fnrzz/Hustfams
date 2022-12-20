class jajargenjang(object):
    def __init__(self, alas, tinggi):
       self.a = alas
       self.t = tinggi

    def luas(self): #ini adalah method
        """ Mengembalikan luas jajargenjang ini """
        L = self.a * self.t
        return L

bangun = jajargenjang(2, 20)
print (bangun.luas())