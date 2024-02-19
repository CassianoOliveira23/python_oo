# Criando a nossa primeira classe em Python:

    # class Nome_Classe(object)
    
# Dentor da classe, vocÊ vai criar a "Função"(método) __init__  (vai iniciar o metodo, instanciar)

# Esse método é quem define o que aocntece quando cria uma instancia da Classe


# A função init cria a televisão:
class televisao:
    def __init__(self):
        self.cor = "preta"
        self.ligado = False
        self.tamanho = 42
        self.canal = "Errei de TV"
        self.volume = 20



# Criando um instâncias da televisão, que começa com as mesmas características definidas acima:
televisao_sala = televisao()
televisao_quarto = televisao()

#redefinindo a cor da tv da sala:
televisao_sala.cor = "Cinza"
print(televisao_sala.cor)
print(televisao_quarto.cor)

#definindo o tamanho da tv do quarto
televisao_quarto.tamanho = 32
print(televisao_sala.tamanho)
print(televisao_quarto.tamanho)