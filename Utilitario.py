import os
import random
import json
import pygame

musica_atual = None
class Utilitario:

    @staticmethod
    def carregar_dados(Arquivo):
        if os.path.exists(Arquivo):
            with open(Arquivo, "r") as f:
                try:
                    dados = json.load(f)
                    return dados
                except ValueError:
                    return {"pontuacao": 0,"errouprimeira": True, "itens": {}, "primeira_vez_L": True, "primeira_vez_G": True, "acertouprimeira": True, "desafioprimeira": True}
        else: 
            return {"pontuacao": 0,"errouprimeira": True, "itens": {}, "primeira_vez_L": True, "primeira_vez_G": True, "acertouprimeira": True, "desafioprimeira": True}
    
    @staticmethod
    def salvar_dados(dados, Arquivo):
        with open(Arquivo, "w") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def var_aleatoria(quant, menor, topo):
        match(quant):
            case 1:
                a = random.randint(menor,topo)
                return a
            case 2:
                a , b = random.randint(menor,topo), random.randint(menor,topo)
                return a,b
            case 3:
                a , b , c = random.randint(menor,topo), random.randint(menor,topo), random.randint(menor,topo)
                return a,b,c
    
    @staticmethod
    def pontuação_respostas(escolher):
        if escolher == 'Linear':
            return 2
        elif escolher == 'Divisão':
            return 1
        elif escolher == 'Quadratica':
            return 4
        elif escolher == 'Trigonometrica':
            return 6
        elif escolher == 'Modular':
            return 4
        elif escolher == 'Comparação':
            return 3
        return 0
    
    @staticmethod
    def Quest_Linear(fonte_dados):
        dica = f'Faça primeiro a multiplicação, depois a subtração'
        dica_t = fonte_dados.render(dica, True, (0,0,0))
        a, b = Utilitario.var_aleatoria(2,0,9)
        questão = f'2 x {a} - {b} = x'
        resposta = f'x = {(2*a) - b}'
        c, d = Utilitario.var_aleatoria(2,0,9)
        respostaf1 = f'x = {(2*c) - d}'
        while respostaf1 == resposta:
            c, d = Utilitario.var_aleatoria(2,0,9)
            respostaf1 = f'x = {(2 * c) - d}'
        e, f = Utilitario.var_aleatoria(2,0,9)
        respostaf2 = f'x = {(2 * e) - f}'
        while respostaf2 == respostaf1 or respostaf2 == resposta:
            e, f = Utilitario.var_aleatoria(2,0,9)
            respostaf2 = f'x = {(2 * e) - f}'
        return questão, resposta, respostaf1, respostaf2, dica_t
    
    @staticmethod
    def Quest_Divisao(fonte_dados):
        dica = f'Amigo....so dividir(qualquer coisa chuta ou usa calculadora ;)'
        dica_t = fonte_dados.render(dica, True, (0,0,0))
        a = Utilitario.var_aleatoria(1,10,100)
        b = Utilitario.var_aleatoria(1,1,10)
        questão = f'{a} / {b} = x'
        resposta = f'x = {a / b:.2f}'
        c = Utilitario.var_aleatoria(1,10,100)
        d = Utilitario.var_aleatoria(1,1,10)
        respostaf1 = f'x = {c / d:.2f}'
        while respostaf1 == resposta:
            c = Utilitario.var_aleatoria(1,10,100)
            d = Utilitario.var_aleatoria(1,1,10)
            respostaf1 = f'x = {c / d:.2f}'
        e = Utilitario.var_aleatoria(1,1,100)
        f = Utilitario.var_aleatoria(1,1,10)
        respostaf2 = f'x = {e / f:.2f}'
        while respostaf2 == respostaf1 or respostaf2 == resposta:
            e = Utilitario.var_aleatoria(1,1,100)
            f = Utilitario.var_aleatoria(1,1,10)
            respostaf2 = f'x = {e / f:.2f}'
        return questão, resposta, respostaf1, respostaf2, dica_t
    
    @staticmethod
    def Quest_Quadratica(fonte_dados):
        dica = f"Que tal focar no primeiro valor e no segundo valor? Talvez isso te ajude!"
        dica_t = fonte_dados.render(dica, True, (0,0,0))
        a,b = Utilitario.var_aleatoria(2,1,9)
        questão = f'{a ** 2}x² + {2 * a * b}x + {b ** 2}'
        resposta = f'({a}x + {b})²'
        c,d = Utilitario.var_aleatoria(2,1,9)
        respostaf1 = f'({c}x + {d})²'
        while respostaf1 == resposta:
            c,d = Utilitario.var_aleatoria(2,1,9)
            respostaf1 = f'({c}x + {d})²'
        e, f = Utilitario.var_aleatoria(2,1,9)
        respostaf2 = f'({e}x + {f})²'
        while respostaf2 == resposta or respostaf2 == respostaf1:
            e, f = Utilitario.var_aleatoria(2,1,9)
            respostaf2 = f'({e}x + {f})²'
        return questão, resposta, respostaf1, respostaf2, dica_t
    
    @staticmethod
    def Quest_Comparacao():
        a,b = Utilitario.var_aleatoria(2,1,30)
        respostaf1 = None
        respostaf2 = None
        questão = f'{a} >= {b}x'
        resposta = f'x <= {a/b:.2f}'
        rand = Utilitario.var_aleatoria(1,1,3)
        match(rand):
            case 1:
                respostaf1 = f'x < {a/b:.2f}'
                respostaf2 = f'x >= {b/a:.2f}'
            case 2:
                c,d = Utilitario.var_aleatoria(2,1,30)
                respostaf1 = f'x <= {c/d:.2f}'
                respostaf2 = f'x = {d/c:.2f}'
                while respostaf1 == resposta:
                    c,d = Utilitario.var_aleatoria(2,1,30)
                    respostaf1 = f'x <= {c/d:.2f}'
            case 3:
                respostaf1 = f'x > {a/b:.2f}'
                c,d = Utilitario.var_aleatoria(2,1,30)
                respostaf2 = f'x <= {c/d:.2f}'
                while respostaf2 == resposta:
                    c,d = Utilitario.var_aleatoria(2,1,30)
                    respostaf2 = f'x <= {c/d:.2f}'
        return questão, resposta, respostaf1, respostaf2
    
    @staticmethod
    def verificar_escolha(porta_x, porta_y, largura_porta, respostas, jogador_x, jogador_y):
        if porta_x - 50 <= jogador_x <= porta_x + largura_porta + 50 and porta_y <= jogador_y <= porta_y + 250:
            if respostas[1] == "correta":
                return "avançar"
            else:
                return "perdeu"
        return -1
          
    @staticmethod
    def efeito_booster(num_sala):
        num_sala += 1
        return num_sala
    
    @staticmethod
    def efeito_vida(vida):
        vida += 1
        return vida
    
    @staticmethod
    def tocar_trilha_sonora(trilha):
        global musica_atual
        if musica_atual != trilha:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(trilha)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            musica_atual = trilha
    
    @staticmethod
    def gerar_desafio(fonte):
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
        return t_sim, t_nao, pergunta_texto, resposta_correta
        
