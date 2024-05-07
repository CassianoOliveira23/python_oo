from random import randint

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
# isso é o Conceito de herança, a classe filho herda as informações da classe pai
class AgenciaVirtual(Agencia):
    #quando definimos um INIT dentro da classe filho ele substitui o da classe pai
    #adicionar o metodo super para conectar os dois inits e chamar o init principal para herdar as características(métodos e atributos)
    def __init__(self, site, fone, cnpj):
        self.site = site
        super().__init__(fone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0
    
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        
        

class AgenciaComun(Agencia):
    def __init__(self, fone, cnpj):
        super().__init__(fone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000



class AgenciaPremium(Agencia):
    def __init__(self, fone, cnpj):
        super().__init__(fone, cnpj, numero=randint(1001, 9999))
        self.caixa = 100000000
            
    def adicionar_cliente(self, nome, cpf, patrimonio):
       if patrimonio >  100000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
       else:
           print("Cliente não possui patrimonio mínimo para entar na Angencia Premium")
              




if __name__ == '__main__':
       
    agencia1 = Agencia(666666666, 12345678910, 2304)

    agencia_virtual  = AgenciaVirtual('www.agenciavirtual.com.br', 9898989898, 12345678954325)
    agencia_virtual.verificar_caixa()
    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    # Lógica do polomorfismo: O método adicionar_clientes funciona com objetos diferentes, e para cada método ele pode funcionar de forma diferente: nas outras agencias ele adciona qualquer cliente mas na agencia premium ele filtra e só adciona o cliente que cumppre os requisitos
    # É o mesmo método que é aplicado em classes diferentes
    agencia_comun = AgenciaComun(9898989898, 987456321021)
    agencia_comun.adicionar_cliente('Lira Doidao', 1525548485125, 20)
    print(agencia_comun.clientes)

    agencia_premium = AgenciaPremium(23659874, 659845125151)
    agencia_premium.adicionar_cliente('Lira', 2356549459659, 9999999999999999  )
    print(agencia_premium.clientes)



