# faturamento = {
#     "Jan": 'R$ 15000,00',
#     "Fev": 'R$ 18000,00',
#     "Mar": 'R$ 17000,00',
#     "Abr": 'R$ 16000,00',
#     "Mai": 'R$ 20000,00',
#     "Jun": 'R$ 21000,00',
#     "Jul": 'R$ 19000,00',
#     "Ago": 'R$ 22000,00',
#     "Set": 'R$ 23000,00',
#     "Out": 'R$ 24000,00',
#     "Nov": 'R$ 25000,00',
#     "Dez": 'R$ 26000,00'
# }

# def transformar_numero(texto):
#     texto = texto.replace("R$", "")
#     texto = texto.replace(" ", "")
#     texto = texto.replace(".", "")
#     texto = texto.replace(",", ".")
#     valor = float(texto)
#     return valor

# def calcular_imposto_mensal(valor_faturamento):
#     iss = valor_faturamento * 0.05
#     pis = valor_faturamento * 0.0065
#     cofins = valor_faturamento * 0.03
#     imposto_mensal = iss + pis + cofins
#     return imposto_mensal

# def calcular_imposto_trimestral(valor_faturamento):
#     ir = valor_faturamento * 0.048
#     csll = valor_faturamento * 0.09
#     adicional_ir = 0
#     if valor_faturamento > 20000:
#         adicional_ir = (valor_faturamento - 20000) * 0.1
#     imposto_trimestral = ir + csll + adicional_ir
#     return imposto_trimestral

# for mes in faturamento:
#     valor_faturamento = transformar_numero(faturamento[mes])
#     print(f"Valor Faturamento ({mes}): {valor_faturamento}")
#     imposto_mensal = calcular_imposto_mensal(valor_faturamento)
#     imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)
#     print(f"Faturamento: R$ {valor_faturamento:.2f}")
#     print(f"Imposto Mensal: R$ {imposto_mensal:.2f}")
#     print(f"Imposto Trimestral: R$ {imposto_trimestral:.2f}")
#     print("-" * 30)


faturamento = {
    "Jan": 'R$ 15000,00',
    "Fev": 'R$ 18000,00',
    "Mar": 'R$ 17000,00',
    "Abr": 'R$ 16000,00',
    "Mai": 'R$ 20000,00',
    "Jun": 'R$ 21000,00',
    "Jul": 'R$ 19000,00',
    "Ago": 'R$ 22000,00',
    "Set": 'R$ 23000,00',
    "Out": 'R$ 24000,00',
    "Nov": 'R$ 25000,00',
    "Dez": 'R$ 26000,00'
}

def transformar_numero(texto):
    texto = texto.replace("R$", "")
    texto = texto.replace(" ", "")
    texto = texto.replace(".", "")
    texto = texto.replace(",", ".")
    valor = float(texto)
    return valor

def calcular_imposto_mensal(valor_faturamento):
    iss = valor_faturamento * 0.05
    pis = valor_faturamento * 0.0065
    cofins = valor_faturamento * 0.03
    imposto_mensal = iss + pis + cofins
    return imposto_mensal

def calcular_imposto_trimestral(valor_faturamento):
    ir = valor_faturamento * 0.048
    csll = valor_faturamento * 0.09
    adicional_ir = 0
    if valor_faturamento > 20000:
        adicional_ir = (valor_faturamento - 20000) * 0.1
    imposto_trimestral = ir + csll + adicional_ir
    return imposto_trimestral

resultado = {}
for mes in faturamento:
    valor_faturamento = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor_faturamento)
    imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)
    resultado[mes] = {
        "Faturamento": valor_faturamento,
        "Imposto Mensal": imposto_mensal,
        "Imposto Trimestral": imposto_trimestral
    }

print(resultado)