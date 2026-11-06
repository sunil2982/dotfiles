class Calculator:

    def add(self,num1,num2):
        return num1 + num2 
    
    def sub(self,num1,num2):
        return num1-num2

    def multi(self,num1,num2):
        return num1 * num2
    
    def division(self,num1,num2):
        return num1/num2


obj =Calculator()

print(obj.add(3,7))