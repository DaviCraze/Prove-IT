
class Falas:

    def __init__(self, nome, falas, bloqueia_jogo=False):
        self.nome = nome
        self.falas = falas
        self.index = 0
        self.bloqueia_jogo = bloqueia_jogo
    
    def mostrar_fala(self):
        if self.index < len(self.falas):
            return f"{self.falas[self.index]["texto"]}"
        else:
            return ""
    
    def mostrar_posicao(self):
        if self.index < len(self.falas):
            return f"{self.falas[self.index]["posicao"]}"
        else:
            return "topo"

    def proximo(self):
        if self.index < len(self.falas) - 1:
            self.index += 1
        else:
            self.terminar()
    
    def terminar(self):
        self.index = len(self.falas)
   
    def acabou(self):
         return self.index >= len(self.falas)
    
    @property
    def mostrar_index(self):
        return self.index

cutscene_falas = {
    "boas_vindasL": Falas("boas_vindasL", [
        {"texto": "Ah! Saudações pequeno amigo, bem vindo a minha LOJA!\nAqui temos bastante variedades de produtos\nque irão te ajudar na sua jornada!", "posicao": "topo"},
        {"texto": "Percebi que você foi selecionado para se transformar numa IA,\ncerto?", "posicao": "topo"},
        {"texto": "Isso é incrivel!(Pelo menos pra você...)", "posicao": "topo"},
        {"texto": "Enfim, fique a vontade para escolher algum produto.", "posicao": "topo"},
        {"texto": "Passe por cima do produto para ver as informações dele\ne aperte o botão ENTER para comprar o produto\n(se voce tiver grana claro)", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "glados1encontro": Falas("glados1encontro", [
        {"texto": "MEU DEUS, OLHA SO PARA VOCÊ!!! TEMOS UM NOVO MEMBRO\nNO NOSSO TIME!", "posicao": "topo"},
        {"texto": "BEM VINDO, VOCÊ PODE ME CHAMAR DE A.V.A, OU DE\nASSISTENTE VIRTUAL ALTRUISTA!", "posicao": "topo"},
        {"texto": "VOCÊ SABE PORQUE ESTA AQUI, CERTO?", "posicao": "topo"},
        {"texto": "CEEEERTO...?", "posicao": "topo"},
        {"texto": "VOCÊ ESTA AQUI PARA SE TORNAR UMA IA, UMA INTELIGENCIA\nARTIFICIAL CAPAZ DE AJUDAR O MUNDO COM SUAS\nDIVERSAS FUNÇÕES.", "posicao": "topo"},
        {"texto": "VOCÊ ESTA AQUI PARA NOS AJUDAR A ALCANÇAR A GLORIOSA\nEVOLUÇÃO TECNOLOGICA!", "posicao": "topo"},
        {"texto": "POR ISSO CRIEI ESTE TESTE PARA TE AJUDAR NESSA\nJORNADA INCRIVEL E DIVERTIDA!", "posicao": "topo"},
        {"texto": "VAMOS COMEÇAR ENTÃO? OTIMO! DEIXE EU PASSAR OS\nPRIMEIROS PASSOS PARA VOCÊ.", "posicao": "topo"},
        {"texto": "SUA FUNÇÃO É RESPONDER QUESTÕES MATEMATICAS ALEATORIAS,\nCADA SALA IRA CONTER UMA QUESTÃO DIFERENTE DA OUTRA.", "posicao": "topo"},
        {"texto": "SUA PERGUNTA SE ENCONTRA NA PAREDE NO MEIO DELA. A PERGUNTA\nPODE SER TANTO UMA FUNÇÃO MATEMATICA OU\nUMA QUESTÃO LOGICA.", "posicao": "baixo"},
        {"texto": "AQUI EMBAIXO SE ENCONTRA AS RESPOSTAS DA SUA PERGUNTA,\nCADA PORTA IRA CONTER UMA RESPOSTA, SENDO FALSA\nOU VERDADEIRA. ANDE ATÉ A PORTA E CLIQUE ENTER\nPARA SELECIONAR ELA.", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "erro1": Falas("erro1", [
        {"texto": "bleh", "posicao": "topo"},
        {"texto": "AAAH NÃO, VOCÊ ERROU A RESPOSTA!", "posicao": "topo"},
        {"texto": "MAS TUDO BEM, NÃO É COMO SE FOSSE O FIM DO MUNDO.\nVOCÊ AINDA TEM MUITAS CHANCES PARA MOSTRAR SEU\nBRILHO!!!", "posicao": "topo"},
        {"texto": "COMO VOCÊ PODE VER, NO CANTO DA TELA TEMOS\nA QUANTIDADE DE VEZES NA QUAL VOCÊ PODE\nERRAR UMA QUESTÃO", "posicao": "topo"},
        {"texto": "A COR REPRESENTA A QUANTIDADE DE VIDAS QUE VOCÊ TEM.\nAMARELO SENDO 3 VIDAS, LARANJA 2 VIDAS\nE VERMELHO 1 VIDA", "posicao": "topo"},
        {"texto": "ENTÃO VAMOS LA! TENTE DE NOVO, EU SEI QUE VOCÊ\nCONSEGUE!", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "acerto": Falas("acerto", [
        {"texto": "pu", "posicao": "topo"},
        {"texto": "PARABENS!!!! VOCÊ ACERTOU A QUESTÃO! ISSO FOI\nINCRIVEL! ESTOU TAO ORGULHOSA T_T", "posicao": "topo"},
        {"texto": "DESCULPA, ME EMOCIONEI MESMO EU SENDO UM ROBO\nQUE NÃO CONSEGUE DERRAMAR LAGRIMAS DE EMOÇÃO.", "posicao": "topo"},
        {"texto": "VOLTANDO PRO PROMPT....", "posicao": "topo"},
        {"texto": "VOCÊ CONSEGUIU ACERTAR A QUESTÃO! AGORA VOCÊ\nGANHOU PONTOS QUE DEMONSTRA SEU DESEMPENHO\nE SUA HONRA NA EMPRESA!", "posicao": "topo"},
        {"texto": "SEUS PONTOS FICAM ACUMULADOS ALI NO CANTO DA TELA.\nCADA FORMATO DE QUESTÃO IRA TE DAR UMA QUANTIDADE\nDE PONTOS DIFERENTES.", "posicao": "baixo"},
        {"texto": "VAMOS VER COM QUANTOS PONTOS VOCÊ VAI ESTAR\nNO FINAL DA SUA JORNADA!", "posicao": "baixo"},
        {"texto": "ALIAS, UMA INFORMAÇÃO IMPORTANTE, VOCÊ TERÁ QUE\nRESPONDER QUESTÕES ATÉ A SALA 100, SIM, ISSO\nMESMO, SALA Nº100...", "posicao": "topo"},
        {"texto": "EU SEI QUE PARECE UMA LONGA JORNADA, MAS TENHO\nCERTEZA QUE VOCÊ IRA CHEGAR ATÉ O FIM!", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "saladesafio": Falas("saladesafio", [
        {"texto": "miau", "posicao": "topo"},
        {"texto": "VOCÊ CONSEGUIU CHEGAR NA SALA 10!!! VOCÊ EVOLUIU\nTÃO RAPIDO...QUE ORGULHO T_T", "posicao": "topo"},
        {"texto": "DESCULPA... PROMETO NAO ME EMOCIONAR DE NOVO(EU ACHO)", "posicao": "topo"},
        {"texto": "VOLTANDO AO PROMPT...", "posicao": "topo"},
        {"texto": "VOCÊ CHEGOU NA SALA DESAFIO!! UMA SALA NA QUAL CONTEM\nUMA QUESTÃO DESAFIO, QUE SERA MAIS DIFICIL QUE AS OUTRAS\nQUE VOCÊ JA RESPONDEU...", "posicao": "topo"},
        {"texto": "EM CADA SALA 10,20,30...ATÉ A SALA 100, ESSAS SALAS\nDESAFIO IRÃO APARECER PARA DIFICULTAR SUA CONCLUSAO.\nOU MELHOR DIZENDO, TE ENTREGAR MAIS INTELIGENCIA\nE INFORMAÇÕES", "posicao": "topo"},
        {"texto": "NESSAS SALAS VOCÊ TERÁ UMA QUESTÃO LOGICA DE MATEMATICA\nNA QUAL VOCÊ TERÁ APENAS QUE RESPONDER SIM OU NÃO\nPARA A QUESTÃO, BEM SIMPLES NÉ?", "posicao": "baixo"},
        {"texto": "CASO VOCÊ ACERTE A QUESTÂO, VOCÊ IRA GANHAR 35 PONTOS!", "posicao": "topo"},
        {"texto": "SÓ ESCOLHER A PORTA COM A RESPOSTA QUE VOCÊ ACHA SER\nA CERTA!", "posicao": "topo"}
    ], bloqueia_jogo=True)
}
                    
