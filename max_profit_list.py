class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        max_element_index,min_element, max_diff = self.find_max_diff(prices)
        #print (prices)
        #print ("min_element " + str(min_element))
        if max_diff == 0:
            return 0
        min_index = prices.index(min_element)
        max_index = max_element_index
        #print ("min_index "+ str(min_index))
        #print ("max_index "+ str(max_index))
        
        first_portion_array = None
        if min_index >= 2:
            first_portion_array = prices[:min_index]
        third_portion_array = None
        if len(prices) - max_index >= 2:
            third_portion_array = prices[max_index+1:]
        inverse_of_second = None
        if max_index - min_index >= 2:
            inverse_of_second = prices[max_index-1:min_index:-1]
        #print (first_portion_array)
        #print (third_portion_array)
        #print (inverse_of_second)
        
        max_diff_last = list()
        max_diff_last.append(max_diff)
                
        max_diff_first = ""
        if first_portion_array and len(first_portion_array) >= 2:
            max_element_index,min_element, max_diff_first = self.find_max_diff(first_portion_array)
            #print (max_diff_first)
            max_diff1 = int(max_diff) + int(max_diff_first)
            max_diff_last.append(max_diff1)
        
        max_diff_third = ""
        if third_portion_array and len(third_portion_array) >= 2:
            max_element_index,min_element, max_diff_third = self.find_max_diff(third_portion_array)
            #print (max_diff_third)
            max_diff3 = int(max_diff) + int(max_diff_third)
            max_diff_last.append(max_diff3)
        
        max_diff_second = ""
        if inverse_of_second and len(inverse_of_second) >= 2:
            max_element_index,min_element, max_diff_second = self.find_max_diff(inverse_of_second)
            #print (max_diff_first)
            max_diff2 = int(max_diff) + int(max_diff_second) 
            max_diff_last.append(max_diff2)
        
        return  max(max_diff_last)
    
    def find_max_diff(self, prices):
        max_element_index = 0
        element = prices[0]
        min_element = prices[0]
        max_diff = prices[1] - prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] - min_element >= max_diff:
                max_diff = prices[i] - min_element
                element = min_element
                max_element_index = i
            if prices[i] < min_element:
                min_element = prices[i]
        
        if max_diff <= 0:
            return 0,element,0
        return max_element_index,element,max_diff

'''
    def maxProfit(self, prices):
        value_list = []
        index_list = []
        value2_list = []
        index2_list = []
        for i in range(1,len(prices)):
            for index in range(0,len(prices)-i):
                if 0 < prices[index+i]-prices[index]:
                    value_list.append(prices[index+i]-prices[index])
                    index_list.append([index,index+i])
        #print (value_list)
        #print (index_list)
        print (len(index_list))
        new_value_list = list(filter(lambda x: x > 0, value_list))
        if new_value_list:
            for index,transaction1 in enumerate(index_list):
                for index2 in range(index+1,len(index_list)):
                    transaction2 = index_list[index2]
                    if not ( transaction2[0]<=transaction1[1] and transaction1[0]<=transaction2[1] ):
                        value2_list.append(value_list[index]+value_list[index2])
                        index2_list.append([index_list[index]+index_list[index2]])
        new_value2_list = list(filter(lambda x: x > 0, value2_list))
        if new_value_list+new_value2_list:
            value_max = max(new_value_list+new_value2_list)
        else:
            value_max = 0
        #index_max = value2_list.index(value_max)
        #transaction_times = index2_list[index_max]
        #print (value2_list)
        #print (index2_list)
        #print (value_max)
        #print (index_max)
        #print (transaction_times)
        return value_max
'''
