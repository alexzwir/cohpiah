import re


'''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
def le_assinatura():
	print("Bem-vindo ao detector automático de COH-PIAH.")
	wal = float(input("Entre o tamanho medio de palavra:"))
	ttr = float(input("Entre a relação Type-Token:"))
	hlr = float(input("Entre a Razão Hapax Legomana:"))
	sal = float(input("Entre o tamanho médio de sentença:"))
	sac = float(input("Entre a complexidade média da sentença:"))
	pal = float(input("Entre o tamanho medio de frase:"))

	return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
	i = 1
	textos = []
	texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
	while texto:
		textos.append(texto)
		i += 1
		texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

	return textos


'''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
def separa_sentencas(texto):
	sentencas = re.split(r'[.!?]+', texto)
	if sentencas[-1] == '':
		del sentencas[-1]
	return sentencas


'''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
def separa_frases(sentenca):
	return re.split(r'[,:;]+', sentenca)

'''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
def separa_palavras(frase):
	return frase.split()


'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
def n_palavras_unicas(lista_palavras):
	freq = dict()
	unicas = 0
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			if freq[p] == 1:
				unicas -= 1
			freq[p] += 1
		else:
			freq[p] = 1
			unicas += 1
	return unicas


'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
def n_palavras_diferentes(lista_palavras):
	freq = dict()
	for palavra in lista_palavras:
		p = palavra.lower()
		if p in freq:
			freq[p] += 1
		else:
			freq[p] = 1
	return len(freq)

texto = "Python é 42. Senão fosse 42, seria 42^2.Valeu =]."

def tamanho_medio(texto):
	'''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.'''

	''' Criando a lista de sentencas brutas (com espacos e sem formatacao) e uma lista de sentenca limpa após tratamento.Após isso, adiciona-se a sentanca limpa numa lista.'''
	sentencas_raw    = separa_sentencas(texto)
	sentencas = []

	palavras_totais = 0
	contador_caracter = 0

	for s in sentencas_raw:
		sentencas.append(s.lstrip())

	
	'''Criando um lista de frases brutas (com espacoe e sem formatação) e utilzando a função separa_frases() para separar as frases.'''
	for s in sentencas:
		frases_raw = separa_frases(s)
		#print("Primeiro Loop")

		

		'''Criando uma lista de frases tratadas.'''
		frases = []
		for f in frases_raw:
			frases.append(f.lstrip())

		#print(frases)

		'''Separando palavras através da funcao separa_palavras() e guardando em um variavel chamada palavras. Além disso, será criado um contador de palavras totais (palavras_totais) do texto e um contador de caracter (contador_caracter)'''
		for f in frases:
			palavras = separa_palavras(f)
			#print("Segundo Loop")

			
			for p in palavras:
				#print("terceiro loop")
				palavras_totais = palavras_totais + 1
				contador_caracter = contador_caracter + len(p)
				# print("A palavra número -",palavras_totais ,"é: ",p)
				# print("O número de caracter é: ",len(p) )
				# print(contador_caracter)
				# print(palavras_totais)

	return(contador_caracter/palavras_totais)

'''Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8'''
def type_token(texto):


	'''Criando uma lista de palavras totais do texto para poder depois usar na funcao de n_palavras_unicas()'''
	lista_de_palavras_totais = []

	''' Criando a lista de sentencas brutas (com espacos e sem formatacao) e uma lista de sentenca limpa após tratamento.Após isso, adiciona-se a sentanca limpa numa lista.'''
	sentencas_raw    = separa_sentencas(texto)
	sentencas = []

	palavras_totais = 0
	contador_caracter = 0

	for s in sentencas_raw:
		sentencas.append(s.lstrip())
	
	'''Criando um lista de frases brutas (com espacoe e sem formatação) e utilzando a função separa_frases() para separar as frases.'''
	for s in sentencas:
		frases_raw = separa_frases(s)
		#print("Primeiro Loop")

		

		'''Criando uma lista de frases tratadas.'''
		frases = []
		for f in frases_raw:
			frases.append(f.lstrip())

		#print(frases)

		'''Separando palavras através da funcao separa_palavras() e guardando em um variavel chamada palavras. Além disso, será criado um contador de palavras totais (palavras_totais) do texto e um contador de caracter (contador_caracter)'''
		for f in frases:
			palavras = separa_palavras(f)
			#print("Segundo Loop")

			
			for p in palavras:
				#print("terceiro loop")
				palavras_totais = palavras_totais + 1
				contador_caracter = contador_caracter + len(p)
				#print("A palavra número -",palavras_totais ,"é: ",p)
				lista_de_palavras_totais.append(p)
				# print("O número de caracter é: ",len(p) )
				# print(contador_caracter)
				# print(palavras_totais)

	# return(contador_caracter/palavras_totais)
	quantidade_de_palavras_texto = len(lista_de_palavras_totais)
	quantidade_de_palavras_unicas = n_palavras_unicas(lista_de_palavras_totais)
	conta_type_token = quantidade_de_palavras_unicas/quantidade_de_palavras_texto
	return conta_type_token

	


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


def main():
	print("O tamanho médio do texto é: ",tamanho_medio(texto))
	print("A relação Type-Token é de: ",type_token(texto) )

	

main()