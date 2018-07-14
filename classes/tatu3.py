class Cliente:
	def __init__(self, nome, telefone):
		self.nome = nome
		self.telefone = telefone

class Conta:
	def __init__(self, clientes, numero, saldo = 0):
		self.clientes = clientes
		self.numero = numero
		self.saldo = 0
		self.operacoes = []
		self.deposito(saldo)

	def resumo(self):
		print ('CC Nmero: %s | Saldo: %10.2f' %
			(self.numero, self.saldo))

	def saque(self, valor):
		if self.saldo >= valor:
			self.saldo -= valor
			self.operacoes.append(['saque', valor])

	def deposito(self, valor):
		self.saldo += valor
		self.operacoes.append(['deposito', valor])

	def extrato(self):
		print ('CC Numero: %s' %(self.numero))
		for op in self.operacoes:
			print ('%10s | %.2f' %(op[0], op[1]))
		print ('Saldo: %.2f' %(self.saldo))

class ContaEspecial(Conta):
	def __init__(self, clientes, numero, saldo = 0, limite = 0):
		Conta.__init__(self, clientes, numero, saldo)
		self.limite = limite
	def saque(self, valor):
			if self.saldo + self.limite >= valor:
				self.saldo -= valor
				self.operacoes.append(['saque', valor])