import pygame
import sys
from Geratriz import *
from Utilitario import *


pygame.init()


arquivo_pontuação = "Dados/pontuação.txt"
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites_andando = []
        self.sprites.append(pygame.image.load('Sprites/personagem_idle1.png'))
        self.sprites.append(pygame.image.load('Sprites/personagem_idle2.png'))
        self.sprites.append(pygame.image.load('Sprites/personagem_idle3.png'))
        self.sprites.append(pygame.image.load('Sprites/personagem_idle4.png'))
        self.sprites_andando.append(pygame.image.load('Sprites/personagem_andando1.png'))
        self.sprites_andando.append(pygame.image.load('Sprites/personagem_andando2.png'))
        self.sprites_andando.append(pygame.image.load('Sprites/personagem_andando3.png'))
        self.sprites_andando.append(pygame.image.load('Sprites/personagem_andando4.png'))
        self.atual = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*4, 32*4))
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 550)

        self.andando = False
        self.velocidade = 5
        self.direção = 'direita'
    def update(self, teclas):
        if teclas[pygame.K_a] or teclas[pygame.K_d]:
            self.andando = True
        else:
            self.andando = False

        if self.andando:
            self.atual += 0.10
            if self.atual >= len(self.sprites_andando):
                self.atual = 0
            self.image = self.sprites_andando[int(self.atual)]
        else:
            self.atual += 0.03
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (32*4, 32*4))

        if teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
            if self.rect.x < 0:
                self.rect.x = 0
            self.direção = 'esquerda'

        if teclas[pygame.K_d]:
            self.rect.x += self.velocidade
            if self.rect.x + self.rect.width > largura:
                self.rect.x = largura - self.rect.width
            self.direção = 'direita'
        
        if self.direção == 'esquerda':
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = pygame.transform.scale(self.image, (32*4, 32*4))

todas_as_sprites = pygame.sprite.Group()
personagem = Sprite()
todas_as_sprites.add(personagem)

x = 0
largura = 1280
altura = 720

largura_Opc = 250
altura_Opc = 50

x_Hist = largura/2 - largura_Opc/2
y_Hist = altura/2

x_Arcd = largura/2 - largura_Opc/2
y_Arcd = altura/1.5

pos_port1_x = largura/4
pos_port2_x = pos_port1_x + 300
pos_port3_x = pos_port2_x + 300

pos_port_y = 397

tela = pygame.display.set_mode((largura, altura))
fonte_nome = pygame.font.SysFont('arial', 100, True, False)
fonte_Opc = pygame.font.SysFont('Arial', 40, False, False)
relogio = pygame.time.Clock()

pygame.display.set_caption("Prove IT")

background = pygame.image.load("Imagens/Tela_Fundo3.png")
background = pygame.transform.smoothscale(background, (1280, 720))
Tela_Menu = True
Tela_Loading = False
Tela_Perdeu = False
questão_gerada = False
Reiniciou = False
r1, g1, b1 = 0, 0, 0
r2, g2, b2 = 0, 0, 0
teclas = None
num_Sala = 0
pontuação = Utilitario.carregar_pontuação(arquivo_pontuação)
Vida = 3
while True:
    if Tela_Menu:
        Geratriz.gerar_menu(tela, background, largura, altura, largura_Opc, altura_Opc, fonte_nome, fonte_Opc)
    teclas = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Utilitario.salvar_pontuação(pontuação, arquivo_pontuação)
            pygame.QUIT()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if (x_Hist <= mouse_x <= x_Hist + largura_Opc and y_Hist <= mouse_y <= y_Hist + altura_Opc):
                    Tela_Loading = not Tela_Loading
                    Tela_Menu = not Tela_Menu
                elif (x_Arcd <= mouse_x <= x_Arcd + largura_Opc and y_Arcd <= mouse_y <= y_Arcd + altura_Opc):
                    pygame.QUIT()
                    sys.exit()
    if Tela_Loading:
        if num_Sala <= 100 and Vida > 0:
            if not questão_gerada or not Reiniciou:
                personagem.rect.x = 50
                personagem.rect.y = 550
                questão, resposta, respostaf1, respostaf2, escolher = Geratriz.gerar_questao()
                largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2 = Geratriz.gerar_texto(questão, resposta, respostaf1, respostaf2, fonte_Opc)
                r1, g1, b1 = Utilitario.var_aleatoria(3,0,255)
                r2, g2, b2 = Utilitario.var_aleatoria(3,0,255)
                port_1, port_2, port_3, respostas = Geratriz.sala_nova(largura, text_resV, text_resF1, text_resF2)
                questão_gerada = True
                Reiniciou = True
            
            Geratriz.gerar_jogo(tela,teclas, r1, g1, b1, r2, g2, b2, background, largura, largura_quest, largura_text, largura_textF1, largura_textF2, port_1, port_2, port_3, pos_port_y, respostas, text_quest, todas_as_sprites)
            ponto_texto = f'Pontos = {pontuação}'
            vida_texto = f'Vida = {Vida}'
            ponto_fonte = fonte_Opc.render(ponto_texto, True, (0, 0, 0))
            vida_fonte = fonte_Opc.render(vida_texto, True, (0, 0, 0))
            tela.blit(ponto_fonte, (50, 50))
            tela.blit(vida_fonte, (50, 100))
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                pygame.event.get(personagem.rect.x, personagem.rect.y)
                
                resultado = Utilitario.verificar_escolha(port_1, pos_port_y, largura_text, respostas[0], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
                resultado = Utilitario.verificar_escolha(port_2, pos_port_y, largura_textF1, respostas[1], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
                resultado = Utilitario.verificar_escolha(port_3, pos_port_y, largura_textF2, respostas[2], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
        elif num_Sala == 101 and Vida > 0:
            botao_inicial = Geratriz.Tela_Ganhou(tela, background, largura, fonte_Opc)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    mouse_x, mouse_y = evento.pos
                    if botao_inicial.collidepoint(evento.pos):
                        Tela_Menu = not Tela_Menu
                        Tela_Loading = not Tela_Loading
        elif Vida == 0:
            Tela_Perdeu = not Tela_Perdeu
            Tela_Loading = not Tela_Loading
            
    if Tela_Perdeu:
        botao_inicial, botao_reiniciar = Geratriz.tela_perdeu(tela, background, largura, fonte_Opc)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if botao_inicial.collidepoint(evento.pos):
                    Vida = 3
                    Reiniciou = not Reiniciou
                    Tela_Menu = not Tela_Menu
                    Tela_Perdeu = not Tela_Perdeu
                elif botao_reiniciar.collidepoint(evento.pos):
                    Vida = 3
                    Reiniciou = not Reiniciou
                    Tela_Perdeu, Tela_Loading = not Tela_Perdeu, not Tela_Loading
    relogio.tick(60)
    pygame.display.flip()
