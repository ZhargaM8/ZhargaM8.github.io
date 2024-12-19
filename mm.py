def largest_monotonically_decreasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # setiap elemen bisa menjadi subsequence dari panjang 1
    
    # Iterasi untuk mengisi dp
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:  # pastikan elemen sebelumnya lebih besar
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Panjang maksimum dari subsequence menurun
    lmds_length = max(dp)
    
    # Rekonstruksi subsequence dari dp
    lmds = []
    max_length = lmds_length
    for i in range(n-1, -1, -1):
        if dp[i] == max_length:
            lmds.append(arr[i])
            max_length -= 1
    
    lmds.reverse()  # urutan asli harus diurutkan mundur
    return lmds, lmds_length

# Contoh data
arr = [7, 13, 2, 5, 4, 15, 6, 8, 1, 9, 0]
subsequence, length = largest_monotonically_decreasing_subsequence(arr)
print(f"Largest Monotonically Decreasing Subsequence: {subsequence}")
print(f"Panjang: {length}")
