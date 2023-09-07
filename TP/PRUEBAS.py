
number=1
option1='AMOR'
option2='DINERO'
option3='PAZ'
while number!=0:
    print('Ingrese 1,2 o 3:')
    number=int(input())
    if number==0:
        break
    elif number==1:
        print(f'Usted recibira {option1}')
    elif number==2:
        print(f'Usted recibira {option2}')
    elif number==3:
        print(f'Usted recibira {option3}')