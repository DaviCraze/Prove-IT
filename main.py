import pygame
import sys
from Geratriz import *
from Utilitario import *
from Tela import *
import falas
import time


pygame.init()
arquivo_pontuação = "Dados/pontuação.txt"
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [
            pygame.image.load('Sprites/robot1.png'),
            pygame.image.load('Sprites/robot2.png'),
            pygame.image.load('Sprites/robot3.png'),
            pygame.image.load('Sprites/robot4.png'),
            pygame.image.load('Sprites/robot5.png'),
            pygame.image.load('Sprites/robot6.png')
        ]
        self.sprites_andando = [
            pygame.image.load('Sprites/personagem_andando1.png'),
            pygame.image.load('Sprites/personagem_andando2.png'),
            pygame.image.load('Sprites/personagem_andando3.png'),
            pygame.image.load('Sprites/personagem_andando4.png')
        ]
        self.sprites_vida = [
            pygame.image.load('Sprites/Vida1.png'),
            pygame.image.load('Sprites/Vida2.png'),
            pygame.image.load('Sprites/Vida3.png'),
            pygame.image.load('Sprites/Vida4.png'),
            pygame.image.load('Sprites/Vida5.png'),
            pygame.image.load('Sprites/Vida6.png')
        ]
        self.atual = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (28*3, 32*4))
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
            self.atual += 0.08
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (28*3, 32*4))

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
            self.image = pygame.transform.scale(self.image, (28*3, 32*4))
    
    def desenhar_vida(self, tela, Vida):
        if Vida > 0 and Vida <= len(self.sprites_vida):
            vida_sprite = self.sprites_vida[Vida - 1]
            vida_sprite = pygame.transform.scale(vida_sprite, (60, 100))
            tela.blit(vida_sprite,(20, 600))

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
fonte = "Better VCR 6.1.ttf"
tela = pygame.display.set_mode((largura, altura))
fonte_nome = pygame.font.Font(fonte, 80)
fonte_Opc = pygame.font.Font(fonte, 25)
fonte_dados = pygame.font.Font(fonte, 20)
fonte_desafios = pygame.font.Font(fonte, 15)
relogio = pygame.time.Clock()

pygame.display.set_caption("Prove IT")

