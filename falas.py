
class Falas:

    def __init__(self, nome, falas, bloqueia_jogo=False):
        self.nome = nome
        self.falas = falas
        self.index = 0
        self.bloqueia_jogo = bloqueia_jogo
    
    def mostrar_fala(self):
        if self.index < len(self.falas):
            return f"{self.falas[self.index]['texto']}"
        else:
            return ""
    
    def mostrar_posicao(self):
        if self.index < len(self.falas):
            return f"{self.falas[self.index]['posicao']}"
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
        {"texto": "Ah! Saudações pequeno amigo, bem vindo a\nminha LOJA! Aqui temos bastante\nvariedades de produtos que irão\nte ajudar na sua jornada!", "posicao": "topo"},
        {"texto": "Percebi que você foi selecionado para se\ntransformar numa IA, certo?", "posicao": "topo"},
        {"texto": "Isso é incrivel!(Pelo menos pra você...)", "posicao": "topo"},
        {"texto": "Enfim, fique a vontade para escolher algum\nproduto.", "posicao": "topo"},
        {"texto": "Passe por cima do produto para ver as\ninformações dele e aperte o botão ENTER\npara comprar o produto\n(se voce tiver grana claro)", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "glados1encontro": Falas("glados1encontro", [
        {"texto": "MEU DEUS, OLHA SO PARA VOCÊ!!! TEMOS UM NOVO\nMEMBRO NO NOSSO TIME!", "posicao": "topo"},
        {"texto": "BEM VINDO, VOCÊ PODE ME CHAMAR DE A.V.A, OU\nDE ASSISTENTE VIRTUAL ALTRUISTA!", "posicao": "topo"},
        {"texto": "VOCÊ SABE PORQUE ESTA AQUI, CERTO?", "posicao": "topo"},
        {"texto": "CEEEERTO...?", "posicao": "topo"},
        {"texto": "VOCÊ ESTA AQUI PARA SE TORNAR UMA IA, UMA\nINTELIGENCIA ARTIFICIAL CAPAZ DE AJUDAR\nO MUNDO COM SUAS DIVERSAS FUNÇÕES.", "posicao": "topo"},
        {"texto": "VOCÊ ESTA AQUI PARA NOS AJUDAR A ALCANÇAR A\nGLORIOSA EVOLUÇÃO TECNOLOGICA!", "posicao": "topo"},
        {"texto": "POR ISSO CRIEI ESTE TESTE PARA TE AJUDAR\nNESSA JORNADA INCRIVEL E DIVERTIDA!", "posicao": "topo"},
        {"texto": "VAMOS COMEÇAR ENTÃO? OTIMO! DEIXE EU PASSAR\nOS PRIMEIROS PASSOS PARA VOCÊ.", "posicao": "topo"},
        {"texto": "SUA FUNÇÃO É RESPONDER QUESTÕES MATEMATICAS\nALEATORIAS, CADA SALA IRA CONTER UMA\nQUESTÃO DIFERENTE DA OUTRA.", "posicao": "topo"},
        {"texto": "SUA PERGUNTA SE ENCONTRA NA PAREDE NO MEIO\nDELA. A PERGUNTA PODE SER TANTO UMA\nFUNÇÃO MATEMATICA OU UMA QUESTÃO LOGICA.", "posicao": "baixo"},
        {"texto": "AQUI EMBAIXO SE ENCONTRA AS RESPOSTAS DA SUA\nPERGUNTA, CADA PORTA IRA CONTER UMA\nRESPOSTA, SENDO FALSA OU VERDADEIRA.\nANDE ATÉ A PORTA E CLIQUE ENTER\nPARA SELECIONAR ELA.", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "erro1": Falas("erro1", [
        {"texto": "bleh", "posicao": "topo"},
        {"texto": "AAAH NÃO, VOCÊ ERROU A RESPOSTA!", "posicao": "topo"},
        {"texto": "MAS TUDO BEM, NÃO É COMO SE FOSSE O FIM DO\nMUNDO. VOCÊ AINDA TEM MUITAS CHANCES\nPARA MOSTRAR SEU BRILHO!!!", "posicao": "topo"},
        {"texto": "COMO VOCÊ PODE VER, NO CANTO DA TELA TEMOS\nA QUANTIDADE DE VEZES NA QUAL VOCÊ PODE\nERRAR UMA QUESTÃO", "posicao": "topo"},
        {"texto": "A COR REPRESENTA A QUANTIDADE DE VIDAS QUE\nVOCÊ TEM. AMARELO SENDO 3 VIDAS,\nLARANJA 2 VIDAS E VERMELHO 1 VIDA", "posicao": "topo"},
        {"texto": "ENTÃO VAMOS LA! TENTE DE NOVO, EU SEI QUE\nVOCÊ CONSEGUE!", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "acerto": Falas("acerto", [
        {"texto": "pu", "posicao": "topo"},
        {"texto": "PARABENS!!!! VOCÊ ACERTOU A QUESTÃO! ISSO\nFOI INCRIVEL! ESTOU TAO ORGULHOSA T_T", "posicao": "topo"},
        {"texto": "DESCULPA, ME EMOCIONEI MESMO EU SENDO UM\n ROBO QUE NÃO CONSEGUE DERRAMAR LAGRIMAS\nDE EMOÇÃO.", "posicao": "topo"},
        {"texto": "VOLTANDO PRO PROMPT....", "posicao": "topo"},
        {"texto": "VOCÊ CONSEGUIU ACERTAR A QUESTÃO! AGORA VOCÊ\nGANHOU PONTOS QUE DEMONSTRA SEU\nDESEMPENHO E SUA HONRA NA EMPRESA!", "posicao": "topo"},
        {"texto": "SEUS PONTOS FICAM ACUMULADOS ALI NO CANTO\nDA TELA. CADA FORMATO DE QUESTÃO IRA TE\nDAR UMA QUANTIDADE DE PONTOS DIFERENTES.", "posicao": "baixo"},
        {"texto": "VAMOS VER COM QUANTOS PONTOS VOCÊ VAI ESTAR\nNO FINAL DA SUA JORNADA!", "posicao": "baixo"},
        {"texto": "ALIAS, UMA INFORMAÇÃO IMPORTANTE, VOCÊ TERÁ\nQUE RESPONDER QUESTÕES ATÉ A SALA 100,\nSIM, ISSO MESMO, SALA Nº100...", "posicao": "topo"},
        {"texto": "EU SEI QUE PARECE UMA LONGA JORNADA, MAS\nTENHO CERTEZA QUE VOCÊ IRA CHEGAR ATÉ O\nFIM!", "posicao": "topo"}
    ], bloqueia_jogo=True),
    "saladesafio": Falas("saladesafio", [
        {"texto": "miau", "posicao": "topo"},
        {"texto": "VOCÊ CONSEGUIU CHEGAR NA SALA 10!!! VOCÊ \nEVOLUIU TÃO RAPIDO...QUE ORGULHO T_T", "posicao": "topo"},
        {"texto": "DESCULPA... PROMETO NAO ME EMOCIONAR DE NOVO(EU ACHO)", "posicao": "topo"},
        {"texto": "VOLTANDO AO PROMPT...", "posicao": "topo"},
        {"texto": "VOCÊ CHEGOU NA SALA DESAFIO!! UMA SALA NA\nQUAL CONTEM UMA QUESTÃO DESAFIO, QUE SERA\nMAIS DIFICIL QUE AS OUTRAS QUE VOCÊ\nJA RESPONDEU...", "posicao": "topo"},
        {"texto": "EM CADA SALA 10,20,30...ATÉ A SALA 100, \nESSAS SALAS DESAFIO IRÃO APARECER PARA\nDIFICULTAR SUA CONCLUSAO. OU MELHOR\nDIZENDO, TE ENTREGAR MAIS INTELIGENCIA E INFORMAÇÕES", "posicao": "topo"},
        {"texto": "NESSAS SALAS VOCÊ TERÁ UMA QUESTÃO LOGICA\nDE MATEMATICA NA QUAL VOCÊ TERÁ APENAS\nQUE RESPONDER SIM OU NÃO PARA A QUESTÃO,\nBEM SIMPLES NÉ?", "posicao": "baixo"},
        {"texto": "CASO VOCÊ ACERTE A QUESTÂO, VOCÊ IRA GANHAR\n35 PONTOS!", "posicao": "topo"},
        {"texto": "SÓ ESCOLHER A PORTA COM A RESPOSTA QUE VOCÊ\nACHA SER A CERTA!", "posicao": "topo"}
    ], bloqueia_jogo=True)
}
                    
