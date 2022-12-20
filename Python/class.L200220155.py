# membuat class pada python
class segitiga(object):
    """proses pengoprasian matematika pada segitiga"""
    def __init__(self, alas, tinggi):
        """mengisi propet yang tidak memiliki nilai default """
        self.a = alas
        self.t = tinggi
    def luas(self):
        """mengembalikan luas segitiga """
        L = self.a * self.t / 2
        return L
    def sisi_miring(self):
        """mengembalikan sisi miring segitiga"""
        h = (self.a ** 2 + self.t ** 2) ** 0.5
        return h
    def keliling(self):
        """mengembalikan keliling segitiga"""
        k = self.a + self.t +self.sisi_miring()
        return k


bangun = segitiga(3,4)
print (bangun.luas())
print (bangun.sisi_miring())
print (bangun.keliling())