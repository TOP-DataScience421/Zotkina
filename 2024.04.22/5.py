def central_tendency(num1: float, num2: float, *nums: float) -> dict[str, float]:
    nums = (num1, num2) + nums
    n=len(nums)
    sort_nums = sorted(nums)
    if n % 2 == 0:
        median = (sort_nums[n // 2 - 1] + sort_nums[n // 2]) / 2
    else:
        median = sort_nums[n // 2]
        
    arithmetic = sum(nums) / n
    geometric = 1

    for num in nums:
        geometric *= num
    geometric **= (1 / n)
    harmonic = n / sum (1 / num for num in nums)

    return {'median': median, 'arithmetic': arithmetic, 'geometric': geometric, 'harmonic': harmonic }
 
#central_tendency(1, 2, 3, 4)
#{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
#>>> central_tendency(1, 2, 3, 4, 5)
#{'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}