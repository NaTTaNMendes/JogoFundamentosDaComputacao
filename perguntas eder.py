import time

respostasJogador = {}

def mensagemErro():
    print("\n" * 130)
    print("Erro, valor inválido")
    time.sleep(1.5)
    print("\n" * 130)

def verificarResposta(numero, resposta):
    alternativas = ["A", "B", "C", "D"]
    resposta = str(resposta)
    resposta = resposta.upper()
    gabarito = {'1': 'A', '2' : 'C', '3' : 'D', '4' : 'B', '5' : 'A', '6' : 'B', '7' : 'C', '8' : 'A', '9' : 'D'}
    if (len(resposta) > 1):
        raise Exception()
    if not(resposta in alternativas):
        raise Exception() 
    respostasJogador[str(numero)] = resposta
    if respostasJogador[str(numero)] == gabarito[str(numero)]:
        print("Acertou")
        time.sleep(1.5)
        print("\n" * 130)
        return True
    else:
        print("Errou")
        time.sleep(1.5)
        print("\n" * 130)
        return False

def main():   
    while True:
        print("JOGO DE PERGUNTAS SOBRE FUNDAMENTOS DA COMPUTAÇÂO")
        print()
        print("Funcionamento:")
        print("Uma pergunta será mostrada e você deverá digitar a resposta correta (ou a mais correta entre as alternativas)! Somente uma das alternativas será considerada.")
        entrada = input()
        if entrada != None:
            break

    while True:
        print("PERGUNTA 1:")
        print()
        print("O que é um programa?")
        print()
        print("A - Um conjunto de instruções descrevendo como realizar determinada tarefa")
        print("B - Um componente do computador")
        print("C - Um método utilizado por cientistas da computação")
        print("D - É um ícone que aparece na área de trabalho")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(1, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 2:")
        print()
        print("Qual é a definição de uma máquina virtual(Tanembaum)?")
        print()
        print("A - Um computador sendo emulado por software dentro de um computador físico")
        print("B - Uma máquina disponível pela internet")
        print("C - Um conceito que está ligado aos níveis do computador, pensamos na máquina virtual em como sendo uma máquina real Mn que opera uma linguagem Ln, assim não dando nenhuma preocupação para o programador sobre os níveis mais abaixo do sistema")
        print("D - Simula o software do Sistema Operacional")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(2, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 3:")
        print()
        print("O que é traduzir?")
        print()
        print("A - É a tradução de uma linguagem para outra")
        print("B - O computador coleta uma instrução, a traduz e executa. Realizando esse processo sobre cada instrução em tempo real.")
        print("C - A instrução é coletada em um nível superior e é diretamente transfomada no nível 0 da máquina")
        print("D - Todo o programa é traduzido até o nível ISA por algum compilador, alocado na memória principal e executado")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(3, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 4:")
        print()
        print("Qual é a ordem correta dos níveis de máquina")
        print()
        print("A - Nível de microarquitetura - nível lógico digital - nível de SO - nível de arquitetura do conjunto de instrução - nível de linguagem Assembly - Nível de POO")
        print("B - Nível lógico digital - nível de microarquitetura - nível de arquitetura do conjunto de instrução - nível de SO - nível de linguagem Assembly - Nível de POO")
        print("C - Nível de POO - nível lógico digital - nível de SO - nível de arquitetura do conjunto de instrução - nível de microarquitetura - nível de linguagem Assembly")
        print("D - Nível de SO - nível lógico digital - nível de microarquitetura - nível de arquitetura do conjunto de instrução - nível de linguagem Assembly - Nível de POO")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(4, resposta):
                break   
        except:
            mensagemErro()

    while True:
        print("PERGUNTA 5:")
        print()
        print("Do que é composto o nível 1?")
        print()
        print("A - 8 a 32 registradores e a ULA")
        print("B - Portas lógicas")
        print("C - Linguagem de montagem (Assembly)")
        print("D - Sistema Operacional")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(5, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 6:")
        print()
        print("Quais níveis costumam ser híbridos?")
        print()
        print("A - 1 e 2")
        print("B - 2 e 3")
        print("C - 4 e 5")
        print("D - 0 e 1")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(6, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 7:")
        print()
        print("O que é um pipeline?")
        print()
        print("A - É um barramento que leva os dados dos registradores até a ULA")
        print("B - É a busca, decodificação e execução de duas ou mais instruções simultâneamente")
        print("C - É o processo onde a CPU tem unidades de busca, decodificação e execução separadas. Fazendo assim com que enquanto ela está executando a instrução N ela pode também estar decodificando a instrulção N + 1 e buscando a instrução N + 2")
        print("D - São os canos de cobre que ficam no dissipador do processador")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(7, resposta):
                break   
        except:
            mensagemErro()

    while True:
        print("PERGUNTA 8:")
        print()
        print("O que é um microcontrolador?")
        print()
        print("A - São computadores pequenos, completos e geralmente executam um número determinado de operações em tempo real")
        print("B - É um mini componente localizado dentro do processador para que sejam controladas as partes do computador")
        print("C - É um mini sistema de controle destinado às indústrias")
        print("D - São computadores pequenos, incompletos, programáveis e de baixo custo")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(8, resposta):
                break   
        except:
            mensagemErro()
    
    while True:
        print("PERGUNTA 9:")
        print()
        print("Suponha que cada um dos 300 milhões de habitantes dos Estados Unidos consome totalmente dois pacotes de mercadoria por dia marcados com etiquetas RFID.? Dado o tamanho do PIB como 20 trilhões, o ano como 365 dias e o preço da etiqueta como um centavo, qual seria porcentagem em relação ao PIB para a aplicação dessa tecnologia")
        print()
        print("A - 0.002 %")
        print("B - 2 %")
        print("C - 0.001 %")
        print("D - 0.01 %")
        print()
        resposta = input("Sua resposta: ")
        try:   
            if verificarResposta(9, resposta):
                break   
        except:
            mensagemErro()

if __name__=="__main__":
    main()