import math

class Points(object):
    # crate constructor (__init__) with 3 arguments
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # create a method __sub__ that returns the subtraction of 2 points and gets a vector from one point to another.
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    # create a method dot that returns the addition dot product of 2 points
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
        
    # create a method cross that returns the sum cross product of 2 points and a vector that is perpendicular to both executed vectors.
    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)
    
    # create a method absolute that returns the length of a vector using the Pythagorean formula
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    
    # calculated as the cross product of the vectors leading from a to b and from b to c.
    x = (b - a).cross(c - b)
    # calculated as the cross product of the vectors leading from b to c and from c to d.
    y = (c - b).cross(d - c)
    
    # The angle between two vectors x and y is calculated using the cosine formula to return the angle in radians.
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
    
# example : input = 1 0 0
#                   0 1 0
#                   0 0 1
#                   1 1 1
# output = 70.53 
#  note : x = (b - a) x (c - b) = (0-1, 1-0, 0-0) x (0-0, 0-1, 1-0) = (-1, 1, 0) x (0, -1, 1) = (1, 1, 1)
#         y = (c - b) x (d - c) = (0-0, 0-1, 1-0) x (1-0, 1-0, 1-1) = (0, -1, 1) x (1, 1, 0) = (-1, 1, 1)

# vektor x
# Cara Menghitung Cross Product:

# Komponen ( x ):

# Hitung dengan rumus: [ x = (1 \cdot 1) - (0 \cdot -1) = 1 ]
# Komponen ( y ):

# Hitung dengan rumus: [ y = -((-1 \cdot 1) - (0 \cdot 0)) = 1 ]
# Komponen ( z ):

# Hitung dengan rumus: [ z = (-1 \cdot -1) - (1 \cdot 0) = 1 ]
# Jadi, kita mendapatkan: [ x = (1, 1, 1) ]

#vektor y
# Cara Menghitung Cross Product:

# Komponen ( x ):

# Hitung dengan rumus: [ x = (-1 \cdot 0) - (1 \cdot 1) = -1 ]
# Komponen ( y ):

# Hitung dengan rumus: [ y = -((0 \cdot 0) - (1 \cdot 1)) = 1 ]
# Komponen ( z ):

# Hitung dengan rumus: [ z = (0 \cdot 1) - (-1 \cdot 1) = 1 ]
# Jadi, kita mendapatkan: [ y = (-1, 1, 1) ]

# Menghitung Dot Product
# Dot product dari dua vektor ( x ) dan ( y ) dihitung dengan rumus:

# [ x \cdot y = x_1 \cdot y_1 + x_2 \cdot y_2 + x_3 \cdot y_3 ]

# Substitusi nilai vektor:

# [ x \cdot y = (1 \cdot -1) + (1 \cdot 1) + (1 \cdot 1) = -1 + 1 + 1 = 1 ]

# Menghitung Panjang (Magnitude) dari Vektor
# Panjang Vektor ( x ): [ |x| = \sqrt{x_1^2 + x_2^2 + x_3^2} = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3} ]

# Panjang Vektor ( y ): [ |y| = \sqrt{y_1^2 + y_2^2 + y_3^2} = \sqrt{(-1)^2 + 1^2 + 1^2} = \sqrt{1 + 1 + 1} = \sqrt{3} ]

# Menghitung Sudut
# Sudut ( \theta ) antara dua vektor dapat dihitung menggunakan rumus:

# [ \cos(\theta) = \frac{x \cdot y}{|x| \cdot |y|} ]

# Substitusi nilai yang telah kita hitung:

# [ \cos(\theta) = \frac{1}{\sqrt{3} \cdot \sqrt{3}} = \frac{1}{3} ]

# Kemudian, kita ambil invers cosinus untuk mendapatkan sudut dalam radian:

# [ \theta = \cos^{-1}\left(\frac{1}{3}\right) ]

# Mengonversi ke Derajat
# Setelah mendapatkan sudut dalam radian, kita perlu mengonversinya ke derajat:

# [ \text{angle in degrees} = \theta \times \left(\frac{180}{\pi}\right) ]

# Jika kita menghitung nilai tersebut, kita akan mendapatkan:

# [ \theta \approx 70.53 \text{ derajat} ]