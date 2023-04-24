

lista = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
        ]

for listaa in lista:
        for item in listaa:
                if (item % 2) == 0:
                        print(f'Este número é PAR {item}')
                elif item == 5:
                        print(f'Este número é cinco {item}')        
                elif (item % 2) != 0:     
                        print(f'Este número é IMPAR {item}')     