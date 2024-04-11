class pessoa:

    def __init__(self):
        self._nome = ""
        self._idade = 0
        self._altura = 0.0

    def set_nome(self,nome):
        self._nome = nome
    def set_idade(self,idade):
        self._idade = idade
    def set_altura(self,altura):
        self._altura = altura
    
    def imprimir(self):
        print(f'O nome dele é {self._nome} ele tem {self._idade} anos de idadee e tem {self._altura} de altura')

pessoa1 = pessoa()
pessoa1.set_nome('Guilherme')
pessoa1.set_idade(21)
pessoa1.set_altura(1.80)
pessoa1.imprimir()