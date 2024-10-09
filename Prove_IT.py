import pygame
import sys
import random
import os


pygame.init()

x_Pers = 100
y_Pers = 500
#musica_fundo = pygame.mixer.music.load("Musicas/12 - Sunken Depths.mp3")
#pygame.mixer.music.play(-1)
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        global x_Pers, y_Pers
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
        self.rect.topleft = (x_Pers, 550)

        self.animar = False
        self.velocidade = 5

    def andar(self):
        self.animar = True
    
    def update(self, teclas):
        global x_Pers, y_Pers
        self.atual += 0.02
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (32*4, 32*4))

        if teclas[pygame.K_a]:
            self.rect.x -= self.velocidade
            if x_Pers < 0:
                x_Pers = 0
        if teclas[pygame.K_d]:
            self.rect.x += self.velocidade
            if x_Pers + self.rect.width > largura:
                x_Pers = largura - self.rect.width
        
        self.rect.topleft = (x_Pers, 550)

todas_as_sprites = pygame.sprite.Group()
personagem = Sprite()
todas_as_sprites.add(personagem)

arquivo_pontuação = "Dados/pontuação.txt"
def carregar_pontuação():
    if os.path.exists(arquivo_pontuação):
        with open(arquivo_pontuação, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    else:
        return 0
def salvar_pontuação(pontuação):
    with open(arquivo_pontuação, "w") as f:
        f.write(str(pontuação))

def gerar_questao():
    tipos_questoes = ['Linear', 'Divisão', 'Quadratica']
    escolher = random.choice(tipos_questoes)
    questão = None
    resposta, respostaf1, respostaf2 = None, None, None
    if escolher == 'Linear':
        a, b = random.randint(0,9), random.randint(0,9)
        questão = f'2 x {a} - {b} = 0'
        resposta = f'x = {(2*a) - b}'
        c, d = random.randint(0,9), random.randint(0,9)
        respostaf1 = f'x = {(2*c) - d}'
        while respostaf1 == resposta:
            c, d = random.randint(0,9), random.randint(0,9)
            respostaf1 = f'x = {(2 * c) - d}'
        e, f = random.randint(0,9), random.randint(0,9)
        respostaf2 = f'x = {(2 * e) - f}'
        while respostaf2 == respostaf1 or respostaf2 == resposta:
            e, f = random.randint(0,9), random.randint(0,9)
            respostaf2 = f'x = {(2 * e) - f}'
    elif escolher == 'Divisão':
        a, b = random.randint(10,100), random.randint(1,10)
        questão = f'{a} / {b} = x'
        resposta = f'x = {a / b:.2f}'
        c, d = random.randint(10,100), random.randint(1,10)
        respostaf1 = f'x = {c / d:.2f}'
        while respostaf1 == resposta:
            c, d = random.randint(10,100), random.randint(1,10)
            respostaf1 = f'x = {c / d:.2f}'
        e, f = random.randint(1,100), random.randint(1,10)
        respostaf2 = f'x = {e / f:.2f}'
        while respostaf2 == respostaf1 or respostaf2 == resposta:
            e, f = random.randint(1,100), random.randint(1,10)
            respostaf2 = f'x = {e / f:.2f}'
    else:
        a,b = random.randint(1,9), random.randint(1,9),
        questão = f'{a ** 2}x² + {2 * a * b}x + {b ** 2}'
        resposta = f'({a}x + {b})²'
        c,d = random.randint(1,9), random.randint(1,9)
        respostaf1 = f'({c}x + {d})²'
        while respostaf1 == resposta:
            c,d = random.randint(1,9), random.randint(1,9)
            respostaf1 = f'({c}x + {d})²'
        e, f = random.randint(1,9), random.randint(1,9)
        respostaf2 = f'({e}x + {f})²'
        while respostaf2 == resposta or respostaf2 == respostaf1:
            e, f = random.randint(1,9), random.randint(1,9)
            respostaf2 = f'({e}x + {f})²'
    return questão, resposta, respostaf1, respostaf2, escolher

def gerar_texto(questão, resposta, respostaf1, respostaf2):
    text_quest = fonte_Opc.render(questão, True, (0, 0, 0))
    text_resV = fonte_Opc.render(resposta, True, (0, 0, 0))
    text_resF1 = fonte_Opc.render(respostaf1, True, (0, 0, 0))
    text_resF2 = fonte_Opc.render(respostaf2, True, (0, 0, 0))
    largura_quest, altura_quest = text_quest.get_size()
    largura_text, altura_text = text_resV.get_size()
    largura_textF1, altura_textF1 = text_resF1.get_size()
    largura_textF2, altura_textF2 = text_resF2.get_size() 
    return largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2

def gerar_menu():
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

def sala_nova():
    lista_de_portas = [pos_port1_x, pos_port2_x, pos_port3_x]
    port_1 = random.choice(lista_de_portas)
    lista_de_portas.remove(port_1)
    port_2 = random.choice(lista_de_portas)
    lista_de_portas.remove(port_2)
    port_3 = lista_de_portas[0]

    respostas = [(text_resV, "correta"), (text_resF1, "errada"), (text_resF2, "errada")]
    random.shuffle(respostas)

    return port_1, port_2, port_3, respostas

def gerar_jogo(r1, g1, b1, r2, g2, b2, port_1, port_2, port_3, respostas):
    tela.blit(background, (0, 0))

    pygame.draw.rect(tela, (r1, g1, b1), (0, 640, 1280, 88))
    pygame.draw.rect(tela, (r2, g2, b2), (0, 0, 1280, 640))

    pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 100, 200, largura_quest + 50, 80))
    pygame.draw.rect(tela, (255, 255, 255), (largura/2 - 88.5, 210, largura_quest + 25, 60))

    tela.blit(text_quest, (largura/2 - 80, 215))
    
    pygame.draw.rect(tela, (0, 0, 0), (pos_port1_x, pos_port_y, largura_text + 50, 250))
    pygame.draw.rect(tela, (255, 255, 255), (pos_port1_x + 13, 407, largura_text + 25, 240))
    pygame.draw.rect(tela, (0, 0, 0), (pos_port2_x, pos_port_y, largura_textF1 + 50, 250))
    pygame.draw.rect(tela, (255, 255, 255), (pos_port2_x + 13, 407, largura_textF1 + 25, 240))
    pygame.draw.rect(tela, (0, 0, 0), (pos_port3_x, pos_port_y, largura_textF2 + 50, 250))
    pygame.draw.rect(tela, (255, 255, 255), (pos_port3_x + 13, 407, largura_textF2 + 25, 240))

    todas_as_sprites.draw(tela)
    todas_as_sprites.update(teclas)
    #pygame.draw.rect(tela, (0, 0, 0), (x_Pers, y_Pers, 50, 50))
    tela.blit(respostas[0][0], (port_1 + 20, 420)) 
    tela.blit(respostas[1][0], (port_2 + 20, 420))
    tela.blit(respostas[2][0], (port_3 + 20, 420))

