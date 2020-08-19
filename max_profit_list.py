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
