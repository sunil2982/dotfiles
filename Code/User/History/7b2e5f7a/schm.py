def spreading():
    height,width = input("enter height and width").split
    for i in range(height):
        for j in range(width):
            print("O")
        print("O")

if __name__ == '__main__':
    spreading()