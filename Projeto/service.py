from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO

class Service:
    #CLIENTE
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
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
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO().excluir(id)
    
    #SERVIÇO

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
    
    #PROFISSIONAL

    @staticmethod
    def profissional_inserir(nome, email, senha, especialidade):
        novo = Profissional(0, nome, email, senha, especialidade)
        ProfissionalDAO().inserir(novo)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_listar_nome(iniciais):
        return ProfissionalDAO().listar_nome(iniciais)

    @staticmethod
    def profissional_atualizar(nome, email, senha, especialidade):
        atualizado = Profissional(0, nome, email, senha, especialidade)
        ProfissionalDAO().atualizar(atualizado)

    @staticmethod
    def profissional_excluir(id):
        return ProfissionalDAO().excluir(id)
    
    
    
    