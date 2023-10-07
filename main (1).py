# x = [1,6,8,576]
# print(x[3])

# frutas = ['Maçã','Banana','Pera','Cereja', True]
# frutas.remove('Banana')
# del frutas[3]
# print(frutas)

# frutas.append('melão')
# print(frutas)
# frutas.append(3)
# print(frutas)

###Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 5 e imprima-a na tela.

numeros = [1,2,3,4,5]
print(numeros)

###Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
print(numeros[2])

###Exercício 3: Adicione o número 6 à lista numeros e imprima a lista atualizada.
numeros.append(6)
print(numeros)

###Exercício 4: Remova o número 3 da lista numeros e imprima a lista resultante.
numeros.remove(3)
print(numeros)

###Exercício 5: Crie uma lista chamada frutas contendo três nomes de frutas diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
frutas = ['Maçã','Banana','Melão']
print(frutas+numeros)

###Exercício 6:** Use um loop `for` para percorrer e imprimir todos os elementos da lista `frutas`.
for fruta in frutas:
  print(fruta)
  
###Exercício 7: Verifique se o número 5 está presente na lista numeros e imprima uma mensagem informando se ele está na lista ou não.
if 5 in numeros:
  print(f'O número 5 está presente')
else:
  print('Não está presente')
  
