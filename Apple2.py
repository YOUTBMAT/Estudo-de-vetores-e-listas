nums = [4,4,4,4,5,5,5,5,5,6,6,6,6,6,5,5]

tempNum = 0
maiorCount = 0
numsRep = []

for digit in nums:
    if digit not in numsRep:
        numsRep.append(digit)
        tempNum = nums.count(digit)
        if tempNum > maiorCount:
            maiorCount = tempNum

print(maiorCount)