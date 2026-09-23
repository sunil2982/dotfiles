def spreading():
    # height and width of neaighbour hood
    height,width = input("enter height and width :").split()

    # house to be painted gray
    house_tob_painted= int(input(" house ot be pained : "))
    no_of_gray_house =int(input("gray painted house : "))
    gray_house_list=[]
    for i in range(no_of_gray_house):
        (h_row,h_col)= input("location of house to be painted: ").split()
        gray_house_list.append((int(h_row),int(h_col)))
    print(gray_house_list)
    for i in range(int(height)):
        for j in range(int(width)):
            print("X", end="")
        print()

if __name__ == '__main__':
    spreading()