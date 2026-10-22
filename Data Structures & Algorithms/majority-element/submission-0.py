class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = defaultdict(int)
        max = res = 0
        for num in nums:
            map[num] += 1
            if max < map[num]:
                res = num
                max = map[num]
        return res
        
        