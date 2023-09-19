abecedario = 'abcdefghijklmnñopqrstuvwxyz'
corrimiento = int(input('Ingresar el numero de corrimiento:'))
mensaje_encriptado = ''
for i in range(5):
  print(f'Mensaje para oficial {i+1}')
  mensaje = input('Ingresar mensaje:')
  mensaje = mensaje.lower()
  mensaje_encriptado=''
  for l in mensaje:

    if l in abecedario:
      posicion = abecedario.index(l)
      letra = abecedario[(posicion + corrimiento)%27]
      mensaje_encriptado += letra
    else:
      mensaje_encriptado+=l
  print(mensaje_encriptado) 
