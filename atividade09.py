# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).

kmpercorrido = int(input("Digite quantos KM você percorreu "))
combustivelconsumido = int(input("Digite quantos litros voçê consumiu "))

consumomedio = kmpercorrido / combustivelconsumido

print("Seu consumo médio é: ", consumomedio, "km/l")
