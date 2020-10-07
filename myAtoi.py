import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s_array = s.split()
        if s_array:
            s_f = s_array[0]
            if re.match(r'^\+-',s_f):
                return 0
        else:
            return 0 
        
        if re.match(r'\+?(\-?\d+)',s_f):
            s_fu = re.match(r'\+?(\-?\d+)',s_f)
            s_f = s_fu.group(1) 
            if re.match(r'(\+?\-?)0+',s_f):
                if re.match(r'.?0+$',s_f):
                    return 0
                s_fu = re.match(r'(.?)0+(\d+)',s_f)
                s_f = s_fu.group(2)
                if s_fu.group(2):
                    if s_fu.group(1) == '-':
                        s_f = s_fu.group(1) + s_fu.group(2)
                    else:
                        s_f = s_fu.group(2)

            if int(s_f) < -2**31:  
                return -2**31
            elif int(s_f) > 2**31 - 1:
                return 2**31 - 1
            else:
                return(s_f)
        
        else:
            return 0
