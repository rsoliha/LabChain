import time

class Block:
    def __init__(self, block_number, merkel_tree_root, predecessor_hash, block_creator_id, transactions):
        """Constructor for Block class

        Args:
            transactions (List): Transactions to form the block

        Class Variables:
            __block_number (int): Unique ID for block created
            __timestamp (time): Time when block was created
            __merkle_tree_root (hash): Hash of Transactions merkle root
            __predecessor_hash (hash): Previous Block hash value
            __nonce (int): Nonce matching blockchain criteria
            __block_creator_id (String): Node ID who created the block
            __transactions (List): Transactions in the block

        """
        self.__block_number = block_number
        self.__timestamp = time.time()
        self.__merkle_tree_root = merkel_tree_root
        self.__predecessor_hash = predecessor_hash
        self.__nonce = None
        self.__block_creator_id = block_creator_id
        self.__transactions = transactions

    def get_json(self):
       pass

    def get_predecessor_hash(self):
       return self.__predecessor_hash

    def get_transactions(self):
        pass
