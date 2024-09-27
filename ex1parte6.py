def bubble_sort(lst):
    n = len(lst)
    swapped = True
    
    while swapped:
        swapped = False
        for i in range(1, n):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                swapped = True
        n -= 1
    
    return lst

my_list = [4, 3, 2, 1]
my_list = bubble_sort(my_list)
print(my_list)
#i-1 posição 0 neste caso é o 4
#Porém, na primeira iteração do loop externo, não podemos garantir que a lista já está ordenada, então precisamos definir a variável swapped como True antes de entrar no loop interno. Dessa forma, garantimos que o loop interno será executado pelo menos uma vez, e teremos a chance de verificar se há elementos fora de ordem na lista e efetuar trocas.