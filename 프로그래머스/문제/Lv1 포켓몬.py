def solution(nums):
    pick = len(nums) // 2
    nums = set(nums)
    answer = pick if len(nums) >= pick else len(nums)
    return answer
