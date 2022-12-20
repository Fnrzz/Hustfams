class Prisma(object):
    def __init__(self, panjang, lebar, tinggi):
       self.p = panjang
       self.t = tinggi
       self.l = lebar

    def luas(self): #ini adalah method
        """ Mengembalikan luas prisma segiempat ini """
        luas_alas = self.p * self.l
        keliling = 2 * (self.p + self.l)
        luas_total =(2*luas_alas)  + (keliling*self.t)
        return luas_total

bangun = Prisma(12, 6,10)
print (bangun.luas())