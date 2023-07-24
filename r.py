import numpy as np
class Multi_Dimensional_array:
    def __init__(self,*dimensions):
        self.O_dimension = dimensions
        multi =1
        for i in dimensions:
            multi*=i
        self.arr = np.zeros(multi,dtype=int)

    def Insert(self,value,D_dimension):
        sum = 0

        for i in range(len(self.O_dimension)):
            multi=1
            for j in range(i+1,len(D_dimension)):
                multi*=self.O_dimension[j]
            sum += multi * D_dimension[i]
        self.arr[sum] = value 
        print(self.arr)

    def Get_value(self,*dimen):
        sum=0
        for i in range(len(self.O_dimension)):
            multi=1
            for j in range(i+1,len(dimen)):
                multi*=self.O_dimension[j]
            sum += multi * dimen[i]
        print(self.arr[sum])
         



M = Multi_Dimensional_array(4,4,8)
M.Insert(34543,[3,1,7])
M.Get_value(3,1,7)

