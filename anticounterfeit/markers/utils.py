from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import os

KEYS_DIR = 'keys'
PRIVATE_KEY_FILE = os.path.join(KEYS_DIR, 'private_key.pem')
PUBLIC_KEY_FILE = os.path.join(KEYS_DIR, 'public_key.pem')

def generate_keys():
    if not os.path.exists(KEYS_DIR):
        os.makedirs(KEYS_DIR)

    #GENERATE THE PRIVATE KEY
    private_key = ed25519.Ed25519PrivateKey.generate()

    with open(PRIVATE_KEY_FILE, 'wb') as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    public_key = private_key.public_key()
    with open(PUBLIC_KEY_FILE, 'wb') as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print(f'Keys generated in {KEYS_DIR}/')