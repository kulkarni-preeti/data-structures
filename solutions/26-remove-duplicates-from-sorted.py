def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        seen = []
        for i in range(len(nums)):
            if(nums[i] not in seen):
                seen.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k