from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    @staticmethod
    def _contiene_mayuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():  # isupper: Si al menos un carácter ASCII en mayúsculas, y no hay ningún
                # carácter ASCII en minúsculas, en cualquier otro caso retorna False
                return True
        return False

    @staticmethod
    def _contiene_minuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():  # Retorna True si hay al menos un carácter ASCII en minúsculas, y no hay ningún
                # carácter ASCII en mayúsculas, en cualquier otro caso retorna False.
                return True
        return False

    @staticmethod
    def _contiene_numero(clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():  # Retorna True si todos los bytes de la secuencia son caracteres decimales ASCII
                # y la secuencia no está vacía, en cualquier otro caso retorna False.
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        if self.regla.es_valida(clave):
            return True
        else:
            return False


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(8)

    @staticmethod
    def contiene_caracter_especial(clave: str) -> bool:
        for caracter in clave:
            if caracter in ["@", "_", "#", "$", "%"]:
                return True
            else:
                pass
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError

        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError

        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError

        if not self._contiene_numero(clave):
            raise NoTieneNumeroError

        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError

        return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    @staticmethod
    def contiene_calisto(clave: str) -> bool:
        pass

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError
        return True
