from algorithm.heap_sort import HeapSort
from data.listas import *

from random import shuffle
from time import perf_counter


if __name__ == '__main__':
    soma = 0
    with open("desordenada 1000000 elementos.txt",'w', encoding = 'utf-8') as f:
        for i in range(1, 33):
            lista_1000000.sort(reverse=True)
            inicio = perf_counter()
            heap = HeapSort().heapsort(lista_1000000)
            fim = perf_counter()
            total = round((fim-inicio)*1000, 2)
            soma += total
            f.write(f'Execução {i} : {total}ms\n')
        f.write(f'-'*30)
        f.write(f'\nMédia: {round(soma / 32,2)}ms')
   