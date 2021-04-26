class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if not isinstance(self, Vector3D) and isinstance(other, Vector3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, other):
        return Vector3D(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __xor__(self, other):
        return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError

        return Vector3D(self.x / other, self.y / other, self.z / other)

    def norm(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


if __name__ == "__main__":
    vector1 = Vector3D(2, 4, 8)
    vector2 = Vector3D(3, 6, 9)

    print(vector1)
    print(vector2)

    print(vector1 + vector2)

    vector3 = Vector3D(20, 40, 80)
    vector3 += vector1
    print(vector3)

    # __neg__
    print(-vector1)

    vector4 = Vector3D(2, 4, 8)

    print(vector1 == vector4)

    print(vector3 * 2)
    print(2 * vector3)

    print(vector3 ^ vector2)

    print(vector3 / 2)

    print(vector3.norm())