def verificar_escolha(porta_x, porta_y, largura_porta, respostas, jogador_x, jogador_y):
    if porta_x <= jogador_x <= porta_x + largura_porta and porta_y <= jogador_y <= porta_y + 250:
        if respostas[1] == "correta":
            return "avançar"
        else:
            return "perdeu"
    return None

def tela_perdeu():
    tela.blit(background, (0, 0))
    perder = f'Você Perdeu...'
    tela_inicial = f'Tela Inicial'
    reiniciar = f'Reiniciar'
    text_inicial = fonte_Opc.render(tela_inicial, True, (0, 0, 0))
    text_reiniciar = fonte_Opc.render(reiniciar, True, (0, 0, 0))
    text_perder = fonte_Opc.render(perder, True, (0, 0, 0))
    largura_inicial, altura_inicial = text_inicial.get_size()
    largura_reiniciar, altura_reiniciar = text_reiniciar.get_size()
    largura_perder, altura_perder = text_perder.get_size()
    pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 140, 200, largura_perder + 50, altura_perder + 20))
    pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 - 140, 210, largura_perder + 25, altura_perder))
    botao_inicial = pygame.draw.rect(tela, (0, 0, 0), (largura/2 + 50, 350, largura_inicial + 50, altura_inicial + 20))
    pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 + 50, 360, largura_inicial + 25, altura_inicial))
    botao_reiniciar = pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 250, 350, largura_reiniciar + 68, altura_reiniciar + 20))
    pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 - 250, 360, largura_reiniciar + 40, altura_reiniciar))

    tela.blit(text_perder, (largura/1.92 - 140, 210))
    tela.blit(text_inicial, (largura/1.92 + 50, 360))
    tela.blit(text_reiniciar, (largura/1.92 - 250, 360))
    return largura_inicial, altura_inicial, largura_reiniciar, altura_reiniciar, botao_inicial, botao_reiniciar

def pontuação_respostas(escolher):
    if escolher == 'Linear':
        return 2
    elif escolher == 'Divisão':
        return 1
    elif escolher == 'Quadratica':
        return 4
    return pontuação_r
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
num_Sala = 0
pontuação = carregar_pontuação()
Vida = 3
while True:
    if Tela_Menu:
        gerar_menu()
    teclas = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvar_pontuação(pontuação)
            pygame.QUIT()
            sys.exit()
        if teclas[pygame.K_a]:
            x_Pers -= 10
            if x_Pers < 0:
                x_Pers = 0
        if teclas[pygame.K_d]:
            x_Pers += 10
            if x_Pers + personagem.rect.width > largura:
                x_Pers = largura - personagem.rect.width
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
                x_Pers = 50
                y_Pers = 600
                questão, resposta, respostaf1, respostaf2, escolher = gerar_questao()
                largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2 = gerar_texto(questão, resposta, respostaf1, respostaf2)
                r1, g1, b1 = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                r2, g2, b2 = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                port_1, port_2, port_3, respostas = sala_nova()
                questão_gerada = True
                Reiniciou = True
            
            gerar_jogo(r1, g1, b1, r2, g2, b2, port_1, port_2, port_3, respostas)
            ponto_texto = f'Pontos = {pontuação}'
            ponto_fonte = fonte_Opc.render(ponto_texto, True, (0, 0, 0))
            tela.blit(ponto_fonte, (50, 100))
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                pygame.event.get(x_Pers, y_Pers)
                
                resultado = verificar_escolha(port_1, pos_port_y, largura_text, respostas[0], x_Pers, y_Pers)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
                resultado = verificar_escolha(port_2, pos_port_y, largura_textF1, respostas[1], x_Pers, y_Pers)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
                resultado = verificar_escolha(port_3, pos_port_y, largura_textF2, respostas[2], x_Pers, y_Pers)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    print(num_Sala)
                elif resultado =="perdeu":
                    num_Sala += 1
                    Vida -= 1
                    questão_gerada = False
        elif Vida == 0:
            Tela_Perdeu = not Tela_Perdeu
            Tela_Loading = not Tela_Loading

    if Tela_Perdeu:
        largura_inicial, altura_inicial, largura_reiniciar, altura_reiniciar, botao_inicial, botao_reiniciar = tela_perdeu()
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
