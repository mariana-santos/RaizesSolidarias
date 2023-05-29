import cx_Oracle

class Alimento:
    def __init__(self, id_alimento, nome_alimento, tempo_colheita, qtd_irrigacao, preco_alimento, qtd_alimento):
        self.__id_alimento = id_alimento
        self.__nome_alimento = nome_alimento
        self.__tempo_colheita = tempo_colheita
        self.__qtd_irrigacao = qtd_irrigacao
        self.__preco_alimento = preco_alimento
        self.__qtd_alimento = qtd_alimento
    
    def get_id_alimento(self):
        return self.__id_alimento
    
    def set_id_alimento(self, id_alimento):
        self.__id_alimento = id_alimento
    
    def get_nome_alimento(self):
        return self.__nome_alimento
    
    def set_nome_alimento(self, nome_alimento):
        self.__nome_alimento = nome_alimento
    
    def get_tempo_colheita(self):
        return self.__tempo_colheita
    
    def set_tempo_colheita(self, tempo_colheita):
        self.__tempo_colheita = tempo_colheita
    
    def get_qtd_irrigacao(self):
        return self.__qtd_irrigacao
    
    def set_qtd_irrigacao(self, qtd_irrigacao):
        self.__qtd_irrigacao = qtd_irrigacao
    
    def get_preco_alimento(self):
        return self.__preco_alimento
    
    def set_preco_alimento(self, preco_alimento):
        self.__preco_alimento = preco_alimento
    
    def get_qtd_alimento(self):
        return self.__qtd_alimento
    
    def set_qtd_alimento(self, qtd_alimento):
        self.__qtd_alimento = qtd_alimento
