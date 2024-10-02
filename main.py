pessoas = int(input('Digite quantas pessoas vão para reunião:'))
if pessoas <=3:
    print ('Sua renião será na sala pequena.')
elif pessoas <=10:
    print ('Sua renião será na sala média.')
elif pessoas >10:
    print ('Sua renião será na sala grande.')
else:
    print ('Está invalído digite novamente')