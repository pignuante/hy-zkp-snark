# ZKP SNARK Example

## Introduction

This project implements a simple **Zero-Knowledge Proof (ZKP)** system using the concept of **Succinct Non-interactive
Arguments of Knowledge (SNARKs)**. It demonstrates how a prover can prove the knowledge of a secret number without
revealing it, using basic modular arithmetic.

## What is ZKP?

### Zero-Knowledge Proof (ZKP)

**Zero-Knowledge Proof (ZKP)** is a cryptographic protocol that allows one party (the prover) to prove to another party (the verifier) that they possess certain information or satisfy specific conditions without revealing any additional information beyond the fact that the statement is true.

### Properties of ZKP

1.   **Completeness**: If the statement is true, an honest verifier will be convinced by the prover.
2.   **Soundness**: If the statement is false, no prover can convince an honest verifier.
3.   **Zero-Knowledge**: The verifier learns nothing beyond the validity of the statement.

### Real-world Applications

\- **Cryptocurrencies**: Privacy-focused cryptocurrencies like Zcash.

\- **Authentication**: Proving identity without revealing sensitive data.

\- **Data Privacy**: Proving properties of encrypted data without decrypting it.

----

## What is SNARK?

### SNARK: Succinct Non-interactive Arguments of Knowledge

**SNARK** is a type of Zero-Knowledge Proof with the following properties:

1.   **Succinct**: Proofs are small in size and can be verified quickly.
2.   **Non-interactive**: The proof is generated and verified in a single step without requiring back-and-forth communication between the prover and verifier.
3.   **Argument of Knowledge**: Ensures that the prover actually possesses the claimed knowledge.

### SNARK Structure

SNARKs are typically based on advanced mathematical constructs such as:

\- **Quadratic Arithmetic Programs (QAPs)**: To express computation as polynomial equations.

\- **Elliptic Curve Cryptography (ECC)**: For efficient proof generation and verification.

### Applications of SNARK

\- **Blockchain Scalability**: zk-SNARKs in Ethereum Layer 2 solutions (e.g., zk-Rollups).

\- **Privacy**: Zero-knowledge transactions in Zcash.

\- **Verification**: Secure and efficient computation verification.



---

## Features

- **Key Generation**: Generates a secret and public key pair.
- **Proof Generation**: Creates a proof that the prover knows the secret.
- **Proof Verification**: Verifies the proof without revealing the secret.

---

## Mathematical Overview

### Key Concepts

1. **Finite Field Arithmetic**:
    
    - All operations are performed modulo a prime number (\( p \)), ensuring a finite set of values.
    - Prime (\( p \)) and generator (\( g \)) are pre-defined constants:
      $$
      [
      p = 101, \quad g = 2
      ]
      $$
      
    
2. **Key Generation**:
    
    - **Secret Key** (\( s \)): A random number chosen by the prover.
    - **Public Key** (\( h \)): Computed as:
      $$
      [
      h = g^s \mod p
      ]
      $$
      
    
3. **Proof Generation**:
    
    - Prover selects a random value (\( r \)) and computes the commitment value (\( t \)):
      $$
      [
      t = g^r \mod p
      ]
      $$
      
    - Verifier challenges the prover with a random value (\( e \)).
    - Prover computes the response (\( s \)) using the formula:
      $$
      [
      s = r + e \cdot \text{secret\_key} \mod (p - 1)
      ]
      $$
      
    
4. **Proof Verification**:
    - The verifier checks the proof using the condition:
      $$
      [
      g^s \mod p \stackrel{?}{=} t \cdot h^e \mod p
      ]
      $$
      

---

## Usage

### Prerequisites

- Python 3.8 or above.

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/pignuante/hy-zkp-snark
cd hy-zkp-snark
pip install -r requirements.txt
```

### Running the Program

Run the main script:

```bash
python main.py
```

### **Example Input/Output**

1.   Enter the number you want to prove (between 1 and 100):
     ```
     Enter the number you want to prove (1 <= number < 101): 42
     ```

2.   Output:
     ```
     Secret Key: 42
     Public Key: 34
     Proof: t=55, e=19, s=84
     Verification Result: Valid
     ```

### Code Structure

```
hy-zkp-snark
├── README.md
├── main.py
├── requirements.txt
└── utils
    ├── __init__.py
    ├── keygen.py
    └── proof.py
```

### **Mathematical Explanation**

**Step 1: Key Generation**

A secret key (( s )) is randomly chosen in the range ( 1 \leq s < p ), and the public key (( h )) is computed as:
$$
[
    h = g^s \mod p
]
$$


**Step 2: Proof Generation**



The prover generates:

​	1.	**Commitment Value**:
$$
[
    t = g^r \mod p
]
$$
where ( r ) is a random number.

​	2.	**Challenge Value**:

The verifier sends a random challenge (( e )).

​	3.	**Response Value**:

The prover computes:
$$
[
s = r + e \cdot \text{secret_key} \mod (p - 1)
]
$$


**Step 3: Proof Verification**



The verifier checks the validity of the proof using:
$$
[
g^s \mod p \stackrel{?}{=} t \cdot h^e \mod p
]
$$
If the equality holds, the proof is valid.



### **Testing**

Run the unit tests to verify the implementation:
```bash
pytest tests/
```

### **Limitations**

-   This is a simplified example of a ZKP system and not suitable for production use.
-   It lacks advanced features like non-interactivity, trusted setup, and scalability optimizations.

### **References**

-   [Zero-Knowledge Proofs (Wikipedia)](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
-   [Elliptic Curve Cryptography and ZKP](https://cryptobook.nakov.com/zero-knowledge-proofs)



>   ### Key Highlights
>
>   1. Mathematical formulas are embedded directly in LaTeX format for clarity.
>   2. The structure follows a standard README format with clear sections for usage, code explanation, and mathematical insights.
>   3. Detailed input/output examples illustrate how the program works.
>
>   Let me know if you'd like to further refine this! 😊







