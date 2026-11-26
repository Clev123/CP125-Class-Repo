# Lab 01 Exercise 5: Triangle Checker
def is_valid_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

valid_triangle1 = is_valid_triangle(3,4,5)
print(valid_triangle1)

valid_triangle2 = is_valid_triangle(1,2,3)
print(valid_triangle2)