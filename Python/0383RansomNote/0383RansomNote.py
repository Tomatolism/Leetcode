## Time: O(m+n)
## Memory: O(m+n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}

        for s in magazine:
            if s in magazineDict:
                magazineDict[s] +=1
            else:
                magazineDict[s] = 1

        for s in ransomNote:
            if s in ransomDict:
                ransomDict[s] +=1
            else:
                ransomDict[s] = 1                       

        for item in ransomDict:
            if item not in magazineDict:
                return False
            if ransomDict[item] > magazineDict[item]:
                return False

        return True
