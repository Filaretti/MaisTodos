class ValidCPF:

    def __init__(self, cpf):
        self.cpf = cpf

    def reorgCPF(self):
        self.cpf = self.cpf[:9], self.cpf[9:]
        print(self.cpf)

    def validCPF(self):
        invalidos = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444',
                     '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']

        if self.cpf in invalidos:
            return False
        print(len(self.cpf))
        if len(self.cpf) != 11:
            return False

        self.reorgCPF()
        print(self.cpf)

        peso = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0

        for i, item in enumerate(self.cpf[0]):
            # print(item)
            soma += int(item) * peso[i]

        # print(soma)
        dig1 = soma % 11

        if (dig1 < 2):
            digit1 = '0'
        else:
            digit1 = str(11 - dig1)

        # print('primeiro digito',digit1, self.cpf[1])

        if (digit1 != self.cpf[1][0]):
            return False

        peso.insert(0, 11)

        soma = 0

        for i, item in enumerate(peso):

            if (i < len(self.cpf[0])):
                soma += item * int(self.cpf[0][i])
                # print(item, int(self.cpf[0][i]))
            else:
                soma += item * int(digit1)
                # print(item, digit1)

        dig2 = soma % 11

        # print('Digito 2: resto e nums',dig2, self.cpf[1])

        if (dig2 < 2):
            digit2 = "0"
        else:
            digit2 = str(11 - dig2)

        # print(digit1+digit2, self.cpf[1])

        if (digit1 + digit2 != self.cpf[1]):
            return False

        return True
