from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 17: 
            op = UI.menu()
            # Clientes
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.cliente_pesquisar_nome()
            # Serviços
            if op == 6: UI.servico_inserir()
            if op == 7: UI.servico_listar()
            if op == 8: UI.servico_atualizar()
            if op == 9: UI.servico_excluir()
            if op == 10: UI.servico_pesquisar_descricao()
            # Profissionais
            if op == 11: UI.profissional_inserir() 
            if op == 12: UI.profissional_listar()
            if op == 13: UI.profissional_atualizar()
            if op == 14: UI.profissional_excluir()
            if op == 15: UI.profissional_pesquisar_id()
            if op == 16: UI.profissional_pesquisar_nome()
            

    @staticmethod
    def menu():
        print("-"*70)
        print(" [CLIENTES]     1-Inserir  2-Listar  3-Atualizar  4-Excluir  5-Pesquisar por Nome")
        print(" [SERVIÇOS]     6-Inserir  7-Listar  8-Atualizar  9-Excluir  10-Pesquisar por Descrição")
        print(" [PROFISSIONAL] 11-Inserir 12-Listar 13-Atualizar 14-Excluir 15-Buscar ID 16-Buscar Nome")
        print(" [SISTEMA]      17-Fim")
        print("-"*70)
        return int(input("Informe uma opção: "))


    #CLIENTES
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o E-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente cadastrado com sucesso!")
    
    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar(): 
            print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar(): 
            print(obj)
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo E-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar(): 
            print(obj)
        id = int(input("Informe o ID do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def cliente_pesquisar_nome():
        iniciais = input("Informe as iniciais do nome para pesquisar: ")
        encontrados = Service.cliente_listar_nome(iniciais)
        if len(encontrados) == 0:
            print("Nenhum cliente encontrado com essas iniciais.")
        else:
            print("\n--- Clientes Encontrados ---")
            for obj in encontrados:
                print(obj)

    

    #SERVIÇOS

    @staticmethod
    def servico_inserir():
        desc = input("Informe a descrição do serviço: ")
        valor = float(input("Informe o valor do serviço: "))
        Service.servico_inserir(desc, valor)
        print("Serviço cadastrado com sucesso!")
    
    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): 
            print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service.servico_listar(): 
            print(obj)
        id = int(input("Informe o ID do serviço a ser atualizado: "))
        desc = input("Informe a nova descrição do serviço: ")
        valor = float(input("Informe o novo valor do serviço: "))
        Service.servico_atualizar(id, desc, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service.servico_listar(): 
            print(obj)
        id = int(input("Informe o ID do serviço a ser excluído: "))
        Service.servico_excluir(id)

    @staticmethod
    def servico_pesquisar_descricao():
        iniciais = input("Informe as iniciais da descrição do serviço para pesquisar: ")
        encontrados = Service.servico_listar_descricao(iniciais)
        if len(encontrados) == 0:
            print("Nenhum serviço encontrado com essas iniciais de descrição.")
        else:
            print("\n--- Serviços Encontrados ---")
            for obj in encontrados:
                print(obj)


    #PROFISSIONAL

    @staticmethod
    def profissional_inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o E-mail: ")
        senha = input("Informe a senha: ")
        especialidade = input("Informe a especialidade: ")
        Service.profissional_inserir(nome, email, senha, especialidade)
        print("Profissional cadastrado com sucesso!")
    
    @staticmethod
    def profissional_listar():
        for obj in Service.profissional_listar(): 
            print(obj)

    @staticmethod
    def profissional_atualizar():
        for obj in Service.profissional_listar(): 
            print(obj)
        id = int(input("Informe o ID do profissional a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo E-mail: ")
        senha = input("Informe a nova senha: ")
        especialidade = input("Informe a nova especialidade: ")
        Service.profissional_atualizar(id, nome, email, senha, especialidade)

    @staticmethod
    def profissional_excluir():
        for obj in Service.profissional_listar(): 
            print(obj)
        id = int(input("Informe o ID do profissional a ser excluído: "))
        Service.profissional_excluir(id)

    @staticmethod
    def profissional_pesquisar_nome():
        iniciais = input("Informe as iniciais do nome para pesquisar: ")
        encontrados = Service.profissional_listar_nome(iniciais)
        if len(encontrados) == 0:
            print("Nenhum profissional encontrado com essas iniciais.")
        else:
            print("\n--- Profissionais Encontrados ---")
            for obj in encontrados:
                print(obj)
                
    @staticmethod
    def profissional_pesquisar_id():
        id = int(input("Informe o ID do profissional: "))
        prof = Service.profissional_listar_id(id)
        if prof is None:
            print("Nenhum profissional encontrado com esse ID.")
        else:
            print(prof)
    
UI.main()