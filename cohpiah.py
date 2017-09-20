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
	quantidade_de_palavras_unicas = n_palavras_diferentes(lista_de_palavras_totais)
	conta_type_token = quantidade_de_palavras_unicas/quantidade_de_palavras_texto
	return conta_type_token

def razao_hapax_legomana(texto):
	'''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6'''

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
	#print(lista_de_palavras_totais)
	quantidade_de_palavras_diferentes = n_palavras_unicas(lista_de_palavras_totais)
	#print(quantidade_de_palavras_diferentes)
	conta_razao_hapax_legomana = quantidade_de_palavras_diferentes/quantidade_de_palavras_texto
	return conta_razao_hapax_legomana


def tamanho_medio_sentenca(texto):
	'''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).'''

	''' Criando a lista de sentencas brutas (com espacos e sem formatacao) e uma lista de sentenca limpa após tratamento.Após isso, adiciona-se a sentanca limpa numa lista.'''
	sentencas_raw    = separa_sentencas(texto)
	sentencas = []

	palavras_totais = 0
	contador_caracter = 0

	for s in sentencas_raw:
		sentencas.append(s.lstrip())

	quantidade_de_sentencas = 0
	quantidade_total_de_caracteres_nas_sentencas = 0
	for s in sentencas:
		quantidade_de_sentencas = quantidade_de_sentencas + 1
		quantidade_total_de_caracteres_nas_sentencas = quantidade_total_de_caracteres_nas_sentencas + len(s)

	# print("Quantidade de senteças:",quantidade_de_sentencas)
	# print("Quantidade de total de caracteres: ",quantidade_total_de_caracteres_nas_sentencas)

	conta_tamanho_medio_sentencas = quantidade_total_de_caracteres_nas_sentencas/quantidade_de_sentencas

	return(conta_tamanho_medio_sentencas)

def complexidade(texto):
	'''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''

	''' Criando a lista de sentencas brutas (com espacos e sem formatacao) e uma lista de sentenca limpa após tratamento.Após isso, adiciona-se a sentanca limpa numa lista.'''
	sentencas_raw = separa_sentencas(texto)
	sentencas = []

	palavras_totais = 0
	contador_caracter = 0

	for s in sentencas_raw:
		sentencas.append(s.lstrip())

	
	'''Criando um lista de frases brutas (com espacoe e sem formatação) e utilzando a função separa_frases() para separar as frases.'''
	'''Criando uma lista de frases tratadas.'''
	frases = []
	for s in sentencas:
		frases_raw = separa_frases(s)
		#print(frases_raw)
		
		for f in frases_raw:
			frases.append(f.lstrip())
	
	conta_complexidade = len(frases)/ len(sentencas)

	return conta_complexidade


def tamanho_medio_frase(texto):
	'''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).'''

	''' Criando a lista de sentencas brutas (com espacos e sem formatacao) e uma lista de sentenca limpa após tratamento.Após isso, adiciona-se a sentanca limpa numa lista.'''
	sentencas_raw = separa_sentencas(texto)
	sentencas = []

	palavras_totais = 0
	contador_caracter = 0

	for s in sentencas_raw:
		sentencas.append(s.lstrip())

	
	'''Criando um lista de frases brutas (com espacoe e sem formatação) e utilzando a função separa_frases() para separar as frases.'''
	'''Criando uma lista de frases tratadas.'''
	frases = []
	for s in sentencas:
		frases_raw = separa_frases(s)
		#print(frases_raw)
		
		for f in frases_raw:
			frases.append(f.lstrip())

	quantidade_de_caracteres_nas_frases = 0
	for f in frases:
		quantidade_de_caracteres_nas_frases = quantidade_de_caracteres_nas_frases + len(f)
	
	quantdade_de_frases = len(frases)

	conta_tamanho_medio_frases = quantidade_de_caracteres_nas_frases/quantdade_de_frases

	return conta_tamanho_medio_frases

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    assinatura_a = as_a
    assinatura_b = as_b
    i = 1
    somatoria = 0

    for i in range(len(assinatura_a)): 
    	diferenca_entre_assinaturas = assinatura_a[i] - assinatura_b[i]
    	#print("A diferencas entre assinaturas é: ", diferenca_entre_assinaturas)
    	somatoria = somatoria + diferenca_entre_assinaturas
    	#print("A somatoria é ", somatoria)
    grau_de_similaridade = somatoria/6

    return grau_de_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    calculos_assinatura = [tamanho_medio,type_token,razao_hapax_legomana,tamanho_medio_sentenca,complexidade,tamanho_medio_frase]
    assinatura = []
    for calc in calculos_assinatura:
    	parametro_assinatura = calc(texto)
    	assinatura.append(parametro_assinatura)

    return assinatura

   
 #    print("O tamanho médio do texto é: ",tamanho_medio(texto))
	# print("A relação Type-Token é de: ",type_token(texto))
	# print("A razão Hapax Legomana é de: ",razao_hapax_legomana(texto))
	# print("O tamanho médio de sentenças é de: ",tamanho_medio_sentenca(texto))
	# print("A complexidade do texto é: ",complexidade(texto))
	# print("O tamanho médio da frase é de: ", tamanho_medio_frase(texto))

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    '''Perceba que quanto mais similares a e b forem, menor Sab será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e no final exibir qual o texto que mais provavelmente foi escrito por algum aluno infectado.'''

    textos = textos
    assinatura_target = ass_cp
    assinaturas_textos = []


    for texto in textos:
    	assinatura_texto = calcula_assinatura(texto)
    	assinaturas_textos.append(assinatura_texto)
    print(assinaturas_textos)

    


def main():
	assinatura_target = [1,2,3,4,5,6]
	textos = ["Python é 42. Senão fosse 42, seria 42^2.Valeu =].","Python é 42. Senão fosse 42, seria 42^2.Valeu =].","Python é 42. Senão fosse 42, seria 42^2.Valeu =]."]

	avalia_textos(textos,assinatura_target)

main()