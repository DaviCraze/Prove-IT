import os
import random

class Utilitario:
    
    @staticmethod
    def carregar_pontuação(Arquivo):
        if os.path.exists(Arquivo):
            with open(Arquivo, "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return -1
        else: 
            return -1
    
    @staticmethod
    def salvar_pontuação(pontuação, Arquivo):
        with open(Arquivo, "w") as f:
            f.write(str(pontuação))
    
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
        return 0
    
    @staticmethod
    def Quest_Linear():
        a, b = Utilitario.var_aleatoria(2,0,9)
        questão = f'2 x {a} - {b} = 0'
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
        return questão, resposta, respostaf1, respostaf2
    
    @staticmethod
    def Quest_Divisao():
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
        return questão, resposta, respostaf1, respostaf2
    
    @staticmethod
    def Quest_Quadratica():
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
        return questão, resposta, respostaf1, respostaf2
    
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
        if porta_x <= jogador_x <= porta_x + largura_porta and porta_y <= jogador_y <= porta_y + 250:
            if respostas[1] == "correta":
                return "avançar"
            else:
                return "perdeu"
        return -1
          
