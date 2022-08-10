import functions as f
from time import sleep

products = ["Pacote de Arroz 5kg" , "Pacote de Feijão 1kg" , "Refrigerante 2L" , "Caixa de cholocate"]
codes = [9649 , 9847 , 2567 , 7830]
stock = [30 , 30 , 10 , 30]
prices = [20.00 , 10.00 , 9.00 , 10.00]


while True:
    f.menu()

    try:
        opcao = int(input("> "))
    except(ValueError,TypeError):
        f.clear()
        print("Tente novamente")
    else:
        if opcao > 3 or opcao < 1:
            f.clear
            print("Tente novamente")
        elif opcao == 1: #EFETUAR VENDA
            f.clear()
            total_compra = 0
            while True:
                try:
                    pesquisa = int(input(f'''
                    [1] INFORMAR CÓDIGO 
                    [2] FINALIZAR
                    
                    TOTAL: R$ {total_compra:.2f}
                    '''))
                except(ValueError,TypeError):
                    f.clear()
                    print("Tente Novamente")
                else:
                    if pesquisa > 2 or pesquisa < 1:
                        f.clear()
                        print("Tente novamente")
                        continue
                    elif pesquisa == 1: #informar código
                        f.clear()
                        try:
                            codigo = int(input("Código do produto: "))
                        except(ValueError,TypeError):
                            f.clear()
                            print("Tent novamente") 
                        else:
                            f.clear()
                            if not f.verificar_codigo(codigo,codes,products,prices):
                                f.clear()
                                print("Código não encontrado")
                            else:
                                f.clear()
                                print("Produto Encontrado")
                                print('----------------------------')
                                f.verificar_codigo(codigo,codes,products,prices)
                                try:
                                    print('----------------------------')
                                    quantidade = int(input("Quantidade: "))
                                except(ValueError,TypeError):
                                    f.clear()
                                    print("Tente novamente")
                                else:
                                    f.clear()
                                    if not f.verificar_estoque(codigo,stock,codes,quantidade):
                                        print()
                                    else:
                                        atualizar = stock[codes.index(codigo)] - quantidade
                                        print("finalizando.....aguarde")
                                        sleep(4)
                                        f.clear()
                                        valor = prices[codes.index(codigo)]
                                        total_compra = total_compra + (valor * quantidade)

                                    file = open('relataorio_de_vendas.txt' , 'a')
                                    produto = products[codes.index(codigo)]
                                    file.write(f"{quantidade} -- {produto} -- {total_compra :.2f}\n")
                                    file.close()

                                    continue                   
                                        
                    elif pesquisa == 2: #finalizar
                        f.clear()
                        print(f"Total da compra R${total_compra:.2f}")
                        try:
                            pagamento = float(input("Valor fornecido: R$ "))
                        except(ValueError,TypeError):
                            print("Tente Novamente")
                        else:
                            f.clear()
                            while pagamento < total_compra:
                                f.clear()
                                print("Valor fornecido menor que o valor da compra")
                                print()
                                print(f"Total da compra R${total_compra:.2f}")
                                pagamento = float(input("Valor fornecido: R$ "))
                            f.clear()
                            troco = pagamento - total_compra
                            if troco > 0:
                                print(f"Vai precisar de troco:   R$ {troco :.2f}")
                                print("Aguarde...")
                                sleep(5)
                            else:
                                print("Não vai precisar de troco")
                                print("Aguarde...")
                                sleep(5)
                            file.close()
                            break
                            
                                                 
        elif opcao == 2: #CADASTRAR PRODUTOS
            f.clear()
            while True:
                try:
                    novo_produto = str(input("Nome do produto: "))
                except(ValueError,TypeError):
                    print("Tente Novamente")
                else:
                    f.clear()
                    


                    try:
                        novo_codigo = int(input("Código: "))
                    except(ValueError,TypeError):
                        print("Tente Novamente")
                    else:
                        f.clear()
                        if not f.codigo_existente(codes,novo_codigo):
                            print("Outro produto já possui esse código")
                            continue
                        else:
                            
                            try:
                                f.clear()
                                novo_valor = float(input("Valor do produto: "))
                            except(ValueError,TypeError):
                                print("Tente Novamente")
                            else:
                            
                                try:
                                    f.clear()
                                    nova_quantidade = int(input("Quantidade: "))
                                except(ValueError,TypeError):
                                    print("Tente Novamente")
                                else:
                                    f.clear()
                                    print(f'''
                                        PRODUTO {novo_produto} CADASTRADO COM SUCESSO

                                        [1] CADASTRAR OUTRO PRODUTO
                                        [2] FINALIZAR CADASTRO
                                    ''')


                                    try:
                                        opcao_cadastro = int(input("> "))
                                    except(ValueError,TypeError):
                                        print("Tente Novamente")
                                    else:
                                        while opcao_cadastro != 1 and opcao_cadastro != 2:
                                                f.clear()
                                                print("Tente novamente")
                                                opcao_cadastro = int(input("> "))
                                        if opcao_cadastro == 1:
                                            f.clear()
                                            products.append(novo_produto)
                                            codes.append(novo_codigo)
                                            prices.append(novo_valor)
                                            stock.append(nova_quantidade)
                                            continue
                                        elif opcao_cadastro == 2:
                                            f.clear()
                                            products.append(novo_produto)
                                            codes.append(novo_codigo)
                                            prices.append(novo_valor)
                                            stock.append(nova_quantidade)
                                            break

    
        elif opcao == 3:
            f.clear()
            print("Sistema finalizado...Relatório de venda já está disponível")
            break
