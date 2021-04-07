def search(nums, target):
    # make high and low
    # make mid from high+low // 2
    # guess = nums[mid]
    # if guess == target, return mid
    # if guess < target, make low = mid + 1
    # else guess > target, make high = mid - 1 
    # finally return -1 if there is no target
    high = len(nums) - 1
    low = 0
    while high >= low :

        mid = (high + low) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
    return -1

a = [-1,0,3,5,9,12] 
b = 9
print(search(a,b))