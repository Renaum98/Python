d = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
vd = d*60
vkm = km*0.15
vf = vd + vkm
print('O total a pagar é de R${:.2f}'.format(vf))
