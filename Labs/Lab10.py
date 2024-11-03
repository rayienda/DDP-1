# Rayienda Hasmaradana
# Pecahan.py

# Function to calculate the greatest common divisor of two positive integers
def gcd(a, b):
    while b > 0:
        rem = a % b
        a = b
        b = rem
    return a

# Function to calculate the lowest common multiple of two positive integers
def lcm(a, b):
    return (a * b) // gcd(a, b)  # // ensures an int is returned

# Class definition for Pecahan
class Pecahan(object):
    """ Pecahan with numerator numer and denominator denom.
    The denominator parameter defaults to 1"""

    # Constructor to initialize a Pecahan object
    def __init__(self, numer, denom=1):
        self.numer = numer
        self.denom = denom

    # String representation for printing
    def __str__(self):
        if self.denom == 1:
            return str(self.numer)
        else:
            return str(self.numer) + '/' + str(self.denom)

    # Used in interpreter's response
    def __repr__(self):
        return f"Pecahan({self.numer},{self.denom})"

    # Addition method for Pecahan objects
    def __add__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            the_lcm = lcm(self.denom, param.denom)
            numerator_sum = (the_lcm * self.numer // self.denom) + \
                            (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_sum, the_lcm)
        else:
            print('wrong type')  # problem: some type we cannot handle
            raise(TypeError)

    # Subtraction method for Pecahan objects
    def __sub__(self, param):
        if type(param) == Pecahan:
            the_lcm = lcm(self.denom, param.denom)
            numerator_diff = (the_lcm * self.numer // self.denom) - \
                             (the_lcm * param.numer // param.denom)
            return Pecahan(numerator_diff, the_lcm)
        else:
            print('wrong type')
            raise(TypeError)

    # Multiplication method for Pecahan objects
    def __mul__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            return Pecahan(self.numer * param.numer, self.denom * param.denom)
        else:
            print('wrong type')
            raise TypeError

    # Right multiplication method for Pecahan objects
    def __rmul__(self, param):
        return self.__mul__(param)

    # Division method for Pecahan objects
    def __truediv__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            return Pecahan(self.numer * param.denom, self.denom * param.numer)
        else:
            print('wrong type')
            raise(TypeError)

    # Greater than comparison method for Pecahan objects
    def __gt__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            return (self.numer * param.denom) > (param.numer * self.denom)
        else:
            print('wrong type')
            raise(TypeError)

    # Greater than or equal to comparison method for Pecahan objects
    def __ge__(self, param):
        if type(param) == int:
            param = Pecahan(param)
        if type(param) == Pecahan:
            return (self.numer * param.denom) >= (param.numer * self.denom)
        else:
            print('wrong type')
            raise TypeError

    # Get the numerator or denominator based on the index
    def __getitem__(self, index):
        if index == 1:
            return self.numer
        elif index == 2:
            return self.denom
        else:
            raise IndexError("Index must be 1 or 2")

    # Return the reduced Pecahan
    def reduce(self):
        the_gcd = gcd(self.numer, self.denom)
        return Pecahan(self.numer // the_gcd, self.denom // the_gcd)

    # Compare two Pecahans for equality, return Boolean
    def __eq__(self, param):
        reduced_self = self.reduce()
        reduced_param = param.reduce()
        return reduced_self.numer == reduced_param.numer and \
               reduced_self.denom == reduced_param.denom

    # Add two Pecahans, with arguments reversed
    def __radd__(self, param):
        return self.__add__(param)

# Main function to test the Pecahan class
def main():
    p1 = Pecahan(3, 5)
    p2 = Pecahan(1, 20)
    print(Pecahan(8, 1))  # 8
    print(p1 * p2)  # 3/100
    print(p1 / p2)  # 60/5
    print(p1 * 3)  # 9/5
    print(3 * p1)  # 9/5
    print(p1[1])  # 3
    print(p1[2])  # 5
    print(p1 > p2)  # True
    print(p2 > p1)  # False
    print(Pecahan(1, 2) >= Pecahan(3, 6))  # True
    print(Pecahan(50, 101)[2])  # 101
    print(Pecahan(2, 5) > Pecahan(4, 5))  # False
    print(Pecahan(3, 7) >= Pecahan(1, 7) * 3)  # True
    print(Pecahan(3, 7) / 3 == Pecahan(1, 7))  # True
    print(Pecahan(9, 20) * Pecahan(20, 9))  # 180/180
    print((Pecahan(9, 20) * Pecahan(20, 9)).reduce())  # 1
    print(Pecahan(29, 100003).reduce())  # 29/100003
    print(Pecahan(2, 3).__repr__())  # Pecahan(2,3)
    # print(p1[0])  # will generate exception ValueError

if __name__ == '__main__':
    main()