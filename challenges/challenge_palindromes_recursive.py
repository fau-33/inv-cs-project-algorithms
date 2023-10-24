def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    if low_index >= high_index:
        return True
    normal_word = word
    reverse_word = word[::-1]

    if normal_word == reverse_word:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False
