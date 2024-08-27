
def main():
    total_numeros = 0
    soma = 0

    while True:
        try:
            numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        if numero == 0:
            break

        total_numeros += 1
        soma += numero

    if total_numeros > 0:
        media = soma / total_numeros
        print(f"Quantidade de números digitados: {total_numeros}")
        print(f"Soma dos números digitados: {soma}")
        print(f"Média dos números digitados: {media:.2f}")
    else:
        print("Nenhum número válido foi digitado.")

if __name__ == "__main__":
    main()
