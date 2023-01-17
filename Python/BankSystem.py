import sys
class bankAccount:
    def __init__(self, saldo, tipe_akun):
        self.saldo = saldo
        self.tipe_akun = tipe_akun
        
    def depo(self, amount = 0):
        pilih = int(input("masukkan nominal depo: "))
        pilih + amount
        self.saldo += pilih
        return self.saldo
        
    def wd(self, amount = 0):
        pilih = int(input("masukkan nominal wd: "))
        pilih + amount
        if pilih > self.saldo:
            print('saldo kurang')
            sys.exit()
        else:
            self.saldo -= pilih
            return self.saldo
        
    def cekSaldo(self):
        return self.saldo
    
#object 
my = bankAccount(0, 'reguler')

while True:
    print(f'Tipe Akun: {my.tipe_akun}')
    choice = input("masukkan pilihan: ")
    if choice == '1':
        print(f'saldo anda adalah ${my.cekSaldo()}')
    elif choice == '2':
        my.depo()
    elif choice == '3':
        my.wd()
    else:
        print("perintah yang anda masukkan invalid!")
        break
    