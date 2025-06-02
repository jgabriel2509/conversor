def converter_dolar_para_real():
    cotacao_dolar = 5.69 # taxa de cambio fixa para exemplo
    dolares = float(input("digite o valor em dolares (USD): "))
    reais = dolares * cotacao_dolar
    print("-----------------------------------------------------------")
    print(f"{dolares} USD equivale a R$ {reais:.2f}")
    print("-----------------------------------------------------------")

def converter_real_para_dolar():
    cotacao_dolar = 5.69 # taxa de cambio fixa para exemplo
    reais = float(input("digite o valor em reais (BRL): "))
    dolares = reais / cotacao_dolar
    print("-----------------------------------------------------------")
    print(f"{reais} BRL equivale a US$ {dolares:.2f}")
    print("-----------------------------------------------------------")

def menu():
    while True:
        print("\nconversor de moedas")
        print("[1] converter dolar para real")
        print("[2] converter real para dolar")
        print("[0] sair")
        opcao = input("escolha uma opcao: ")

        if opcao == '1':
            converter_dolar_para_real()
        elif opcao == '2':
            converter_real_para_dolar()
        elif opcao == '0':
            print("saindo...")
            break
        else:
            print("-----------------------------------------------------------")
            print("!!!!!!! Opcao invalida. Tente novamente !!!!!!!")
            print("-----------------------------------------------------------")
            
if __name__ == "__main__":
    menu()