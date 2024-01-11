import time, random

def binary_search_recusion(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recusion(data, target, low, mid - 1)
        else:
            return binary_search_recusion(data, target, mid + 1, high)
        
def binary_search_unrecusion(data, target, low, high):

    while True:
        mid = int((low +high)/2)

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid +1

        if low == mid or mid == high or low == high:
            return False
        
def normal_search(data, target):
    for i in data:
        if target == i:
            return True
    return False

startTime = time.time()
data = []
for i in range(10000000):
    data.append(random.randint(0, 10000000))
data = sorted(data)
target = 5555222
print(time.time() - startTime)

print("binary search recusion")
startTime = time.time()
print(binary_search_recusion(data, target, 0, len(data)-1))
print(time.time() - startTime)

print("normal search")
startTime = time.time()
print(normal_search(data, target))
print(time.time() - startTime)

print("binary search unrecusion")
startTime = time.time()
print(binary_search_unrecusion(data, target, 0, len(data)-1))
print(time.time() - startTime)