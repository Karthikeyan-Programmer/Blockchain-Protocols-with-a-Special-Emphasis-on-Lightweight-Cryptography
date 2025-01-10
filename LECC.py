from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from tinyec import registry
import os
import base64
def Encryptionkeyexchange():
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
    def encrypt(username, password, fingerprint):
        curve = registry.get_curve('secp192r1')
        private_key = int.from_bytes(os.urandom(24), byteorder='big')
        public_key = private_key * curve.g

        salt = os.urandom(16)
        key = derive_key(password, salt)
        data = f"Username: {username}, Fingerprint: {fingerprint}, Public Key: {public_key.x},{public_key.y}"
        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data.encode()) + encryptor.finalize()
        return salt, ciphertext
    def decrypt(password, salt, ciphertext):
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CFB(os.urandom(16)))
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_data
    def main():
        username = "kk"
        password = "kk@123"
        fingerprint = "661594"
        salt, ciphertext = encrypt(username, password, fingerprint)
        decrypted_data = decrypt(password, salt, ciphertext)
        print("Encrypted Data:")
        print(f"Salt: {salt.hex()}")
        print(f"Ciphertext: {base64.b64encode(ciphertext).decode()}\n")
        print("Decrypted Data:")
        print(decrypted_data)
    main()
if __name__ == "__main__":
    Encryptionkeyexchange()
