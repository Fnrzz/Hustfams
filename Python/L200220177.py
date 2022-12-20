print("jajargenjang")

class jajargenjang:
    
    #default value for a is 5 & t is 10
    a = 5
    t = 10
    
    def hitung(self):
        calculate = self.a * self.t
        return calculate
    

p = jajargenjang()
print("alas: ", p.a)
print("luas: ", p.hitung())