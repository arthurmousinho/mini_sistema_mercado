def clear():
  import os 
  os.system('cls') or None


def menu():
    print('''
            -----------------------------
                PROJETO SUPERMERCADO
            -----------------------------
              [1]   EFETUAR VENDA
              [2]   CADASTRAR PRODUTOS
              [3]   SAIR DO PROGRAMA
            -----------------------------
        ''')


def verificar_codigo(codigo,lista_codigos,lista_produtos,lista_valores):
  if codigo in lista_codigos:
    produto = lista_produtos[lista_codigos.index(codigo)]
    valor = lista_valores[lista_codigos.index(codigo)]
    print(f"Produto = {produto}            R$ {valor}")
    return True
  else:
    return False 


def verificar_estoque(codigo,stock,lista_codigo,quantidade_informada):
  quantidade_disponivel = stock[lista_codigo.index(codigo)]
  if quantidade_informada > quantidade_disponivel:
    print("Estoque insuficiente")
    return False
  else:
    print("Quantidade Disponível")
    return True


def codigo_existente(lista_codigos,codigo):
  if codigo in lista_codigos:
    return False
  else:
    return True 
