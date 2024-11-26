import pygame
from Questoes import *

class Geratriz:
    
    @staticmethod
    def gerar_questao(fonte_dados):
        tipos_questoes = ['Linear', 'Divisão', 'Quadratica']
        escolher = random.choice(tipos_questoes)
        questao, resposta = None, None
        falsa1, falsa2 = None, None
        if escolher == 'Linear':
            questao, resposta, falsa1, falsa2, dica_t = Utilitario.Quest_Linear(fonte_dados)
            return questao, resposta, falsa1, falsa2, escolher, dica_t
        elif escolher == 'Divisão':
            questao, resposta, falsa1, falsa2, dica_t = Utilitario.Quest_Divisao(fonte_dados)
            return questao, resposta, falsa1, falsa2, escolher, dica_t
        elif escolher == 'Quadratica':
            questao, resposta, falsa1, falsa2, dica_t = Utilitario.Quest_Quadratica(fonte_dados)
            return questao, resposta, falsa1, falsa2, escolher, dica_t
        else:
            questao, resposta, falsa1, falsa2 = Utilitario.Quest_Comparacao
            return questao, resposta, falsa1, falsa2, escolher, dica_t
    
    @staticmethod
    def exibir_fala(tela, fala_atual, fonte, posicao="topo"):
        if fala_atual:
            if posicao == "topo":
                dialogoP = (50, 50, 1180, 200)
                dialogoB = (60, 60, 1160, 180)
                texto_y = 70
            elif posicao == "baixo":
                dialogoP = (50, 500, 1180, 200)
                dialogoB = (60, 510, 1160, 180)
                texto_y = 520

            pygame.draw.rect(tela, (0,0,0),dialogoP)
            pygame.draw.rect(tela, (255,255,255),dialogoB)

            linhas = fala_atual.split("\n")
            for linha in linhas:
                fala_texto = fonte.render(linha, True,(0,0,0))
                tela.blit(fala_texto, (70, texto_y))
                texto_y += 30

    @staticmethod
    def gerar_desafio(fonte_desafios,tela,teclas,todas_as_sprites, fonte, background,personagem):
        tipos_desafio = [
            {"Pergunta": "Sejam p e q proposições, tais que p: “minha caneta é roxa”\ne q: “meu caderno é azul”. A expressão logica equivalente a\n“se minha caneta é roxa então meu caderno nao é azul” é p→ ¬ q?", "resposta": "sim"},
            {"Pergunta": "Quanto as derivadas de uma função, a primeira derivada denuncia\ncurvatura e concavidade da função, enquanto a segunda\n diz respeito a decrescimento/crescimento.", "resposta": "nao"},
            {"Pergunta": "Os conceitos originados na trigonometria, chamados de cosseno e\nseno são conceitos universais no nível de poderem ser\n aplicados em praticamnte qualquer área da matemática.", "resposta": "sim"},
            {"Pergunta": "Séries são conceitos matemáticos fundamentais para áreas como\n física, engenharia, cálculo, entre outras áreas.", "resposta": "sim"},
            {"Pergunta": "O Teorema Fundamental do Cálculo junta conceitos de integral,\nlimite, derivada para provar que uma função, mesmo que\ndescontínua, tem uma integral definida existente.", "resposta": "nao"},
            {"Pergunta": "Infinito é um conceito bem variado e que se estende para várias\naplicações, é possível que um infinito seja “menor” que outro?", "resposta": "sim"},
            {"Pergunta": "Algoritmos recorrentes são conceitos geralmente usados, na\n matemática existem conceitos análogos de recorrências, \ncomo: Fatorial e Número de ouro.", "resposta": "sim"},
            {"Pergunta": "Sejam x e y pertencentes a N respectivamente um número par\ne um número ímpar a multiplicação desse dois números dará\nsempre um par?", "resposta": "sim"},
            {"Pergunta": "O Teorema de Pitágoras cria uma relação entre geometria básica\ncomo triângulos retângulos com análise estatística?", "resposta": "nao"},
            {"Pergunta": "A soma de 2 números naturais a e b repectivamente par e ímpar\nsempre será ímpar e igual a um número natural par qualquer\nc mais 1.", "resposta": "sim"},
            {"Pergunta": "Programas que usam tratamento de imagem para edição entre outras\ncoisas usam muito aplicações diferenciais focando em\nresultados exatos eque modelam fenômenos.", "resposta": "nao"},
            {"Pergunta": "Problemas numéricos trabalham com aproximações e erros, um\nerro de 1e-20(10^-20) é considerado insignificante na maioria\ndas aplicações numéricas?", "resposta": "sim"},
            {"Pergunta": "A definição ou a fórmula de Euler é central para a matemática\ne encapsula conceitos extremamente importantes como o\ndesvio padrão, o 0, o 1 e a constante euler.", "resposta": "nao"},
            {"Pergunta": "Probabilidade e Estatística são bem usadas na previsão de\ncomportamento em áreas variadas, como química, estudo demográfico,\nanálise econômica, engenharia, etc.", "resposta": "sim"},
            {"Pergunta": "A linearidade de funções facilita o estudo e o processamento\nde resultados, principalmente quando se fala em áreas como\ncalculo numérico e análise de sistemas.", "resposta": "sim"},
            {"Pergunta": "A trigonometria consegue ter ligação direta com conceitos como\nconjuntos, principalmente quando se fala em reais/complexos,\nindispensáveis na explicação de periodicidade e continuidade.", "resposta": "sim"},
            {"Pergunta": "Matemática discreta toma um papel extremamente importante no\nentendimento do raciocínio por trás de logaritmos computacionais,\nalém de preparar para matérias como Análise.", "resposta": "nao"},
            {"Pergunta": "Um limite não retorna um resultado e sim um comportamento, assim\ncomo integrais retornam uma área e uma assinatura.", "resposta": "nao"},
            {"Pergunta": "Um conjunto contínuo só em um intervalo, sendo diferencial neste\nintervalo, e limitado pode admitir integrais e derivadas?", "resposta": "sim"},
            {"Pergunta": "Uma boa forma de calcular constantes como a de euler, pi, ou\nfunções como seno e cosseno é com o uso de séries, como a harmônica.", "resposta": "nao"},
            {"Pergunta": "Convergência e divergência são bem aplicados em séries,\nanalogamente em integrais devido ao sua natureza somatória, a\npartir disso toda integral é convergente?", "resposta": "nao"},
            {"Pergunta": "A utilização de matrizes é uma maneira eficiente e eficaz\nde resolver muitos problemas numéricos, principalmente com\nsistema lineares.", "resposta": "sim"},
            {"Pergunta": "Em um grafo completo, todos os vértices estão conectados\npor uma aresta.", "resposta": "nao"},
            {"Pergunta": "O Teorema dos Primos em Progressões aritméticas assume que\nexistem infinitos números primos na forma 2n+1.", "resposta": "nao"},
            {"Pergunta": "A ordenação é uma das áreas mais estudadas em questão de\nalgortimos e complexidade, em busca de tornar mais rápido o processo,\nmas o mais rápido possível até hoje é O(nlogn) em casos isolados.", "resposta": "nao"},
            {"Pergunta": "A indução matemática é um método válido para provar afirmações\nsobre números naturais e inteiros.", "resposta": "nao"}
        ]
        sim = f'Sim'
        nao = f'Não'
        t_sim = fonte.render(sim, True, (0, 0, 0))
        t_nao = fonte.render(nao, True, (0, 0, 0))
        random.shuffle(tipos_desafio)
        pergunta_atual = tipos_desafio.pop(0)
        pergunta_texto = pergunta_atual["Pergunta"]
        resposta_correta = pergunta_atual["resposta"]
        pygame.draw.rect(tela, (0, 0, 0), (470, 397, 150, 250))
        porta_S = pygame.draw.rect(tela, (255, 255, 255), (470 + 13, 407, 125 , 240))
        pygame.draw.rect(tela, (0, 0, 0), (880, 397, 250 , 250))
        porta_N = pygame.draw.rect(tela, (255, 255, 255), (880 + 13, 407, 125, 240))
        tela.blit(background, (0, 0))
        if resposta_correta == "sim":
            respostas_d = [(t_sim, "correta"), (t_nao, "errada")]
        else:
            respostas_d = [(t_sim, "errada"), (t_nao, "correta")]

        linhas = pergunta_texto.split("\n")
        y = 100
        for linha in linhas:
            text_pergunta = fonte_desafios.render(linha, True, (0, 0, 0))
            tela.blit(text_pergunta,(400, y))
            y += 20
        tela.blit(respostas_d[0][0], (520, 350))
        tela.blit(respostas_d[1][0], (930, 350))

        personagem.desenhar_jogo_desafio(tela)
        todas_as_sprites.draw(tela)
        todas_as_sprites.update(teclas)

        return porta_S, porta_N, respostas_d
    @staticmethod
    def gerar_menu(tela, background, largura, altura, largura_Opc, altura_Opc, fonte_nome, fonte_Opc,logo):
        #nome_do_jogo = f'Prove It'
        bot_Hist = f'Modo Historia'
        bot_Arcd = f'Modo Arcade'
        
        x_Hist = largura/2 - largura_Opc/2
        y_Hist = altura/2

        x_Arcd = largura/2 - largura_Opc/2
        y_Arcd = altura/1.5
        
        #texto_jogo = fonte_nome.render(nome_do_jogo, True, (0, 0, 0))
        texto_Hist = fonte_Opc.render(bot_Hist, True, (255, 255, 255))
        texto_Arcd = fonte_Opc.render(bot_Arcd, True, (255, 255, 255))

        tela.blit(background, (0, 0))
        tela.blit(logo, (340, 100))

        pygame.draw.rect(tela, (0, 0, 0), (x_Hist, y_Hist, largura_Opc, altura_Opc))
        pygame.draw.rect(tela, (0, 0, 0), (x_Arcd, y_Arcd, largura_Opc, altura_Opc))

        #tela.blit(texto_jogo, (420, altura - 600))
        tela.blit(texto_Hist, (x_Hist + 2, y_Hist + 10))
        tela.blit(texto_Arcd, (x_Arcd + 12, y_Arcd + 15))
    
    @staticmethod
    def gerar_texto(questão, resposta, respostaf1, respostaf2, fonte):
        text_quest = fonte.render(questão, True, (0, 0, 0))
        text_resV = fonte.render(resposta, True, (0, 0, 0))
        text_resF1 = fonte.render(respostaf1, True, (0, 0, 0))
        text_resF2 = fonte.render(respostaf2, True, (0, 0, 0))
        largura_quest, altura_quest = text_quest.get_size()
        largura_text, altura_text = text_resV.get_size()
        largura_textF1, altura_textF1 = text_resF1.get_size()
        largura_textF2, altura_textF2 = text_resF2.get_size() 
        return largura_quest, largura_text, largura_textF1, largura_textF2, text_quest, text_resV, text_resF1, text_resF2
    
    @staticmethod
    def sala_nova(largura, text_resV, text_resF1, text_resF2):
        
        pos_port1_x = 470
        pos_port2_x = pos_port1_x + 200
        pos_port3_x = pos_port2_x + 200
        
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
    def gerar_jogo(tela,teclas, background, largura, port_1, port_2, port_3, pos_port_y, respostas, text_quest, todas_as_sprites, personagem):
        
        pos_port1_x = 470
        pos_port2_x = pos_port1_x + 200
        pos_port3_x = pos_port2_x + 200

        pygame.draw.rect(tela, (0, 0, 0), (pos_port1_x, pos_port_y, 120 + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (pos_port1_x + 13, 407, 120 + 25, 240))
        pygame.draw.rect(tela, (0, 0, 0), (pos_port2_x, pos_port_y, 120 + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (pos_port2_x + 13, 407, 120 + 25, 240))
        pygame.draw.rect(tela, (0, 0, 0), (pos_port3_x, pos_port_y, 120 + 50, 250))
        pygame.draw.rect(tela, (255, 255, 255), (pos_port3_x + 13, 407, 120 + 25, 240))

        tela.blit(background, (0, 0))
        text_quest_widht = text_quest.get_width()
        x_text_quest = (largura - text_quest_widht) // 1.65
        tela.blit(text_quest, (x_text_quest, 150))

        personagem.desenhar_jogo(tela)
        todas_as_sprites.draw(tela) 

        tela.blit(respostas[0][0], (port_1 + 20, 350)) 
        tela.blit(respostas[1][0], (port_2 + 20, 350))
        tela.blit(respostas[2][0], (port_3 + 20, 350))

        todas_as_sprites.update(teclas)
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
        pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 140, 200, largura_perder + 50, altura_perder + 50))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 - 140, 210, largura_perder + 25, altura_perder + 25))
        botao_inicial_P = pygame.draw.rect(tela, (0, 0, 0), (largura/2 + 50, 350, largura_inicial + 50, altura_inicial + 40))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 + 50, 360, largura_inicial + 25, altura_inicial+ 20))
        botao_reiniciar = pygame.draw.rect(tela, (0, 0, 0), (largura/2 - 250, 350, largura_reiniciar + 68, altura_reiniciar + 40))
        pygame.draw.rect(tela, (255, 255, 255), (largura/1.96 - 250, 360, largura_reiniciar + 40, altura_reiniciar+ 20))

        tela.blit(text_perder, (largura/1.92 - 140, 220))
        tela.blit(text_inicial, (largura/1.92 + 50, 370))
        tela.blit(text_reiniciar, (largura/1.92 - 250, 370))
        
        return botao_inicial_P, botao_reiniciar
        
    @staticmethod
    def gerar_fundo(tela, r1, g1, b1, r2, g2, b2):
        
        pygame.draw.rect(tela, (r1, g1, b1), (0, 640, 1280, 88))
        pygame.draw.rect(tela, (r2, g2, b2), (0, 0, 1280, 640))
    
    @staticmethod
    def Tela_Ganhou(tela, background, fonte_Opc):
        tela.blit(background, (0, 0))
        ganhou = f'Parabens! Você concluiu o Modo Historia!'
        tela_inicial = f'Tela Inicial'
        text_ganhou = fonte_Opc.render(ganhou, True, (0, 0, 0))
        text_inicial = fonte_Opc.render(tela_inicial, True, (0, 0, 0))
        largura_ganhou, altura_ganhou = text_ganhou.get_size()
        largura_inicial, altura_inicial = text_inicial.get_size()
        pygame.draw.rect(tela, (0, 0, 0), (250, 200, largura_ganhou + 50, altura_ganhou + 40))
        pygame.draw.rect(tela, (255, 255, 255), (262, 210, largura_ganhou + 25, altura_ganhou+20))
        botao_inicial_G = pygame.draw.rect(tela, (0, 0, 0), (500, 350, largura_inicial + 50, altura_inicial + 40))
        pygame.draw.rect(tela, (255, 255, 255), (513, 360, largura_inicial + 25, altura_inicial+20))

        tela.blit(text_inicial, (522, 370))
        tela.blit(text_ganhou, (272, 220))

        return botao_inicial_G
    @staticmethod
    def Tela_Loja(tela, background, largura, fonte_Opc, todas_as_sprites, teclas):
        tela.blit(background, (0,0))
        Loja, Booster, Dica, Vida, Continuar = f'Loja de Itens', f'Booster', f'Dica', f'Vida', f'Continuar'
        t_loja, t_booster, t_dica, t_vida, t_continuar = fonte_Opc.render(Loja, True, (0, 0, 0)), fonte_Opc.render(Booster, True, (0, 0, 0)), fonte_Opc.render(Dica, True, (0, 0, 0)), fonte_Opc.render(Vida, True, (0, 0, 0)), fonte_Opc.render(Continuar, True, (0, 0, 0))
        (largura_loja, altura_loja), (largura_booster, altura_booster), (largura_dica, altura_dica), (largura_vida, altura_vida), (largura_continuar, altura_continuar) = t_loja.get_size(), t_booster.get_size(), t_dica.get_size(), t_vida.get_size(), t_continuar.get_size()      
        b_continuar = pygame.draw.rect(tela,(255,255,255), (1050, 563, largura_continuar+40, altura_continuar+100))
        pygame.draw.rect(tela,(135, 135, 135), (0, 0, largura, 720))
        pygame.draw.rect(tela,(221, 75, 23), (0, 640, largura, 88))
        pygame.draw.rect(tela,(0, 0, 255), (0, 540, largura, 100))
        pygame.draw.rect(tela,(0, 0, 0), (0, 535, largura, 10))
        pygame.draw.rect(tela,(0, 0, 0), (0, 635, largura, 10))
        b_booster = pygame.draw.rect(tela,(255,255,255), (52, 570, largura_booster+40, altura_booster+10))
        b_dica = pygame.draw.rect(tela,(255,255,255), (300, 570, largura_booster+40, altura_booster+10))
        b_vida = pygame.draw.rect(tela,(255,255,255), (548, 570, largura_booster+40, altura_booster+10))
        pygame.draw.rect(tela,(255,255,255), (1050, 570, largura_continuar+40, altura_continuar+10))
        tex_booster = tela.blit(t_booster, (75, 575))
        tela.blit(t_loja, (largura/2.5, 100))
        tela.blit(t_continuar, (1070, 575))
        tex_dica = tela.blit(t_dica, (345, 575))
        tex_vida = tela.blit(t_vida, (595, 575))

        todas_as_sprites.draw(tela)
        todas_as_sprites.update(teclas)
        return b_continuar, b_dica, b_vida, b_booster, tex_dica, tex_booster, tex_vida
    @staticmethod
    def gerar_dados(pontuação, num_Sala, Vida, tela, fonte_dados, dica, booster, personagem):
        ponto_texto, vida_texto, sala_texto, dica_texto, booster_texto = f'Pontos = {pontuação}', f'Vida = {Vida}', f'Nº {num_Sala}', f'Dicas = {dica}', f'Boosters = {booster}'
        ponto_fonte, vida_fonte, sala_fonte, dica_fonte, booster_fonte = fonte_dados.render(ponto_texto, True, (0, 0, 0)), fonte_dados.render(vida_texto, True, (0, 0, 0)), fonte_dados.render(sala_texto, True, (0, 0, 0)), fonte_dados.render(dica_texto, True, (0, 0, 0)), fonte_dados.render(booster_texto, True, (0, 0, 0))
        tela.blit(ponto_fonte, (20, 30))
        tela.blit(vida_fonte, (20, 65))
        tela.blit(sala_fonte, (1180, 30))
        tela.blit(dica_fonte, (20, 100))
        tela.blit(booster_fonte, (20, 135))
        personagem.desenhar_vida(tela, Vida)
