class Solution:

    def playground():

        nums = [54,22,15,48,332,1265,1,664,223,156]
        evens = []

        print(f"nums: {nums}")

        # Without list comprehension
        for num in nums:
            if num%2==0: evens.append(num)
        print(f"evens WITHOUT: {evens}")

        evens = []
        evens = [num for num in nums if num%2==0]
        print(f"evens WITH: {evens}")


        doubles1To11 = []
        for i in range(1,11):
            if i%2==0: doubles1To11.append(i)
        print(f"doubles1To11 WITHOUT: {doubles1To11}")

        doubles1To11 = []
        doubles1To11 = [i for i in range(1,11) if i%2==0]
        print(f"doubles1To11 WITH: {doubles1To11}")

if __name__ == "__main__":
    sol = Solution
    sol.playground()