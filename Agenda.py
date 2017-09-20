agenda = []         #Criando uma lista.
 
#Definindo as Funções:
 
def p_nome():       #Função para pedir o nome.
     return(input("Nome: "))

def p_rua():   #Função para pedir o endereco.
     return(input("        Rua: "))

def p_cep():   #Função para pedir o endereco.
     return(input("        Cep: "))

def p_bairro():   #Função para pedir o endereco.
     return(input("        Bairro: "))

def p_estado():   #Função para pedir o endereco.
     return(input("        Estado: "))

def p_telefone():      #Função para pedir o telefone.
     return(input("Telefone: "))

def listar_dados(nome, endereco, telefone):      #Função que mostra todos os dados do contato.
     print("%s\nNome: %s\nRua:  %s\nCep: %s\nBairro: %s\nEstado: %s\nTelefone" % (nome, rua, cep, bairro, estado, telefone))
 
 
def pesquisa(nome):           #Função para pesquisar contatos.
     name = nome.lower()     #Convertendo todas as letras em minúsculas.
     for d, e in enumerate(agenda):     #Executando o loop.
         if e[0].lower() == name:       #Determinando uma condição.
               return d                 #Executa caso a condição for verdadeira.
     return None                        #Executa caso a condição for falsa.

 
def novo():                   #Função para adicionar novo Contato.
     global agenda  #Definindo variável como Global.  
     nome = p_nome()          #Entrada de dados.
     print("Endereço ")
     rua = p_rua()
     cep = p_cep()
     bairro = p_bairro()
     estado = p_estado()
     telefone = p_telefone()        
     agenda.append([nome, rua, cep, bairro, estado, telefone])
     with open ("Pepa.txt","a") as arq:    #Jogando no TXT.
         arq.write ("Nome: "+nome+"\n")
         arq.write ("\n")
         arq.write ("Endereço")
         arq.write ("\n")
         arq.write ("Rua: "+rua+"\n")
         arq.write ("\n")
         arq.write ("Cep: "+cep+"\n")
         arq.write ("\n")
         arq.write ("Bairro: "+bairro+"\n")
         arq.write ("\n")
         arq.write ("Estado: "+estado+"\n")
         arq.write ("\n")
         arq.write ("Telefone: "+telefone+"\n")
         arq.close()

def pesquisar():                   #Função para Pesquisar os contatos.
     p = pesquisa(p_nome())        #Entrada de dados.
     if p != None:                 #Determinando uma condição, caso seja verdadeira:
         nome = agenda[p][0]       #Procurando os dados na agenda.
         endereco = agenda [p] [1]       
         telefone = agenda [p] [2]     #Procurando os dados na agenda.
         print("Encontrado:")      #Exibi informação na tela.
         listar_dados(nome, endereco, telefone)  #Mostra os dados.
     else:
          print("Nome não encontrado.")      #Executa caso a condição seja falsa.
 
def validar(pergunta, inicio, fim):          #Função para validar numeros inteiros.
     while True:                             #Criando um loop infinito.
         try:                                #Criando um acordo/condição.
               valor = int(input(pergunta))  #Entrada de dados.
               if inicio <= valor <= fim:    #Deterimando uma condição.
                   return(valor)             #Executa caso for verdadeira.
               return                       
         except ValueError:                  #Executa caso for falsa.
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

    
def menu():                   #Função que exibe o menu de opções.
     print("""
   1 - Adicionar novo contato
   2 - Consultar por nome
   3 - Sair
""")
    
     return validar("Escolha uma opção: ",1,3) #Retorna o valor da opção desejada.


 
while True:                             #Criando um loop infinito.
     opção = menu()
     if opção == 3:                   
         break
     elif opção == 1:
         novo()
     elif opção == 2:
         pesquisar()

         


        

