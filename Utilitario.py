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
        return 0
    
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
        
