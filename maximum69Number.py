class Solution:
    def maximum69Number (self, num: int) -> int:
        list_num = [n for n in str(num)]
        try:
            index_6 = list_num.index('6')
        except:
            index_6 = None
        if index_6 is not None:
            list_num[index_6] = '9'
        return int(''.join(list_num))


class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = num.replace("6","9",1)
        
        return int(num)
