from classes import Cliente, Conta


class CaixaEletronico():
  def __init__(self):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')

    cliente = Cliente(nome, cpf)
    self.conta = Conta(cliente)

    print(f'Olá, {self.conta.titular.nome}, sua conta é {self.conta.numero}')

  def exibir_menu(self):
    print(f'1- Consultar saldo\n2- Depositar\n3- Sacar')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
      valor = self.conta.consultar_saldo()
      print(f'Seu saldo é R$ {valor}.')
    elif escolha == '2':
      self.depositar()
    elif escolha == '3':
      self.sacar()
    else:
      print('Opção inválida.')


  def depositar(self):
    valor = float(input('Digite o valor: '))
    self.conta.depositar(valor)
    print('Depósito efetuado.')

  def sacar(self):
    valor = float(input('Digite o valor: ')) 
    if self.conta.sacar(valor):
      print('Saque efetuado.')
    else:
      print('Saldo insuficiente.')