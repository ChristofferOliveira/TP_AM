

def main():
    cria_arquivo()


def cria_arquivo():

    arq_data = open('teste.txt', 'r')
    arq_pronto = open('arquivo_pronto.txt', 'w')

    for line in arq_data:

        #Cria uma lista separando pela virgula
        linha_sem_virgula = line.split(',')

        linha_pronta = padroniza_linha(linha_sem_virgula)

        arq_pronto.write(linha_pronta)

    arq_data.close()
    arq_pronto.close()


# Coloca numeros no lugar das palavras
def padroniza_linha(linha_sem_virgula):

    linha_semipronta = ' '.join(map(str, linha_sem_virgula))

    linha_pronta = linha_semipronta.replace('vhigh', '4')
    linha_pronta = linha_pronta.replace('high', '3')
    linha_pronta = linha_pronta.replace('med', '2')
    linha_pronta = linha_pronta.replace('low', '1')
    linha_pronta = linha_pronta.replace('5more', '5')
    linha_pronta = linha_pronta.replace('more', '5')
    linha_pronta = linha_pronta.replace('small', '1')
    linha_pronta = linha_pronta.replace('big', '3')
    linha_pronta = linha_pronta.replace('unacc', '1')
    linha_pronta = linha_pronta.replace('acc', '2')
    linha_pronta = linha_pronta.replace('vgood', '4')
    linha_pronta = linha_pronta.replace('good', '3')

    return linha_pronta


main()