class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        character_map = {"2" : ["a","b","c"], "3" : ["d","e","f"], 
                         "4" : ["g", "h", "i"], "5" : ["j", "k", "l"], 
                         "6" : ["m", "n", "o"], "7" : ["p", "q", "r", "s"], 
                         "8" : ["t", "u", "v"], "9" : ["w", "x", "y", "z"]}
        
        res, cur = [], []

        def dfs(index):
            if index >= len(digits):
                res.append("".join(cur.copy()))
                return
            
            characters = character_map[digits[index]]

            for i in range(len(characters)):
                cur.append(characters[i])
                dfs(index + 1)
                cur.pop()
        
        dfs(0)

        return res