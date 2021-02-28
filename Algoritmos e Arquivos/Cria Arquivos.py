import random


def cria_arquivo():

    # Abertura dos aquivos
    arq_Carros = open('Carros.txt', 'w')
    arq_CarrosAlvo = open('CarrosAlvo.txt', 'w')
    arq_Testes = open('Testes.txt', 'w')
    arq_TestesAlvo = open('TestesAlvo.txt', 'w')
    arq_unacceptable = open('unacceptable.txt', 'r')
    arq_acceptable = open('acceptable.txt', 'r')
    arq_good = open('good.txt', 'r')
    arq_verygood = open('verygood.txt', 'r')

    # Quantidade de Carros de cada classificação
    unacceptable = 1210
    acceptable = 384
    good = 69
    verygood = 65

    # Total de Carros
    total = 1728

    while total > 0:

        # Sorteando um número para selecionar um arquivo de caracters
        num = random.randint(0, 3)

        if num == 0:
            if unacceptable > 0:

                # Se for maior que 30% dos dados armazena em Carros
                if unacceptable > 363:
                    arquivar(arq_unacceptable, arq_Carros, arq_CarrosAlvo, num)

                # Os 30% restantes serão usados para testes
                else:
                    arquivar(arq_unacceptable, arq_Testes, arq_TestesAlvo, num)

                unacceptable -= 1
                total -= 1

        elif num == 1:
            if acceptable > 0:

                # Se for maior que 30% dos dados armazena em Carros
                if acceptable > 115:
                    arquivar(arq_acceptable, arq_Carros, arq_CarrosAlvo, num)

                # Os 30% restantes serão usados para testes
                else:
                    arquivar(arq_acceptable, arq_Testes, arq_TestesAlvo, num)

                acceptable -= 1
                total -= 1

        elif num == 2:
            if good > 0:

                # Se for maior que 30% dos dados armazena em Carros
                if good > 20:
                    arquivar(arq_good, arq_Carros, arq_CarrosAlvo, num)

                # Os 30% restants serão usados para testes
                else:
                    arquivar(arq_good, arq_Testes, arq_TestesAlvo, num)

                good -= 1
                total -= 1

        elif num == 3:
            if verygood > 0:

                # Se for maior que 30% dos dados armazena em Carros
                if verygood > 19:
                    arquivar(arq_verygood, arq_Carros, arq_CarrosAlvo, num)

                # Os 30% restantes serão usados para testes
                else:
                    arquivar(arq_verygood, arq_Testes, arq_TestesAlvo, num)

                verygood -= 1
                total -= 1

    arq_Carros.close()
    arq_CarrosAlvo.close()
    arq_Testes.close()
    arq_TestesAlvo.close()
    arq_unacceptable.close()
    arq_acceptable.close()
    arq_good.close()
    arq_verygood.close()

    print(unacceptable, acceptable, good, verygood, total)


def arquivar(arq_Leitura,  arq_Escrita, arq_EscriaAlvo, verdade):

    # Armazena no arqvuivo carros
    linha = arq_Leitura.readline()
    arq_Escrita.write(linha)

    # Armazenando no arquivo de alvo, o alvo de Carros
    arq_EscriaAlvo.write(str(verdade) + ' ')


cria_arquivo()
