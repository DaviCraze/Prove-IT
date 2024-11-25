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

        todas_as_sprites.draw(tela)
        todas_as_sprites.update(teclas)
        return b_continuar, b_dica, b_vida, b_booster, tex_dica, tex_booster, tex_vida
