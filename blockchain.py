import hashlib


class Block:
    def __init__(self, payload, previous):
        self.payload = payload
        self.previous = previous
        self.nonce = None
        self.hash = None
        self.mine()

    def mine(self):
        self.nonce = 0
        self.hash_block()
        while self.hash[0:2] != "00":
            self.nonce += 1
            self.hash_block()

    def hash_block(self):
        hex_hash = hashlib.sha256(str(self.previous) + str(self.payload) + str(self.nonce))
        self.hash = hex_hash.hexdigest()

    def block_valid(self):
        return self.hash[0:2] == "00"

    def print_block(self):
        if self.previous is None:
            previous = None
        else:
            previous = self.previous.hash
        print "hash    : %s\n" \
              "payload : %s\n" \
              "nonce   : %s\n" \
              "previous: %s\n" % (str(self.hash), str(self.payload), str(self.nonce), str(previous))


class BlockChain:
    def __init__(self, start=None):
        self.start = start
        self.end = start

    def add_block(self, payload):
        new_block = Block(payload=payload, previous=self.end)
        self.end = new_block

    def verify_chain(self):
        valid = True
        current_block = self.end
        while current_block is not None:
            if not current_block.block_valid():
                print "invalid hash hash: %s" % current_block.hash()
                valid = False
            current_block = current_block.previous
        return valid

    def print_chain(self):
        current_block = self.end
        while current_block is not None:
            current_block.print_block()
            current_block = current_block.previous


my_chain = BlockChain()
my_chain.add_block(1)
my_chain.add_block(2)
my_chain.add_block(3)
my_chain.add_block(4)
my_chain.add_block(5)

my_chain.print_chain()
