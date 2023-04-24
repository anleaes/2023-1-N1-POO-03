#Jimmy
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
        
        
        
#Hiro
cinema = Cinema("Cineplex", "Rua A, 123", [Sala(1, 50), Sala(2, 80)])

sessoes = [Sessao("Vingadores: Ultimato", "18:00", cinema.salas[0], 20),
           Sessao("O Rei Leão", "20:00", cinema.salas[1], 25),
           Sessao("Toy Story 4", "22:00", cinema.salas[0], 18)]

clientes = []



#Dreyer
while True:
    print("Opções:")
    print("1 - Criar cliente")
    print("2 - Comprar ingresso")
    print("3 - Filmes em cartaz")
    print("4 - Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o email do cliente: ")
        cliente = Cliente(nome, idade, email)
        clientes.append(cliente)
        print(f"Cliente {cliente.nome} criado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do cliente: ")
        cliente = None
        for c in clientes:
            if c.nome == nome:
                cliente = c
                break
        if cliente is None:
            print("Cliente não encontrado!")
            continue

        filme = input("Digite o nome do filme: ")
        sessao = None
        for s in sessoes:
            if s.filme == filme:
                sessao = s
                break
        if sessao is None:
            print("Sessão não encontrada!")
            continue

        ingresso = sessao.comprar_ingresso()
        if ingresso is None:
            print("Sessão esgotada!")
            continue

        print(f"Ingresso para a sessão de {sessao.filme} às {sessao.horario} comprado por {cliente.nome} por R${ingresso.preco}.")

    elif opcao == "3":
        print("Filmes em cartaz:")
        for s in sessoes:
            print(f"- {s.filme} ({s.horario}) - R${s.preco}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")
        continue

#Bruno
while True:
    comando = input("Digite um comando (criar cliente, comprar ingresso, filmes em cartaz, sair): ")
    
    if comando == "criar cliente":
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o email do cliente: ")
        cliente = Cliente(nome, idade, email)
        clientes.append(cliente)
        print(f"Cliente {cliente.nome} criado com sucesso!")
    
    elif comando == "comprar ingresso":
        nome = input("Digite o nome do cliente: ")
        cliente = None
        for c in clientes:
            if c.nome == nome:
                cliente = c
                break
        if cliente is None:
            print("Cliente não encontrado!")
            continue
        
        filme = input("Digite o nome do filme: ")
        sessao = None
        for s in sessoes:
            if s.filme == filme:
                sessao = s
                break
        if sessao is None:
            print("Sessão não encontrada!")
            continue
        
        ingresso = sessao.comprar_ingresso()
        if ingresso is None:
            print("Sessão esgotada!")
            continue
        
        print(f"Ingresso para a sessão de {sessao.filme} às {sessao.horario} comprado por {cliente.nome} por R${ingresso.preco}.")
    
    elif comando == "filmes em cartaz":
        print("Filmes em cartaz:")
        for s in sessoes:
            print(f"- {s.filme} ({s.horario}) - R${s.preco}")
    
    elif comando == "sair":
        break
    
    else:
        print("Comando inválido!")
        continue


        
#Bruno
while True:
    comando = input("Digite um comando (criar cliente, comprar ingresso, filmes em cartaz, sair): ")
    
    if comando == "criar cliente":
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o email do cliente: ")
        cliente = Cliente(nome, idade, email)
        clientes.append(cliente)
        print(f"Cliente {cliente.nome} criado com sucesso!")
    
    elif comando == "comprar ingresso":
        nome = input("Digite o nome do cliente: ")
        cliente = None
        for c in clientes:
            if c.nome == nome:
                cliente = c
                break
        if cliente is None:
            print("Cliente não encontrado!")
            continue
        
        filme = input("Digite o nome do filme: ")
        sessao = None
        for s in sessoes:
            if s.filme == filme:
                sessao = s
                break
        if sessao is None:
            print("Sessão não encontrada!")
            continue
        
        ingresso = sessao.comprar_ingresso()
        if ingresso is None:
            print("Sessão esgotada!")
            continue
        
        print(f"Ingresso para a sessão de {sessao.filme} às {sessao.horario} comprado por {cliente.nome} por R${ingresso.preco}.")
    
    elif comando == "filmes em cartaz":
        print("Filmes em cartaz:")
        for s in sessoes:
            print(f"- {s.filme} ({s.horario}) - R${s.preco}")
    
    elif comando == "Sair":
        break
    
    else:
        print("Comando inválido!")
        continue
    
