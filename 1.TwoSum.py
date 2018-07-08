class Solution:

    def twoSum(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: List[int]

        """

        List = []

        for i in range(len(nums)):

            if len(nums) == 1:

                if nums[i] == target:
                    List.append(i)

            else:

                for j in range(i + 1, len(nums)):

                    if nums[i] + nums[j] == target:
                        List.append(i)

                        List.append(j)

        return List