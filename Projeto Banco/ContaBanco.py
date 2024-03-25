#Sempre nomear as classes assim: ContaCorrente
#Sempre nomear os métodos assim: consultar_saldo

from random import randint
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
        self.cartoes = []
         
         
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
        
        
        
        
        
class CartaoCredito:
    @staticmethod
    def _data_hora():
        fuso_brasil = pytz.timezone('Brazil/East')
        horario_brasil = datetime.now(fuso_brasil)
        return horario_brasil.strftime('%d/%m/%Y %H:%M:%S')
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.nome_titular = titular
        self.validade = CartaoCredito._data_hora()
        self.codigo_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)




#Criando a conta:
conta_cassiano = ContaCorrente('Cassiano', '032.610.100.45', 2304, 199423)

cartao_cassiano = CartaoCredito('Cassiano Oliveira de Borba', conta_cassiano)

print(cartao_cassiano.conta_corrente._numero_conta)

print(cartao_cassiano.numero)

print(cartao_cassiano.codigo_seguranca)

print(cartao_cassiano.validade)

