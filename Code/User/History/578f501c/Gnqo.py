def digit(a):
    num_list=[]
    for i in range(1,a+1):

        #num_list.append(str(i))
                        
        for j in range(1,i):
            #print(j,end="")
            if len(num_list)==0:
                num_list.append(str(j))
            else:
                num_list[0] = num_list[0] + str(j)
            
    print(num_list)
    return int(num_list[a-1])
digit(10)