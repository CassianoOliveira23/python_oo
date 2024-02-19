#Criando métodos dentro da classe:

# Já criamos o método __init__

class televisao:
    def __init__(self):
        self.cor = "preta"
        self.ligado = False
        self.tamanho = 42
        self.canal = "Errei de TV"
        self.volume = 20
        
    #Criando o método mudar_canal, que vai editar o self.canal:
    def mudar_canal(self):
        self.canal = "Rede Recorte"
        

#Programa
televisao_sala = televisao()
televisao_quarto = televisao()

televisao_sala.mudar_canal()

print(televisao_sala.canal)
print(televisao_quarto.canal)