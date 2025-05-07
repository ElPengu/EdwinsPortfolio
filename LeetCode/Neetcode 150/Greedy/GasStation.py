from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        - n gas stations in circular array
        - gas[i] is gas you can get at station i
        - cost[i] is the amount of gas to travel from the ith station 
        to the (i+1)th station (the last is connected to the first)
        - You begin with an empty tank at a gas station
        - Which gas station can you start at to travel around in 1 circuit
        - At most 1 solution
        - If impossible, return -1

        - At station i, cost[i] tells you how much to reach the NEXT 
        station, and gas[i] tells you how much you can get

        - Let's write gas and cost on top of each other
        - Also, diff is gas subtract cost
        - gas : [ 1, 2, 3, 4, 5]
        - cost: [ 3, 4, 5, 1, 2]
        - diff: [-2,-2,-2, 3, 3]
        - pos:  [ 0, 1, 2, 3, 4]
        - At start position i, we have 0 gas. To reach i+1 we fuel up 
        gas[i] and pay cost[i]
        - This leads to diff[i]=gas[i]+cost[i], clearly we can only 
        start at a position i where leave with >=0 fuel
        - In this example we cannot start at positions 0,1,2
        - We could start at position 3, leaving with 3 fuel
        - Now we are at position 4, we can leave with (3+3=)6 fuel
        - Now we are at position 0, we can leave with (6-2=)4 fuel
        - Now we are at position 1, we can leave with (4-2=)2 fuel
        - Now we are at position 2, we can leave with (2-2=)0 fuel
        - Now we are at position 3, which we were able to leave 
        already!
        - Return station 3!
        
        - We save some time with an insight
        - sum(gas)>=sum(cost) must be the case, otherwise there is not 
        enough gas to cover the cost

        - Algorithm
        - SET i=0
        - SET res=-1
        - FOR i in range(0, LEN(gas)): 
        -> SET total+=diff[i]
        -> IF total == 0 AND res != -1: res=i
        - RETURN res
        - O(n) time <- We check every station 1
        - O(1) space <- We only store the fuel we have

        - Here is a proof of why this greedy solution works
        - 1. We are guaranteed a unique solution
        -> There is ONLY one gas station that can go through the circuit!
        - 2. The solution must wrap around to the start, therefore it 
        must reach the end of the array at some point
        -> If it doesn't, then it is certainly NOT a station that you 
        can start at 
        - 3. The first index that can reach the end of the array will 
        always result in a higher gas total by the end of the array 
        than any index after it can reach the end of the array
        -> If you can reach the final station by i or i+1, you will have 
        more fuel by starting at i
        - 4. By conditions 1, 2, and 3, the solution must be the first 
        index that can reach the end of the array
        -> The solution must reach the end of the circuit at minimum. As 
        there is only a single solution, we'd better finish at the end 
        with as much fuel as possible, so we start at exactly the 
        first station that we see can reach the end of the circuit 
        since it will end up there with the most fuel on balance compared 
        to starting at any other station!
        '''

        if sum(gas) < sum(cost):
            # There is not enough fuel to pay the cost regardless of 
            # where we start
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                # This position cannot reach the 
                # end!

                # Try the next position by resetting 
                # the total to zero
                total = 0
                res = i+1
        
        return res
    
if __name__ == "__main__":
    sol = Solution()
    gas = [1,2,3,4]
    cost = [2,2,4,1]
    print(sol.canCompleteCircuit(gas, cost)) # 3
    gas = [1,2,3]
    cost = [2,3,2]
    print(sol.canCompleteCircuit(gas, cost)) # -1