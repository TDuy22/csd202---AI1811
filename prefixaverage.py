import time

def prefix_average(S):
    n = len(S)
    A = [0] * n
    for j in range (n):
        total =0
        for i in range(j+1):
            total += S[i]
        A[j] = total / (j+1)
    return A
start_time = time.time()
prefix_average(range(20000))
print("--- %s seconds ---" % (time.time() - start_time))