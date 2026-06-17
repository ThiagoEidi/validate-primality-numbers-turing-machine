from turing_machine import is_prime_turing


def test_primos():
    primos = [
        2, 3, 5, 7, 11, 13, 17, 19,
        23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79,
        83, 89, 97
    ]

    for numero in primos:
        binario = bin(numero)[2:]
        assert is_prime_turing(binario) is True, \
            f"Falhou para primo {numero} ({binario})"


def test_nao_primos():
    nao_primos = [
        0, 1, 4, 6, 8, 9, 10,
        12, 14, 15, 16, 18, 20,
        21, 22, 24, 25, 26, 27,
        28, 30, 32, 33, 34, 35,
        36, 38, 39, 40, 42, 44,
        45, 46, 48, 49, 50, 51,
        52, 54, 55, 56, 57, 58,
        60, 62, 63, 64, 65, 66,
        68, 69, 70, 72, 74, 75,
        76, 77, 78, 80, 81, 82,
        84, 85, 86, 87, 88, 90,
        91, 92, 93, 94, 95, 96,
        98, 99, 100
    ]

    for numero in nao_primos:
        binario = bin(numero)[2:]
        assert is_prime_turing(binario) is False, \
            f"Falhou para não primo {numero} ({binario})"


def executar_testes():
    test_primos()
    test_nao_primos()
    print("✅ Todos os testes passaram!")


if __name__ == "__main__":
    executar_testes()