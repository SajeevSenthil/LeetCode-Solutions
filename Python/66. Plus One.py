class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = num*10 + i
        num += 1
        List = [int(i) for i in str(num)]
        return List
        
