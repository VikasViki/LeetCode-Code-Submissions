class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        arr_len = len(arr)
        good_triplets_count = 0
        for i in range(arr_len):
            for j in range(i+1, arr_len):
                if abs(arr[i]-arr[j]) > a: continue
                for k in range(j+1, arr_len):
                    if abs(arr[j]-arr[k]) > b: continue
                    if abs(arr[i]-arr[k]) <= c:
                        good_triplets_count += 1
        return good_triplets_count
