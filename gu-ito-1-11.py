'''A group of friends is planning a road trip to visit multiple destinations. Each friend owns a car, and they need to ensure that the total fuel consumption of their vehicles matches the distance they plan to travel. The distance to each destination is represented by a list of integers, where positive values indicate the distance in kilometers they need to travel, and negative values indicate the distance they need to backtrack.

The friends can adjust the fuel levels of their cars by adding or subtracting fuel, with each adjustment costing one coin. They want to minimize the total cost of adjusting their fuel levels to match the total distance they plan to travel.

What is the minimum cost the group will have to pay to ensure that the total fuel consumption of their vehicles equals the total distance they plan to travel?

Input:

The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of destinations the group plans to visit.
The second line contains n integers a1, a2, ..., an (-10^9 ≤ ai ≤ 10^9) — representing the distances to each destination. Positive values indicate the distance they need to travel, and negative values indicate the distance they need to backtrack.
Output:

Output a single number — the minimal number of coins you need to pay to make the product equal to 1.

Sample input:

4
0 0 0 0

Sample output:

4'''



class NumberProcessor:
    def __init__(self, l):
        self.l = l
        self.s = 0
        self.odd = 0
        self.nz = 0

    def process_numbers(self):
        #..... YOUR CODE STARTS HERE .....

        for i in range(len(self.l)):
            if int(self.l[i])<0:
                self.odd+=1
                self.s+=abs(-1-int(self.l[i]))
            elif int(self.l[i])>0:
                self.s+=(int(self.l[i])-1)
            else:
                
                self.nz+=1
        
        if self.odd%2!=0:
            if '0' in self.l:
                return self.s+1*self.za
            else:
                return self.s+2
        else:
            if '0' in self.l:
                return self.s+1*self.nz
            else:
                return self.s
       #..... YOUR CODE ENDS HERE .....        
  

if __name__ == "__main__":
    n = int(input())
    l = str(input()).split(" ")

    number_processor = NumberProcessor(l)
    result = number_processor.process_numbers()
    print(result)
