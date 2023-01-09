medico = []
paciente = []
convenio = []

def cadastrarMedicos():
    print("\n")
    resposta = input("Você deseja cadastrar um médico? ").upper()
    print("\n")
    while resposta == "S":
        lista = [input("Nome do médico: "),
                input("CPF do médico: "),
                input("RG do médico: "),
                input("CRM do médico: "),
                input("Sexo do médico: "),
                input("Telefone do médico: "),
                input("Endereço do médico: ")]
        medico.append(lista)
        print("\n")
        resposta = input("Deseja cadastrar mais algum médico? ").upper()
        print("\n")

def buscarMedicos():
    print("\n")
    busca = input("Digite o nome ou o CRM do médico que deseja buscar: ")
    print("\n")
    for elemento in medico:
        if busca == elemento[0]:
            print("Nome............: ", elemento[0])
            print("CPF.............: ", elemento[1])
            print("RG..............: ", elemento[2])
            print("CRM.............: ", elemento[3])
            print("Telefone........: ", elemento[5])
            print("Consulta........: ", elemento[7])
            print("Data da consulta: ", elemento[8])
            print("Compromisso.....: ", elemento[9])
            print("Data do compromisso: ", elemento[10])
            print("Hora do compromisso: ", elemento[11])

        else:
            print("Médico não encontrado!")

def alterarMedicos():
    print("\n")
    alteracao = input("Digite o nome do médico que deseja alterar o dado: ")
    print("\n")
    for elemento in medico:
        if alteracao==elemento[0]:
                dado = input("Digite qual dado você deseja alterar: ").upper()
                if dado == "CPF":
                    elemento[1] = input("CPF do médico: ")
                if dado == "RG":
                    elemento[2] = input("RG do médico: ")
                if dado == "CRM":
                    elemento[3] = input("CRM do médico: ")
                if dado == "SEXO":
                    elemento[4] = input("Sexo do médico: ")
                if dado == "NOME":
                    elemento[0] = input("Nome do médico: ")
                else:
                    print("\n")
                    print("Dado não encontrado!")
                    print("\n")
                    dado = input("Digite qual dado você deseja alterar: ").upper()
        else:
            print("\n")
            print("Médico não encontrado!")

def cadastrarConvenios():
    print("\n")
    resposta = input("Você deseja cadastrar um convênio? ").upper()
    print("\n")
    while resposta == "S":
        lista = [input("Nome do convênio: "),
                input("Telefone para contato: "),
                input("Digite o endereço: "),
                input("Digite a CNPJ: "),
                input("Planos do convênio: ")]
        convenio.append(lista)
        print("\n")
        resposta = input("Você deseja cadastrar mais algum convênio? ").upper()
        print("\n")

def buscarConvenios():
    print("\n")
    busca = input("Digite o nome ou o CNPJ do convênio que deseja buscar: ")
    print("\n")
    for elemento in convenio:
        if busca == elemento[0] or elemento[3]:
            print("Nome............: ", elemento[0])
            print("Telefone........: ", elemento[1])
            print("Endereço........: ", elemento[2])
            print("CNPJ............: ", elemento[3])
        else:
            print("Convênio não encontrado!")

def cadastrarPacientes():
    print("\n")
    resposta = input("Você deseja cadastrar um paciente? ").upper()
    print("\n")
    while resposta == "S":
        lista = [input("Nome do paciente: "),
        input("CPF do paciente: "),
        input("RG do paciente: "),
        input("Sexo do paciente: "),
        input("Telefone do paciente: "),
        input("Endereço do paciente: ")]
        paciente.append(lista)
        print("\n")
        resposta = input("Você deseja cadastrar mais algum paciente? ").upper()
        print("\n")

def buscarPacientes():
    print("\n")
    busca = input("Digite o nome ou o CPF do paciente que deseja buscar: ")
    print("\n")
    for elemento in paciente:
        if busca == elemento[0] or elemento[1]:
            print("Nome............: ", elemento[0])
            print("CPF.............: ", elemento[1])
            print("Telefone........: ", elemento[4])
            print("Consulta........: ", elemento[6])
            print("Data da consulta: ", elemento[7])
        else:
            print("Paciente não encontrado!")

def alterarPacientes():
    print("\n")
    alteracao = input("Digite o nome do paciente que deseja alterar o dado: ")
    print("\n")
    for elemento in paciente:
        if alteracao==elemento[0]:
                dado = input("Digite qual dado você deseja alterar: ").upper()
                if dado == "NOME":
                    elemento[0] = input("Nome do paciente: ")
                if dado == "CPF":
                    elemento[1] = input("CPF do paciente: ")
                if dado == "RG":
                    elemento[2] = input("RG do paciente: ")
                if dado == "SEXO":
                    elemento[3] = input("Sexo do paciente: ")
                if dado == "TELEFONE":
                    elemento[4] = input("Telefone do paciente: ")
                if dado == "ENDEREÇO":
                    elemento[5] = input("Endereço do paciente: ")
                else:
                    print("\n")
                    print("Dado não encontrado!")
                    print("\n")
                    dado = input("Digite qual dado você deseja alterar: ").upper()
        else:
            print("\n")
            print("Paciente não encontrado!")

def marcarConsulta():
    busca = input("Digite o nome do paciente da consulta: ")
    for elemento in paciente:
        if busca == elemento[0]:
            indice = input("Digite o nome do médico da consulta: ")
            for medic in medico:
                if indice == medic[0]:
                    consultas = [input("Tipo da consulta: "),
                    input("Data da consulta: ")]
                    paciente.append(consultas)
                    medico.append(consultas)
                else:
                    print("Médico não encontrado")
            else:
                print("Paciente não encontrado")

def marcarCompromisso():
    busca = input("Digite o nome do médico: ")
    for elemento in medico:
        if busca == elemento[0]:
                    compromisso = [input("Tipo do compromisso: "),
                    input("Data do compromisso: "),
                    input("Hora do compromisso: ")]
                    medico.append(compromisso)
        else:
            print("Médico não encontrado")

def emitirRelatorio():
    print("Lista de médicos: \n")
    for elemento in medico:
        print("Nome...........: ", elemento[0])
        print("CPF............: ", elemento[1])
        print("RG.............: ", elemento[2])
        print("CRM............: ", elemento[3])
        print("Sexo...........: ", elemento[4])
        print("Telefone.......: ", elemento[5])
        print("Endereço.......: ", elemento[6], "\n")

    print("Lista de pacientes: \n")
    for dado in paciente:
        print("Nome............: ", dado[0])
        print("CPF.............: ", dado[1])
        print("RG..............: ", dado[2])
        print("Sexo............: ", dado[3])
        print("Telefone........: ", dado[4])
        print("Endereço........: ", dado[5], "\n")

    print("Lista de convênios: \n")
    for element in convenio:
        print("Nome...........: ", element[0])
        print("CNPJ...........: ", element[3])
        print("Telefone.......: ", element[1])
        print("Endereço.......: ", element[2], "\n")