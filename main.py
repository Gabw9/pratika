try:
    idade = int(input("Idade, por favor: "))
    
    if idade < 12:
        print("Kid")
    elif 12 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("CLT")
    elif 60 <= idade <= 90:
        print("Coroa")

    else: 
        print("mumia")

except ValueError:
    print("Por favor, insira um número válido para a idade.")
