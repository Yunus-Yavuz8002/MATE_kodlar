class BankaHesabi:
    def __init__(self,hesap_sahibi:str,bakiye=0):
        self.hesap_sahibi=hesap_sahibi
        self.bakiye=bakiye
    def para_yatir(self,miktar):
        self.bakiye+=miktar
        print(f"Güncel Bakiye:{self.bakiye}")
    def para_cek(self,miktar):
        if(miktar>self.bakiye):
            print("Yetersiz bakiye!")
        else:
            self.bakiye-=miktar
ziraat=BankaHesabi("Yunus")
ziraat.para_yatir(400)
ziraat.para_cek(200)
        