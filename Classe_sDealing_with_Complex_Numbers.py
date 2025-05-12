import math  # Import the math module for mathematical functions

class Complex(object):  # Define a class named Complex to represent complex numbers
    def __init__(self, real, imaginary):  # Constructor to initialize real and imaginary parts
        self.real = real  # Assign the real part
        self.imaginary = imaginary  # Assign the imaginary part
        
    def __add__(self, no):  # Define addition for complex numbers
        return Complex(self.real + no.real, self.imaginary + no.imaginary)  # Return a new Complex number

    def __sub__(self, no):  # Define subtraction for complex numbers
        return Complex(self.real - no.real, self.imaginary - no.imaginary)  # Return a new Complex number

    def __mul__(self, no):  # Define multiplication for complex numbers
        return Complex(self.real * no.real - self.imaginary * no.imaginary,  # Real part
                       self.real * no.imaginary + self.imaginary * no.real)  # Imaginary part

    def __truediv__(self, no):  # Define division for complex numbers
        denominator = no.real ** 2 + no.imaginary ** 2  # Calculate the denominator
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / denominator,  # Real part
                       (self.imaginary * no.real - self.real * no.imaginary) / denominator)  # Imaginary part

    def mod(self):  # Define a method to calculate the modulus (magnitude) of the complex number
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)  # Return the modulus as a Complex number

    def __str__(self):  # Define a string representation for the complex number
        if self.imaginary == 0:  # If the imaginary part is zero
            result = "%.2f+0.00i" % (self.real)  # Format as "real+0.00i"
        elif self.real == 0:  # If the real part is zero
            if self.imaginary >= 0:  # If the imaginary part is positive
                result = "0.00+%.2fi" % (self.imaginary)  # Format as "0.00+imaginary"
            else:  # If the imaginary part is negative
                result = "0.00-%.2fi" % (abs(self.imaginary))  # Format as "0.00-imaginary"
        elif self.imaginary > 0:  # If the imaginary part is positive
            result = "%.2f+%.2fi" % (self.real, self.imaginary)  # Format as "real+imaginary"
        else:  # If the imaginary part is negative
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))  # Format as "real-imaginary"
        return result  # Return the formatted string

if __name__ == '__main__':  # Check if the script is being run directly
    c = map(float, input().split())  # Read the first complex number (real and imaginary parts)
    d = map(float, input().split())  # Read the second complex number (real and imaginary parts)
    x = Complex(*c)  # Create a Complex object for the first number
    y = Complex(*d)  # Create a Complex object for the second number
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')  # Print the results of operations
    
    # example : input = 1 2
    #                 = 3 4
    #             output = 4.00+6.00i
    #                      -2.00-2.00i
    #                      -5.00+10.00i
    #                      0.44+0.08i
    #                      2.24+0.00i
    #                      5.00+0.00i