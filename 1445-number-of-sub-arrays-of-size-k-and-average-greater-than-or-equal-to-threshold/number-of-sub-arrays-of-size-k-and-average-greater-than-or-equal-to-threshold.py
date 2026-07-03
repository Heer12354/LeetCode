class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int):
        s = 0
        i = 0

        while i < k:
            s += arr[i]
            i += 1

        ans = 0
        if s >= k * threshold:
            ans += 1

        i = k
        while i < len(arr):
            s = s + arr[i] - arr[i - k]

            if s >= k * threshold:
                ans += 1

            i += 1

        return ans