import logging 

nums = [3,2,2,3]
val = 3

def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        resultant = []
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k = k + 1
        return k

result = removeElement(nums, val)

print (f'{result}')
