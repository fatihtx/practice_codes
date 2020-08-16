class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        folder_dict = dict()
        for index,name in enumerate(names):
            if name in folder_dict:
                in_dict = True
                i = folder_dict[name] 
                while in_dict:
                    try_name = name + "(" + str(i) + ")"
                    if try_name in folder_dict:
                        i += 1
                        continue
                    else:
                        names[index] = try_name
                        folder_dict[name] = i
                        folder_dict[try_name] = 1
                        in_dict = False
            else:
                folder_dict[name] = 1
        return names
