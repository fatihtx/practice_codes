class Solution:
    def romanToInt(self, s: str) -> int:
        dict_rom_to_latin = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        
        list_s = list(s)
        new_list = list()
        for i,v in enumerate(list_s):
            if i>0:
                if dict_rom_to_latin[list_s[i]] > dict_rom_to_latin[list_s[i-1]]:
                    next
                else:
                    if i != len(list_s)-1 and dict_rom_to_latin[list_s[i]] < dict_rom_to_latin[list_s[i+1]]:
                        v = list_s[i] + list_s[i+1]
                    else:
                        v = list_s[i]
                    new_list.append(v)
            else:
                if i != len(list_s)-1 and dict_rom_to_latin[list_s[i]] < dict_rom_to_latin[list_s[i+1]]:
                    v = list_s[i] + list_s[i+1]
                else:
                    v = list_s[i]
                new_list.append(v)
        
        value = 0

        for i in new_list:
            if i in dict_rom_to_latin:
                value += dict_rom_to_latin[i]
                
        return value
