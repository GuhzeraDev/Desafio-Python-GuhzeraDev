'''
Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
de tinta pinta uma área de 2 metros quadrados.
'''


p1 = float (input('Largura da parede: '))
p2 = float (input('Altura da parede:  '))
area = p1 * p2
tinta = area/2

print('Sua parede tem a dimensão de {}x{} e sua area e de {}m².'.format(p1,p2,area))
print('Para pintar essa parede, você precisa de {}l de tinta.'.format(tinta))

