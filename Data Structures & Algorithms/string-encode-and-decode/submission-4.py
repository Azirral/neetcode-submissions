class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "$" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])   
            strings.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return strings
