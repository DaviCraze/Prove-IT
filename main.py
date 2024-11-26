import pygame
import sys
from Geratriz import *
from Utilitario import *
import falas
import time

pygame.init()

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
efeito_acerto = pygame.mixer.Sound("Musicas/Musicas/acerto.wav")
efeito_erro = pygame.mixer.Sound("Musicas/Musicas/erro.wav")
efeito_AVA = pygame.mixer.Sound("Musicas/Musicas/AVA.wav")
efeito_LOJISTA = pygame.mixer.Sound("Musicas/Musicas/LOJISTA.wav")
arquivo_pontuação = "Dados/Dados/pontuação.json"
trilha_loja = "Musicas/Musicas/Loja.mp3"
trilha_jogo = "Musicas/Musicas/Jogo.mp3"
musica_atual = None
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = [pygame.image.load(f'Sprites/Sprites/robotidle{i}.png') for i in range(1,11)]
        self.sprites_andando = [pygame.image.load(f'Sprites/Sprites/robotWalk{i}.png') for i in range(1,16)]
        self.sprites_vida = [pygame.image.load(f'Sprites/Sprites/Vida{i}.png') for i in range(1, 7)]
        self.sprites_jogo = [pygame.image.load(f'Sprites/Sprites/portasOverlay{i}.png') for i in range(1,4)]
        self.sprites_desafio = [pygame.image.load(f'Sprites/Sprites/2portas{i}.png') for i in range(1,4)]
        self.sprites_hud = [pygame.image.load(f'Sprites/Sprites/ui{i}.png') for i in range(1,4)]
        self.sprites_dialogo_AVA = [pygame.image.load(f'Sprites/Sprites/AVAdiag{i}.png') for i in range(1,17)]
        self.sprites_loja = [pygame.image.load(f'Sprites/Sprites/ShopOverlay{i}.png') for i in range(1,7)]
        self.sprites_lojista = [pygame.image.load(f'Sprites/Sprites/eyes{i}.png') for i in range(1,11)]
        self.sprites_dia_LOJ = [pygame.image.load(f'Sprites/Sprites/ShopDiag{i}.png') for i in range(1,13)]

        self.atual_personagem = 0
        self.atual_jogo = 0
        self.atual_hud = 0
        self.atual_dia_AVA = 0
        self.atual_dia_LOJ = 0
        self.tempo_anterior = time.time()
        self.delay_entre_frames = 0.1
        self.atual_loja = 0
        self.atual_lojista = 0

        self.image = self.sprites[self.atual_personagem]
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
            self.atual_personagem += 0.10
            if self.atual_personagem >= len(self.sprites_andando):
                self.atual_personagem = 0
            self.image = self.sprites_andando[int(self.atual_personagem)]
        else:
            self.atual_personagem += 0.08
            if self.atual_personagem >= len(self.sprites):
                self.atual_personagem = 0
            self.image = self.sprites[int(self.atual_personagem)]

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

    def desenhar_jogo(self, tela):
        tempo_atual = time.time()
        if tempo_atual - self.tempo_anterior > self.delay_entre_frames:
            self.atual_jogo += 1
            self.tempo_anterior = tempo_atual

        if self.atual_jogo >= len(self.sprites_jogo):
            self.atual_jogo = 0
        
        jogo_sprite = self.sprites_jogo[int(self.atual_jogo)]
        jogo_sprite = pygame.transform.scale(jogo_sprite, (1280, 720))
        tela.blit(jogo_sprite, (0, 0))
    
    def desenhar_jogo_desafio(self, tela):
        tempo_atual = time.time()
        if tempo_atual - self.tempo_anterior > self.delay_entre_frames:
            self.atual_jogo += 1
            self.tempo_anterior = tempo_atual

        if self.atual_jogo >= len(self.sprites_desafio):
            self.atual_jogo = 0
        
        jogo_sprite = self.sprites_desafio[int(self.atual_jogo)]
        jogo_sprite = pygame.transform.scale(jogo_sprite, (1280, 720))
        tela.blit(jogo_sprite, (0, 0))
    
    def desenhar_hud(self, tela):
        self.atual_hud += 0.10
        if self.atual_hud >= len(self.sprites_hud):
            self.atual_hud = 0
        hud_sprite = self.sprites_hud[int(self.atual_hud)]
        tela.blit(hud_sprite,(25,25))
    
    def desenhar_dialogo(self, tela, posicao, Tela_Loja, Tela_Jogo):
        if Tela_Jogo:
            self.atual_dia_AVA += 0.10
            if self.atual_dia_AVA >= len(self.sprites_hud):
                self.atual_dia_AVA = 0
            dialogo_sprite = self.sprites_dialogo_AVA[int(self.atual_dia_AVA)]
        elif Tela_Loja:
            self.atual_dia_LOJ += 0.10
            if self.atual_dia_LOJ >= len(self.sprites_dia_LOJ):
                self.atual_dia_LOJ = 0
            dialogo_sprite = self.sprites_dia_LOJ[int(self.atual_dia_LOJ)]
        if posicao == "topo":
            tela.blit(dialogo_sprite,(0,0))
        elif posicao == "baixo":
            tela.blit(dialogo_sprite,(0,400))
        
    def desenhar_loja(self,tela):
        self.atual_loja += 0.1
        if self.atual_loja >= len(self.sprites_loja):
            self.atual_loja = 0
        loja_sprite = self.sprites_loja[int(self.atual_loja)]
        tela.blit(loja_sprite,(0,0))
    
    def desenhar_lojista(self,tela):
        self.atual_lojista += 0.1
        if self.atual_lojista >= len(self.sprites_lojista):
            self.atual_lojista = 0
        lojista_sprite = self.sprites_lojista[int(self.atual_lojista)]
        lojista_sprite = pygame.transform.scale(lojista_sprite,(100, 100))
        tela.blit(lojista_sprite,(528,382))

    
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
fonte_derivada = pygame.font.Font(fonte, 10)
relogio = pygame.time.Clock()

