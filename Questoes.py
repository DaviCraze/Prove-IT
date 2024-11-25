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
# Adicionar pelo menos mais 2 tipos de questões


# Tipo de questão em avaliação, pode ou não ir para o código final
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
