"""
Programa: 
Descrição: Este programa calcula a média aritmética de 4 números fornecidos pelo usuário.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória
numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0

# Entrada de dados 

numero1 = float(input("Insira o primeiro numero"))
numero2 = float(input("Insira o segundo numero"))
numero3 = float(input("Insira o terceiro numero"))
numero4 = float(input("Insira o quarto numero"))

# Processamento de dados
resultado = float((numero1 + numero2 + numero3 + numero4) / 4)


# Saída de dados
print(f"A média aritmética dos números é {resultado}")