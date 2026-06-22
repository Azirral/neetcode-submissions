class Solution:
    def isValid(self, s: str) -> bool:
        # Intuition: two pointer solution
        # ( - 40
        # ) - 41

        # [ - 91
        # ] - 93

        # { - 123
        # } - 125
        
        # how to track the order in which the brackets are closed
        # always the newest bracket should be closed first
        # popping from a FIFO queue 
        # if queue empty, then all are closed
        q = collections.deque()
        res = False if s else True
        for char in s:
            ascii = ord(char)
            if ascii in [40, 91, 123]:
                q.append(ascii)
            elif q and (q[-1] == ascii - 1 or q[-1] == ascii - 2):
                q.pop()
            else:
                return False
        
        return False if q else True
                