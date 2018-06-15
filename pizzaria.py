sabor = []
bebida = []
preco = 0.0

validacao = True

while validacao:
    while True:
        print("Bem vindo à Off White Pizzaria, a melhor pizza da região acreana")
        nome = input("Para começar o seu pedido, informe o seu nome com apenas letras): ").capitalize()
        aux = nome.replace(" ", "")
        if aux.isalpha():
            break

    while True:
        telefone = input("Informe o seu telefone: ")
        if len(telefone) < 8:    
            print("Telefone tem que ter 9 dígitos")
        elif len(telefone) > 10:
            print("Telefone no máximo 9 dígitos")
        elif telefone.isnumeric():
            break
        
                                            ##MENU DOS SABORES DAS PIZZAS AQUI

    while True:  
        sabor = int(input("""
*****************************                          
1) Calabresa - R$ 59,99
2) Salsicha - R$ 55,50
3) Portuguesa - R$ 64,00
4) Camarão - R$ 220,00
5) Filé com Cheddar - R$ 89,99
6) Milho - R$ 62,50 
7) Açaí - R$ 110,50
Informe o sabor da Pizza:"""))
        if sabor == 1:
            sabor_pizza = "Calabresa"
            preco += 59.99
            break
        elif sabor == 2:
            sabor_pizza = "Salsicha"
            preco += 55.50
            break
        elif sabor == 3:
            sabor_pizza = "Portuguesa"
            preco += 64.00
            break
        elif sabor == 4:
            sabor_pizza = "Camarão"
            preco += 220.00
            break
        elif sabor == 5:
            sabor_pizza = "Filé com Cheddar"
            preco += 89.99
            break
        elif sabor == 6:
            sabor_pizza = "Milho"
            preco += 62.50
            break
        elif sabor == 7:
            sabor_pizza = "Açaí"
            preco += 110.50
            break
        else:
            print("Dado inválido!")

  
                                                  #MENU SOBRE OS TAMANHOS DA PIZZA
      
    while True: 
        tamanho = int(input("""
*******************************                            
1) Tamanho Pequeno(6 pedaços) - R$ 69,00
2) Tamanho Médio(8 pedaços) - R$ 120,00
3) Tamanho Grande(14 pedaços)+ broto de 8 pedaços,sabor chocolate willi wonka - R$ 210,00
Informe o tamanho da Pizza:"""))
        if tamanho == 1:
            tamanho_pizza = "Pequeno"
            preco += 69.00
            break
        elif tamanho == 2:
            tamanho_pizza = "Médio"
            preco += 120.00
            break
        elif tamanho == 3:
            tamanho_pizza = "Grande"
            preco += 210.00
            break
        else:
            print("Dado inválido!")


                                                            #MENU DAS BEBIDAS
    while True: 
        bebida_leitura = int(input("""
**************************************                                   
1) Coca-cola supreme- R$ 30,00
2) Sprite off white- R$ 25,00
3) Suco gucci- R$ 33,50
4) Sem bebida
Informe a sua bebida: """))
        if bebida_leitura == 1:
            bebida = "Coca-cola supreme"
            preco += 30.00
            break
        elif bebida_leitura == 2:
            bebida = "Sprite off white"
            preco += 25.00
            break
        elif bebida_leitura == 3:
            bebida = "Suco gucci"
            preco += 33.50
            break
        elif bebida_leitura == 4:
            bebida = "Sem bebida"
            break
        else:
            print("Dado inválido!")

    print("Obrigada por escolher a nossa pizzaria!".upper().center(50, '*'))
    print("--------------------------------")
    print("""
    Bem-vindo, {}
    Dados do pedido:
    Sabor: {}
    Tamanho: {}
    Bebida: {}
    Total: {:.2f}
    """.format(nome, sabor_pizza, tamanho_pizza, bebida,preco))
    
    from datetime import datetime
    now = datetime.now()
    print ("Data:",now.day, end="/")
    print (now.month,end="/")
    print (now.year,end="  ")
    print ("às:",now.hour,end=":")
    print (now.minute)
    print("----------------------------------")

    validacao = False
