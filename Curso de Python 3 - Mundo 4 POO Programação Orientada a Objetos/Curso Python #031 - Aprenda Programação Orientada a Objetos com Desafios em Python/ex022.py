# Crie a Classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)


def onOff():

    print('TV SAMSUNG')

    verificar = input('')
    ligada = False
    while True:
        verificar = input('')

        if not ligada and verificar == '@':
            print('TV LIGADA!')
            ligada = True

            continue

        else:
            ligada = False
            print('TV DESLIGADA!')


def volume():

    verificar = input('')
    volume = 0
    while True:
        atual = 0
        print(f'Volume {atual}')
        verificar = input('')
        if verificar == '+':
            if atual
            atual += 1
            continue

        elif verificar == '-':

        elif volume == 0:
            print('MUDO!')
            continue



onOff()




