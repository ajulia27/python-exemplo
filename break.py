print('operação de divisão')
while true:
     n1=int(input('informe o primeiro numero: '))
     n2=int(input('informe o segundo numero: '))
     if n2 == 0:
          print('divisor não pode ser 0')
          break
        print(f"{n1} / {n2} = {n1/n2}")
        print (f"{20 * 'x'}")
print ('fim do programa')