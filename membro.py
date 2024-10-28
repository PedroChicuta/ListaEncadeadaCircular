class Membro:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.next = None
    
    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getNext(self):
        return self.next
    
    def setNome(self, nome):
        self.nome = nome
    
    def setEmail(self, email):
        self.email = email
    
    def setNext(self, next):
        self.next = next    
    
    def __str__(self):
        return f"{self.getNome()}"
    
