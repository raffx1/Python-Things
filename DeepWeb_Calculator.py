while True:
    resp = int(input('Quer conhecer minha calculadora?\n1 - Sim\n2 - Não\nResponda:'))
    if resp == 1:
        print('Okay')
        num1 = int(input('Digite o primeiro numero:'))
        num2 = int(input('Digite o segundo numero:'))
        resp4 = int(input('Você deseja acrescentar mais algum numero?\n1 - Sim\n2 - Não\nResponda:'))
        if resp4 == 1:
            num3 = int(input('Digite o terceiro numero:'))
        else:
            resp2 = int(input(
                'Você quer fazer o que com esses numeros?\n1 - Adicionar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\nResponda:'))
            if resp2 == 1:
                print(f'O resultado é {num1 + num2}')
                resp3 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
                if resp3 == 1:
                    continue
                if resp3 == 2:
                    break
            elif resp2 == 2:
                print(f'O resultado é {num1 - num2}')
                resp3 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
                if resp3 == 1:
                    continue
                if resp3 == 2:
                    break
            elif resp2 == 3:
                print(f'O resultado é {num1 * num2}')
                resp3 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
                if resp3 == 1:
                    continue
                if resp3 == 2:
                    break
            elif resp2 == 4:
                print(f'O resultado é {num1 / num2}')
                resp3 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
                if resp3 == 1:
                    continue
                if resp3 == 2:
                    break
            else:
                print('Seu imbecil, é de 1 a 4')
                continue
        resp5 = int(input('Você quer fazer o que com esses numeros?\n1 - Adicionar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\nResponda:'))
        if resp5 == 1:
            print(f'O resultado é {num1 + num2 + num3}')
            resp6 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
            if resp6 == 1:
                continue
            if resp6 == 2:
                break
        elif resp5 == 2:
            print(f'O resultado é {num1 - num2 - num3}')
            resp6 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
            if resp6 == 1:
                continue
            if resp6 == 2:
                break
        elif resp5 == 3:
            print(f'O resultado é {num1 * num2 * num3}')
            resp6 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
            if resp6 == 1:
                continue
            if resp6 == 2:
                break
        elif resp5 == 4:
            print(f'O resultado é {num1 / num2 / num3}')
            resp6 = int(input('Deseja fazer de novo?\n1 - Sim\n2 - Não\nResponda:'))
            if resp6 == 1:
                continue
            if resp6 == 2:
                break
        else:
            print('Seu imbecil, é de 1 a 4')
            continue
    else:
        print('Foda-se')
        break