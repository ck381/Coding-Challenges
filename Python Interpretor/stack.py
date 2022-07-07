# Import necessary libraries
import math

# This class contains all functionality for the Fifth interpretor
class fifth_interpretor:

    # Class constructor
    def __init__(self):
        self.stack = [] # This is the stack initialised as an empty list


    # Push x onto the top of the stack, where x is a valid integer
    def push(self,x):
        self.stack.append(x)


    # Remove the top element of the stack
    def pop(self):
        if len(self.stack) != 0: # The list must not be empty otherwise an IndexError will be thrown
            self.stack.pop()
        else:
            print('ERROR')

    # Swap the top two elements of the stack
    def swap(self):
        if len(self.stack) >= 2:
            self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]
        else:
            print('ERROR')

    # Duplicate the top element of the stack
    def dup(self):
        if len(self.stack) >= 1:
            self.stack.append(self.stack[-1])
        else:
            print('ERROR')


    # Performs addition to the two values on the top of the stack and pushes the result to the top of the stack
    def addition(self):
        if len(self.stack) >= 2:
            addition_result = self.stack[-2] + self.stack[-1] # Calculate addition value
            self.pop()
            self.pop()
            self.push(addition_result) # Push value to top of stack
        else:
            print('ERROR')

    # Performs subtraction to the two values on the top of the stack and pushes the result to the top of the stack
    def subtraction(self):
        if len(self.stack) >= 2:
            subtraction_result = self.stack[-2] - self.stack[-1]  # Calculate subtracted value
            self.pop()
            self.pop()
            self.push(subtraction_result)
        else:
            print('ERROR')

    # Performs division to the two values on the top of the stack and pushes the result to the top of the stack
    def divide(self):
        if len(self.stack) >= 2:
            division_result = self.stack[-2] / self.stack[-1]  # Calculate division value
            # Check whether the result is a non integer and if it is round down
            if not isinstance(division_result,int):
                division_result = math.floor(division_result)
            self.pop()
            self.pop()
            self.push(division_result)
        else:
            print('ERROR')

    # Performs multiplication to the two values on the top of the stack and pushes the result to the top of the stack
    def multiply(self):
        if len(self.stack) >= 2:
            multiplication_result = self.stack[-2] * self.stack[-1]  # Calculate multiplication value
            self.pop()
            self.pop()
            self.push(multiplication_result)
        else:
            print('ERROR')



# Main function
def main():
    interpretor = fifth_interpretor() # Initialise an interpretor object
    while True:
        command = input('Enter a command: ')
        command = command.upper()
        if 'PUSH' in command:
            value = [char for char in command if char.isdigit()] # Get an array of all digits in the command
            value = ''.join(value) # Convert array of digits to string
            try:
                value = int(value)
                interpretor.push(value)
            except:
                # Value error from trying to push a non integer value to the stack
                print('ERROR')

        if 'POP' in command:
            interpretor.pop()

        if 'SWAP' in command:
            interpretor.swap()

        if 'DUP' in command:
            interpretor.dup()

        if '+' in command:
            interpretor.addition()

        if '-' in command:
            interpretor.subtraction()

        if '*' in command:
            interpretor.multiply()

        if '/' in command:
            interpretor.divide()

        # Display updated stack
        print('stack is ' + str(interpretor.stack))


main()






