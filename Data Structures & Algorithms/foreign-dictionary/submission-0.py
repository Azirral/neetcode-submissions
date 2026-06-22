class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
            Let's play around a bit
            The problem is defined as follows:

            We've got a dictionary "words" that contains words from a different language
            The words are composed of letters from the latin alphabet, meaning 'a' to 'z'
            The words in the dictionary are supposed to be sorted lexicographically
            Which means, that if we have a dictionary, like: ["tro", "tre"]
            The letter 'o' is smaller than the letter 'e'

            Now, the output of the solution is supposed to return the lexicographical order
            of the language, based on the provided strings,
            There can be multiple orders of language, we are supposed to return all of them, 
            the order of the 'orders' isn't specified. If, the lexicographical order cannot be 
            constructed (is invalid), we are supposed to return an empty string.

            Invalid ordering is present, when:
            - Word that is a prefix of a different word appears after the longer word
            - There is a cycle present: A < B, B < C, C < A -> cycle (I don't know how to define it in words now, so let's just leave it like this)
            - The words are appearing incosistently, meaning that if we deduce that A < B, but then another pair of words tells us that B < A
            
            To determine a order between pairs, first we have to compare the first letters of the pair, then the second letters of the pair, and so on:
        '''
        adj = { letter:set() for word in words for letter in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False if visited True if in currentPath
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False

            res.append(c)
            return False
        
        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)