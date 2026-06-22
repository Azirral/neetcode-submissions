class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            cur.append(candidates[index])
            dfs(index + 1, cur, candidates[index] + total)
            cur.pop()
            i = index + 1
            while i < len(candidates) and candidates[index] == candidates[i]:
                i += 1
            
            dfs(i, cur, total)
        
        dfs(0, [], 0)
        return res