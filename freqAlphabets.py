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
        out = ''
        currentindex = len(s)-1
        add_list = list()
        while currentindex > -1:
            if s[currentindex] == "#":
                add_list.append(s[currentindex-2]+s[currentindex-1]+s[currentindex])
                currentindex -= 3
            else:
                add_list.append(s[currentindex])
                currentindex -= 1
        
        for i in add_list[::-1]:
            out += decode_list[i]
        
        return out
