print("jajargenjang")

class jajargenjang:
    
    #user input value
    a = int(input("masukkan jumlah value alas: "))
    t = int(input("masukkan jumlah value tinggi: "))
    
    def hitung(self):
        calculate = self.a * self.t
        return calculate
    
#make object
p = jajargenjang()
print("alas: ", p.a)
print("luas: ", p.hitung())