class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        length = len(self.nums)
        i = 0
        i2 = 0
        x = 0
        y = x + 1
        while(i < length):
            t_y = y
            while(i2 < length-1):
                if(self.target == self.nums[x]+self.nums[t_y]):
                    return ([x,t_y])
                t_y += 1
                if(t_y>length-1):
                    t_y = 0
                i2 += 1
            i += 1
            i2 = 0
            x += 1
            y += 1
            if(y>length-1):
                y=0
            if(x>length-1):
                x=0
            
test_nums = [2, 7, 11, 15]
test_target = 9
testclass = Solution()
result = testclass.twoSum(test_nums,test_target)
print(result)