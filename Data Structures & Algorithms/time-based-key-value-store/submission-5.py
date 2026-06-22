class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not(key in self.t_map):
            self.t_map[key] = []    
        self.t_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not(key in self.t_map):
            return ""
        pairs = self.t_map[key]
        pairs.sort
        if timestamp < pairs[0][0]:
            return ""
        l, r = 0, len(pairs) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp < pairs[m][0]:
                r = m - 1
            elif timestamp > pairs[m][0]:
                l = m + 1
            else:
                return pairs[m][1]
        
        return pairs[r][1]
        
