import pymysql


class Conector:
    def __init__(self, server='localhost', usuario='root', password='', basedato='crud'):
        self.__server = server
        self.__usuario = usuario
        self.__pasword = password
        self.__basedato = basedato
        self.__conn = ""
        self.__conector = ""

    def conectar(self):
        self.__conn = pymysql.connect(host=self.__server, user=self.__usuario, password=self.__pasword,
                                      db=self.__basedato)
        self.__conector = self.__conn.cursor()

    def cerrar(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn
