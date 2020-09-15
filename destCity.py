class Solution:
    def destCity(self, paths) -> str:
        from_dest = set(list(map(lambda x:x[0],paths)))
        to_dest = set(list(map(lambda x:x[1],paths)))
        dest = list(filter(lambda x: x not in from_dest, to_dest))        
        return dest[0]
