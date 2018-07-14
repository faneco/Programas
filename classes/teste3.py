from tatu3 import Cliente
from tatu3 import Conta, ContaEspecial

joao = Cliente('Joao da silva', '777-1234')
print ('Nome: %s | Telefone: %s' %(joao.nome, joao.telefone))
conta1 = ContaEspecial([joao], 1, 1000, 1000)
conta1.deposito(100)
conta1.saque(1500)
conta1.resumo()
conta1.extrato()