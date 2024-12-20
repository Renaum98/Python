#Usando cores no terminal
# sintaxe: 
# \033[style;text;backm
'''style = 
0 none
1 bold
4 underline
7 negativa'''

'''
text =
30 white
31 red
32 green
33 yellow
34 blue
35 purple
36 light blue
37 grey'''

'''
back =
40 white
41 red
42 green
43 yellow
44 blue
45 purple
46 light blue
47 grey
'''
print('\033[0;30;41mOlá Mundo\033[m')

print('\033[0;33;45mOlá Mundo\033[m')