class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        out_list = list()
        for i,v1 in enumerate(prices):
            mid_list = prices[i+1::]
            for v2 in mid_list:
                if v1>=v2:
                    out_list.append(v1-v2)
                    break
            if not out_list or len(out_list)-1 != i:
                out_list.append(v1)
        return out_list
