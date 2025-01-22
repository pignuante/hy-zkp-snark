# main.py
from utils.keygen import generate_keys
from utils.proof import generate_proof, verify_proof

if __name__ == "__main__":
    """
    메인 실행 파일.

    - 사용자가 증명하려는 숫자를 입력받아 비밀 키로 사용.
    - 증명을 생성하고 검증 과정을 실행.
    """
    try:
        # 사용자가 증명하길 원하는 숫자 입력
        user_secret = int(input("Enter the number you want to prove (1 <= number < 101): "))
        if not (1 <= user_secret < 101):
            raise ValueError("Number out of range. Must be between 1 and 100.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        exit(1)

    # 키 생성
    secret_key, public_key, prime, generator = generate_keys()
    secret_key = user_secret  # 사용자의 입력을 비밀 키로 설정
    public_key = pow(generator, secret_key, prime)  # 공개 키 재계산

    print(f"Secret Key: {secret_key}")
    print(f"Public Key: {public_key}")

    # 증명 생성
    t, e, s = generate_proof(secret_key, prime, generator)
    print(f"Proof: t={t}, e={e}, s={s}")

    # 검증
    is_valid = verify_proof(public_key, t, e, s, prime, generator)
    print(f"Verification Result: {'Valid' if is_valid else 'Invalid'}")
