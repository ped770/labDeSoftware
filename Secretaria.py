from ControlSecretaria import *

lang = input("O que você deseja fazer? \n")

match lang:
    case "1":
        cadastrarMedicos()
        lang = input("O que você deseja fazer? \n")

    case "2":
        cadastrarPacientes()
        lang = input("O que você deseja fazer? \n")

    case "3":
        cadastrarConvenios()
        lang = input("O que você deseja fazer? \n")
    
    case "4":
        buscarMedicos()
        lang = input("O que você deseja fazer? \n")

    case "5":
        buscarPacientes()
        lang = input("O que você deseja fazer? \n")
        
    case "6":
        buscarConvenios()
        lang = input("O que você deseja fazer? \n")

    case "7":
        alterarMedicos()
        lang = input("O que você deseja fazer? \n")

    case "8":
        alterarPacientes()
        lang = input("O que você deseja fazer? \n")
    
    case "9":
        marcarCompromisso()
        lang = input("O que você deseja fazer? \n")
    
    case "10":
        marcarConsulta()
        lang = input("O que você deseja fazer? \n")

    case "11":
        emitirRelatorio()
        lang = input("O que você deseja fazer? \n")

    case _:
        print("Escolha uma opção válida")
        lang = input("O que você deseja fazer? \n")