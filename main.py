from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from turing_machine import is_prime_turing

# API da Máquina de Turing
app = FastAPI(title="Máquina de Turing para Números Primos")


# DTO de resposta
class PrimeResponse(BaseModel):
    isPrime: bool


# Endpoint
@app.post(
    "/check/binary/{number}",
    response_model=PrimeResponse
)
def check_binary(number: int):
    numero_binario = bin(number)[2:]
    try:

        result = is_prime_turing(numero_binario)

        return PrimeResponse(
            isPrime=result
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )