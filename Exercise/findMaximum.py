def find_maximum(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num  


#[2,3,5,67,8]
