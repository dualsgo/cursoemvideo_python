# Curso Python #23 - Tratamento de Erros e Exceções

# try e except são estruturas fundamentais em Python para tratamento de exceções, permitindo que você lide com erros de forma controlada durante a execução do programa.

# A estrutura básica é a seguinte:

# No bloco try, você coloca o código que pode gerar exceções.
try:  # Código que pode gerar exceções
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 / num2

    # Se ocorrer uma exceção, o código dentro do bloco except correspondente será executado. Pode haver vários blocos except para lidar com diferentes tipos de exceções.
except ValueError:  # Trata a ValueError
    print("Digite apenas números inteiros.")
except ZeroDivisionError: # Trata a ZeroDivisionError
    print("Não é possível dividir por zero.")

    # O bloco else é executado se nenhum erro ocorrer no bloco try.
else:  # Executado se nenhum erro ocorrer no bloco try
    print(f"O resultado da divisão é: {resultado}")

    # O bloco finally é sempre executado, independentemente de ocorrerem exceções ou não. É útil para ações que precisam ser realizadas, como limpeza de recursos, independentemente do resultado do bloco try.
finally: # Sempre é executado, independentemente de ocorrer exceções ou não
    print("Encerrando o programa.")