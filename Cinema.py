class Cinema:
    def _init_(self, nome, endereco, salas):
        self.nome = nome
        self.endereco = endereco
        self.salas = salas

class Sala:
    def _init_(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

class Sessao:
    def _init_(self, filme, horario, sala, preco):
        self.filme = filme
        self.horario = horario
        self.sala = sala
        self.preco = preco
        self.ingressos_vendidos = 0

    def comprar_ingresso(self):
        if self.ingressos_vendidos < self.sala.capacidade:
            self.ingressos_vendidos += 1
            return Ingresso(self, self.preco)
        else:
            return None

class Ingresso:
    def _init_(self, sessao, preco):
        self.sessao = sessao
        self.preco = preco

class Cliente:
    def _init_(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
