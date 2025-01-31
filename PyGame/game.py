import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()#inicializar todas as funçoes e bibliotecas

som_colisao = pygame.mixer.Sound('coin.wav')

largura = 640
altura = 480
x = int(largura/2) #colocando o objeto no meio da tela
y = int(altura/2)

x_azul = randint(40,600)
y_azul = randint(50,430)
fonte = pygame.font.SysFont('gabriola', 40, True, True)
conta_ponto = 0


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')#muda o nome que fica na janela
relogio = pygame.time.Clock()#chama a função de fps


while True:# Loop principal do jogo
    relogio.tick(30)#ajusta a taxa de quadros que o jogo sera rodado
    tela.fill((0,0,0))
    mensagem = f'Pontos: {conta_ponto}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -=20
            if event.key == K_s:
                y +=20'''
    if pygame.key.get_pressed()[K_a]:
        x-=20
    if pygame.key.get_pressed()[K_d]:
        x+=20
    if pygame.key.get_pressed()[K_w]:
        y-=20
    if pygame.key.get_pressed()[K_s]:
        y+=20
    #desenhando na tela     cores em RGB  proporção do objeto referente a tela e medidas do objeto
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) 
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        conta_ponto +=1
        som_colisao.play()



    tela.blit(texto_formatado,(450,40))
    pygame.display.update()


