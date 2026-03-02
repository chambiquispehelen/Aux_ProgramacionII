class Televisor:

    def __init__(self, marca=None, resolucion=None, tipo=None):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return (f"marca: {self.__marca} "
                f"resolucion: {self.__resolucion} "
                f"tipo: {self.__tipo}")

    # GETTERS
    def get_marca(self):
        return self.__marca

    def get_resolucion(self):
        return self.__resolucion

    def get_tipo(self):
        return self.__tipo

    # SETTERS
    def set_marca(self, marca):
        self.__marca = marca

    def set_resolucion(self, resolucion):
        self.__resolucion = resolucion

    def set_tipo(self, tipo):
        self.__tipo = tipo