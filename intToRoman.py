class Solution:
    def intToRoman(self, num: int) -> str:
        dict_rom_to_int = {
            1   :'I',
            5   :'V',
            10  :'X',
            50  :'L',
            100 :'C',
            500 :'D',
            1000:'M',
        }
        out_l = list()
        list_num = list(str(num))
        list_num.reverse()
        for i,v in enumerate(list_num):
            value = int(v) * (10**i)
            if value >= 5 * (10**i):
                if value == 9 * (10**i):
                    ret_v = dict_rom_to_int[1 * (10**i)] + dict_rom_to_int[10 * (10**i)]
                else:    
                    ret_v =  dict_rom_to_int[5 * (10**i)] + ''.join(dict_rom_to_int[1 * (10**i)]*(int(v)-5))
            else:
                if value == 4 * (10**i):
                        ret_v = dict_rom_to_int[1 * (10**i)] + dict_rom_to_int[5 * (10**i)]
                else:    
                    ret_v = ''.join(dict_rom_to_int[1 * (10**i)]*int(v))
            out_l.append(ret_v)
        return ''.join(out_l[::-1]) 
