somar = 1
subtrair = 2
multiplicar = 3
dividir = 4


conta = int(input( "1 para soma, 2 para subtrair, 3 para multiplicar, 4 para dividir"))

x = int(input("Digite o primeiro numero"))
z = int(input("Digite o segundo numero"))

if conta == 1:
    print(z + x)
elif conta == 2:
    print(x-z)
elif conta == 3:
    print(x * z)
elif conta == 4:
    print(x / z)
else:
    print("Operação Inválida")