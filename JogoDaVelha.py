import random;

print ("");
print ("--------------------------- Jogo da Velha - Versão 0.1 ----------------------");
print ("");
print ("                                    Bem Vindo!");
print ("");
print ("                                 Jogar em dupla? ");
print ("");

jogadores=input('                         [ S ] -> SIM ou  [ N ] -> NÂO ?: ');
print ("");print ("");print ("");
jogadores=jogadores.upper();

##Verifico se o símbolo é permitido
while jogadores!="S" and jogadores!="N":
    jogadores=input(" - Símbolo não permitido. Por favor escolha [ S ] -> SIM ou  [ N ] -> NÂO : ");
    #Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
    jogadores=jogadores.upper();


if jogadores=="S":
    print ("");print ("");
    jogador1=input('Digite o nome do Primeiro jogador: ');

    print ("");print ("");
    jogador2=input('Digite o nome do Segundo jogador: ');

else:
    jogador1=input('Digite o nome do Primeiro jogador: ');
    jogador2='Computador';

jogador1=jogador1.upper();
jogador2=jogador2.upper();

print ("");print ("");
figjogador1=input(jogador1+' - Escolha entre [ X ] ou [ O ]: ');
#Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
figjogador1=figjogador1.upper();


while figjogador1!="X" and figjogador1!="O" :
    figjogador1=input(jogador1+" - Símbolo não permitido. Por favor escolha [ X ] ou  [ O ]: ");
    #Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
    figjogador1=figjogador1.upper();
    
print ("");  
# Verifico se no jogar com o pc as letras estão adequadas para cada jogador
if figjogador1=="O":
        figjogador2="X";
else:
        figjogador2="O";
        
print (jogador2+" - Você jogará com a letra [ "+ figjogador2 +" ]");
print ("");  					 
print ("OK! Agora podemos começar.");
print ("");  
print ("Veja as instruções logo abaixo.");
print ("");
print ("");
print ("----------------------------------- Instruções -------------------------------");
print ("-    Utilize os números de 1 a 3 para indicar a linha e os mesmos números    -");
print ("-                    de 1 à 3 para indicar a coluna que desejar.             -");
print ("-      Desta forma: 12 -> sendo o número 1 - Linha e o número 2 - Coluna.    -");
print ("------------------------------------------------------------------------------");
print ("                                   1    2   3");
print ("                                      |   |");
print ("                                 1    | X |");
print ("                                   ___|___|___");
print ("                                      |   |");
print ("                                 2    |   |");
print ("                                   ___|___|___");
print ("                                      |   |");
print ("                                 3    |   |");
print ("                                      |   |");
print ("");

print ("------------------------------------------------------------------------------");
print ("Boa sorte "+jogador1+" !");
print ("");
print ("                                   1    2   3");
print ("                                      |   |");
print ("                                 1    |   |");
print ("                                   ___|___|___");
print ("                                      |   |");
print ("                                 2    |   |");
print ("                                   ___|___|___");
print ("                                      |   |");
print ("                                 3    |   |");
print ("                                      |   |");
print ("");
print ("");

#Inicializando a lista Vetores com 3 campos - Para o tabuleiro
L1 = [0]*3;
L2 = [0]*3;
L3 = [0]*3;

#Variável para verificar a cordenada da jogada
cordjogador1=0;
cordjogador2=0;

#Variável para verificar o número de jogadas que só pode chegar a no máximo 9 jogadas
qtDJogadas=0;

#Conteúdo inicial da lista dos vetores para preencher uma posição na tabela
L1[0] = ' ';L1[1] = ' ';L1[2] = ' ';
L2[0] = ' ';L2[1] = ' ';L2[2] = ' ';
L3[0] = ' ';L3[1] = ' ';L3[2] = ' ';

#Variável para verificar se posso seguir em frente no tabuleiro: 0 - Inicial; 1 - Livre; 2 - Ocupado
posicaoOcupada=0;
#Utilizado para verificar se um dos jogadores ganha
ganhou=0;
#Verifico qual jogador esta jogando
jogador=1;

