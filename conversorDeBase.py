
# A função pode não dar suporte para algumas bases, como é o caso da sexagesimal

# se for usada com numeros nao suportados pela base (ex.: 8 e 9 na base 8), a função
# pode retornar valores errados
	
# aceita os argumentos num e base como int ou str
# no caso de numeros emm hexadecimal a função é case insensitiva

def conversorDeBase(num, base, paraBase=10):
	number = str(num)
	listNumDigits = list(number)	#transforma a str number em uma lista com os digitos do numero
	listNumDigits.reverse()
	decimalNum = 0

	# se a base for 16 substitui os digitos com letras por seus valores correspondentes
	hexadecimal = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
	if int(base) == 16:
		for i, v in enumerate(listNumDigits):
			if v.lower() in hexadecimal:
				listNumDigits[i] = hexadecimal[v.lower()]

	
	# eleva a base pela posição do digito em listNumDigit , multiplica pelo digito
	# e soma o resultado à variavel decimalNum
	for i, v in enumerate(listNumDigits):
		decimalNum += int(base)**i * int(v)
		
	if paraBase == 10:
		# decimalNum tem o valor numerico na base 10
		# retorna uma str
		return str(decimalNum)

	else:
		# quando paraBase != 10 o programa converte o numero para decimal antes de converter para
		# a base desejada
		digits = []
		result = ''

		if decimalNum == 1 or decimalNum == 0 or decimalNum < paraBase and decimalNum < 10:
			return str(decimalNum)
			
		else:
			# divide o decimalNum pela base desejada ate nao poder mais,
			# insere os digitos do resto e do ultimo divisor "1" na lista digits
			# inverte a lista, concatena  os digitos em uma string e retorna 
			while True:
				if decimalNum // int(paraBase) == 1:
					remainder = decimalNum % int(paraBase)
					digits.append(remainder)
					digits.append(1)
					break
					
				else:
					remainder = decimalNum % int(paraBase)
					digits.append(remainder)
					decimalNum //= int(paraBase)

			digits.reverse()

			# substitui os digitos entre(inclusive) 10 e 15 por letras da base 16 (A a F), os 
			# concatena em uma str e retorna
			if paraBase == 16:
				for i, v in enumerate(digits):
					if v < 10:
						result += str(v)

					else:
						for j in hexadecimal.keys():
							if v == hexadecimal[j]:
								result += str(hexadecimal[j])
								break

					return result

			# com exceção de paraBase == 16, concatena todos os digitos de digits na variavel result
			for i in digits:
				result += str(i)
				
			return result




print(conversorDeBase('30', 10, paraBase=8))
