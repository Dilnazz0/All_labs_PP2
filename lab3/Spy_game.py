a=list(map(int,input("Enter the num separated by space:").split()))
def has_007(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
print(has_007(a))