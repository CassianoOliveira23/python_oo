#Sempre nomear as classes assim: ContaCorrente
#Sempre nomear os métodos assim: consultar_saldo

from datetime import datetime
import pytz


class ContaCorrente:
    '''
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes
    
    Atributos:
        nome(string): Nome do Cliente
        cpf (string): CPF do Cliente
        agencia (integer): Agência responsável epla conta do cliente
        num_conta (integer): Numero da conta corrente do cliente
        saldo (Float): Saldo disponível na conta do cliente
        limite (Float): Limite de cheque especial do cliente
        transacoes: Histórico de transações
    '''
    
    @staticmethod
    def _data_hora():
        fuso_brasil = pytz.timezone('Brazil/East')
        horario_brasil = datetime.now(fuso_brasil)
        return horario_brasil.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.transacoes = []
         
         
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))
         
         
    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor,
                                'Salddo R$ {}'.format(self.saldo), 
                                self._data_hora()))
        
        
    def _limite_conta(self): #O underline define como um método privado
        self.limite = -1000
        return self.limite
    
    
    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar este valor")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor,
                                    'Salddo R$ {}'.format(self.saldo), 
                                    self._data_hora()))
            
            
    def consultar_limite_cheque_especial(self):
        print("Seu limite de Cheque Especial é de {:,.2f}".format(self._limite_conta()))
        
        
    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)
        

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, 'Salddo R$ {}'.format(self.saldo), self._data_hora()))
        
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, 'Salddo R$ {}'.format(conta_destino.saldo), self._data_hora()))
        
        



#Criando a conta:
conta_cassiano = ContaCorrente('Cassiano', '032.610.100.45', 2304, 199423)
conta_cassiano.consultar_saldo()

#Depositando dinheiro na conta:
conta_cassiano.depositar(10000)
conta_cassiano.consultar_saldo()


print('Saldo Final')
conta_cassiano.consultar_saldo()
conta_cassiano.consultar_limite_cheque_especial()


print('-'*50)
conta_cassiano.consultar_historico_transacoes()
   
   
   
print('-'*50) 

#criando uma nova conta:
conta_namorada = ContaCorrente('Ketlin Wolski Goetz', '033.666.777-330', 3233, 766776)  

conta_cassiano.transferir(666.33, conta_namorada)
conta_cassiano.consultar_saldo()
conta_namorada.consultar_saldo()
        