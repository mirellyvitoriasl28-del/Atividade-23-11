8. Implemente o algoritmo Bubble Sort para ordenar uma lista sem usar .sort() ou sorted().
R:
def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr
