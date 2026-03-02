class Instrumento:

    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo

    def __str__(self):
        return f"nombre: {self.nombre} material: {self.__material} tipo: {self.__tipo}"

    # GETTERS
    def get_nombre(self):
        return self.nombre

    def get_material(self):
        return self.__material

    def get_tipo(self):
        return self.__tipo

    # SETTERS
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_material(self, material):
        self.__material = material

    def set_tipo(self, tipo):
        self.__tipo = tipo