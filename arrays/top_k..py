def top_k(nums,k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    topk = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    return [num for num, count in topk[:k]]      
    


print(top_k([1,1,1,2,2,3], 2))