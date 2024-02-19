# Atributos de Classe: faz parte da classe mas obrigatóriamente tem que ter o mesmo valor pra todas as televisões que criar.

# Exemplo: A cor, atualmente todas as TVs são pretas
# Então o parâmetro cor é definido na classe e não no método:

class televisao:
    cor = "Preta"
    
    def __init__(self, tamanho): 
        self.ligado = False
        self.tamanho = tamanho 
        self.canal = "Errei de TV"
        self.volume = 20
        
   
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


# Instanciando a TV Sala:
televisao_sala = televisao(tamanho=42)
televisao_sala.mudar_canal("Rede Goebbles")
print(televisao_sala.tamanho)
print(televisao_sala.canal)
print(televisao_sala.cor)


print('-'*50)


# Instanciando a TV Quarto:
televisao_quarto = televisao(tamanho=70)
televisao_quarto.mudar_canal("Rede Recorte")
print(televisao_quarto.tamanho)
print(televisao_quarto.canal)
print(televisao_quarto.cor)



