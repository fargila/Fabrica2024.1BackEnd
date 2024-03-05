for i in range(10, 200, 3):
    print(i)

def retorno():
    alto = "Quelque chose cloche"
    return alto
def ñretorno():
    print("Quelque chose ne cloche pas...")

print(retorno())
print(ñretorno())

nome = "klu klux klan"
novo_nome = nome.capitalize()
print(novo_nome)

# while(True):
#     print("Bom dia, irei consumir a sua memória agora...")

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        print("Meu nome é",self.nome, "e tenho",self.idade)

individuo = pessoa("Mario", 19)
individuo.apresentacao()