logo = pygame.image.load("Imagens/Logo1.png")
logo_R = pygame.transform.scale(logo, (600,140))
background = pygame.image.load("Imagens/Tela_Fundo3.png")
background = pygame.transform.smoothscale(background, (1280, 720))
Tela_Menu = True
Tela_Loading = False
Tela_Perdeu = False
Tela_Loja = False
Tela_Ganhou = False
questão_gerada = False
Reiniciou = False
r1, g1, b1 = 0, 0, 0
r2, g2, b2 = 0, 0, 0
teclas = None
num_Sala = 1
dica_jogo = False
ultima_acao = 0
delay = 0.5
dados = Utilitario.carregar_dados("Dados/pontuação.json")
pontuação = dados.get("pontuação", 0)
itens = dados.get("itens", {"booster": 0, "dica": 0, "vida": 0})
primeira_vez_L = dados.get("primeira_vez_L", None)
errouprimeira = dados.get("errouprimeira", None)
primeira_vez_G = dados.get("primeira_vez_G", None)
jogo_bloqueado = False
while True:
    Vida = itens.get("vida", 0)
    tempo_atual = time.time()
    if Tela_Menu:
        Geratriz.gerar_menu(tela, background, largura, altura, largura_Opc, altura_Opc, fonte_nome, fonte_Opc, logo_R)
    teclas = pygame.key.get_pressed()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            if Vida < 3:
                itens["vida"] = 3
            dados = {"pontuação": pontuação, "itens": itens}
            Utilitario.salvar_dados(dados, "Dados/pontuação.json")
            pygame.QUIT()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if (x_Hist <= mouse_x <= x_Hist + largura_Opc and y_Hist <= mouse_y <= y_Hist + altura_Opc):
                    if pontuação >= 1:
                        Tela_Loja = not Tela_Loja
                        Tela_Menu = False
                    else:
                        Tela_Loading = not Tela_Loading
                        Tela_Menu = False
                elif (x_Arcd <= mouse_x <= x_Arcd + largura_Opc and y_Arcd <= mouse_y <= y_Arcd + altura_Opc):
                    Utilitario.salvar_pontuação(pontuação, arquivo_pontuação)
                    pygame.QUIT()
                    sys.exit()
    if Tela_Loja:
        b_continuar, b_dica, b_vida, b_booster, tex_dica, tex_booster, tex_vida = Geratriz.Tela_Loja(tela,background,largura,fonte_Opc,todas_as_sprites,teclas)
        falas_ativas = falas.cutscene_falas["boas_vindasL"]
        if primeira_vez_L:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                        falas_ativas.proximo()
                        ultima_acao = tempo_atual

            if not falas_ativas.acabou():
                Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_Opc, falas_ativas.mostrar_posicao())
                jogo_bloqueado = True
            else:
                jogo_bloqueado = False
            
            if jogo_bloqueado:
                pygame.display.flip()
                relogio.tick(60)
                continue 
            primeira_vez_L = False
            dados["primeira_vez_L"] = False
            Utilitario.salvar_dados(dados, "Dados/pontuação.json")
        Geratriz.gerar_dados(pontuação, num_Sala, Vida, tela, fonte_dados, dados.get("itens", {}).get("dica", 0), dados.get("itens", {}).get("booster", 0), personagem)
        if tex_dica.colliderect(personagem.rect):
            dica_info = "Dica, um otimo item para te ajudar na sua jornada.\nEste item te da uma dica de como resolver a questão"
            dica_preco = f'30 Pontos'
            como_usar = f'Aperte o botão 2 para usar a dica'
            linhas = dica_info.split("\n")
            y = 300
            for linha in linhas:
                dica_fonte, precod_fonte, fonte_usar = fonte_dados.render(linha, True, (0, 0, 0)), fonte_dados.render(dica_preco, True, (0,0,0)), fonte_dados.render(como_usar, True, (0,0,0))
                tela.blit(dica_fonte, (300, y))
                tela.blit(precod_fonte, (580, 360))
                tela.blit(fonte_usar, (410, 450))
                y += 20
        elif tex_booster.colliderect(personagem.rect):
            booster_info = "Booster, um item que te deixa ELETRIZANTE!!\nEle fará com que você passe de proxima fase sem dificuldade"
            booster_preco = f'80 Pontos'
            comob_usar = f'Aperte o botão 1 para usar a dica'
            linhas = booster_info.split("\n")
            y = 300
            for linha in linhas:
                booster_fonte, precob_fonte, comob_fonte = fonte_dados.render(linha, True, (0, 0, 0)), fonte_dados.render(booster_preco, True, (0,0,0)), fonte_dados.render(comob_usar, True,(0,0,0))
                tela.blit(booster_fonte, (300, y))
                tela.blit(precob_fonte, (580, 360))
                tela.blit(comob_fonte, (410, 450))
                y += 20
        elif tex_vida.colliderect(personagem.rect):
            vida_info = "Vida, uma fonte incrivel de energia, ah como eu gosto dela...\nAumenta sua quantidade de vida, podendo errar mais questões"
            vida_preco = f'100 Pontos'
            linhas = vida_info.split("\n")
            y = 300
            for linha in linhas:
                vida_fonte, precov_fonte = fonte_dados.render(linha, True, (0, 0, 0)), fonte_dados.render(vida_preco, True, (0,0,0))
                tela.blit(vida_fonte, (270, y))
                tela.blit(precov_fonte, (550, 360))
                y += 20
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
            if b_dica.colliderect(personagem.rect) and pontuação >= 30 and tempo_atual - ultima_acao > delay:
                itens["dica"] +=1
                pontuação -= 30
                ultima_acao = tempo_atual
            elif b_booster.colliderect(personagem.rect) and pontuação >= 80 and tempo_atual - ultima_acao > delay:
                itens["booster"] += 1
                pontuação -= 80
                ultima_acao = tempo_atual
            elif b_vida.colliderect(personagem.rect) and pontuação >= 100 and tempo_atual - ultima_acao > delay:
                if Vida < 6:
                    itens["vida"] += 1
                    Vida += 1
                    pontuação -= 100
                    ultima_acao = tempo_atual
                elif Vida > 6:
                    continue
            if b_continuar.colliderect(personagem.rect):
                Tela_Loading = not Tela_Loading
                Tela_Loja = not Tela_Loja
    if Tela_Loading:
        if num_Sala % 10 == 0 and Vida > 0:
            if not questão_gerada or not Reiniciou:
                personagem.rect.x = 50
                personagem.rect.y = 550
                r1, g1, b1 = Utilitario.var_aleatoria(3,0,255)
                r2, g2, b2 = Utilitario.var_aleatoria(3,0,255)
                questão_gerada = True
                Reiniciou = True
            porta_S, porta_N, respostas_d = Geratriz.gerar_desafio(fonte_desafios,tela,teclas, r1, g1, b1, r2, g2, b2,todas_as_sprites, fonte_Opc)
            Geratriz.gerar_dados(pontuação, num_Sala, Vida, tela, fonte_dados, dados.get("itens", {}).get("dica", 0), dados.get("itens", {}).get("booster", 0), personagem)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                resultado = None
                if porta_S.colliderect(personagem.rect):
                    if respostas_d[0][1] == "correta":
                        resultado = "avançar"
                    else:
                        resultado = "perdeu"
                elif porta_N.colliderect(personagem.rect):
                    if respostas_d[1][1] == "correta":
                        resultado = "avançar"
                    else:
                        resultado = "perdeu"
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação += 50
                    dica_jogo = False
                elif resultado == "perdeu":
                    num_Sala += 1
                    itens["vida"] -= 1
                    Vida -= 1
                    questão_gerada = False
                    dica_jogo = False
        elif num_Sala <= 100 and Vida > 0:
            
            if not questão_gerada or not Reiniciou:
                personagem.rect.x = 50
                personagem.rect.y = 550
                questão, resposta, respostaf1, respostaf2, escolher, dica_t = Geratriz.gerar_questao(fonte_dados)
                largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2 = Geratriz.gerar_texto(questão, resposta, respostaf1, respostaf2, fonte_Opc)
                r1, g1, b1 = Utilitario.var_aleatoria(3,0,255)
                r2, g2, b2 = Utilitario.var_aleatoria(3,0,255)
                port_1, port_2, port_3, respostas = Geratriz.sala_nova(largura, text_resV, text_resF1, text_resF2)
                questão_gerada = True
                Reiniciou = True
                if errouprimeira:
                    falas_ativas = falas.cutscene_falas["erro1"]
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                                falas_ativas.proximo()
                                ultima_acao = tempo_atual
                    if not falas_ativas.acabou():
                        Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_Opc, falas_ativas.mostrar_posicao())
                        jogo_bloqueado = True
                    else:
                        jogo_bloqueado = False
                    
                    if jogo_bloqueado:
                        pygame.display.flip()
                        relogio.tick(60)
                        continue
                    errouprimeira = False
                    dados["errouprimeira"] = False
                    Utilitario.salvar_dados(dados, "Dados/pontuação.json")
            Geratriz.gerar_jogo(tela,teclas, r1, g1, b1, r2, g2, b2, background, largura, largura_quest, largura_text, largura_textF1, largura_textF2, port_1, port_2, port_3, pos_port_y, respostas, text_quest, todas_as_sprites)
            falas_ativas = falas.cutscene_falas["glados1encontro"]
            if primeira_vez_G:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                            falas_ativas.proximo()
                            ultima_acao = tempo_atual

                if not falas_ativas.acabou():
                    Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_Opc, falas_ativas.mostrar_posicao())
                    jogo_bloqueado = True
                else:
                    jogo_bloqueado = False
                
                if jogo_bloqueado:
                    pygame.display.flip()
                    relogio.tick(60)
                    continue
                primeira_vez_G = False
                dados["primeira_vez_L"] = False
                Utilitario.salvar_dados(dados, "Dados/pontuação.json")
                
            Geratriz.gerar_dados(pontuação, num_Sala, Vida, tela, fonte_dados, dados.get("itens", {}).get("dica", 0), dados.get("itens", {}).get("booster", 0), personagem)
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                pygame.event.get(personagem.rect.x, personagem.rect.y)
                
                resultado = Utilitario.verificar_escolha(port_1, pos_port_y, largura_text, respostas[0], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    dica_jogo = False
                elif resultado =="perdeu":
                    num_Sala += 1
                    itens["vida"] -= 1
                    Vida -= 1
                    questão_gerada = False
                    dica_jogo = False
                resultado = Utilitario.verificar_escolha(port_2, pos_port_y, largura_textF1, respostas[1], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    dica_jogo = False
                elif resultado =="perdeu":
                    num_Sala += 1
                    itens["vida"] -= 1
                    Vida -= 1
                    questão_gerada = False
                    dica_jogo = False
                resultado = Utilitario.verificar_escolha(port_3, pos_port_y, largura_textF2, respostas[2], personagem.rect.x, personagem.rect.y)
                if resultado == "avançar":
                    num_Sala += 1
                    questão_gerada = False
                    pontuação_r = Utilitario.pontuação_respostas(escolher)
                    pontuação += pontuação_r
                    dica_jogo = False
                elif resultado =="perdeu":
                    num_Sala += 1
                    itens["vida"] -= 1
                    Vida -= 1
                    questão_gerada = False
                    dica_jogo = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and tempo_atual - ultima_acao > delay:
            if itens["booster"] >= 1:
                itens["booster"] -= 1
                num_Sala += 1
                questão_gerada = False
                dica_jogo = False
                ultima_acao = tempo_atual
        elif keys[pygame.K_2] and tempo_atual - ultima_acao > delay:
            if itens["dica"] >= 1:
                itens["dica"] -= 1
                dica_jogo = True
                ultima_acao = tempo_atual
        if dica_jogo:
            if escolher == 'Linear':
                tela.blit(dica_t,(250,330))
            elif escolher == 'Divisão':
                tela.blit(dica_t,(250,330))
            elif escolher == "Quadratica":
                tela.blit(dica_t,(150,330))

        elif num_Sala == 101 and Vida > 0:
            Tela_Ganhou = not Tela_Ganhou
            Tela_Loading = not Tela_Loading
            dica_jogo = False

        elif Vida == 0:
            Tela_Perdeu = not Tela_Perdeu
            Tela_Loading = not Tela_Loading
            dica_jogo = False
    if Tela_Ganhou:
        botao_inicial_G = Geratriz.Tela_Ganhou(tela, background, fonte_Opc)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if botao_inicial_G.collidepoint(evento.pos):
                    personagem.rect.x = 50
                    personagem.rect.y = 550
                    num_Sala = 1
                    itens["vida"] = 3
                    Reiniciou = not Reiniciou
                    Tela_Menu = True
                    Tela_Ganhou = False
                    Tela_Loja = False
                    dica_jogo = False
    if Tela_Perdeu:
        botao_inicial_P, botao_reiniciar = Geratriz.tela_perdeu(tela, background, largura, fonte_Opc)
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_x, mouse_y = evento.pos
                if botao_inicial_P.collidepoint(evento.pos):
                    personagem.rect.x = 50
                    personagem.rect.y = 550
                    num_Sala = 1
                    itens["vida"] = 3
                    Reiniciou = not Reiniciou
                    Tela_Menu = not Tela_Menu
                    Tela_Perdeu = not Tela_Perdeu
                    dica_jogo = False
                elif botao_reiniciar.collidepoint(evento.pos):
                    personagem.rect.x = 50
                    personagem.rect.y = 550
                    num_Sala = 1
                    itens["vida"] = 3
                    Reiniciou = not Reiniciou
                    Tela_Perdeu, Tela_Loja = not Tela_Perdeu, not Tela_Loja
                    dica_jogo = False
    relogio.tick(60)
    pygame.display.flip()
