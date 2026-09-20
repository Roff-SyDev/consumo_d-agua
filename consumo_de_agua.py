# Importando "libraries".

import time

# Pedindo informações necessárias.

time.sleep(0.1)

propType = int(input("Digite o tipo de imóvel (1 - Comercial |  2 - Apartamento | 3 - Casa): ")) # Limita a variável a ser um valor inteiro, não uma string.
while propType >= 4:
    propType = int(input("Tipo de imóvel inexistente. Digite o tipo de imóvel (1 - Comercial | 2 - Casa | 3 - Apartamento): "))
# O loop "while" previne que o usuário digite qualquer valor fora dos três disponíveis, dando uma espécie de "travada" no código antes de prosseguir.
waterCons = float(input("Digite o consumo mensal de água em metros cúbicos (m³): ")) # Pede o valor decimal do consumo de água por mês.

# Condicionais para cada caso.
if propType == 1: # "Se o tipo de imóvel for Comercial."
    print("Tarifa comercial aplicada. Verifique seu plano corporativo.")

elif propType == 2 and waterCons < 10: # "Se o tipo de imóvel for Apartamento e o consumo de água for menor que 10 m³."
    print("Consumo econômico. Excelente controle do consumo de água!")
    
elif propType == 2 | 3 and waterCons < 25: # "Se o tipo de imóvel for Apartamento ou Casa e o consumo de água for menor que 25 m³."
    print("Consumo moderado, porém dentro dos padrão residencial.")

elif waterCons > 25: # "Se o consumo de água for maior que 25 m³ (limite residencial)."
    print("Consumo excessivo, adote medidas de economia e procure por vazamentos.")

'''
-- Comentários Finais --

Enquanto eu desenvolvia esse código, tentei utilizar do formato de "cases" do "match", porém optei por utilizar "elif" por ser uma estrutura que, mesmo não tão limpa,
tornou-se levemente mais prática de ser elaborada.
'''
