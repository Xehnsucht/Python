def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def delete(text):
    text = [tuple(i for i in text if i != ' ')]
    ''.join(text)
    print(text)


if __name__ == "__main__":
    # something = input('Введите текст: ')

    something = 'А роза упала на лапу Азора'
    delete(something)

    if is_palindrome(something):
        print("Да, это палиндром")
    else:
        print("Нет, это не палиндром")
