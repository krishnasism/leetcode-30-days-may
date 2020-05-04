class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num).replace('0b', '')
        binary = "".join(["1" if b == "0" else "0" for b in binary])
        return int(binary, 2)
