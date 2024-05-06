class Agencia:
    def __init__(self, fone, cnpj, numero):
        self.fone = fone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado\nCaixa atual {self.caixa}")
        else:
            print(f"Valor de caixa está comforme solicitado.\nCaixa atual {self.caixa}")
            
        
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("emprestimo negado. Saldo não disponível em caixa")
            
    
    def adicionar_cliente(self, nome, cpf, patimonio):
        self.clientes.append((nome, cpf, patimonio))
        
        
        
        
# Para a classe AgenciaVirtual existir precisa da classe agencia AgenciaVirtual(Agencia)
# Conceito de herança, a classe filho herda as informações da classe pai
class AgenciaVirtual(Agencia):
    pass



class Agenciacomun(Agencia):
    pass



class AgenciaPremium(Agencia):
    pass
            
            
        
            
agencia1 = Agencia(666666666, 12345678910, 2304)

agencia_virtual  = AgenciaVirtual(989340681, 236548795412, 3233)
agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()

agencia_premium = AgenciaPremium(9894477556, 3584681861651, 3333)
agencia_premium.caixa = 50000
agencia_premium.verificar_caixa()

