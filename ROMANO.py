#NÚMERO ROMANO

#definindo qual converção será feita
def romano_or_numeral():
    num=0
    while (num!=1) and (num!=2):
        num=int(input('Escolha a opção: \n \n 1- ROMANO PARA NÚMERO \n 2- NUMÉRICO PARA ROMANO \n \n Ditige 1 ou 2: ' ))
        print('')

        #mensagem de escolha inválida
        if (num!=1) and (num!=2):
            print('Número inválido, digite novamente.')
            print('')

    #direcionamento para a converção de romano para numeral
    if num==1:
        geral_romano()

    #direcionamento para a converção de numeral para romano
    else:
        geral_numeral()



# FUNÇÃO GERAL DE CONVERÇÃO NUMERAL_ROMANO
def geral_numeral():
    
    #chamando funcão que recebe e valida o número 
    num=prepara_numerico()
    converte=converte_numerico(num)



# FUNÇÃO GERAL DE CONVERÇÃO ROMANO_NUMERAL
def geral_romano():
    #chamando funcão que recebe e prepara os números romanos para a converção 
    lista, romano = prepara_romano()
    lista= converte_romano(lista)
    convercao= soma_romano(lista)
    print('')
    print(f'O número romano {romano} em númerico é {convercao}')




#RECEBENDO E PREPARANDO NUMERO ROMANO
def prepara_romano():
    lista=[]

    #PEGANDO O NÚMERO ROMANO
    y=str(input('Digite um número romano: '))
    print('')
    y=y.upper()

    #VERIFICANDO SE O NÚMERO É VALIDO, SE VALIDO: SEPARA CADA NUMERO EM UMA LISTA PARA CONVERÇÃO
    for i in y:
        if i!='I' and i!='V' and i!='X' and i!='L' and i!='C' and i!='D' and i!='M':
            print('Número romano inválido.')
            print('')
            prepara_romano()
        lista.append(i)
    return lista, y




#CONVERTENDO NUMERO ROMANO
def converte_romano(lista):
    convercao=[]
    #contador de indice da lista
    for i in range(0,len(lista)-1):
        # verificando se o item já foi executado ou não
        if lista[i]!=0:

            #VERIFICANDO I
            if lista[i]=='I':
                # se houver V depois registrar 4 
                if lista[i+1]=='V':
                    convercao.append(4)
                    lista[i+1]=0

                # se houver X depois registrar 9 
                elif lista[i+1]=='X':
                    convercao.append(9)
                    lista[i+1]=0
                # se nao houver V nem X depois, registrar 1
                else:
                    convercao.append(1)

            #VERIFICANDO V
            elif lista[i]=='V':
                    convercao.append(5)

            #VERIFICANDO X     
            if lista[i]=='X':
                if lista[i+1]=='L':
                    convercao.append(40)
                    lista[i+1]=0
                elif lista[i+1]=='C':
                    convercao.append(90)
                    lista[i+1]=0
                else:
                    convercao.append(10)

            #VERIFICANDO L
            elif lista[i]=='L':
                    convercao.append(50)

            #VERIFICANDO C    
            if lista[i]=='C':
                if lista[i+1]=='D':
                    convercao.append(400)
                    lista[i+1]=0
                elif lista[i+1]=='M':
                    convercao.append(900)
                    lista[i+1]=0
                else:
                    convercao.append(100)

            #VERIFICANDO L
            elif lista[i]=='D':
                    convercao.append(500)

            #VERIFICANDO L
            elif lista[i]=='M':
                        convercao.append(1000)
    return convercao




#SOMANDO OS NUMEROS DA LISTA 
def soma_romano(lista):
    soma=0
    for i in lista:
        soma=soma+i
    return soma




#RECEBENDO O NÚMERO
def prepara_numerico():
    
    #PEGANDO O NÚMERO e verificando se ele é válido 
    y=-1
    while y<0:
        y=int(input('Digite um número inteiro positivo: '))
        #mensagem de aviso se o numero for inválido
        if y<0:
            print('')
            print('Número negativo, por favor digite novamente')
    print('')
    return y



#CONVERTE NUMERO PARA ROMANO
def converte_numerico(num):
    while num!=0:
        if (num//1000)






#http://www.climaat.angra.uac.pt/produtos/calculadoras/numeros_romanos.htm



romano_or_numeral()