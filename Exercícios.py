salario = float(input("Digite o salário do colaborador: "))

if salario <= 280.00:
    percentual_aumento = 20
elif salario <= 700.00:
    percentual_aumento = 15
elif salario <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)

novo_salario = salario + aumento

taxa_inflacao = 0.038
aumento_real = aumento - (aumento * taxa_inflacao)

print("Salário antes do reajuste: R$", salario)
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$", aumento)
print("Novo salário após o aumento: R$", novo_salario)
print("Valor do aumento real, descontada a inflação: R$", aumento_real)
