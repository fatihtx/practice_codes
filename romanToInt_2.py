class Solution:
    def romanToInt(self, s: str) -> int:
        dict_rom_to_latin = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        value = 0
        for i in range(len(s)-1):
            if dict_rom_to_latin[s[i]] >= dict_rom_to_latin[s[i+1]]:
                value += dict_rom_to_latin[s[i]]
            else:
                value -= dict_rom_to_latin[s[i]]
        return value + dict_rom_to_latin[s[-1]]
