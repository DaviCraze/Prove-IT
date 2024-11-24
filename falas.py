
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
        {"texto": "AAAH NÃO, VOCÊ ERROU A RESPOSTA!", "posicao": "topo"},
        {"texto": "MAS TUDO BEM, NÃO É COMO SE FOSSE O FIM DO MUNDO.\nVOCÊ AINDA TEM MUITAS CHANCES PARA MOSTRAR SEU\nBRILHO!!!", "posicao": "topo"},
        {"texto": "COMO VOCÊ PODE VER, NO CANTO DA TELA TEMOS\nA QUANTIDADE DE VEZES NA QUAL VOCÊ PODE\nERRAR UMA QUESTÃO", "posicao": "topo"},
        {"texto": "A COR REPRESENTA A QUANTIDADE DE VIDAS QUE VOCÊ TEM.\nAMARELO SENDO 3 VIDAS, LARANJA 2 VIDAS\nE VERMELHO 1 VIDA", "posicao": "topo"},
        {"texto": "ENTÃO VAMOS LA! TENTE DE NOVO, EU SEI QUE VOCÊ\nCONSEGUE!", "posicao": "topo"}
    ], bloqueia_jogo=True)
}
                    