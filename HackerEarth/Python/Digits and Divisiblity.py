n = int(input())
nums = list(map(int, input().split()))
k = int(input())

last_digit = -1
for num in nums:
    if num == 0 or num == 5:
        last_digit = num
        break

if last_digit == -1:
    print(-1)
else:
    nums.remove(last_digit)
    nums.sort()

    if k == 1:
        print(last_digit)
    else:
        if nums[0] == 0:
            if k == 1:
                print(0)
            else:
                for i in range(1, len(nums)):
                    if nums[i] != 0:
                        result = [nums[i]] + [0] * (k - 1)
                        result.append(last_digit)
                        print("".join(map(str, result)))
                        break
        else:
            result = nums[:k-1]
            result.append(last_digit)
            print("".join(map(str, result)))
