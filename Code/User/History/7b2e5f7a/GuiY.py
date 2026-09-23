def spreading():
    height,width = input("enter height and width").split()

    house_tob_painted= int(input(""))
    
    for i in range(int(height)):
        for j in range(int(width)):
            print("X", end="")
        print()

if __name__ == '__main__':
    spreading()