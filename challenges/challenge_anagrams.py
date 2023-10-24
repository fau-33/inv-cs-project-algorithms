def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[0]
    left = []
    right = []

    for i in range(1, len(lista)):
        if lista[i] < pivot:
            left.append(lista[i])
        else:
            right.append(lista[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def is_anagram(first_string, second_string):
    string1 = first_string.lower().replace(" ", "")
    string2 = second_string.lower().replace(" ", "")

    first_string_sorted = quick_sort(list(string1))
    second_string_sorted = quick_sort(list(string2))

    if first_string == "" or second_string == "":
        return ("".join(first_string_sorted), ""
                .join(second_string_sorted), False)
    is_anagram = first_string_sorted == second_string_sorted
    return ("".join(first_string_sorted), ""
            .join(second_string_sorted), is_anagram)
