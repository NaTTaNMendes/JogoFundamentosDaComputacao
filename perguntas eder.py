import time

respostasJogador = {}

def mensagemErro():
    print("\n" * 130)
    print("Erro, valor inválido")
    time.sleep(1.5)
    print("\n" * 130)

def processarResposta(resposta):
    alternativas = ["A", "B", "C", "D"]
    resposta = str(resposta)
    resposta = resposta.upper()
    if (len(resposta) > 1):
        raise Exception()
    if not(resposta in alternativas):
        raise Exception()
    return resposta

def verificarResposta(numero, resposta):
    gabarito = {'1': 'A'}
    respostasJogador[str(numero)] = resposta
    if respostasJogador[str(numero)] == gabarito[str(numero)]:
        print("Acertou")
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
        print("Uma pergunta será mostrada e você deverá digitar a resposta que acha correta! Somente uma das alternativas está certa.")
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
            resposta = processarResposta(resposta)
            if verificarResposta(1, resposta):
                break   
        except:
            mensagemErro()

if __name__=="__main__":
    main()