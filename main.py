from listaEncadeadaCircular import *
from membro import *

def main():
    l = ListaEncadeadaCircular()
    a = Membro("Abel", "aaa")
    b = Membro("Bia", "bbb")
    c = Membro("Carlos", "ccc")
    d = Membro("Davi", "ddd")
    l.adicionar_membro(a)
    l.mostrarLista()
    print(l.proximo_responsavel())
    l.adicionar_membro(b)
    l.mostrarLista()
    print(l.proximo_responsavel())
    print(l.proximo_responsavel())
    l.adicionar_membro(c)
    l.mostrarLista()
    print(l.proximo_responsavel())
    print(l.proximo_responsavel())
    l.adicionar_membro(d)
    l.mostrarLista()
    l.remover_membro("Bruno")
    print(l.proximo_responsavel())
    print(l.proximo_responsavel())
    l.mostrarLista()
if __name__ == "__main__":
    main()
