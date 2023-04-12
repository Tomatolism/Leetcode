class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index_M = {}
        for i, w in enumerate(words):
            index_M[w] = i

        visited_words = set()
        res_list = []

        words = sorted(words,key = len) 

        for word in words:
            for L in range(len(word)+1):

                if word[L:] == word[L:][::-1] and word[:L][::-1] in visited_words:
                    res_list.append([index_M[word], index_M[word[:L][::-1]]]) 
    
                if word[:L] == word[:L][::-1] and word[L:][::-1] in visited_words:
                    res_list.append([index_M[word[L:][::-1]], index_M[word]])
            visited_words.add(word)

        return res_list
