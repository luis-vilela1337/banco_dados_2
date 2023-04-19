class Televisao:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.__volume = 0
        self.__canal = 0
    
    def aumentar_volume(self, quantidade):
        self.__volume += quantidade
    
    def diminuir_volume(self, quantidade):
        self.__volume -= quantidade
    
    def trocar_canal(self, canal):
        self.__canal = canal
    
    def imprimir_info(self):
        print("Modelo:", self.__modelo)
        print("Volume:", self.__volume)
        print("Canal:", self.__canal)


class SmartTV(Televisao):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.internet = False
    
    def conectar_internet(self):
        self.internet = True



televisao = Televisao("TV01")
televisao.aumentar_volume(70)
televisao.diminuir_volume(27)
televisao.trocar_canal("Canal #1")
televisao.imprimir_info()


smart_tv = SmartTV("SmartTV01")
smart_tv.conectar_internet()
smart_tv.imprimir_info()
