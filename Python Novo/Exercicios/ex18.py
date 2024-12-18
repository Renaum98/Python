#seno, cosseno e tangente
from math import radians, sin, cos, tan
an = float(input('Digite o angulo que você deseja: '))
sen = sin(radians(an))#o radians formata como radianos
cos = cos(radians(an))
tan = tan(radians(an))

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, tan))