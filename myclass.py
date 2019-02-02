class Point:
 a = 5
 b = 9

 def print_xy(self):
  print("a = ", self.a)
  print("b = ", self.b)

 if __name__ == "__main__":
  p = Point() # create the object
 p.print_xy()
 print(p.a, p.b)
