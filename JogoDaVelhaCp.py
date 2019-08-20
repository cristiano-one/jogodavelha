print ("");
print ("--------------------------- Jogo da Velha - Versão 0.1 ----------------------");
print ("                                    Bem Vindo!");
print ("");


jogadores=input('Gostaria de jogar em dupla? [ S ] -> SIM ou  [ N ] -> NÂO ?: ');
jogadores=jogadores.upper();

print (jogadores);

while jogadores!="S" and jogadores!="N":
    jogadores=input(" - Símbolo não permitido. Por favor escolha [ S ] -> SIM ou  [ N ] -> NÂO : ");
    #Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
    jogadores=jogadores.upper();


if jogadores=="S":
    jogador1=input('Digite o nome do Primeiro jogador: ');
    jogador2=input('Digite o nome do Segundo jogador: ');
else:
    jogador1=input('Digite o nome do Primeiro jogador: ');
    jogador2='Computador';


figjogador1=input(jogador1+' - Escolha entre [ X ] ou [ O ]: ');
#Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
figjogador1=figjogador1.upper();


while figjogador1!="X" and figjogador1!="O" :
    figjogador1=input(jogador1+" - Símbolo não permitido. Por favor escolha [ X ] ou  [ O ]: ");
    #Deixo as letras Maiúsculas se o jogador digitar Minúsculo    
    figjogador1=figjogador1.upper();
    
