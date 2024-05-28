from typing import Dict
from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get("/multiply-matrices")
def multiply_matrices():
    matrix_size = (10, 10)

    # Генерація випадкових матриць та обчислення їх добутку
    matrix_a = np.random.rand(*matrix_size)
    matrix_b = np.random.rand(*matrix_size)
    product = np.matmul(matrix_a, matrix_b)

    # Повернення результату у вигляді словника
    return {
        "matrix_a": matrix_a.tolist(),
        "matrix_b": matrix_b.tolist(),
        "product": product.tolist(),
    }
