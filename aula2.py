salario=int(input("Qual é o seu salário atual? "))
if(salario >= 710):
    #aumento de 20% é igual salario * 1.20
    x = salario*1.20
    z = x - salario
    print("Salário atual", x)
    print("Porcentual de almento foi de 20%")
    print("Valor do almento", z)
    print("Seu novo salário" x)
elif(salario > 710 and salario <= 1000):
