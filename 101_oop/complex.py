class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return 'Complex({!r}, {!r})'.format(self.real, self.imaginary)

    def __str__(self):
        return '{}{:+d}i'.format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** .5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

def main():
    c1 = Complex(2, 5)
    c2 = Complex(2, 5)
    c3 = Complex(3, 7)

    print('Dev print ' + repr(c1))
    print('User print {}'.format(c1))
    print('Sum: {}'.format(Complex(2, 3) + Complex(3, 5)))
    print('Neg {}'.format(c1.__neg__()))
    print('Sub: {}'.format(Complex(2, 3) - Complex(3, 5)))

    print('Abs: {}'.format(abs(c1)))

    print('Eq vs ne: {}'.format(c1 == c2 != c3))

if __name__ == "__main__":
    main()
