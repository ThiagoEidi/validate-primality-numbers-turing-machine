from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# API da Máquina de Turing
app = FastAPI(title="Máquina de Turing para Números Primos")


# DTO de resposta
class PrimeResponse(BaseModel):
    isPrime: bool


# Sub-rotina NORMALIZE
def normalize(bits):

    while len(bits) > 1 and bits[0] == "0":
        bits.pop(0)

    return bits


# Sub-rotina COPY
def copy_tape(tape):

    return tape.copy()


# Sub-rotina EQ
def equals(a, b):

    a = normalize(a.copy())
    b = normalize(b.copy())

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True


# Sub-rotina GEQ
def greater_or_equals(a, b):

    a = normalize(a.copy())
    b = normalize(b.copy())

    while len(a) < len(b):
        a.insert(0, "0")

    while len(b) < len(a):
        b.insert(0, "0")

    for i in range(len(a)):

        bit_a = 1 if a[i] == "1" else 0
        bit_b = 1 if b[i] == "1" else 0

        if bit_a > bit_b:
            return True

        if bit_a < bit_b:
            return False

    return True


# Sub-rotina INC
def increment(bits):

    bits = bits.copy()

    carry = 1

    for i in range(len(bits) - 1, -1, -1):

        if bits[i] == "1":
            bits[i] = "0"

        else:
            bits[i] = "1"
            carry = 0
            break

    if carry == 1:
        bits.insert(0, "1")

    return normalize(bits)


# Sub-rotina SUB
def subtract(a, b):

    result = a.copy()
    b = b.copy()

    while len(b) < len(result):
        b.insert(0, "0")

    borrow = 0

    for i in range(len(result) - 1, -1, -1):

        bit_a = int(result[i])
        bit_b = int(b[i])

        diff = bit_a - bit_b - borrow

        if diff == 0:
            result[i] = "0"
            borrow = 0

        elif diff == 1:
            result[i] = "1"
            borrow = 0

        elif diff == -1:
            result[i] = "1"
            borrow = 1

        else:
            result[i] = "0"
            borrow = 1

    return normalize(result)


# Máquina de Turing
def is_prime_turing(binary_number: str) -> bool:

    # Validação da entrada
    if not all(c in ("0", "1") for c in binary_number):
        raise ValueError("Número binário inválido")

    # T0 = número original
    tape0 = normalize(list(binary_number))

    # Casos especiais
    if equals(tape0, ["0"]):
        return False

    if equals(tape0, ["1"]):
        return False

    # T1 = divisor atual
    tape1 = ["1", "0"]

    while True:

        # T2 = cópia de T0
        tape2 = copy_tape(tape0)

        # Enquanto T2 >= T1
        while greater_or_equals(tape2, tape1):
            tape2 = subtract(tape2, tape1)

        # Verifica resto
        if equals(tape2, ["0"]):

            # Verifica se divisor = número
            if equals(tape1, tape0):
                return True

            return False

        # Incrementa divisor
        tape1 = increment(tape1)

        # Verifica fim
        if greater_or_equals(tape1, tape0):
            return True


# Endpoint
@app.post(
    "/check/binary/{number}",
    response_model=PrimeResponse
)
def check_binary(number: str):

    try:

        result = is_prime_turing(number)

        return PrimeResponse(
            isPrime=result
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )