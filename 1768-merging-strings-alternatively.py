class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2)

        l=max(w1,w2)

        s=""

        for i in range (l):
            if i<w1:
                s+=word1[i]
                
            if i<w2:
                s+=word2[i]            
        return s