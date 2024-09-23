import pygame
import sys

pygame.init()

musica_fundo = pygame.mixer.music.load("12 - Sunken Depths.mp3") 
pygame.mixer.music.play(-1)

largura = 1280
altura = 720

largura_Opc = 250
altura_Opc = 50

x_Hist = largura/2 - largura_Opc/2
y_Hist = altura/2

x_Arcd = largura/2 - largura_Opc/2
y_Arcd = altura/1.5

tela = pygame.display.set_mode((largura, altura))
fonte_nome = pygame.font.SysFont('arial', 100, True, False)
fonte_Opc = pygame.font.SysFont('Arial', 40, False, False)
relogio = pygame.time.Clock()

cor_fundo = (255, 255, 255)

pygame.display.set_caption("Tela Inicial")

background = pygame.image.load("Fundo.jpg")
background = pygame.transform.smoothscale(background, (1280,720))

while True:
    relogio.tick(60)
    nome_do_jogo = f'Prove It'
    bot_Hist = f'Modo Historia'
    bot_Arcd = f'Modo Arcade'
    texto_jogo = fonte_nome.render(nome_do_jogo, True, (0, 0, 0))
    texto_Hist = fonte_Opc.render(bot_Hist, True, (255, 255, 255))
    texto_Arcd = fonte_Opc.render(bot_Arcd, True, (255, 255, 255))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if (x_Hist <= mouse_x <= x_Hist + largura_Opc and y_Hist <= mouse_y <= y_Hist + altura_Opc):
                    pygame.QUIT()
                    sys.exit()
                elif (x_Arcd <= mouse_x <= x_Arcd + largura_Opc and y_Arcd <= mouse_y <= y_Arcd + altura_Opc):
                    pygame.QUIT()
                    sys.exit()
        '''
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:
                x -= 10
        if teclas[pygame.K_d]:
                x += 10
        if teclas[pygame.K_s]:
                y += 10
        if teclas[pygame.K_w]:
                y -= 10'''
        
    tela.blit(background, (0,0))
    
    pygame.draw.rect(tela, (0, 0, 0), (x_Hist, y_Hist, largura_Opc, altura_Opc))
    pygame.draw.rect(tela, (0, 0, 0), (x_Arcd, y_Arcd, largura_Opc, altura_Opc))

    tela.blit(texto_jogo, (largura/2 - 180 , altura - 600))
    tela.blit(texto_Hist, (x_Hist + 2, y_Hist))
    tela.blit(texto_Arcd, (x_Arcd + 10, y_Arcd)) 

    pygame.display.flip()