print ("");  
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
print ("");
print ("Vamos Começar!");

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
#Verificar se posso seguir em frente: 0 - Inicial; 1 - Livre; 2 - Ocupado
posicaoOcupada=0;
#Utilizado para verificar se um dos jogadores ganha
ganhou=0;
#Verifico qual jogador esta jogando
jogador=1;

    
while qtDJogadas!=9 :
          
    while posicaoOcupada==0 or posicaoOcupada==2:
      
        if jogador==1:
            cordjogador1=int(input(jogador1 +" - Sua vez! Digite a Linha e a Coluna desejada: "));
            cordenada=cordjogador1;
            figura=figjogador1;
        if jogador==2:
            cordjogador2=int(input(jogador2 +" - Sua vez! Digite a Linha e a Coluna desejada: "));
            cordenada=cordjogador2;
            figura=figjogador2;
        

        if jogador==1 or jogador==2:
            #Se não entrar em nehuma condição abaixo entao posicaoOcupada=2, quer dizer que o valor
            #digitado esta errado.
            posicaoOcupada=2;
            
            #Verifico se a posição escolhida esta vazia e gravo a posição escolhida na lista
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
            print ("-----------------------------------Computador---------------------------------");
            
            figura=figjogador2;
            
            #Analizo primeiro a jogado do computador e vejo se ele tem chances de ganhar e ataco

            #Verificando as Linhas
            #Linha 1
            if L1[0]==figura and L1[1]==figura and L1[2]==' ' or L1[0]==figjogador1 and L1[1]==figjogador1 and L1[2]==' ':
                L1[2]=figura;
                if L1[0]==figura:
                    ganhou = 1;
            if L1[2]==figura and L1[1]==figura and L1[0]==' ' or L1[2]==figjogador1  and L1[1]==figjogador1 and L1[0]==' ':
                L1[0]=figura;
                if L1[0]==figura:
                    ganhou = 1;
                
            if L1[0]==figura and L1[2]==figura and L1[1]==' ' or L1[0]==figjogador1 and L1[2]==figjogador1 and L1[1]==' ':
                L1[1]=figura;
                if L1[0]==figura:
                    ganhou = 1;
            #Linha 2
            if L2[0]==figura and L2[1]==figura and L2[2]==' ' or L2[0]==figjogador1 and L2[1]==figjogador1 and L2[2]==' ':
                L2[2]=figura;
                if L2[0]==figura:
                    ganhou = 1;
            if L2[2]==figura and L2[1]==figura and L2[0]==' ' or L2[2]==figjogador1 and L2[1]==figjogador1 and L2[0]==' ':
                L2[0]=figura;
                if L2[0]==figura:
                    ganhou = 1;
            if L2[0]==figura and L2[2]==figura and L2[1]==' ' or L2[0]==figjogador1 and L2[2]==figjogador1 and L2[1]==' ':
                L2[1]=figura;
                if L2[0]==figura:
                    ganhou = 1;
            #Linha 3
            if L3[0]==figura and L3[1]==figura and L3[2]==' ' or L3[0]==figjogador1 and L3[1]==figjogador1 and L3[2]==' ':
                L3[2]=figura;
                if L3[0]==figura:
                    ganhou = 1;
            if L3[2]==figura and L3[1]==figura and L3[0]==' ' or L3[2]==figjogador1 and L3[1]==figjogador1 and L3[0]==' ':
                L3[0]=figura;
                if L3[0]==figura:
                    ganhou = 1;
            if L3[0]==figura and L2[2]==figura and L3[1]==' ' or L3[0]==figjogador1 and L2[2]==figjogador1 and L3[1]==' ':
                L3[1]=figura;
                if L3[0]==figura:
                    ganhou = 1;

            #Verificadndo as colunas
            #Coluna 1
            if L1[0]==figura and L2[0]==figura and L3[0]==' ' or L1[0]==figjogador1 and L2[0]==figjogador1 and L3[0]==' ':
                L3[0]=figura;
                if L3[0]==figura:
                    ganhou = 1;
            if L3[0]==figura and L2[0]==figura and L1[0]==' ' or L3[0]==figjogador1 and L2[0]==figjogador1 and L1[0]==' ':
                L1[0]=figura;
                if L3[0]==figura:
                    ganhou = 1;
            if L1[0]==figura and L3[0]==figura and L2[0]==' ' or L1[0]==figjogador1 and L3[0]==figjogador1 and L2[0]==' ':
                L2[0]=figura;
                if L1[0]==figura:
                    ganhou = 1;
            #Coluna 2
            if L1[1]==figura and L2[1]==figura and L3[1]==' ' or L1[1]==figjogador1 and L2[1]==figjogador1 and L3[1]==' ':
                L3[1]=figura;
                if L1[1]==figura:
                    ganhou = 1;
            if L3[1]==figura and L2[1]==figura and L1[1]==' ' or L3[1]==figjogador1 and L2[1]==figjogador1 and L1[1]==' ':
                L1[1]=figura;
                if L3[1]==figura:
                    ganhou = 1;
            if L1[1]==figura and L3[1]==figura and L2[1]==' ' or L1[1]==figjogador1 and L3[1]==figjogador1 and L2[1]==' ':
                L2[1]=figura;
                if L1[1]==figura:
                    ganhou = 1;                             
            #Coluna 3
            if L1[2]==figura and L2[2]==figura and L3[2]==' ' or L1[2]==figjogador1 and L2[2]==figjogador1 and L3[2]==' ':
                L3[2]=figura;
                if L1[2]==figura:
                    ganhou = 1; 
            if L3[2]==figura and L2[2]==figura and L1[2]==' ' or L3[2]==figjogador1 and L2[2]==figjogador1 and L1[2]==' ':
                L1[2]=figura;
                if L3[2]==figura:
                    ganhou = 1; 
            if L1[2]==figura and L3[2]==figura and L2[2]==' ' or L1[2]==figjogador1 and L3[2]==figjogador1 and L2[2]==' ':
                L2[2]=figura;
                if L1[2]==figura:
                    ganhou = 1; 

            #Verificando as diagonais
            if L1[0]==figura and L2[1]==figura and L3[2]==' ' or L1[0]==figjogador1 and L2[1]==figjogador1 and L3[2]==' ':
               L3[2]=figura;
               if L1[0]==figura:
                   ganhou = 1;

            #Verificando o meio vazio
            if L1[0]==figura and L3[2]==figura and L2[1]==' ' or L1[0]==figjogador1 and L3[2]==figjogador1 and L2[1]==' ':
               L2[1]=figura;
               if L1[0]==figura:
                   ganhou = 1;

            if L1[2]==figura and L2[1]==figura and L3[0]==' ' or L1[2]==figjogador1 and L2[1]==figjogador1 and L3[0]==' ':
               L3[0]=figura;
               if L1[2]==figura:
                   ganhou = 1;

            #Verificando o meio vazio
            if L1[2]==figura and L3[0]==figura and L2[1]==' ' or L1[2]==figjogador1 and L3[0]==figjogador1 and L2[1]==' ':
               L2[1]=figura;
               if L1[2]==figura:
                   ganhou = 1;


            if L3[0]==figura and L2[1]==figura and L1[2]==' ' or L3[0]==figjogador1 and L2[1]==figjogador1 and L1[2]==' ':
               L1[2]=figura;
               if L3[0]==figura:
                   ganhou = 1;

            #Verificando o meio vazio
            if L3[0]==figura and L1[0]==figura and L2[1]==' ' or L3[0]==figjogador1 and L1[0]==figjogador1 and L2[1]==' ':
               L2[1]=figura;
               if L3[0]==figura:
                   ganhou = 1;

            if L3[2]==figura and L2[1]==figura and L1[0]==' ' or L3[2]==figjogador1 and L2[1]==figjogador1 and L1[0]==' ':
               L1[0]=figura;
               if L3[2]==figura:
                   ganhou = 1;

            #Verificando o meio vazio
            if L3[2]==figura and L1[0]==figura and L2[1]==' ' or L3[2]==figjogador1 and L1[0]==figjogador1 and L2[1]==' ':
               L2[1]=figura;
               if L3[2]==figura:
                   ganhou = 1;


            if L2[1]==" ":
                L2[1]=figjogador2;
                posicaoOcupada=1;
            if L1[1]==figjogador1 and L3[1]==figjogador1 and L2[1]==figjogador2:
                L3[0]=figjogador2;
                posicaoOcupada=1;
         
        print  (L1[2]);

        if posicaoOcupada==2: 
            print ("Posição inválida ou já ocupada!");        
        else:
            #Controlo a quantidade de jogadas que inicia com 0 e adiciono + 1, chegando ate 9.
            qtDJogadas=qtDJogadas+1;
            if jogador==1:
                if jogadores=="S":
                    jogador=2;
                else:
                    jogador=3;
            else:
               jogador=1;  

    #Montando o tabuleiro
    print ("                                      |"+"   |"+"");
    print ("                                    "+L1[0]+" |"+" "+L1[1]+" |"+" "+L1[2]+"  ");
    print ("                                   ___|"+"___|"+"___");
    print ("                                      |"+"   |"+"");
    print ("                                    "+L2[0]+" |"+" "+L2[1]+" |"+" "+L2[2]+"  ");
    print ("                                   ___|"+"___|"+"___");
    print ("                                      |"+"   |"+"");
    print ("                                    "+L3[0]+" |"+" "+L3[1]+" |"+" "+L3[2]+"  ");
    print ("                                      |"+"   |"+"");

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

    #Verifico se o jogo empada
    if qtDJogadas==9 and ganhou==0:
        print ("Jogo empatado!!!");
        break;

    #Deixo posicaoOcupada=0 para o jogador2 poder voltar e indicar a posicao correta
    #E também para que não gere loop infinito
    posicaoOcupada=0;

    #--------Verifico se aguém ganha ou se pode continuar--------
    if ganhou == 1:
        if jogadores=="S":
            print (" Parabéns "+jogador1+", você venceu ! que pena "+jogador2+" você perdeu , mas pode melhorar ! ");
        else:
            print (" Que pena. Você perdeu mas pode melhorar!");
        ganhou=1;
        qtDJogadas=0;
        break;
            
