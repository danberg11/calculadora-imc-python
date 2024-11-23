def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de IMC")
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")

if __name__ == "__main__":
    main()
