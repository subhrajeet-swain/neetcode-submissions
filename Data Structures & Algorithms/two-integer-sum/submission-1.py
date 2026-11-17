class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #All seen numbers
        #Complement number = target-num
        #If complement in seen, then retun complement number and it's index, else add to seen


        seen ={}

        for i, num in enumerate(nums):
            complement = target-num

            if complement in seen:
                return [seen[complement], i]

            seen[num]=i

        return None