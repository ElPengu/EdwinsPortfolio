class Solution:

    def add(self, x: int, y: int)->int:
        
        return self.helper(x,y)
    
    def helper(self, x: int, y: int)->int:
        return x+y

if __name__ == "__main__":
    sol = Solution()
    x, y = 3, 5
    print(sol.add(x,y)) # 8