pygame.display.set_caption("Prove IT")

drive = pygame.image.load("Imagens/Imagens/drive.png")
logo = pygame.image.load("Imagens/Imagens/Logo1.png")
logo_R = pygame.transform.scale(logo, (600,140))
background = pygame.image.load("Imagens/Imagens/Tela_Fundo3.png")
background = pygame.transform.smoothscale(background, (1280, 720))
background_jogo = pygame.image.load("Imagens/Imagens/background.png")
background_jogo = pygame.transform.scale(background_jogo, (1280,720))
background_desafio = pygame.image.load("Imagens/Imagens/2portasBackground.png")
background_desafio = pygame.transform.scale(background_desafio, (1280,720))
background_loja = pygame.image.load("Imagens/Imagens/ShopBackground.png")
Tela_Menu = True
Tela_Loading = False
Tela_Perdeu = False
Tela_Loja = False
Tela_Ganhou = False
questão_gerada = False
Reiniciou = False
teclas = None
num_Sala = 1
dica_jogo = False
ultima_acao = 0
delay = 0.5
dados = Utilitario.carregar_dados("Dados/pontuação.json")
pontuação = dados.get("pontuacao", 0)
itens = dados.get("itens", {"booster": 0, "dica": 0, "vida": 3})
primeira_vez_L = dados.get("primeira_vez_L", True)
errouprimeira = dados.get("errouprimeira", True)
primeira_vez_G = dados.get("primeira_vez_G", True)
acertouprimeira = dados.get("acertouprimeira", True)
desafioprimeira = dados.get("desafioprimeira", True)
jogo_bloqueado = False
dica_desafio = True
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
            dados = {"pontuacao": pontuação, "itens": itens}
            dados["primeira_vez_L"] = primeira_vez_L
            dados["primeira_vez_G"] = primeira_vez_G
            dados["errouprimeira"] = errouprimeira
            dados["acertouprimeira"] = acertouprimeira
            dados["desafioprimeira"] = desafioprimeira
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
    if Tela_Loja:
        Utilitario.tocar_trilha_sonora(trilha_loja)
        b_continuar, b_dica, b_vida, b_booster, tex_dica, tex_booster, tex_vida = Geratriz.Tela_Loja(tela,background_loja,largura,fonte_Opc,todas_as_sprites,teclas, personagem)
        falas_ativas = falas.cutscene_falas["boas_vindasL"]
        if primeira_vez_L:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                        efeito_LOJISTA.play()
                        falas_ativas.proximo()
                        ultima_acao = tempo_atual

            if not falas_ativas.acabou():
                pygame.mixer.music.set_volume(0.1)
                Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_dados,personagem,Tela_Loja, Tela_Loading, falas_ativas.mostrar_posicao())
                jogo_bloqueado = True
            else:
                pygame.mixer.music.set_volume(0.3)
                jogo_bloqueado = False
            
            if jogo_bloqueado:
                pygame.display.flip()
                relogio.tick(60)
                continue 
            primeira_vez_L = False
            dados["primeira_vez_L"] = primeira_vez_L
        Geratriz.gerar_dados(pontuação, num_Sala, Vida, tela, fonte_dados, dados.get("itens", {}).get("dica", 0), dados.get("itens", {}).get("booster", 0), personagem)
        if tex_dica.colliderect(personagem.rect):
            dica_info = "Dica, um otimo item para te ajudar na sua jornada.\nEste item te da uma dica de como resolver a questão"
            dica_preco = f'30'
            como_usar = f'Dica, aperte 2 para usar'
            linhas = dica_info.split("\n")
            y = 330
            for linha in linhas:
                dica_fonte, precod_fonte, fonte_usar = fonte_derivada.render(linha, True, (0, 0, 0)), fonte_dados.render(dica_preco, True, (0,0,0)), fonte_desafios.render(como_usar, True, (0,0,0))
                tela.blit(dica_fonte, (510, y))
                tela.blit(precod_fonte, (740, 390))
                tela.blit(fonte_usar, (570, 280))
                y += 20
        elif tex_booster.colliderect(personagem.rect):
            booster_info = "Booster, um item que te deixa ELETRIZANTE!! Ele fará\n com que você passe de proxima fase sem dificuldade"
            booster_preco = f'80'
            comob_usar = f'Booster, aperte 1 para usar'
            linhas = booster_info.split("\n")
            y = 330
            for linha in linhas:
                booster_fonte, precob_fonte, comob_fonte = fonte_derivada.render(linha, True, (0, 0, 0)), fonte_dados.render(booster_preco, True, (0,0,0)), fonte_desafios.render(comob_usar, True,(0,0,0))
                tela.blit(booster_fonte, (510, y))
                tela.blit(precob_fonte, (740, 390))
                tela.blit(comob_fonte, (570, 280))
                y += 20
        elif tex_vida.colliderect(personagem.rect):
            vida_info = "Vida, uma fonte incrivel de energia.\nAumenta sua quantidade de vida. Vai aguentar mais!"
            vida_preco = f'100'
            vida_nome = f'Vida'
            linhas = vida_info.split("\n")
            y = 330
            for linha in linhas:
                vida_fonte, precov_fonte, vida_fonte_nome = fonte_derivada.render(linha, True, (0, 0, 0)), fonte_dados.render(vida_preco, True, (0,0,0)), fonte_dados.render(vida_nome, True,(0,0,0))
                tela.blit(vida_fonte, (510, y))
                tela.blit(precov_fonte, (740, 390))
                tela.blit(vida_fonte_nome, (680, 270))
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
        Utilitario.tocar_trilha_sonora(trilha_jogo)
        if num_Sala % 10 == 0 and Vida > 0:
            dica_desafio = False
            if not questão_gerada or not Reiniciou:
                personagem.rect.x = 50
                personagem.rect.y = 550
                t_sim, t_nao, pergunta_texto, resposta_correta = Utilitario.gerar_desafio(fonte_Opc)
                #r1, g1, b1 = Utilitario.var_aleatoria(3,0,255)
                #r2, g2, b2 = Utilitario.var_aleatoria(3,0,255)
                questão_gerada = True
                Reiniciou = True
            porta_S, porta_N, respostas_d = Geratriz.gerar_desafio(fonte_desafios,tela,teclas,todas_as_sprites, background_desafio, personagem,t_sim, t_nao, pergunta_texto, resposta_correta)
            if desafioprimeira:
                falas_ativas = falas.cutscene_falas["saladesafio"]
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                            efeito_AVA.play()
                            falas_ativas.proximo()
                            ultima_acao = tempo_atual

                if not falas_ativas.acabou():
                    pygame.mixer.music.set_volume(0.1)
                    Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_dados, personagem,Tela_Loja, Tela_Loading, falas_ativas.mostrar_posicao())
                    jogo_bloqueado = True
                else:
                    pygame.mixer.music.set_volume(0.3)
                    jogo_bloqueado = False
                
                if jogo_bloqueado:
                    pygame.display.flip()
                    relogio.tick(60)
                    continue 
                desafioprimeira = False
                dados["desafioprimeira"] = desafioprimeira
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
                    pontuação += 35
                    dica_jogo = False
                    dica_desafio = True
                elif resultado == "perdeu":
                    num_Sala += 1
                    itens["vida"] -= 1
                    Vida -= 1
                    questão_gerada = False
                    dica_jogo = False
                    dica_desafio = True
        elif num_Sala <= 100 and Vida > 0:
            if not questão_gerada or not Reiniciou:
                personagem.rect.x = 50
                personagem.rect.y = 550
                questão, resposta, respostaf1, respostaf2, escolher, dica = Geratriz.gerar_questao(fonte_desafios)
                largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2 = Geratriz.gerar_texto(questão, resposta, respostaf1, respostaf2, fonte_dados)
                #r1, g1, b1 = Utilitario.var_aleatoria(3,0,255)
                #r2, g2, b2 = Utilitario.var_aleatoria(3,0,255)
                port_1, port_2, port_3, respostas = Geratriz.sala_nova(largura, text_resV, text_resF1, text_resF2)
                questão_gerada = True
                Reiniciou = True
            Geratriz.gerar_jogo(tela,teclas, background_jogo, largura, port_1, port_2, port_3, pos_port_y, respostas, text_quest, todas_as_sprites, personagem)
            if Vida < 3 and errouprimeira:
                falas_ativas = falas.cutscene_falas["erro1"]
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                            efeito_AVA.play()
                            falas_ativas.proximo()
                            ultima_acao = tempo_atual

                if not falas_ativas.acabou():
                    pygame.mixer.music.set_volume(0.1)
                    if falas_ativas.mostrar_index >= 3:
                        personagem.desenhar_vida(tela, Vida)
                    Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_dados,personagem,Tela_Loja, Tela_Loading, falas_ativas.mostrar_posicao())
                    jogo_bloqueado = True
                else:
                    pygame.mixer.music.set_volume(0.3)
                    jogo_bloqueado = False

                if jogo_bloqueado:
                    pygame.display.flip()
                    relogio.tick(60)
                    continue
                errouprimeira = False
                dados["errouprimeira"] = errouprimeira
            elif pontuação > 0 and acertouprimeira:
                falas_ativas = falas.cutscene_falas["acerto"]
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                            efeito_AVA.play()
                            falas_ativas.proximo()
                            ultima_acao = tempo_atual

                if not falas_ativas.acabou():
                    pygame.mixer.music.set_volume(0.1)
                    if falas_ativas.mostrar_index >= 5:
                        tela.blit(drive,(25,25))
                    Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_dados, personagem,Tela_Loja, Tela_Loading, falas_ativas.mostrar_posicao())
                    jogo_bloqueado = True
                else:
                    pygame.mixer.music.set_volume(0.3)
                    jogo_bloqueado = False

                if jogo_bloqueado:
                    pygame.display.flip()
                    relogio.tick(60)
                    continue
                acertouprimeira = False
                dados["acertouprimeira"] = acertouprimeira
            elif primeira_vez_G:
                falas_ativas = falas.cutscene_falas["glados1encontro"]
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if not falas_ativas.acabou() and tempo_atual - ultima_acao > delay:
                            efeito_AVA.play()
                            falas_ativas.proximo()
                            ultima_acao = tempo_atual

                if not falas_ativas.acabou():
                    pygame.mixer.music.set_volume(0.1)
                    Geratriz.exibir_fala(tela, falas_ativas.mostrar_fala(), fonte_dados,personagem,Tela_Loja, Tela_Loading, falas_ativas.mostrar_posicao())
                    jogo_bloqueado = True
                else:
                    pygame.mixer.music.set_volume(0.3)
                    jogo_bloqueado = False

                if jogo_bloqueado:
                    pygame.display.flip()
                    relogio.tick(60)
                    continue
                primeira_vez_G = False
                dados["primeira_vez_L"] = False
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
            if dica_desafio:
                if itens["dica"] >= 1:
                    itens["dica"] -= 1
                    dica_jogo = True
                    ultima_acao = tempo_atual
        if dica_jogo:
            if escolher == 'Linear':
                tela.blit(dica,(380,220))
            elif escolher == 'Divisão':
                tela.blit(dica,(380,220))
            elif escolher == "Quadratica":
                linhas = dica.split("\n")
                y = 220
                for linha in linhas:
                    dica_pergunta = fonte_desafios.render(linha, True, (0, 0, 0))
                    tela.blit(dica_pergunta,(380, y))
                    y += 20
            elif escolher == "Comparação":
                tela.blit(dica,(380,220))
            elif escolher == "Modular":
                linhas = dica.split("\n")
                y = 220
                for linha in linhas:
                    dica_pergunta = fonte_desafios.render(linha, True, (0, 0, 0))
                    tela.blit(dica_pergunta,(380, y))
                    y += 20
            elif escolher == "Trigonometrica":
                linhas = dica.split("\n")
                y = 220
                for linha in linhas:
                    dica_pergunta = fonte_desafios.render(linha, True, (0, 0, 0))
                    tela.blit(dica_pergunta,(380, y))
                    y += 20
        elif num_Sala == 101 and Vida > 0:
            Tela_Ganhou = not Tela_Ganhou
            Tela_Loading = not Tela_Loading
            dica_jogo = False

        elif Vida == 0:
            Tela_Perdeu = not Tela_Perdeu
            Tela_Loading = not Tela_Loading
            dica_jogo = False
    if Tela_Ganhou:
        pygame.mixer.music.stop()
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
        pygame.mixer.music.stop()
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
