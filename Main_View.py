import os
import sys
import csv
import shutil
import time
import pandas as pd
from tkinter import *
import time
from time import sleep
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import glob
from tkinter import *
from Network import *
import User_Registration
import LECC
import LECSKEA
import simulation
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from plyer import notification
from SHA_3 import *
from Metrics import *
from tkinter import Tk, Label, Button
from tkinter import messagebox
import warnings
warnings.filterwarnings("ignore")
def Network():
    print ("\t\t\t |--------- ****** Design and Analysis of Blockchain Protocols with a Special Emphasis on Lightweight Cryptography ****** --------|")
    time.sleep(1)
    print('================================================================================================================================')
    print ("\t\t\t ****** A NETWORK, IT CONSISTS OF 50- IOT NODES, 1- CLOUD SERVER AND 1- BLOCKCHAIN ******")
    print('================================================================================================================================')
    time.sleep(1)
    print ("\t\t\t ****** NETWORK CONSTRUCTION ******")
    notification.notify(
            message='NETWORK CONSTRUCTION',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    Network_Construction();
    time.sleep(1)
    messagebox.showinfo('Network','Network Construction process is successfully completed!')
    print('\nNetwork Construction process is successfully completed!\n')
    print('\nNext Click USER REGISTRATION button...\n')
def UserRegistration():
    time.sleep(1)
    print ("\t\t\t ****** USER REGISTRATION ******")
    notification.notify(
            message='USER REGISTRATION',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    User_Registration.main();
    time.sleep(1)
    messagebox.showinfo('USER REGISTRATION','USER REGISTRATION successfully completed!')
    print('\nUSER REGISTRATION is successfully completed!\n')
    print('\nNext Click ENCRYPTION button...\n')
def Encryption():
    time.sleep(1)
    print ("\t\t\t ****** ENCRYPTION ******")
    notification.notify(
            message='ENCRYPTION',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    notification.notify(
            message='Lightweight Elliptic Curve Cryptography (LECC)',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    print ("\t\t\t ****** Lightweight Elliptic Curve Cryptography (LECC) ******")
    LECC.Encryptionkeyexchange();
    time.sleep(1)
    notification.notify(
            message='Lightweight Elliptic Curve Secure Key Exchange and Authentication (LECSKEA)',
            app_name='My Python App',
            app_icon=None,
        )
    print ("\t\t\t ****** Lightweight Elliptic Curve Secure Key Exchange and Authentication (LECSKEA) ******")
    LECSKEA.Decryption();
    time.sleep(1)
    messagebox.showinfo('ENCRYPTION','ENCRYPTION process is Completed!')
    print('\nENCRYPTION is successfully completed!\n')
    print('\nNext Click INTEGRATE THE BLOCKCHAIN button...\n')
def Blockchain():
    time.sleep(1)
    print ("\t\t\t ****** INTEGRATE THE BLOCKCHAIN ******")
    notification.notify(
            message='INTEGRATE THE BLOCKCHAIN',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    main();
    time.sleep(1)
    messagebox.showinfo('INTEGRATE THE BLOCKCHAIN','INTEGRATE THE BLOCKCHAIN process is Completed!')
    print('\nINTEGRATE THE BLOCKCHAIN is successfully completed!\n')
    print('\nNext Click STORE THE DATA IN BLOCKCHAIN button...\n')
def StoreBlockchain():
    time.sleep(1)
    print ("\t\t\t ****** STORE THE DATA IN BLOCKCHAIN ******")
    notification.notify(
            message='STORE THE DATA IN BLOCKCHAIN',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    import hashlib
    import json
    import random
    from reedsolo import RSCodec
    class Block:
        def __init__(self, index, previous_hash, data, hash_value, nonce):
            self.index = index
            self.previous_hash = previous_hash
            self.data = data
            self.hash = hash_value
            self.nonce = nonce
    class Blockchain:
        def __init__(self):
            self.chain = []
            self.create_genesis_block()
        def create_genesis_block(self):
            genesis_block = Block(0, "0", "Genesis Block", "0", 0)
            self.chain.append(genesis_block)
        def create_new_block(self, data, previous_hash, nonce):
            index = len(self.chain)
            block_hash = self.calculate_hash(index, previous_hash, data, nonce)
            new_block = Block(index, previous_hash, data, block_hash, nonce)
            self.chain.append(new_block)
            return new_block
        def calculate_hash(self, index, previous_hash, data, nonce):
            block_header = f"{index}{previous_hash}{data}{nonce}"
            return hashlib.sha256(block_header.encode()).hexdigest()
        def proof_of_work(self, previous_proof):
            new_proof = 1
            while not self.is_valid_proof(previous_proof, new_proof):
                new_proof += 1
            return new_proof
        def is_valid_proof(self, previous_proof, proof):
            guess = f"{previous_proof}{proof}".encode()
            guess_hash = hashlib.sha256(guess).hexdigest()
            return guess_hash[:4] == "0000" 
        def get_previous_block(self):
            return self.chain[-1]
        def encode_data(self, data):
            rs = RSCodec(10)  
            encoded_data = rs.encode(data.encode())
            return encoded_data
        def add_block(self, data):
            previous_block = self.get_previous_block()
            previous_proof = previous_block.nonce
            nonce = self.proof_of_work(previous_proof)
            encoded_data = self.encode_data(data)
            new_block = self.create_new_block(encoded_data, previous_block.hash, nonce)
            return new_block
        def decode_data(self, encoded_data, node_id):
            rs = RSCodec(10)  
            try:
                decoded_data, _ = rs.decode(encoded_data)
                return decoded_data.decode(), node_id
            except ValueError:
                print(f"Unable to decode data for Node {node_id}. More nodes needed for reconstruction.")
                return None, None
    blockchain = Blockchain()
    data_to_store = "Hello, Blockchain!"
    blockchain.add_block(data_to_store)
    random_node_id = random.randint(1, 100)
    decoded_data, node_id = blockchain.decode_data(blockchain.chain[1].data, random_node_id)
    if decoded_data is not None:
        print(f"Decoded Data for Node {node_id}:", decoded_data)
    else:
        print(f"No Decoded Data for Node {node_id}")
    time.sleep(1)
    messagebox.showinfo('STORE THE DATA IN BLOCKCHAIN','STORE THE DATA IN BLOCKCHAIN process is Completed!')
    print('\nSTORE THE DATA IN BLOCKCHAIN process is successfully completed!\n')
    print('\nNext Click PERFORMANCE METRICS button...\n')
def Performancemetrics():
    time.sleep(1)
    print ("\t\t\t ****** PERFORMANCE METRICS ******")
    print('\nGraph generation process is starting\n')
    notification.notify(
            message='PERFORMANCE METRICS',
            app_name='My Python App',
            app_icon=None,
        )
    time.sleep(1)
    PerformanceMetrics();
    print('\nGraph is Generated Successfully...!')
    print('==========================================================================================')
    print("\n\n+++++++++++++++++++++++++++++++++++++++ END ++++++++++++++++++++++++++++++++++++")
def main_screen():
    global window
    window = Tk()
    window.title("Design and Analysis of Blockchain Protocols")
    window_width = 850
    window_height = 800
    window.geometry(f"{window_width}x{window_height}")
    window.configure(background="floralwhite")
    Label(window, text = "Design and Analysis of Blockchain Protocols",bg ="hotpink",fg ="floralwhite",width = "500", height = "6",font=('Georgia',14)).pack()
    Label(text = "",bg="floralwhite").pack()
    b1 = Button(text = "START", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = Network)
    b1.pack(pady=10)
    b2 = Button(text = "USER REGISTRATION", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = UserRegistration)
    b2.pack(pady=10)
    b3 = Button(text = "ENCRYPTION", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = Encryption)
    b3.pack(pady=10)
    b4 = Button(text = "INTEGRATE THE BLOCKCHAIN", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = Blockchain)
    b4.pack(pady=10)
    b5 = Button(text = "STORE THE DATA\nIN BLOCKCHAIN", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = StoreBlockchain)
    b5.pack(pady=10)
    b6 = Button(text = "PERFORMANCE\nMETRICS", height = "2", width = "25",bg = "lightsteelblue3",fg ="black",font=('Georgia',13), command = Performancemetrics)
    b6.pack(pady=10)
    Label(text = "",bg="floralwhite").pack()    
    window.mainloop()
main_screen()
