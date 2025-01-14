def processar_dados(lista_numeros):
    if not lista_numeros:
        return None
    

    total = 0
    maior = lista_numeros[0]
    menor = lista_numeros[0]

    for numero in lista_numeros:
        total += numero
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    



    media = round(total / len(lista_numeros), 2)

    return {
        "média": media,
        "maior": maior,
        "menor": menor,
        "total": total
}

dados_sensor = [23,25,21,24,22,26,28,24]
resultados = processar_dados(dados_sensor)
print("Resultados da análise:")
for chave, valor in resultados.items():
    print(f"{chave}: {valor}")


