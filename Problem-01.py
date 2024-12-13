#Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

#declare a class called calculator.
class Calculator:
  #initialize the class with the constructor __init__ which first runs as soon as object is created following attributes.
  def __init__(self, a, b, operation):
    self.a = a
    self.b = b
    self.operation = operation
    
  def calculate(self):            #define a function called calculate implementing the methods in the constructor.
      if self.operation == 'add':  #if the operation is addition, return the sum of a and b.
        return self.a + self.b
      elif self.operation == 'sub': #if the operation is subtraction, return the difference of a and b.
        return self.a - self.b
      elif self.operation == 'mul': #if the operation is multiplication, return the product of a and b.
        return self.a * self.b
      elif self.operation == 'div': #if the operation is division, return the quotient of a and b.
         if self.b != 0:
            return self.a / self.b
         else:
            return "You are trying to divide by zero! Please enter a valid number!" #if the user tries to divide by zero, return this message.
      else:
        return 'Sorry not a valid operation! :( Try again! i\'ll give u another chance ;)' #if the operation is not valid, return this message.

a = float(input("Enter a number : ")) #since in python float and double ranges same
b = float(input("Enter another number : "))
operation = input("What would you like to perform? select one among them : Addition, Subtraction, Multiplication, Division (kindly type in words ur choice): ").lower() #take the operation as input from the user.
calc = Calculator(a, b, operation) #create an object of the class calculator.
print(calc.calculate()) #print the result of the operation.