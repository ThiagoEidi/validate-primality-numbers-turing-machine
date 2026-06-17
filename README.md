# Trabalho de Teoria da Computação

**Thiago Eidi Hamada - 812243**

## Descrição

Este projeto implementa uma **Máquina de Turing** para verificação de números primos.

A aplicação foi desenvolvida em **Python** utilizando **FastAPI**, permitindo a execução e testes através do Swagger.

---

## Como rodar

É necessário ter o **Python 3.10+** instalado na máquina.

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar a aplicação

```bash
uvicorn main:app --reload
```

A aplicação ficará disponível em:

```text
http://localhost:8000/docs
```

Nesta página é possível testar os endpoints da Máquina de Turing diretamente pelo navegador.
