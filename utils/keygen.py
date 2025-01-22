# utils/keygen.py
import random
from sympy import mod_inverse, isprime

PRIME = 101  # 소수 (유한군의 크기)
GENERATOR = 2  # 소수 생성기


def generate_keys():
    """
    비밀 키와 공개 키 생성
    """
    secret_key = random.randint(1, PRIME - 1)  # 비밀 키
    public_key = pow(GENERATOR, secret_key, PRIME)  # 공개 키 계산
    return secret_key, public_key, PRIME, GENERATOR
