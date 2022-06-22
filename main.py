import informacoes
import random


import calendar
aa = 2022
mm = 7


def resultado(usuario, exame=None, diaEhora=None, agend=None):
    continuar = True
    while(continuar):
        result = random.randrange(1, 3)
        escolha = int(input(
            "Deseja ver o resultado do exame ou do agendamento caro cliente?\nEscolha:\n[1] para Exame\n[2] para Agendamento\n[3] para retornar\n "))
        if (escolha == 1):  # Vai verificar o resultado do Exame
            if (exame == 1):  # Exame de hemograma,coloquei 3 opções aleatórias para serem escolhidas de maneira aleatória com o "random"
                if (result == 1):
                    print(f"{usuario} indivíduo está saudável.")
                elif (result == 2):
                    print(f"{usuario} tem um excesso de gordura no sangue.")
                elif (result == 3):
                    print(f"{usuario} está com uma falta de ferro no sangue.")
            elif (exame == 2):  # Exame Parasitológico
                if (result == 1):
                    print(f"{usuario} está saudável.")
                elif (result == 2):
                    print(f"{usuario} está com vermes no intestino.")
                elif (result == 3):
                    print(f"{usuario} está com vermes na garganta.")
            elif (exame == 3):  # Exame Glicêmico
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
            if (diaEhora != None):
                if (agend == 1):
                    if(diaEhora[1] == 1):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]},10:30h.")
                    elif(diaEhora[1] == 2):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]}, 12:45h.")
                    elif(diaEhora[1] == 3):
                        print(
                            f"Sua consulta está marcada para o dia {diaEhora[0]}, 14:10h.")
                elif(agend == 2):
                    if(diaEhora[1] == 1):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]},10:30h.")
                    elif(diaEhora[1] == 2):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]}, 12:45h.")
                    elif(diaEhora[1] == 3):
                        print(
                            f"Seu exame está marcado para o dia {diaEhora[0]}, 14:10h.")
            else:
                print("Sem Consulta ou Exame marcado.")
        elif(escolha == 3):
            print("Voltando para o Menu Principal...")
            break
        else :
            print("Opção inválida,tente novamente...")
            continue
        # Abaixo,caso o usuário ja tenha visto o resultado do agendamento ou do exame,será perguntado se deseja continuar
        opcao = int(input("Deseja continuar?\n[1]Sim\n[2]Não\n"))
        while(True):
            if (opcao == 1):
                break
            elif(opcao == 2):
                continuar = False
                break
            else:
                while (opcao != 1 and opcao != 2):
                    opcao = int(
                        input("Opção inválida,escolha [1] para Sim ou [2] para Não:\n"))

                    
#EXAMES                    

while True:
    def ex(exames):
        if exames == '1':
            print (f'Você selecionou exame de {ex1}. Selecione entre as datas disponíveis: \n {calendar.month(aa,mm)}')
            data = int(input('Digite um dia em formato dd: \n '))
            while (data < 1) or (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n')
            while (hora <'1') or (hora >'3'):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')
            
            print (f"Exame {ex1} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return 2, data, hora, 1
        
        elif exames == '2':
            print (f'Você selecinou exame {ex2}. Selecione entre as datas disponíveis: \n{calendar.month(aa,mm)} ')
            data = int(input('Digite um dia em formato dd: \n '))
            while (data < 1) and (data > 30):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = int(input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n'))
            while (hora <1) or (hora >3):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')

            print (f"Exame {ex2} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return 2, data, hora, 2           
        
        elif exames == '3':
            print (f'Você selecionou exame de {ex3}. Selecione entre as datas disponíveis: \n{calendar.month(aa,mm)}')
            data = input ('Digite um dia em formato dd: \n ')
            while (data < '1') and (data > '30'):
                data = int(input('Dia inválido. Digite um dia em formato dd: \n '))

            hora = input(f'Escolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n')
            while (hora <'1') or (hora >'3'):
                hora = input(f'Horário não disponível. \nEscolha uma opção de horário: \n1.{hr1} \n2.{hr2} \n3.{hr3} \n ')

            print (f"Exame {ex3} agendado em {data}/07 no horário {hora} com sucesso! \nVocê receberá um SMS para a confirmação do seu agendamento.")
            return 2, data, hora, 3
  
    
    ex1 = 'Hemograma'
    ex2 = 'Parasitológico'
    ex3 = 'Glicemico'
    hr1 = '10:30h'
    hr2 = '12:45h'
    hr3 = '14:10h' 
    nome = str(input('Digite seu nome: '))
    exames = input(f'Olá {nome}! Selecione o exame desejado: \n 1.{ex1} \n 2.{ex2} \n 3.{ex3} \n ')
    while (exames != '1') and (exames != '2') and (exames != '3'):
        exames = input(f'Opção inválida, {nome}. Selecione o exame desejado: \n 1.{ex1} \n 2.{ex2} \n 3.{ex3} \n ')

    ex(exames)

    
