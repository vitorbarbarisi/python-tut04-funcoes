def cumprimentar(nome):
    # Retorna um cumprimento maneiro para o nome passado como argumento em formato de string
    return

def negar(nome):
    # Retorna uma negação educada para o nome passado como argumento em formato de string
    return

def chamar(nome):
    # Retorna um chamado para o nome passado como argumento em formato de string
    return

def pode_entrar(nome, lista_convidados):
    # Retorna True se o nome está presente na lista de convidados, caso contrário, retorna False.
    return

def receber_convidados(lista_convidados, lista_vieram):
    # Para cada convidado na lista de convidados:
        # Se o convidado pode entrar, cumprimente-o.
        # Caso contrário, negue a entrada.
    return

def chamar_faltantes(lista_convidados, lista_vieram):
    # Para cada convidado na lista de convidados:
        # Se o convidado não veio, chame-o.
    return

def main():
    lista_convidados = ["Maria", "Ana", "João", "Pedro", "José"]
    lista_vieram = ["João", "Ana", "Maria", "Caio O Penetra"]	
    receber_convidados(lista_convidados, lista_vieram)
    chamar_faltantes(lista_convidados, lista_vieram)

if __name__ == '__main__':
    main()
