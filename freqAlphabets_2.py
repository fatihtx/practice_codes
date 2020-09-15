class Solution:
    def freqAlphabets(self, s: str) -> str:
        decode_list = {
            "1"  :"a",
            "2"  :"b",
            "3"  :"c",
            "4"  :"d",
            "5"  :"e",
            "6"  :"f",
            "7"  :"g",
            "8"  :"h",
            "9"  :"i",
            "10#":"j",
            "11#":"k",
            "12#":"l",
            "13#":"m",
            "14#":"n",
            "15#":"o",
            "16#":"p",
            "17#":"q",
            "18#":"r",
            "19#":"s",
            "20#":"t",
            "21#":"u",
            "22#":"v",
            "23#":"w",
            "24#":"x",
            "25#":"y",
            "26#":"z",
        }
        count = 0
        temp = ''
        out = ''
        for i in s[::-1]:
            if i == "#":
                temp  = i
                count = 2
                continue
                
            if count == 0:
                if "#" in temp:
                    if decode_list[temp[::-1]]:
                        out += decode_list[temp[::-1]]
                        temp = ''
                else:
                    if decode_list[i]:
                        out += decode_list[i]
            else:
                temp  += i
                count -= 1
                if count == 0:
                    if "#" in temp:
                        if decode_list[temp[::-1]]:
                            out += decode_list[temp[::-1]]
                            temp = ''
                
        return out[::-1] 
