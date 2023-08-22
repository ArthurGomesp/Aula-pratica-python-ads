print("Bem vindo")

print("Digite a sua altura em metros: ")
altura = input()

print("Digite o seu peso: ")
peso = input()
resultado = ""
imc = float(peso) /(float(altura) * 2 )

if imc < 18.5 :
    resultado = "esta abaixo do peso"
elif imc < 24.5 :
    resultado = "esta com peso normal"
elif imc < 29.9 :
    resultado = "esta com excesso de peso"
elif imc < 35 :
    resultado = "esta com obesidade"
elif imc > 35 :
    resultado = "esta com obesidade extrema"
print("Seu imc é de: ", "%.2f" %  imc , "você", resultado)
