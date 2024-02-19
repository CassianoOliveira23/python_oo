
# Passando parâmetros para o __init__ da classe:

class televisao:
    # quando criar um tv o usuario vai dizer qual o tamanho:
    def __init__(self, tamanho): 
        self.cor = "preta"
        self.ligado = False
        # Atributo da tv vai receber o tamanho definido pelo usuário:
        self.tamanho = tamanho 
        self.canal = "Errei de TV"
        self.volume = 20
        
   
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        



# TV Sala:
televisao_sala = televisao(tamanho=42)
televisao_sala.mudar_canal("Rede Goebbles")
print(televisao_sala.tamanho)
print(televisao_sala.canal)

print('-'*20)

# TV Quarto:
televisao_quarto = televisao(tamanho=70)
televisao_quarto.mudar_canal("Rede Recorte")
print(televisao_quarto.tamanho)
print(televisao_quarto.canal)





