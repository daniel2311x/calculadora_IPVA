def ipva():
    while True:
        print('---Calculadora de IPVA---')

        print("1 - Motocicletas até 150cc")
        print("2 - Motoclicletas acima de 150cc até 400cc")
        print("3 - Motocicletas acima de 400cc")
        print("4 - Automoveis até 80 HP")
        print("5 - Automoveis acima de 80 até 160 HP")
        print("6 - Automoveis acima de 160 HP")
        print("7 - Onibus e Caminhoes")
        print("8 - Veiculos com Kit GNV")
        print("9 - Calculo de IPVA proporcional")
        print("0 - Sair")

        opcao = input("\nEscolha a categoria do seu veiculo (1, 2, 3, 4, 5, 6, 7, 8, 0):")

        if opcao == "0":
            print("Encerrando calculadora... até mais")

            break

        if opcao in ('1', '2', '3', '4', '5', '6', '7', '8'):
            try:
                valor_venal = float(input("Informe o valor venal do seu veículo: "))

                if opcao == '1':
                    aliquota = 0.02

                elif opcao == '2':
                    aliquota = 0.0275

                elif opcao == '3':
                    aliquota = 0.0325

                elif opcao == '4':
                    aliquota = 0.0275

                elif opcao == '5':
                    aliquota = 0.03

                elif opcao == '6':
                    aliquota = 0.0325

                elif opcao == '7':
                    aliquota = 0.01

                elif opcao == '8':
                    aliquota = 0.015   

                ipva_total = valor_venal * aliquota

                print(f"O IPVA a pagar é de R${ipva_total:.2f}")

                if opcao == '9':
                    meses = int(input("Informe quantidade de meses devidos: "))

                    if meses > 12 and meses < 1:
                        print("Quantidade invalida! informe um numero entre 1 e 12")

                    else:
                        ipva_proporcional = ipva_total * (meses / 12)
                        print(f"O valor do IPVA proporcional é de R${ipva_proporcional}")   

            except ValueError:
                print("Por favor, informe numeros validos.")      

        else:
            print("Opcao invalida! Informe opcao de 1 a 8.")                               


ipva()


    
        
