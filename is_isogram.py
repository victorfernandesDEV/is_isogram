
#Verifica se uma palavra é ou não um isograma
def is_isogram(word):
	validador = set(word)
	if len(validador) < len(word):
		return False
	return True

#entrada so usuário com a palavra a ser verificada
word = input("Informe a palavra: ")

#saida com a informação se a palavra é ou não um isograma
print(is_isogram(word))