nome = str(input('Digite seu nome completo')).strip()
print('Analisando seu nome')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print(' Seu nome em letras minusculas é {}'.format(nome.lower()))
print(' Q quantidade de letras que seu nome tem é {}'.format(len(nome) - nome.count(' ')))
#print(' O seu primeiro nome possui {} letras'.format(nome.find(' ')))  (vou fazer de uma 2 forma agora)
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
