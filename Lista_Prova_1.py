import random
import timeit

def selection_sort(list_func):
    n = len(list_func)

    for i in range(0, n):
        index_min = i
        for j in range(i+1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[i], list_func[index_min] = list_func[index_min], list_func[i]

    return list_func

def bubble_sort(lista):
    n = len(lista)

    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def insertion_sort(lista):
    n = len(lista)

    for i in range(1, n):
        insert_value = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > insert_value:
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = insert_value

    return lista

if __name__ == '__main__':

    # lista = [10, 9, 5, 8, 11, -1, 3] Variaveis para teste

    valor1 = 0
    valor2 = 0
    valor3 = 0


    for i in range(1, 4):

        lista = random.sample(range(100_000), 50_000)

        print()
        print(f'  Loop  {i}')
        print(f'  Unordered:      {lista}')

        print()
        # print(' Selection Sort: ')
        ordered_list = selection_sort(lista)
        start_time = timeit.default_timer()
        selection_sort(lista)
        print(f'  Selection Sort: {ordered_list}')
        tempo1 = timeit.default_timer() - start_time
        print(f' Duração do tempo : {timeit.default_timer() - start_time:.5f}')

        print()
        # print(' Bubble Sort: ')
        ordered_list2 = bubble_sort(lista)
        start_time = timeit.default_timer()
        print(f'  Bubble Sort:    {ordered_list2}')
        tempo2 = timeit.default_timer() - start_time
        print(f' Duração do tempo : {timeit.default_timer() - start_time:.5f}')

        print()
        # print(' Insertion sort: ')
        ordered_list3 = insertion_sort(lista)
        start_time = timeit.default_timer()
        print(f'  Insertion Sort: {ordered_list3}')
        tempo3 = timeit.default_timer() - start_time
        print(f' Duração do tempo : {timeit.default_timer() - start_time:.5f}')

        valor1 = tempo1 + valor1
        valor2 = tempo2 + valor2
        valor3 = tempo3 + valor3

media1 = valor1/3
media2 = valor2/3
media3 = valor3/3

print()

print(f' Valor de Media de tempo Selection_Sort: {media1:.5f}')
print(f' Valor de media de tempo Bubble_Sort:    {media2:.5f}')
print(f' Valor de Media de tempo Insertion_Sort: {media3:.5f} ')

print()
print(' -- Fim do Loop -- ')


# Resposta 1 - E.
# O algoritmo Insertion sort tem a melhor eficiência ela passa o menor valor para o primeiro vetor da lista
# e depois o segundo menor em sequência e assim sucessivamente até completa a lista que deseja.


# Resposta 2
# A busca binária é um eficiente algoritmo para encontrar um item em uma lista ordenada de itens.
# Ela funciona dividindo repetidamente pela metade a porção da lista que deve conter o item,
# até reduzir as localizações possíveis a apenas uma.
