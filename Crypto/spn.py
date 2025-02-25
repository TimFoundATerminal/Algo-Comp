

def format_state(state: list, group_size=4) -> None:
    """Display the state in a readable format"""
    binary_string = ''.join(str(bit) for bit in state)
    # Add spaces every group_size characters
    chunks = [binary_string[i:i+group_size] for i in range(0, len(binary_string), group_size)]
    return ' '.join(chunks)

class SBOX:
    """SBOX class for SPN cipher"""
    def __init__(self, table: list=None, bits=4):
        self.bits = bits
        self.size = 2**bits

        if table is None:
            table = [
                0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
                0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2
            ]

        self._validate_table(table)

        self._compute_inverse()


    def _validate_table(self, table):
        """Check if the mapping is valid"""
        if len(table) != self.size:
            raise ValueError("Invalid SBOX mapping")
        
        if not self._is_bijective(table):
            raise ValueError("Invalid SBOX mapping")
        else:
            self.table = table
        
    def _is_bijective(self, table):
        """Check if the mapping is bijective by having a one to one mapping"""
        # check the ranges of the table
        if not all(0 <= i < self.size for i in table):
            return False
        
        # check if the mapping is one to one
        return len(set(table)) == self.size
    
    def _compute_inverse(self) -> None:
        """Compute the inverse of the SBOX"""
        self.inverse = [0] * self.size
        for i, val in enumerate(self.table):
            self.inverse[val] = i

    def _convert_to_int(self, x: list) -> int:
        """Convert a binary list to an integer"""
        return sum([x[i] << i for i in range(self.bits)])
    
    def _convert_to_binary(self, x: int) -> list:
        """Convert an integer to a binary list"""
        return [x >> i & 1 for i in range(self.bits)]

    def encrypt(self, x: list) -> list:
        """Encrypt using the SBOX"""
        x = self._convert_to_int(x)
        y = self.table[x]
        return self._convert_to_binary(y)
    
    def decrypt(self, x: int) -> int:
        """Decrypt using the SBOX"""
        x = self._convert_to_int(x)
        y = self.inverse[x]
        return self._convert_to_binary(y)


class SubstitutionLayer:
    def __init__(self, sboxes: list, length: int):
        """Substitution layer for SPN cipher"""
        self.length = length
        
        # check sboxes are all of SBOX class and have the same size
        sbox_size, sbox_bits = sboxes[0].size, sboxes[0].bits
        if not all(isinstance(sbox, SBOX) and sbox.size == sbox_size for sbox in sboxes):
            raise ValueError("Invalid SBOX mapping/size")
        
        # check the length of the sboxes is a multiple of the length
        if self.length != (sbox_bits * len(sboxes)):
            raise ValueError("Invalid SBOX length")
        
        self.sboxes = sboxes
        self.bits = sbox_bits

    def encrypt(self, state: list) -> list:
        """Encrypt the state using the SBOXES"""
        if len(state) != self.length:
            raise ValueError("Invalid state length")
        
        return [sbox.encrypt(state[i:i+self.bits]) for i, sbox in enumerate(self.sboxes)]
    

    def decrypt(self, state: list) -> list:
        """Decrypt the state using the SBOXES"""
        if len(state) != self.length:
            raise ValueError("Invalid state length")
        
        return [sbox.decrypt(state[i:i+self.bits]) for i, sbox in enumerate(self.sboxes)]


class PermutationLayer:
    def __init__(self, perm_map: dict=None):
        """Permutation layer for SPN cipher"""
        self.length = len(perm_map)
        self.permutation = self._validate_perm_map(perm_map)
        self.inverse_permutation = self._inverse_perm_map()

    def _validate_perm_map(self, perm_map):
        """Check if the permutation map is valid"""
        if not all(0 <= i < self.length for i in perm_map.values()):
            raise ValueError("Invalid permutation map")
        
        if len(set(perm_map.keys())) != self.length:
            raise ValueError("Invalid permutation map")
        
        return perm_map

    def _inverse_perm_map(self):
        """Compute the inverse of the permutation map"""
        return {v: k for k, v in self.perm_map.items()}
    
    def encrypt(self, state: list) -> list:
        """Encrypt the state using the permutation map"""
        if len(state) != self.length:
            raise ValueError("Invalid state length")
        
        # create a list of all zeros
        return [state[self.permutation(i)] for i in state]
    
    def decrypt(self, state: list) -> list:
        """Decrypt the state using the inverse permutation map"""
        if len(state) != self.length:
            raise ValueError("Invalid state length")
        
        # create a list of all zeros
        return [state[self.inverse_permutation(i)] for i in state]

        


        