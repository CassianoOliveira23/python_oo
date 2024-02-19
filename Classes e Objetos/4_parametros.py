# Adicionando o parâmetro mudar canal

class televisao:
    def __init__(self):
        self.cor = "preta"
        self.ligado = False
        self.tamanho = 42
        self.canal = "Errei de TV"
        self.volume = 20
        
    #Parâmetro novo canal:
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        

#Programa
televisao_sala = televisao()
televisao_quarto = televisao()

televisao_sala.mudar_canal("Rede Goebbles")
televisao_quarto.mudar_canal("Rede Recorte")

print(televisao_sala.canal)
print(televisao_quarto.canal)