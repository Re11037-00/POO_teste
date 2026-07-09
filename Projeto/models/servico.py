class Servico:
    def __init__(self, id, desc, valor):
        self.set_id(id)
        self.set_desc(desc)
        self.set_valor(valor)
    def __str__(self):
        return f"{self.__id} - {self.__desc} - {self.__valor}"
    
    def set_id(self, id):
        if id<0: raise ValueError("Id deve ser positivo")
        self.__id= id
    def set_desc(self, desc):
        if desc == "": raise ValueError("Descrição deve ser informada")
        self.__desc = desc
    def set_valor(self, valor):
        if valor<0: raise ValueError("Valor deve ser positivo")
        self.__valor= valor
    

    def get_id(self) : return self.__id
    def get_desc(self) : return self.__desc
    def get_valor(self) : return self.__valor
    

    def to_json(self):
        return { "id":self.__id, "descrição":self.__desc, "valor":self.__valor}

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descrição"], dic["valor"])