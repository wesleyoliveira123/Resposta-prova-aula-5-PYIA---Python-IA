#Crie uma função chamada maior_numero que receberá três números como argumentos. 
# Esta função deve comparar os três números e identificar qual deles é o maior.
#  Para isso, utilize uma estrutura de controle que verifique qual número é maior que os outros dois.
#  A função deve então retornar o maior número encontrado

def maior_numero(num1,num2,num3):
    maior=max(num1,num2,num3)
    return maior

num1=float(input('digite o primeiro numero: '))
num2=float(input('digite o segundo numero: '))
num3=float(input('digite o terceiro numero: '))
resultado=maior_numero(num1,num2,num3)
print(f'o maior deles é {resultado}')