def spreading():
    # height and width of neaighbour hood
    height,width = input("enter height and width :").split()

    # house to be painted gray
    house_tob_painted= int(input(" : "))
    no_of_gray_house =int(input(" : "))
    gray_house_list=[]
    for i in range(no_of_gray_house):
        (h_row,h_col)= input().split()
        gray_house_list.append((h_row,h_col))
    print(gray_house_list)
    for i in range(int(height)):
        for j in range(int(width)):
            print("X", end="")
        print()

if __name__ == '__main__':
    spreading()