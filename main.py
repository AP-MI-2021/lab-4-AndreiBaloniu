def menu():
    print('1. Dati numere: ')
    print('2. Afisarea partii intregi a tuturor numerelor din lista.')
    print('3. Afisarea tuturor numerelor care apartin unui interval deschis.')
    print('4. Afisarea tuturor numerelor a caror parte intreaga este un div al partii fractionare.')
    print('5. Afisarea numerelor caracter cu caracter.')
    print('x. Iesire din program')


def citire_lista():
    l = []
    n = int(input("Dati nr de elem din lista: "))
    for i in range(n):
        l.append(float(input("l["+ str(i) + "]=")))
    return l


def parte_intreaga(l):
    '''
    Fucntia returneaza partea intreaga a unui nr
    :param l: lista
    :return: lista de nr
    '''
    result = []
    for i in l:
        result.append(int(i))
    return result


def nr_interval(l, capat_inferior, capat_superior):
    '''
    Functia returneaza nr dintr-un interval citit de la tastatura
    :param l: lista
    :param capat_inferior: capatul inferior al intervalului
    :param capat_superior: capatul superior al intervalului
    :return: lista noua ce indeplineste conditia
    '''
    result= []
    for i in l:
        if i>capat_inferior and i<capat_superior:
            result.append(i)
    return result


def div_parte_fract(l):
    '''
    Functia returneaza
    :param l: lista
    :return: lista ce indeplineste conditia
    '''
    result = []
    for i in l:
        if i != int(i):
            x= str(i)
            y = int((x.split(",")[1]))
            if y%int(i) == 0:
                result.append(i)
    return result

'''
def test_div_parte_fract():
    assert div_parte_fract([1.5, 6, 8]) ==  [1.5]

def test_nr_interval():
    assert nr_interval([1.5, -3.3, 55, 10], -4, 5) == [1.5, -3.3]

def test_parte_intreaga():
    assert  parte_intreaga([1.5, -3.3, 9, 3.2]) == [1, -3, 9, 3]
'''


def main():
    while True:
        menu()
        opt = input('Optiunea: ')
        if opt == '1':
            l = citire_lista()
        elif opt == '2':
            print(f'Partea intreaga a listei {l} este {parte_intreaga(l)}')
        elif opt == '3':
            capat_inferior = int(input('Dati capatul inferior: '))
            capat_superior = int(input('Dati capatul superior: '))
            print(f'Numerele din interval sunt {nr_interval(l)}')
        elif opt == '4':
            print(f'Toate numerele a caror parte intreaga este divizor este: {div_parte_fract(l)}')
        elif opt == 'x':
            break
        else:
            print('Optiune invalida')
        '''elif opt == '5'
            print(f'')
        '''


#test_div_parte_fract()
main()
