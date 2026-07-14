from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_listar_nome(iniciais):
        return ClienteDAO().listar_nome(iniciais)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO().excluir(id)
    


    @staticmethod
    def servico_inserir(desc, valor):
        obj = Servico(0, desc, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    
    @staticmethod
    def servico_listar_descricao(iniciais):
        return ServicoDAO().listar_descricao(iniciais)

    @staticmethod
    def servico_atualizar(id, desc, valor):
        obj = Servico(id, desc, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        return ServicoDAO().excluir(id)
    
    
    