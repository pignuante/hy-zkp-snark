# utils/keygen.py
import random

# 유한군의 크기와 생성기 설정
PRIME = 101  # 소수 (유한군의 크기). 유한군에서의 모든 연산은 이 값을 기준으로 모듈러 연산이 수행됩니다.
GENERATOR = 2  # 유한군의 생성기. 유한군의 모든 원소를 생성할 수 있는 기본 값입니다.

def generate_keys():
    """
    비밀 키와 공개 키를 생성하는 함수.

    - 비밀 키 (secret_key): 1부터 PRIME-1 사이의 무작위 정수로 선택되며, 증명자가 알고 있는 비밀 정보입니다.
    - 공개 키 (public_key): 유한군의 생성기 (GENERATOR)를 비밀 키로 거듭제곱하여 모듈러 연산으로 계산된 값입니다.

    Returns:
        secret_key (int): 증명자가 사용하는 비밀 키.
        public_key (int): 검증자가 사용하는 공개 키. 공개적으로 공유됩니다.
        PRIME (int): 유한군의 크기, 모듈러 연산의 기준 값.
        GENERATOR (int): 유한군의 생성기.

    Example:
        secret_key, public_key, prime, generator = generate_keys()
    """
    # 비밀 키 생성 (1 <= secret_key < PRIME)
    secret_key = random.randint(1, PRIME - 1)

    # 공개 키 계산 (public_key = GENERATOR^secret_key % PRIME)
    public_key = pow(GENERATOR, secret_key, PRIME)

    return secret_key, public_key, PRIME, GENERATOR