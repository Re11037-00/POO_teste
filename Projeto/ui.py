from service import Service

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            

    @staticmethod
    def menu():
        print("1-Inserir clientes, 2-Listar clientes, 3-Atualizar clientes, 4-Excluir clientes")
        print("5-Inserir serviços, 6-Listar serviços, 7-Atualizar serviços, 8-Excluir serviços, 9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o E-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, fone)
    
    @staticmethod
    def cliente_listar():
        for obj in Service().cliente_listar(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo E-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o ID do cliente a ser excluído: "))
        Service.cliente_excluir(id)


    @staticmethod
    def servico_inserir():
        id = int(input("Informe o ID: "))
        desc = input("Informe a descrição do serviço: ")
        valor = int(input("Informe o valor do serviço"))
        Service.servico_inserir(id, desc, valor)
    
    @staticmethod
    def servico_listar():
        for obj in Service().servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o ID do serviço a ser atualizado: "))
        desc = input("Informe a nova descrição do serviço: ")
        valor = int(input("Informe o novo valor do serviço"))
        Service.servico_atualizar(id, desc, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o ID do serviço a ser excluído: "))
        Service.servico_excluir(id)
UI.main()


    
