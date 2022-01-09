#!/usr/bin/env python3

def diverse(nums, size):
    """
    find the max size of nums you can diversify
    Time: O(n)
    Space: O(n)
    """
    nums.sort()
    for i in range(size - 1):
        if nums[i] == nums[i + 1]:
            nums[i] *= -1
    return len(set(nums))


if __name__ == "__main__":
    for _ in range(int(input())):
        size = int(input())
        nums = list(map(int, input().split()))
        print (diverse(nums, size))