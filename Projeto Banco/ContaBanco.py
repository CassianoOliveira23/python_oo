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
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._gencia = agencia
        self._numero_conta = numero_conta
        self._transacoes = []
         
         
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))
         
         
    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor,
                                'Salddo R$ {}'.format(self._saldo), 
                                self._data_hora()))
        
        
    def _limite_conta(self): #O underline define como um método privado
        self._limite = -1000
        return self._limite
    
    
    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para sacar este valor")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor,
                                    'Salddo R$ {}'.format(self._saldo), 
                                    self._data_hora()))
            
            
    def consultar_limite_cheque_especial(self):
        print("Seu limite de Cheque Especial é de {:,.2f}".format(self._limite_conta()))
        
        
    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)
        

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, 'Salddo R$ {}'.format(self._saldo), self._data_hora()))
        
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, 'Salddo R$ {}'.format(conta_destino._saldo), self._data_hora()))
        
        


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
conta_namorada = ContaCorrente('Ketlyn Wolski Goetz', '033.666.777-330', 3233, 766776)  

conta_cassiano.transferir(666.33, conta_namorada)
conta_cassiano.consultar_saldo()
conta_namorada.consultar_saldo()
        