import os
import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
def Decryption():
    def sha256(message):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(message)
        return digest.finalize()
    def derive_key(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1000000,
        )
        return kdf.derive(password.encode())
    def generate_ecdh_key_pair():
        private_key = ec.generate_private_key(ec.SECP256R1())
        public_key = private_key.public_key()

        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_key_bytes, public_key_bytes
    def derive_shared_key(private_key_bytes, peer_public_key_bytes):
        private_key = serialization.load_pem_private_key(private_key_bytes, password=None)
        peer_public_key = serialization.load_pem_public_key(peer_public_key_bytes)
        shared_key = private_key.exchange(ec.ECDH(), peer_public_key)
        return shared_key
    def encrypt(data, key):
        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
        return ciphertext
    def decrypt(ciphertext, key):
        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data
    def save_user_data(filename, username, password, fingerprint, public_key, private_key):
        with open(filename, 'a') as file:
            file.write(f"Public Key: {public_key}\n")
            file.write(f"Private Key: {private_key}\n")
    def load_user_data(filename):
        user_data = []
        with open(filename, 'r') as file:
            for line in file:
                user_data.append(line.strip())
        return user_data
    def main():
        username = "kk"
        password = "kk123"
        fingerprint = "123456"
        private_key_bytes, public_key_bytes = generate_ecdh_key_pair()
        public_key = base64.b64encode(public_key_bytes).decode()
        private_key = base64.b64encode(private_key_bytes).decode()
        save_user_data("user_data1.txt", username, password, fingerprint, public_key, private_key)
        loaded_user_data = load_user_data("user_data1.txt")
        for user_entry in loaded_user_data:
            print(user_entry)

    main()
if __name__ == "__main__":
    Decryption()
