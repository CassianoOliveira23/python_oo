from ContaBanco import  ContaCorrente, CartaoCredito

#Criando a conta:
conta_cassiano = ContaCorrente('Cassiano', '032.610.100.45', 2304, 199423)

cartao_cassiano = CartaoCredito('Cassiano Oliveira de Borba', conta_cassiano)


# SETTER e GETTER
conta_cassiano.nome = "Cassiano Kovalenko" 
print(conta_cassiano.nome)


#getter e setter da senha:
cartao_cassiano.senha = '231994'
print(cartao_cassiano.senha)


print(conta_cassiano.__dict__)

