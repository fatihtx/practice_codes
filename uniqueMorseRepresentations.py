class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dot_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        list_dot = list()
        for w in words:
            list_e = '' 
            for l in w:
                index_l = letter_list.index(l)
                list_e += dot_list[index_l]
            list_dot.append(list_e)
        return(len(set(list_dot)))
