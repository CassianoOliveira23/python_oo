# O que é o SELF:

# O primeiro pâmetro de uma fução tem que ser o self, mas não é obrigatório que ele se chame self, mas é uma boa pratica

class televisao:
    def __init__(self):
        self.cor = "preta"  #O parâmetro cor da classe
        self.ligado = False #O parâmetro ligado da classe
        self.tamanho = 42 #O parâmetro tamanho da classe
        self.canal = "Errei de TV" #O parâmetro canal da classe
        self.volume = 20 #O parâmetro volume da classe
        self.definicao = '4k'


# Sempre que você quizer acessar um parâmetro da claase tem que colocar o self na frente

# so se escreve o SELF dentro da classe