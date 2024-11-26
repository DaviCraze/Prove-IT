import math
import random
from sympy import symbols, diff, sin, cos, exp
from Utilitario import *

class Questoes:
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
        dica = f"Que tal focar no primeiro valor e no segundo valor?\nTalvez isso te ajude!"
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
        return questão, resposta, respostaf1, respostaf2, dica
    
    @staticmethod
    def Quest_Comparacao(fonte_dados):
        a, b = Utilitario.var_aleatoria(2, 1, 30)
        questão = f'{a} >= {b}x'
        resposta = f'x <= {a / b:.2f}'

        dica = f"Tal qual uma divisão normal, mas lembra que não é um igual tá!"
        dica_t = fonte_dados.render(dica, True, (0,0,0))
        
        rand = Utilitario.var_aleatoria(1, 1, 3) 
        respostaf1 = None
        respostaf2 = None

        match rand:
            case 1:  
                respostaf1 = f'x < {a / b:.2f}'  
                respostaf2 = f'x >= {b / a:.2f}'  
            case 2:  
                c, d = Utilitario.var_aleatoria(2, 1, 30)
                respostaf1 = f'x <= {c / d:.2f}'
                while respostaf1 == resposta:
                    c, d = Utilitario.var_aleatoria(2, 1, 30)
                    respostaf1 = f'x <= {c / d:.2f}'
                respostaf2 = f'x = {d / c:.2f}'
            case 3:  
                respostaf1 = f'x > {a / b:.2f}'  
                c, d = Utilitario.var_aleatoria(2, 1, 30)
                respostaf2 = f'x <= {c / d:.2f}'
                while respostaf2 == resposta:
                    c, d = Utilitario.var_aleatoria(2, 1, 30)
                    respostaf2 = f'x <= {c / d:.2f}'

        return questão, resposta, respostaf1, respostaf2, dica_t
    
    @staticmethod
    def Quest_Modular(fonte_dados):
        dica = f"Lembra que é um módulo, ou seja, 2 formas de resolver, mas aqui\nbasta saber 1 das formas!"
        dica_t = fonte_dados.render(dica, True, (0, 0, 0))

        a, b = Utilitario.var_aleatoria(2, 1, 9)
        c = Utilitario.var_aleatoria(1, -9, 9)  

        questão = f"|{a}x + {b}| = {c if c > 0 else -c}"
        resposta1 = f"x = {(-b + c) / a:.2f}"
        resposta2 = f"x = {(-b - c) / a:.2f}"

        resposta = resposta1 if Utilitario.var_aleatoria(1, 0, 1) == 0 else resposta2

        d, e = Utilitario.var_aleatoria(2, 1, 9)
        respostaf1 = f"x = {d / e:.2f}"
        while respostaf1 == resposta1 or respostaf1 == resposta2:
            d, e = Utilitario.var_aleatoria(2, 1, 9)
            respostaf1 = f"x = {d / e:.2f}"

        f, g = Utilitario.var_aleatoria(2, 1, 9)
        respostaf2 = f"x = {f / g:.2f}"
        while respostaf2 == resposta1 or respostaf2 == resposta2 or respostaf2 == respostaf1:
            f, g = Utilitario.var_aleatoria(2, 1, 9)
            respostaf2 = f"x = {f / g:.2f}"

        return questão, resposta, respostaf1, respostaf2, dica

    @staticmethod
    def Quest_Trigonometrica(fonte_dados):

        intervalo = (0, 360)  
        angulo = Utilitario.var_aleatoria(1, 0, 360)  
        função = random.choice(['sin', 'cos', 'tan'])  
        valor = round(math.sin(math.radians(angulo)), 2) if função == 'sin' else (
        round(math.cos(math.radians(angulo)), 2) if função == 'cos' else round(math.tan(math.radians(angulo)), 2)
        )

        questão = f"{função}(x) = {valor}, 0° ≤ x ≤ 360°"

        if função == 'sin':
            resposta = f"x = {angulo}°"
        elif função == 'cos':
            resposta = f"x = {angulo}°"
        else:  
            resposta = f"x = {angulo}°"

        respostaf1 = f"x = {angulo + random.randint(10, 90)}°"
        respostaf2 = f"x = {random.randint(0, 360)}°"

        while respostaf1 == resposta or respostaf2 == resposta or respostaf1 == respostaf2:
            respostaf1 = f"x = {angulo + random.randint(10, 90)}°"
            respostaf2 = f"x = {random.randint(0, 360)}°"

        dica = f"Claro, a querida trigonometria, a função é {função},\ncomo ela funciona no circulo trigonométrico?"
        dica_t = fonte_dados.render(dica, True, (0, 0, 0))

        return questão, resposta, respostaf1, respostaf2, dica

    @staticmethod
    def Quest_Derivada(fonte_dados):
        dica = (
            "Lembra que caso tenha trigonometria, 1 delas inverte,\na exponecial quase sempre é ela mesma, uma fração\nsegue a regra do quociente, você consegue..."
        )
        dica_t = fonte_dados.render(dica, True, (0, 0, 0))

        x = symbols('x')

        escolha = Utilitario.var_aleatoria(1, 1, 4)
        a, b = Utilitario.var_aleatoria(2, -5, 5)
        
        while a == 0 and b == 0:
            a, b = Utilitario.var_aleatoria(2, -5, 5)
            
        if escolha == 1:
            func = a*x**2 + b*3*x + 2
        elif escolha == 2:
            func = a*sin(x) + cos(b*x)
        elif escolha == 3:
            func = a*exp(x) + b*3*x**2
        else:
            func = (a*x**2 + 1) / (b*x + 1)

        derivada_correta = diff(func, x)

        c = Utilitario.var_aleatoria(1, -5, 5)
        
        respostaf1 = diff(func + c*x, x)
        respostaf2 = derivada_correta * Utilitario.var_aleatoria(1, 2, 3)

        while respostaf1 == derivada_correta or respostaf2 == derivada_correta or respostaf1 == respostaf2:
            c = Utilitario.var_aleatoria(1, -5, 5)
            
            respostaf1 = diff(func + c*x, x)
            respostaf2 = derivada_correta * Utilitario.var_aleatoria(1, 2, 3)

        questão = f"f(x) = {func}, f'(x) = ?"
        resposta = f"{derivada_correta}"
        respostaf1 = f"{respostaf1}"
        respostaf2 = f"{respostaf2}"

        return questão, resposta, respostaf1, respostaf2, dica
