class Solution(object):
    total_ways = 0
    recursive_call_dict = {}
    # calls = 0
    def next_step(self, n):
        if n == 2:
            self.calls += 1
            return 2
        if n == 1:
            self.calls += 1
            return 1
        if n-1 in self.recursive_call_dict:
            v1 = self.recursive_call_dict[n-1]
        else:
            v1 = self.next_step(n-1)
            self.recursive_call_dict[n-1] = v1
        if n-2 in self.recursive_call_dict:
            v2 = self.recursive_call_dict[n-2]
        else:
            v2 = self.next_step(n-2)
            self.recursive_call_dict[n-2] = v2
        return v1 + v2
        # return self.next_step(n-1) + self.next_step(n-2)


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 2
        if n==1:
            return 1
        self.total_ways += self.next_step(n-1) + self.next_step(n-2)
        return self.total_ways
        # return self.total_ways, self.calls

# comparing total number of calls using self.calls shows the importance of using a dict
obj = Solution()
print(obj.climbStairs(32))
