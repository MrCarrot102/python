class solution:
    def majorityElement(self, nums: list[int]) ->int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                condidate = num
            count += 1 if condidate == num else -1 