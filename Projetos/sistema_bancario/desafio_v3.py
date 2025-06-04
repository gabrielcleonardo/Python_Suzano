from datetime import date
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome: str, cpf: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Saque inválido.")
            return False
        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("❌ Depósito inválido.")
            return False
        self.saldo += valor
        return True

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):
        if self._saques_realizados >= self.limite_saques:
            print("❌ Limite de saques diários excedido.")
            return False
        if valor > self.limite:
            print("❌ Valor excede o limite de saque por operação.")
            return False
        if super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False


def main():
    clientes = []
    contas = []

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, clientes)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            conta = recuperar_conta_cliente(cliente)

            if conta:
                transacao.registrar(conta)

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, clientes)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            conta = recuperar_conta_cliente(cliente)

            if conta:
                transacao.registrar(conta)

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, clientes)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            conta = recuperar_conta_cliente(cliente)
            if conta:
                print("\n====== EXTRATO ======")
                for transacao in conta.historico.transacoes:
                    print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")
                print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
                print("======================")

        elif opcao == "nu":
            cpf = input("Informe o CPF (somente números): ")

            if buscar_cliente(cpf, clientes):
                print("Já existe cliente com esse CPF.")
                continue

            nome = input("Informe o nome completo: ")
            nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

            cliente = PessoaFisica(nome=nome, cpf=cpf, endereco=endereco, data_nascimento=nascimento)
            clientes.append(cliente)
            print("✅ Cliente criado com sucesso!")

        elif opcao == "nc":
            cpf = input("Informe o CPF do cliente: ")
            cliente = buscar_cliente(cpf, clientes)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            numero_conta = len(contas) + 1
            conta = ContaCorrente(cliente, numero=numero_conta)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print("✅ Conta criada com sucesso!")

        elif opcao == "lc":
            for conta in contas:
                print(f"""
Agência: {conta.agencia}
C/C: {conta.numero}
Titular: {conta.cliente.nome}
""")

        elif opcao == "q":
            break

        else:
            print("Opção inválida, tente novamente.")

def buscar_cliente(cpf, clientes):
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return None
    return cliente.contas[0]
