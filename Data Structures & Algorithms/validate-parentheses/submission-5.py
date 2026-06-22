class Solution:
    def isValid(self, s: str) -> bool:
        # Intuition: two pointer solution
        # ( - 40
        # ) - 41

        # [ - 91
        # ] - 93

        # { - 123
        # } - 125
        stack = []
        close_to_open = {")" : "(", 
                         "]" : "[", 
                         "}" : "{"}
        res = False if s else True
        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True
                