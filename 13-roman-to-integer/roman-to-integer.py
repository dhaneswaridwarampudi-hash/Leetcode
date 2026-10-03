class Solution:
    def value(self,r):
        if r=='C':
            return 100
        elif r=='V':
            return 5
        elif r=='X':
            return 10
        elif r=='L':
            return 50
        elif r=='I':
            return 1
        elif r=='D':
            return 500 
        elif r=='M':
            return 1000                 

    def romanToInt(self, s: str) -> int:
        
        total=0
        for i in range(len(s)):
            num1=self.value(s[i]) #1
            if i+1<len(s):
                num2=self.value(s[i+1])
                if num1>=num2:
                    total+=num1
                else:
                    total-=num1
            else:
                 total+=num1
        return total