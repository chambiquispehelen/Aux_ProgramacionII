class anime:

    def __init__(self, nombre, genero, nro_episodios):
        self.nombre = nombre
        self.genero = genero
        self.__nro_episodios = nro_episodios
        self.__episodios = []

    def __str__(self):
        return (f"nombre: {self.nombre} "
                f"genero: {self.genero} "
                f"nroEpisodios: {self.__nro_episodios} "
                f"episodios: {self.__episodios}")

    # GETTERS
    def get_nombre(self):
        return self.nombre

    def get_genero(self):
        return self.genero

    def get_nro_episodios(self):
        return self.__nro_episodios

    def get_episodios(self):
        return self.__episodios

    # SETTERS
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_genero(self, genero):
        self.genero = genero

    def set_nro_episodios(self, nro):
        self.__nro_episodios = nro

    def set_episodios(self, lista):
        self.__episodios = lista
