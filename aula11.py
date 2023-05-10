#Padrão ANSI scape sequence  por enquanto todos que queremos colocar cor vamo colocar o codigo entre
#\33[style;text;backGround m
#ex:\33[0;33;44m
#style:0(nada),1(Negrito),4(Sublinhado),7(corNegativo)
#cor:30(Branco)/31(Vermelho)/32(Verde)/33(Amarelo)/34(Azul)/35(Roxo)/36(Ciano)/37(Cinza)
#BackGround:40(Branco)/41(Vermelho)/42(Verde)/43(Amarelo)/44(Azul)/45(Roxo)/46(Ciano)/47(Cinza)
print('\33[1;33;40mOlá Mundo!!\33[m')