from hashlib import sha3_256
import time
import simulation
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash_value, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash_value
        self.nonce = nonce
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
    def create_genesis_block(self):
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", "0", 0)
        self.chain.append(genesis_block)
    def create_new_block(self, data, previous_hash, nonce):
        index = len(self.chain)
        timestamp = int(time.time())
        block_hash = self.calculate_hash(index, previous_hash, timestamp, data, nonce)
        new_block = Block(index, previous_hash, timestamp, data, block_hash, nonce)
        self.chain.append(new_block)
        return new_block
    def calculate_hash(self, index, previous_hash, timestamp, data, nonce):
        block_header = f"{index}{previous_hash}{timestamp}{data}{nonce}"
        return sha3_256(block_header.encode()).hexdigest()
    def proof_of_work(self, previous_proof):
        new_proof = 1
        while not self.is_valid_proof(previous_proof, new_proof):
            new_proof += 1
        return new_proof
    def is_valid_proof(self, previous_proof, proof):
        guess = f"{previous_proof}{proof}".encode()
        guess_hash = sha3_256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    def get_previous_block(self):
        return self.chain[-1]
class BFTNode:
    def __init__(self):
        self.node_id = simulation.simInt(1, 100)
    def reach_consensus(self, blockchain):
        if len(blockchain.chain) >= 2:
            print(f"Node {self.node_id} reached consensus. Block added to the blockchain.")
            return True
        else:
            print(f"Node {self.node_id} did not reach consensus. Block rejected.")
            return False

def main():
    blockchain = Blockchain()
    bft_node1 = BFTNode()
    bft_node2 = BFTNode()
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block.nonce
    proof = blockchain.proof_of_work(previous_proof)
    data = "Some transaction data"
    new_block = blockchain.create_new_block(data, previous_block.hash, proof)
    if bft_node2.reach_consensus(blockchain):
        print("Consensus reached. Block added to the blockchain.")
    else:
        print("Consensus not reached. Block rejected.")
if __name__ == "__main__":
    main()
