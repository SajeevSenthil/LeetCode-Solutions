class Solution:
    def factorial(self,n):
        if n == 0:
            return 1
        return n*factorial(n-1)

    def nCr(self, n, r):
        a = self.factorial(n) // (self.factorial(r) * self.factorial(n - r))
        return a
        
    def generate(self, numRows: int) -> List[List[int]]:
        List = []
        for i in range(numRows):
            newList = []
            for r in range(i+1):
                a = self.nCr(i,r)
                newList.append(a)
            List.append(newList)
        return List
