abecedario = 'abcdefghijklmnñopqrstuvwxyz'
corrimiento = int(input('Corrimiento:'))
mensaje_encriptado = ''
for i in range(5):
  print(f'Mensaje para oficial {i+1}')
  mensaje = input('Ingresar mensaje:')
  mensaje = mensaje.lower()
  mensaje_encriptado=''
  for l in mensaje:
    if l==' ':
      mensaje_encriptado+=' '
    else:
      posicion = abecedario.index(l)
      letra = abecedario[(posicion + corrimiento)%27]
      mensaje_encriptado += letra
  print(mensaje_encriptado)
