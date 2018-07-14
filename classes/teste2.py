from tatu2 import Cliente
from tatu2 import Conta

joao = Cliente('Joao da silva', '777-1234')
print ('Nome: %s | Telefone: %s' %(joao.nome, joao.telefone))
conta1 = Conta([joao], 1, 1000)
conta1.saque(400)
conta1.deposito(50)
conta1.resumo()
conta1.extrato()