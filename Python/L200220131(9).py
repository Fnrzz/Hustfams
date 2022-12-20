class Limas():
    def __init__(self,alas,tinggi,sTegak):
        self.a = alas
        self.t = tinggi
        self.sT = sTegak
        self.luasAlas = 0.5 * self.a * self.t

    def luasPermukaan(self):
        return self.luasAlas + self.sT