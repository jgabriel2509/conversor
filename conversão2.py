def converter_dolar_para_real():
    cotacao_dolar = 5.69  # taxa de câmbio fixa para exemplo
    try:
        dolares = float(input("Digite o valor em dólares (USD): ").strip())
        reais = dolares * cotacao_dolar
        print("-----------------------------------------------------------")
        print(f"{dolares} USD equivale a R$ {reais:.2f}")
        print("-----------------------------------------------------------")
    except ValueError:
        print("Valor inválido! Digite um número válido para dólares.")
    except Exception as e:
        print(f"Ocorreu um erro na conversão: {e}")

def converter_real_para_dolar():
    cotacao_dolar = 5.69  # taxa de câmbio fixa para exemplo
    try:
        reais = float(input("Digite o valor em reais (BRL): ").strip())
        dolares = reais / cotacao_dolar
        print("-----------------------------------------------------------")
        print(f"{reais} BRL equivale a US$ {dolares:.2f}")
        print("-----------------------------------------------------------")
    except ValueError:
        print("Valor inválido! Digite um número válido para reais.")
    except Exception as e:
        print(f"Ocorreu um erro na conversão: {e}")

def menu():
    while True:
        try:
            print("\nCONVERSOR DE MOEDAS")
            print("[1] Converter dólar para real")
            print("[2] Converter real para dólar")
            print("[0] Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                converter_dolar_para_real()
            elif opcao == '2':
                converter_real_para_dolar()
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("-----------------------------------------------------------")
                print("!!!!!!! Opção inválida. Tente novamente !!!!!!!")
                print("-----------------------------------------------------------")
        except Exception as e:
            print(f"Ocorreu um erro no menu: {e}")

if __name__ == "__main__":
    menu()
