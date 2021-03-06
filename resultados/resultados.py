import random
#  1.Hemograma
#  2.Fezes e urina
#  3.Glicemia
# hr1 = '10:30h'
# hr2 = '12:45h'
# hr3 = '14:10h'


def resultado(usuario, diaEhoraC=None, diaEhoraE=None):
    continuar = True
    while(continuar):
        result = random.randrange(1, 3)
        escolha = int(input(
            "Deseja ver o resultado do exame ou do agendamento caro cliente?\nEscolha:\n[1] para Exame\n[2] para Agendamento\n[3] para retornar ao Menu Principal\n "))
        if (escolha == 1):  # Vai verificar o resultado do Exame
            # Exame de hemograma,coloquei 3 opções aleatórias para serem escolhidas de maneira aleatória com o "random"
            if (diaEhoraE[3] == 1):
                if (result == 1):
                    print(f"{usuario} indivíduo está saudável.")
                elif (result == 2):
                    print(f"{usuario} tem um excesso de gordura no sangue.")
                elif (result == 3):
                    print(f"{usuario} está com uma falta de ferro no sangue.")
            elif (diaEhoraE[3] == 2):  # Exame Parasitológico
                if (result == 1):
                    print(f"{usuario} está saudável.")
                elif (result == 2):
                    print(f"{usuario} está com vermes no intestino.")
                elif (result == 3):
                    print(f"{usuario} está com vermes na garganta.")
            elif (diaEhoraE[3] == 3):  # Exame Glicêmico
                if (result == 1):
                    print(
                        f"{usuario} tem uma quantidade de açucar baixa/média no sangue.")
                elif (result == 2):
                    print(
                        f"{usuario} tem uma quantidade de açucar média/alta no sangue.")
                elif(result == 3):
                    print(
                        f"{usuario} tem uma quantidade de açucar alta/alarmável no sangue.")
            else:
                print("Nenhum exame ou consulta encontrada.")
        elif(escolha == 2):  # Vai verificar or resultado do Agendamento
            while(True):
                verifica = int(input(
                    "Deseja verificar o agendamento da Consulta ou do Exame?\n[1]Consulta\n[2]Exame\n"))
                if (verifica == 1):
                    if (diaEhoraC != None):
                        if(diaEhoraC[2] == 1):
                            print(
                                f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 10:30h.")
                            break
                        elif(diaEhoraC[2] == 2):
                            print(
                                f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 12:45h.")
                            break
                        elif(diaEhoraC[2] == 3):
                            print(
                                f"Sua consulta está marcada para o dia {diaEhoraC[1]} de Julho, 14:10h.")
                            break
                    else:
                        print("Sem consulta marcada.")
                elif(verifica == 2):
                    if(diaEhoraE != None):
                        if(diaEhoraE[2] == 1):
                            print(
                                f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 10:30h.")
                            break
                        elif(diaEhoraE[2] == 2):
                            print(
                                f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 12:45h.")
                            break
                        elif(diaEhoraE[2] == 3):
                            print(
                                f"Seu exame está marcado para o dia {diaEhoraE[1]} de Julho, 14:10h.")
                            break
                    else:
                        print("Sem exame marcado.")
                else:
                    print("Escolha inválida!\nTente novamente...")
        elif(escolha == 3):
            print("Voltando para o Menu Principal...")
            break
        else:
            print("Opção inválida,tente novamente...")
            continue
        # Abaixo,caso o usuário ja tenha visto o resultado do agendamento ou do exame,será perguntado se deseja continuar
        opcao = int(input("Deseja continuar?\n[1]Sim\n[2]Não\n"))
        while(True):
            if (opcao == 1):
                break
            elif(opcao == 2):
                print("Voltando para o Menu Principal...")
                continuar = False
                break
            else:
                while (opcao != 1 and opcao != 2):
                    opcao = int(
                        input("Opção inválida,escolha [1] para Sim ou [2] para Não:\n"))


if(__name__ == "__main__"):
    # Argumento passado é (Número 1 ou 2 dizendo se é parâmetro do Consulta ou Exame,data,hora,Tipo de exame)
    resultado("Ronald Mc Donald", (1, 2, 1, 1), (2, 3, 3, 1))
