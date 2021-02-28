
def main():
    arq_data = open('arquivo_pronto.txt', 'r')
    arq_acceptable = open('acceptable.txt','w')
    arq_unacceptable = open('unacceptable.txt', 'w')
    arq_good = open('good.txt', 'w')
    arq_verygood = open('verygood.txt','w')

    num_acceptable = 0
    num_unacceptable = 0
    num_good = 0
    num_verygood = 0

    for line in arq_data:
        # Se for unacceptable armazenar a linha no arquivo unacceptable
        if line[len(line) - 2] == '1':

            num_unacceptable += 1
            arquivar(line, arq_unacceptable)

        # Se for acceptable armazenar a linha no arquivo acceptable
        elif line[len(line) - 2] == '2':

            num_acceptable += 1
            arquivar(line, arq_acceptable)

        # Se for good armazenar a linha no arquivo good
        elif line[len(line) - 2] == '3':

            num_good += 1
            arquivar(line, arq_good)

        # Se for verygood armazenar a linha no arquivo verygood
        else:

            num_verygood += 1
            arquivar(line, arq_verygood)

    arq_unacceptable.close()
    arq_acceptable.close()
    arq_good.close()
    arq_verygood.close()
    arq_data.close()

    print(num_unacceptable, num_acceptable, num_good, num_verygood)


def arquivar(linha, arquivo):

    # Arquivando sem o alvo contido na linha e quebra de linha
    linha = linha[:-2]
    arquivo.write(linha + '\n')

    return


main()