#Se a quantidade de jogadas for menor que 10 continuo.
while qtDJogadas<10:
    #Se aposição estiver livre posso ocupar a casa     
    while posicaoOcupada==0 or posicaoOcupada==2:
        print ("------------------------------------------------------------------------------");
        if jogador==1:
            cordjogador1=int(input(jogador1+" - Sua vez! Digite a Linha e a Coluna desejada: "));            
            cordenada=cordjogador1;
            figura=figjogador1;
        if jogador==2:
            cordjogador2=int(input(jogador2+" - Sua vez! Digite a Linha e a Coluna desejada: "));            
            cordenada=cordjogador2;
            figura=figjogador2;
        

        if jogador==1 or jogador==2:
            #Se não entrar em nehuma condição abaixo entao posicaoOcupada=2, quer dizer que o valor
            #digitado esta errado ou ocupado.
            posicaoOcupada=2;
            
            #Primeiro verifico se a posição escolhida esta vazia e gravo a posição escolhida na lista
            if cordenada==11:
                if L1[0]==" ":
                    L1[0]=(figura);               
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==12:
                if L1[1]==" ":
                    L1[1]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==13:
                if L1[2]==" ":
                    L1[2]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==21:
                if L2[0]==" ":
                    L2[0]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==22:
                if L2[1]==" ":
                    L2[1]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==23:
                if L2[2]==" ":
                    L2[2]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==31:
                if L3[0]==" ":
                    L3[0]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==32:
                if L3[1]==" ":
                    L3[1]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
            if cordenada==33:
                if L3[2]==" ":
                    L3[2]=(figura);
                    posicaoOcupada=1;
                else:
                    posicaoOcupada=2;
                
        else:
            
            ##################################Computador joga########################################

            figura=figjogador2;
            
            #Analizo primeiro a jogada do computador e vejo se ele tem chances de ganhar, se não, ataco ou bloqueio.

            #Verificando as Linhas
            #Linha 1
            if L1[0]==figura and L1[1]==figura and L1[2]==' ':
                L1[2]=figura;
               # if L1[0]==figura:
                ganhou = 1;
                posicaoOcupada=1;

            if L1[2]==figura and L1[1]==figura and L1[0]==' ':
                L1[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;
                
            if L1[0]==figura and L1[1]==' ' and L1[2]==figura:
                L1[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            #Linha 2
            if L2[0]==figura and L2[1]==figura and L2[2]==' ':
                L2[2]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L2[2]==figura and L2[1]==figura and L2[0]==' ':
                L2[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L2[0]==figura and L2[1]==' ' and L2[2]==figura:
                L2[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            #Linha 3
            if L3[0]==figura and L3[1]==figura and L3[2]==' ':
                L3[2]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L3[2]==figura and L3[1]==figura and L3[0]==' ':
                L3[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;
            
            if L3[0]==figura and L3[1]==' ' and L3[2]==figura:
                L3[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            #Verificadndo as colunas
            #Coluna 1
            if L1[0]==figura and L2[0]==figura and L3[0]==' ':
                L3[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L3[0]==figura and L2[0]==figura and L1[0]==' ':
                L1[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L1[0]==figura and L2[0]==' ' and L3[0]==figura:
                L2[0]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            #Coluna 2
            if L1[1]==figura and L2[1]==figura and L3[1]==' ':
                L3[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L3[1]==figura and L2[1]==figura and L1[1]==' ':
                L1[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L1[1]==figura and L2[1]==' ' and L3[1]==figura:
                L2[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;   

            #Coluna 3
            if L1[2]==figura and L2[2]==figura and L3[2]==' ':
                L3[2]=figura;
                ganhou = 1; 
                posicaoOcupada=1;

            if L3[2]==figura and L2[2]==figura and L1[2]==' ':
                L1[2]=figura;
                ganhou = 1; 
                posicaoOcupada=1;

            if L1[2]==figura and L2[2]==' ' and L3[2]==figura:
                L2[2]=figura;
                ganhou = 1; 
                posicaoOcupada=1;

            #Verificando as diagonais
            if L1[0]==figura and L2[1]==figura and L3[2]==' ':
               L3[2]=figura;
               ganhou = 1;
               posicaoOcupada=1;

            #Verificando as diagonais
            if L1[0]==figura and L2[1]==' ' and L3[2]==figura:
               L2[1]=figura;
               ganhou = 1;
               posicaoOcupada=1;
            #Verificando as diagonais
            if L1[2]==figura and L2[1]==figura and L3[0]==' ':
               L3[0]=figura;
               ganhou = 1;
               posicaoOcupada=1;

            #Verificando as diagonais
            if L1[2]==figura and L2[1]==' ' and L3[0]==figura:
               L2[1]=figura;
               ganhou = 1;
               posicaoOcupada=1;

            #Verificando as diagonais
            if L3[0]==figura and L2[1]==figura and L1[2]==' ':
                L1[2]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            #Verificando as diagonais*
            if L3[0]==figura and L2[1]==' ' and L1[2]==figura:
                L2[1]=figura;
                ganhou = 1;
                posicaoOcupada=1;

            if L3[2]==figura and L2[1]==figura and L1[0]==' ':
               L1[0]=figura;
               ganhou = 1;
               posicaoOcupada=1;

            #Verificando o meio vazio
            if L3[2]==figura and L2[1]==' ' and L1[0]==figura:
               L2[1]=figura;
               ganhou = 1;

                      
            #BLOQUEANDO A JOGADA DO JOGADOR 1 
            if ganhou==0:

                if L1[0]==figjogador1 and L1[1]==figjogador1 and L1[2]==' ':
                    L1[2]=figura;
                    posicaoOcupada=1;

                if L1[2]==figjogador1  and L1[1]==figjogador1 and L1[0]==' ':
                    L1[0]=figura;
                    posicaoOcupada=1;                   
                    
                if L1[0]==figjogador1 and L1[1]==' ' and L1[2]==figjogador1:
                    L1[1]=figura;
                    posicaoOcupada=1;

                #Linha 2
                if L2[0]==figjogador1 and L2[1]==figjogador1 and L2[2]==' ':
                    L2[2]=figura;
                    posicaoOcupada=1;

                if L2[2]==figjogador1 and L2[1]==figjogador1 and L2[0]==' ':
                    L2[0]=figura;
                    posicaoOcupada=1;

                if L2[0]==figjogador1 and L2[1]==' ' and L2[2]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;

                #Linha 3
                if L3[0]==figjogador1 and L3[1]==figjogador1 and L3[2]==' ':
                    L3[2]=figura;
                    posicaoOcupada=1;

                if L3[2]==figjogador1 and L3[1]==figjogador1 and L3[0]==' ':
                    L3[0]=figura;
                    posicaoOcupada=1;
                  
                if L3[0]==figjogador1 and L3[1]==' ' and L3[2]==figjogador1:
                    L3[1]=figura;
                    posicaoOcupada=1;

                #Verificadndo as colunas
                #Coluna 1
                if L1[0]==figjogador1 and L2[0]==figjogador1 and L3[0]==' ':
                    L3[0]=figura;
                    posicaoOcupada=1;
                  
                if L3[0]==figjogador1 and L2[0]==figjogador1 and L1[0]==' ':
                    L1[0]=figura;
                    posicaoOcupada=1;
                  
                if L1[0]==figjogador1 and L2[0]==' ' and L3[0]==figjogador1:
                    L2[0]=figura;
                    posicaoOcupada=1;
                  
                #Coluna 2
                if L1[1]==figjogador1 and L2[1]==figjogador1 and L3[1]==' ':
                    L3[1]=figura;
                    posicaoOcupada=1;
                   
                if L3[1]==figjogador1 and L2[1]==figjogador1 and L1[1]==' ':
                    L1[1]=figura;
                    posicaoOcupada=1;
                   
                if L1[1]==figjogador1 and L2[1]==' ' and L3[1]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;
                                           
                #Coluna 3
                if L1[2]==figjogador1 and L2[2]==figjogador1 and L3[2]==' ':
                    L3[2]=figura;
                    posicaoOcupada=1;
                   
                if L3[2]==figjogador1 and L2[2]==figjogador1 and L1[2]==' ':
                    L1[2]=figura;
                    posicaoOcupada=1;
                   
                if L1[2]==figjogador1 and L2[2]==' ' and L3[2]==figjogador1:
                    L2[2]=figura;
                    posicaoOcupada=1;
                    

                #Verificando as diagonais
                #Diagonal direita
                if L1[0]==figjogador1 and L2[1]==figjogador1 and L3[2]==' ':
                    L3[2]=figura;
                    posicaoOcupada=1;

                #Verificando o meio vazio da diagonal
                if L1[0]==figjogador1 and L2[1]==' ' and L3[2]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;

                #Diagonal Esquerda
                if L1[2]==figjogador1 and L2[1]==figjogador1 and L3[0]==' ':
                    L3[0]=figura;
                    posicaoOcupada=1;

                #Verificando o meio vazio da diagonal
                if L1[2]==figjogador1 and L2[1]==' ' and L3[0]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;

                if L3[0]==figjogador1 and L2[1]==figjogador1 and L1[2]==' ':
                    L1[2]=figura;
                    posicaoOcupada=1;

                #Verificando o meio vazio da diagonal
                if L3[0]==figjogador1 and L2[1]==' ' and L1[0]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;

                if L3[2]==figjogador1 and L2[1]==figjogador1 and L1[0]==' ':
                    L1[0]=figura;
                    posicaoOcupada=1;

                #Verificando o meio vazio da diagonal
                if L3[2]==figjogador1 and L2[1]==' ' and L1[0]==figjogador1:
                    L2[1]=figura;
                    posicaoOcupada=1;
                
                #Em posições diferentes verifico a melhor jogada.
                
                #Mapeio a jogada efetuada na tabela sendo:---1---|---2---|---3---
                #                                         ---4---|---5---|---6---
                #                                         ---7---|---8---|---9--- 
                #Somo cada linha diferente de zero. Com base que o computador joga sempre por segundo.
                posicaoTab=0;
                for i in range(2):
                                       
                    if L1[i]!=" " and i==0:
                        posicaoTab=1; 
                    if L1[i]!=" " and i==1:
                        posicaoTab=posicaoTab+2;                        
                    if L1[i]!=" " and i==2:
                        posicaoTab=posicaoTab+3;

                    if L2[i]!=" " and i==0:
                        posicaoTab=posicaoTab+4; 
                    if L2[i]!=" " and i==1:                        
                        posicaoTab=posicaoTab+5;                                           
                        
                    if L2[i]!=" " and i==2:
                        posicaoTab=posicaoTab+6;
                    
                    if L3[i]!=" " and i==0:
                        posicaoTab=posicaoTab+7;
                                             
                    if L3[i]!=" " and i==1:
                        posicaoTab=posicaoTab+8;
                                                                 
                    if L3[i]!=" " and i==2:
                        posicaoTab=posicaoTab+9;                 

                    i=i+1; #**


                passa=0;
              
                while passa==0 and qtDJogadas==3:                    
                    passa=1;


                    #Jogada 15 em especial é uma jogada que o jogador 1 tenta armar uma cilada
                    #ou joga apenas para testar se o computador consegue jogar em uma situação inesperada. 
                    if posicaoTab==15 :
                        opcoes=[1,2,3,7,8,9];
                        random.shuffle(opcoes);
                        opcao=opcoes[:1];
                        if opcao==[1] and passa==0 and L1[0]==" ":                        
                            L1[0]=figura;
                            passa=1;
                            posicaoOcupada=1;
                        if opcao==[2] and passa==0 and L1[1]==" ":                        
                            L1[1]=figura;
                            passa=1;
                            posicaoOcupada=1;
                        if opcao==[3] and passa==0 and L1[2]==" ":                        
                            L1[2]=figura;
                            passa=1;
                            posicaoOcupada=1;
                        #falta alguma coisa******
                        if opcao==[7] and passa==0 and L3[0]==" ":                        
                            L3[0]=figura;
                            passa=1;
                            posicaoOcupada=1;                       
                        if opcao==[8] and passa==0 and L3[1]==" ":                        
                            L3[1]=figura;
                            passa=1;
                            posicaoOcupada=1;
                        if opcao==[9] and passa==0 and L3[2]==" ":                        
                            L3[2]=figura;
                            passa=1;
                            posicaoOcupada=1;


                print ("Jogada :");          
                print (posicaoTab); 

                if posicaoTab==78:
                    if L1[0]==" ":
                        L1[0]=figura;
                        posicaoOcupada=1;
                    else:
                        L1[1]=figura;
                        posicaoOcupada=1;   

                if posicaoTab==30 and qtDJogadas==5:
                    print (posicaoTab); 
                    if L1[0]==" ":
                        L1[0]=figura;
                        posicaoOcupada=1;
                    else: 
                        L3[0]=figura;
                        posicaoOcupada=1;

                #if posicaoTab==26 or posicaoTab==28 or posicaoTab==32 or posicaoTab==36:

                if L1[1]==figjogador1 and L2[1]==figjogador2 and L3[1]==figjogador1 and L3[0]==" ":
                    L3[0]=figura;
                    posicaoOcupada=1;
                if L1[0]==figjogador1 and L1[2]==figjogador1 and L3[1]==figjogador1 and L2[2]==" ":
                    L2[2]=figura;
                    posicaoOcupada=1; 
                if L2[1]==" ":
                    L2[1]=figura;
                    posicaoOcupada=1;
                
                if L2[1]==figjogador1 and qtDJogadas==1:
                    opcoes=[1,3,7,9];
                    random.shuffle(opcoes);
                    #busco apenas um casa da lista 
                    opcao=opcoes[:1];
                    if opcao==[1]:
                        L1[0]=figura;
                        posicaoOcupada=1;
                    if opcao==[3]:
                        L1[2]=figura;
                        posicaoOcupada=1;
                    if opcao==[7]:
                        L3[0]=figura;
                        posicaoOcupada=1;
                    if opcao==[9]:
                        L3[2]=figura;  
                        posicaoOcupada=1;

                #Se no final ouver algum campo vazio por alguma jogada diferente da verificada eu apenas preencho
                #o campo que sobra
                if qtDJogadas==9:
                    if L1[0]==" ":
                        L1[0]==figura;
                        posicaoOcupada=1; 
                    if L1[1]==" ":
                        L1[1]==figura;
                        posicaoOcupada=1; 
                    if L1[2]==" ":
                        L1[2]==figura;
                        posicaoOcupada=1; 
                    if L2[0]==" ":
                        L2[0]==figura;
                        posicaoOcupada=1; 
                    if L2[1]==" ":
                        L2[1]==figura;
                        posicaoOcupada=1; 
                    if L3[0]==" ":
                        L3[0]==figura;
                        posicaoOcupada=1; 
                    if L3[1]==" ":
                        L3[1]==figura;
                        posicaoOcupada=1; 
                    if L3[2]==" ":
                        L3[2]==figura;
                        posicaoOcupada=1; 

                                       
       ##################################Fim da Jogada do computador####################################

        if posicaoOcupada==2: 
            print ("Posição inválida ou já ocupada!");        
        else:
            #Controlo a quantidade de jogadas que inicia com 0 e adiciono + 1, chegando ate 9.
            qtDJogadas=qtDJogadas+1;
            
            if jogador==1:
                #Se for o jogador1 eu verifico se ele esta jogando com o computador
                if jogadores=="S":
                    print  (jogador1+" jogou...");
                    #Se ele estiver jogando com o pc então será a vez do jogador2
                    jogador=2;
                else:                    
                    #Se não será a vez do jogador3 que no caso é o computador
                    print  ("Montando o tabuleiro...");
                    jogador=3;
            else:
               print  (jogador2+" jogou...");
               jogador=1;
       
    print ("");
    #Montando o tabuleiro
    print ("                                   1    2   3");
    print ("                                      |"+"   |"+"");
    print ("                                 1  "+L1[0]+" |"+" "+L1[1]+" |"+" "+L1[2]+"  ");
    print ("                                   ___|"+"___|"+"___");
    print ("                                      |"+"   |"+"");
    print ("                                 2  "+L2[0]+" |"+" "+L2[1]+" |"+" "+L2[2]+"  ");
    print ("                                   ___|"+"___|"+"___");
    print ("                                      |"+"   |"+"");
    print ("                                 3  "+L3[0]+" |"+" "+L3[1]+" |"+" "+L3[2]+"  ");
    print ("                                      |"+"   |"+"");
    print ("");
    #Se o jogador ganhar então - [ ganhou ] será igual a 1.
    # ganhou=0;

    #Verificando as Linhas
    if L1[0]==figura and L1[1]==figura and L1[2]==figura:
        ganhou = 1;
      
    if L2[0]==figura and L2[1]==figura and L2[2]==figura:
        ganhou = 1;

    if L3[0]==figura and L3[1]==figura and L3[2]==figura:
        ganhou = 1;

    #Verificadndo as colunas
    if L1[0]==figura and L2[0]==figura and L3[0]==figura:
        ganhou = 1;
    if L1[1]==figura and L2[1]==figura and L3[1]==figura:
        ganhou = 1;
    if L1[2]==figura and L2[2]==figura and L3[2]==figura:
        ganhou = 1;

    #Verificando as diagonais
    if L1[0]==figura and L2[1]==figura and L3[2]==figura:
        ganhou = 1;
    if L1[2]==figura and L2[1]==figura and L3[0]==figura:
        ganhou = 1;

    #Verifico se o jogo empata
    if qtDJogadas==9 and ganhou==0:
        print ("Deu velha ! Jogo empatado!!!");
        break;

    if qtDJogadas==9 and ganhou==1:
        print ("Parabéns "+jogador1+", você venceu !");
        break;

    #Deixo posicaoOcupada=0 para o jogador2 poder voltar e indicar a posicao correta
    #E também para que não gere loop infinito
    posicaoOcupada=0;

    #--------Verifico se aguém ganha ou se pode continuar--------
    if ganhou == 1:

        if jogadores=="S":
            print ("Parabéns "+jogador1+", você venceu !");
        else:
            print ("Que pena! Você perdeu, mas pode melhorar!");
        ganhou=1;
        qtDJogadas=0;
        jogadores="N"
        break;
    else:
        ganhou=0;     
