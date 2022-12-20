# Rumus tabung
class tabung(object):
    """ data dan proses terhadap tabung dengan jari-jari r dan tinggi t """
    pi = 3.14
    def __init__(self, jejari, tinggi):
       self.j = jejari
       self.t = tinggi

# Rumus luas alas tabung
    def luas_alas(self): #ini adalah method
        L = self.pi * self.j
        return L

# Rumus Luas selimut tabung
    def luas_selimut(self):
        L = 2 * self.pi * self.j * self.t
        return L

# Rumus Luas permukaan tabung
    def luas_permukaan(self):
        L = 2 * self.luas_alas() + self.luas_selimut()
        return L

# Menampilkan fungsi bangun tabung
bangun = tabung(12, 15)
print (bangun.luas_alas())
print (bangun.luas_selimut())
print (bangun.luas_permukaan())


# Jika ingin menggunakan 2 file untuk menampilkan gunakan code program di bawah ini

# Memanggil rumus tabung dari file tabung.py
# Modul Tabung
#from tabung import tabung

# Menampilkan fungsi bangun tabung
# bangun = tabung(12, 15)
# print (bangun.luas_alas())
# print (bangun.luas_selimut())
# print (bangun.luas_permukaan())

