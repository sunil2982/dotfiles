def spreading():
    height,width = input("enter height and width").split()
    for i in range(int(height)):
        for j in range(int(width)):
            print("X", end="")
        print("O")

if __name__ == '__main__':
    spreading()