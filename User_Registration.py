import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
class RegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.fingerprint_var = tk.StringVar()
        self.create_registration_widgets()

    def create_registration_widgets(self):
        tk.Label(self.root, text="Username:").pack()
        tk.Entry(self.root, textvariable=self.username_var).pack()
        tk.Label(self.root, text="Password:").pack()
        tk.Entry(self.root, textvariable=self.password_var, show="*").pack()
        tk.Label(self.root, text="Fingerprint:").pack()
        tk.Entry(self.root, textvariable=self.fingerprint_var).pack()
        tk.Button(self.root, text="Choose Fingerprint Image", command=self.choose_fingerprint).pack()
        tk.Button(self.root, text="Register", command=self.register_user).pack()

    def choose_fingerprint(self):
        file_path = filedialog.askopenfilename(title="Select Fingerprint Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            random_value = random.randint(100000, 999999)
            self.fingerprint_var.set(f"{random_value}")

    def register_user(self):
        username = self.username_var.get()
        password = self.password_var.get()
        fingerprint = self.fingerprint_var.get()
        if not username or not password or not fingerprint:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        with open("user_data.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}, Fingerprint: {fingerprint}\n")
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        self.username_var.set("")
        self.password_var.set("")
        self.fingerprint_var.set("")
        self.create_login_screen()

    def create_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.login_username_var = tk.StringVar()
        self.login_password_var = tk.StringVar()
        self.login_fingerprint_var = tk.StringVar()

        tk.Label(self.root, text="Login").pack()

        tk.Label(self.root, text="Username:").pack()
        tk.Entry(self.root, textvariable=self.login_username_var).pack()

        tk.Label(self.root, text="Password:").pack()
        tk.Entry(self.root, textvariable=self.login_password_var, show="*").pack()

        tk.Label(self.root, text="Fingerprint:").pack()
        tk.Entry(self.root, textvariable=self.login_fingerprint_var).pack()

        tk.Button(self.root, text="Login", command=self.login_user).pack()

    def login_user(self):
        login_username = self.login_username_var.get()
        login_password = self.login_password_var.get()
        login_fingerprint = self.login_fingerprint_var.get()

        with open("user_data.txt", "r") as file:
            user_data = file.readlines()

        login_credentials = f"Username: {login_username}, Password: {login_password}, Fingerprint: {login_fingerprint}\n"
        if login_credentials in user_data:
            messagebox.showinfo("Login Successful", "Login successful!")

            self.encrypt_and_save_login_details(login_username, login_password, login_fingerprint)

        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def encrypt_and_save_login_details(self, login_username, login_password, login_fingerprint):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
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

        with open("private_key.pem", 'wb') as f:
            f.write(private_key_bytes)

        with open("public_key.pem", 'wb') as f:
            f.write(public_key_bytes)

        data_to_encrypt = f"{login_username},{login_password},{login_fingerprint}".encode()
        encrypted_data = public_key.encrypt(
            data_to_encrypt,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open("encrypted_login_details.bin", 'wb') as f:
            f.write(encrypted_data)

def main():
    root = tk.Tk()
    app = RegistrationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
