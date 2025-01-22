# utils/proof.py
import random


def generate_proof(secret_key, prime, generator):
    """
    증명 생성 함수.

    - 무작위 값 (r): 증명 과정에서 사용되는 무작위 값.
    - 커밋 값 (t): r을 기반으로 계산된 값.
    - 챌린지 값 (e): 검증자가 생성하는 무작위 질문 값.
    - 응답 값 (s): 증명자가 비밀 키를 기반으로 계산한 응답 값.

    Args:
        secret_key (int): 증명자가 사용하는 비밀 키.
        prime (int): 유한군의 크기.
        generator (int): 유한군의 생성기.

    Returns:
        t (int): 커밋 값.
        e (int): 챌린지 값.
        s (int): 응답 값.

    Example:
        t, e, s = generate_proof(secret_key, prime, generator)
    """
    # 무작위 값 생성
    r = random.randint(1, prime - 1)  # 무작위 값

    # 커밋 값 계산
    t = pow(generator, r, prime)

    # 챌린지 값 생성 (보통 검증자가 생성하지만, 이 코드에서는 내부에서 생성)
    e = random.randint(1, prime - 1)

    # 응답 값 계산
    s = (r + e * secret_key) % (prime - 1)

    return t, e, s


def verify_proof(public_key, t, e, s, prime, generator):
    """
    증명을 검증하는 함수.

    - 공개 키 (public_key): 증명자의 비밀 키로부터 생성된 공개 값.
    - 커밋 값 (t): 증명자가 생성한 커밋 값.
    - 챌린지 값 (e): 검증자가 증명 과정에서 사용한 무작위 값.
    - 응답 값 (s): 증명자가 비밀 키와 r을 사용하여 계산한 응답 값.

    Args:
        public_key (int): 검증자가 사용하는 공개 키.
        t (int): 증명 과정에서 생성된 커밋 값.
        e (int): 검증자가 생성한 챌린지 값.
        s (int): 증명자가 계산한 응답 값.
        prime (int): 유한군의 크기.
        generator (int): 유한군의 생성기.

    Returns:
        bool: 증명이 유효하면 True, 그렇지 않으면 False.

    Example:
        is_valid = verify_proof(public_key, t, e, s, prime, generator)
    """
    # 좌변: G^s % PRIME 계산
    left = pow(generator, s, prime)

    # 우변: T * (PublicKey^e) % PRIME 계산
    right = (t * pow(public_key, e, prime)) % prime

    # 좌변과 우변 비교
    return left == right
