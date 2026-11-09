class Araba:
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
    def bilgi_ver(self):
        print(f"Marka:{self.marka}\nModel:{self.model}\nYıl:{self.yil}")
araba1=Araba("Toyota","Corolla","2018")
araba2=Araba("BMW","3 Series","2021")