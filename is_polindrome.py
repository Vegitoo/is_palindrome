import string

def is_palindrome(data): 
    
    if data == "":
        return True

    if isinstance(data, (int, float)):
        data = str(data).replace('.', '')
    elif isinstance(data, str):
        data = ''.join([char.lower() for char in data if char in string.ascii_letters + string.digits])
    elif isinstance(data, (list, tuple)):
        return data == data[::-1]
    else:
        raise ValueError("Nieprawidłowy typ danych. Obsługiwane są: stringi, liczby całkowite, liczby zmiennoprzecinkowe, listy i krotki.")

    return data == data[::-1]

def run_tests():
    assert is_palindrome("A man, a plan, a canal: Panama") == True, "Powinno być True"
    assert is_palindrome("No lemon, no melon") == True, "Powinno być True"
    assert is_palindrome("racecar") == True, "Powinno być True"
    assert is_palindrome("palindrome") == False, "Powinno być False"
    assert is_palindrome("") == True, "Pusty ciąg to palindrom"
    assert is_palindrome(" ") == True, "Pusty ciąg ze spacjami to palindrom"
    assert is_palindrome(121) == True, "Liczba 121 to palindrom"
    assert is_palindrome(123) == False, "Liczba 123 to nie palindrom"
    assert is_palindrome(123.321) == True, "Liczba 123.321 to palindrom"
    assert is_palindrome(123.456) == False, "Liczba 123.456 to nie palindrom"
    assert is_palindrome([1, 2, 3, 2, 1]) == True, "Lista to palindrom"
    assert is_palindrome([1, 2, 3, 4, 5]) == False, "Lista to nie palindrom"
    assert is_palindrome(('a', 'b', 'b', 'a')) == True, "Krotka to palindrom"

    try:
        is_palindrome({1: "a", 2: "b"})
    except ValueError as e:
        assert str(e) == "Nieprawidłowy typ danych. Obsługiwane są: stringi, liczby całkowite, liczby zmiennoprzecinkowe, listy i krotki.", "Zły typ danych powinien wywołać ValueError"
    else:
        assert False, "Wyjątek nie został rzucony dla nieobsługiwanego typu danych"

    print("Wszystkie testy przeszły pomyślnie!")

run_tests()
