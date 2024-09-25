import pygame
import sys
import random

pygame.init()

musica_fundo = pygame.mixer.music.load("Musicas/12 - Sunken Depths.mp3")
pygame.mixer.music.play(-1)

Num_Sala = 0
questoes = [f'2x - 4 = 0', f'90 / 2 = x',f'4x² + 4x +1 = 0']
respostas_v = [f'x = 2', f'x = 45', f'(2x + 1)²']
x = 0
largura = 1280
altura = 720

x_Pers = 50
y_Pers = 600

largura_Opc = 250
altura_Opc = 50

x_Hist = largura/2 - largura_Opc/2
y_Hist = altura/2

x_Arcd = largura/2 - largura_Opc/2
y_Arcd = altura/1.5

pos_port1_x = largura/1.5
pos_port2_x = largura/2
pos_port3_x = largura/3
pos_port_y = 397

tela = pygame.display.set_mode((largura, altura))
fonte_nome = pygame.font.SysFont('arial', 100, True, False)
fonte_Opc = pygame.font.SysFont('Arial', 40, False, False)
relogio = pygame.time.Clock()

pygame.display.set_caption("Prove IT")

background = pygame.image.load("Imagens/Fundo.jpg")
background = pygame.transform.smoothscale(background, (1280, 720))

Tela_Loading = False

while True:
    relogio.tick(60)
    nome_do_jogo = f'Prove It'
    bot_Hist = f'Modo Historia'
    bot_Arcd = f'Modo Arcade'
    texto_jogo = fonte_nome.render(nome_do_jogo, True, (0, 0, 0))
    texto_Hist = fonte_Opc.render(bot_Hist, True, (255, 255, 255))
    texto_Arcd = fonte_Opc.render(bot_Arcd, True, (255, 255, 255))

    tela.blit(background, (0, 0))

    pygame.draw.rect(tela, (0, 0, 0), (x_Hist, y_Hist, largura_Opc, altura_Opc))
    pygame.draw.rect(tela, (0, 0, 0), (x_Arcd, y_Arcd, largura_Opc, altura_Opc))

    tela.blit(texto_jogo, (largura/2 - 180, altura - 600))
    tela.blit(texto_Hist, (x_Hist + 2, y_Hist))
    tela.blit(texto_Arcd, (x_Arcd + 10, y_Arcd))

    teclas = pygame.key.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if teclas[pygame.K_a]:
            x_Pers -= 15
        if teclas[pygame.K_d]:
            x_Pers += 15
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if (x_Hist <= mouse_x <= x_Hist + largura_Opc and y_Hist <= mouse_y <= y_Hist + altura_Opc):
                    Tela_Loading = not Tela_Loading
                    numeros = list(range(0,9))
                    numero_excluir = 2
                    numeros.remove(numero_excluir)
                    resp_alea1 = random.choice(numeros)
                    resp_alea2 = random.choice(numeros)
                    resp_alea3 = random.randint(0,9)
                    resp_alea4 = random.randint(0,9)
                elif (x_Arcd <= mouse_x <= x_Arcd + largura_Opc and y_Arcd <= mouse_y <= y_Arcd + altura_Opc):
                    pygame.QUIT()
                    sys.exit()

    if Tela_Loading:

        respostas_f1 = [f"x ={resp_alea1}",f"x ={resp_alea1 + 30}",f"({resp_alea1}x + {resp_alea2})²"]
        respostas_f2 = [f"x ={resp_alea2}",f"x ={resp_alea2 + 30}",f"({resp_alea3}x + {resp_alea4})²"]
        text_quest = fonte_Opc.render(questoes[Num_Sala], True, (0, 0, 0))
        text_resV = fonte_Opc.render(respostas_v[Num_Sala], True, (0, 0, 0))
        text_res2 = fonte_Opc.render(respostas_f1[Num_Sala], True, (0, 0, 0,))
        text_res3 = fonte_Opc.render(respostas_f2[Num_Sala], True, (0, 0, 0,))

        largura_quest, altura_quest = text_quest.get_size()
        largura_text, altura_text = text_resV.get_size()
        largura_textF2, altura_textF2 = text_res2.get_size()
        largura_textF3, altura_textF3 = text_res3.get_size()
        
        tela.blit(background, (0, 0))

        pygame.draw.rect(tela, (0, 0, 0), (largura/1.85 - 100, 200, largura_quest + 50, 80))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.818 - 100, 210, largura_quest + 25, 60))

        tela.blit(text_quest, (largura/1.8 - 100, 215))
        

        pygame.draw.rect(tela, (0, 0, 0), (pos_port1_x, pos_port_y, largura_text + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.478, 407, largura_text + 25, 250))
        pygame.draw.rect(tela, (0, 0, 0), (pos_port2_x, pos_port_y, largura_textF2 + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.96, 407, largura_textF2 + 25, 240))
        pygame.draw.rect(tela, (0, 0, 0), (pos_port3_x, pos_port_y, largura_textF3 + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (largura/2.92, 407, largura_textF3 + 25, 240))
        pygame.draw.rect(tela, (0, 0, 0), (x_Pers, y_Pers, 50, 50))
        
        tela.blit(text_resV, (pos_port1_x + 20, 420)) 
        tela.blit(text_res2, (pos_port2_x + 20, 420))
        tela.blit(text_res3, (pos_port3_x + 20, 420))  
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            pygame.event.get(x_Pers, y_Pers)
            if (pos_port1_x <= x_Pers <= pos_port1_x + 125 and pos_port_y <= y_Pers <= pos_port_y + 250):
                Num_Sala = (Num_Sala + 1) % len(questoes)
                resp_alea1 = random.randint(0,9)
                resp_alea2 = random.randint(0,9)
                resp_alea3 = random.randint(0,9)
                resp_alea4 = random.randint(0,9)
                x_Pers = 50
                y_Pers = 600
            elif (pos_port2_x <= x_Pers <= pos_port2_x + largura_textF2 + 50 and pos_port_y <= y_Pers <= pos_port_y + 250):
                tela.blit(background, (0, 0))
                perder = f'Você Perdeu...'
                text_perder = fonte_Opc.render(perder, True, (0, 0, 0))
                largura_perder, altura_perder = text_perder.get_size()
                pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 150, 200, largura_perder + 50, altura_perder + 20))
                pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 - 150, 210, largura_perder + 25, altura_perder))
                tela.blit(text_perder, (largura/1.92 - 150, 210))
    pygame.display.flip()
