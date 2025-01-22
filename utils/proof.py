# utils/proof.py
import random


def generate_proof(secret_key, prime, generator):
    """
    증명 생성
    """
    r = random.randint(1, prime - 1)  # 무작위 값
    t = pow(generator, r, prime)  # 커밋 값

    e = random.randint(1, prime - 1)  # 검증자가 보내는 무작위 챌린지 값
    s = (r + e * secret_key) % (prime - 1)  # 응답 계산

    return t, e, s


def verify_proof(public_key, t, e, s, prime, generator):
    """
    증명 검증
    """
    left = pow(generator, s, prime)  # G^s
    right = (t * pow(public_key, e, prime)) % prime  # T * (PublicKey^e)
    return left == right
