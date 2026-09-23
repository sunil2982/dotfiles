def digit(a):
    num_list=[0]
    for i in range(1,a+1):

        #num_list.append(str(i))
                        
        for j in range(1,i):
            num_list[0] = num_list[0] +str(j)
            
    print(num_list)

digit(10)