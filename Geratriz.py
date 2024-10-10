import pygame
from Utilitario import *

class Geratriz:
    
    @staticmethod
    def gerar_questao():
        tipos_questoes = ['Linear', 'Divisão', 'Quadratica']
        escolher = random.choice(tipos_questoes)
        questao, resposta = None, None
        falsa1, falsa2 = None, None
        if escolher == 'Linear':
            questao, resposta, falsa1, falsa2 = Utilitario.Quest_Linear()
            return questao, resposta, falsa1, falsa2, escolher
        elif escolher == 'Divisão':
            questao, resposta, falsa1, falsa2 = Utilitario.Quest_Divisao()
            return questao, resposta, falsa1, falsa2, escolher
        elif escolher == 'Quadratica':
            questao, resposta, falsa1, falsa2 = Utilitario.Quest_Quadratica()
            return questao, resposta, falsa1, falsa2, escolher
        else:
            questao, resposta, falsa1, falsa2 = Utilitario.Quest_Comparacao
            return questao, resposta, falsa1, falsa2, escolher
    
    @staticmethod
    def gerar_menu(tela, background, largura, altura, largura_Opc, altura_Opc, fonte_nome, fonte_Opc):
        nome_do_jogo = f'Prove It'
        bot_Hist = f'Modo Historia'
        bot_Arcd = f'Modo Arcade'
        
        x_Hist = largura/2 - largura_Opc/2
        y_Hist = altura/2

        x_Arcd = largura/2 - largura_Opc/2
        y_Arcd = altura/1.5
        
        texto_jogo = fonte_nome.render(nome_do_jogo, True, (0, 0, 0))
        texto_Hist = fonte_Opc.render(bot_Hist, True, (255, 255, 255))
        texto_Arcd = fonte_Opc.render(bot_Arcd, True, (255, 255, 255))

        tela.blit(background, (0, 0))

        pygame.draw.rect(tela, (0, 0, 0), (x_Hist, y_Hist, largura_Opc, altura_Opc))
        pygame.draw.rect(tela, (0, 0, 0), (x_Arcd, y_Arcd, largura_Opc, altura_Opc))

        tela.blit(texto_jogo, (largura/2 - 180, altura - 600))
        tela.blit(texto_Hist, (x_Hist + 2, y_Hist))
        tela.blit(texto_Arcd, (x_Arcd + 10, y_Arcd))
    
    @staticmethod
    def gerar_texto(questão, resposta, respostaf1, respostaf2, fonte_Opc):
        text_quest = fonte_Opc.render(questão, True, (0, 0, 0))
        text_resV = fonte_Opc.render(resposta, True, (0, 0, 0))
        text_resF1 = fonte_Opc.render(respostaf1, True, (0, 0, 0))
        text_resF2 = fonte_Opc.render(respostaf2, True, (0, 0, 0))
        largura_quest, altura_quest = text_quest.get_size()
        largura_text, altura_text = text_resV.get_size()
        largura_textF1, altura_textF1 = text_resF1.get_size()
        largura_textF2, altura_textF2 = text_resF2.get_size() 
        return largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2
    
    @staticmethod
    def sala_nova(largura, text_resV, text_resF1, text_resF2):
        
        pos_port1_x = largura/4
        pos_port2_x = pos_port1_x + 300
        pos_port3_x = pos_port2_x + 300
        
        lista_de_portas = [pos_port1_x, pos_port2_x, pos_port3_x]
        port_1 = random.choice(lista_de_portas)
        lista_de_portas.remove(port_1)
        port_2 = random.choice(lista_de_portas)
        lista_de_portas.remove(port_2)
        port_3 = lista_de_portas[0]

        respostas = [(text_resV, "correta"), (text_resF1, "errada"), (text_resF2, "errada")]
        random.shuffle(respostas)

        return port_1, port_2, port_3, respostas
    
    @staticmethod
    def gerar_jogo(tela,teclas, r1, g1, b1, r2, g2, b2,  background, largura, largura_quest, largura_text, largura_textF1, largura_textF2, port_1, port_2, port_3, pos_port_y, respostas, text_quest, todas_as_sprites):
        tela.blit(background, (0, 0))
        
        Geratriz.gerar_fundo(tela, r1, g1, b1, r2, g2, b2)
        
        pos_port1_x = largura/4
        pos_port2_x = pos_port1_x + 300
        pos_port3_x = pos_port2_x + 300

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

    @staticmethod
    def tela_perdeu(tela, background, largura, fonte_Opc):
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
        
        return botao_inicial, botao_reiniciar
        
    @staticmethod
    def gerar_fundo(tela, r1, g1, b1, r2, g2, b2):
        
        pygame.draw.rect(tela, (r1, g1, b1), (0, 640, 1280, 88))
        pygame.draw.rect(tela, (r2, g2, b2), (0, 0, 1280, 640))
    
    @staticmethod
    def Tela_Ganhou(tela, background, largura, fonte_Opc):
        tela.blit(background, (0, 0))
        ganhou = f'Parabens! Você concluiu o Modo Historia!'
        tela_inicial = f'Tela Inicial'
        text_ganhou = fonte_Opc.render(ganhou, True, (0, 0, 0))
        text_inicial = fonte_Opc.render(tela_inicial, True, (0, 0, 0))
        largura_ganhou, altura_ganhou = text_ganhou.get_size()
        largura_inicial, altura_inicial = text_inicial.get_size()
        pygame.draw.rect(tela, (0, 0, 0), (largura/3 - 140, 200, largura_ganhou + 50, altura_ganhou + 20))
        pygame.draw.rect(tela, (255, 255, 255), (largura/2.93 - 140, 210, largura_ganhou + 25, altura_ganhou))
        botao_inicial = pygame.draw.rect(tela, (0, 0, 0), (largura/2, 350, largura_inicial + 50, altura_inicial + 20))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.96, 360, largura_inicial + 25, altura_inicial))

        tela.blit(text_inicial, (largura/1.92, 360))
        tela.blit(text_ganhou, (largura/2.88 - 140, 210))

        return botao_inicial
