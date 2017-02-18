import os
os.system('clear')

print("\n\nCALCULATE OVERLAPPING AREA BETWEEN TWO RECTANGLES")
print("\nEnter two co-ordinates for each rectangle, with x and y separated by a comma.")
print("For example:  1,1 5,5\n")
A_in = input("Enter first rectangle co-ordinates: ") 
B_in = input("Enter second rectangle co-ordinates: ")

A = []
B = []

for point in A_in.split():
  A.append([float(i) for i in point.split(",")])

for point in B_in.split():
  B.append([float(i) for i in point.split(",")])

def overlaps(A, B):

# Basic idea and insight is that the overlapping area will be the product of
# the overlaps on the x and y axes.
# This means there are no special cases to evaluate.
# And it's easy to work out the overlaps on each of the single axes.

# To get the overlaps on one axis we will want to compare the total span
# of the rectangles combined, vs the sum of their lengths on that axis.

# So to start we find the lengths of each side of each rectangle.

  x_lenA = A[1][0] - A[0][0]
  x_lenB = B[1][0] - B[0][0]
  y_lenA = A[1][1] - A[0][1]
  y_lenB = B[1][1] - B[0][1]

# Then we can calculate the total span on each axis  
  x_span = max(A[1][0], B[1][0]) - min(A[0][0], B[0][0])
  y_span = max(A[1][1], B[1][1]) - min(A[0][1], B[0][1])

# The overlap on each axis is the difference between the sum of separate
# lengths and the spanned length
  x_overlap = x_lenA + x_lenB - x_span
  y_overlap = y_lenA + y_lenB - y_span

# Finally return the product, as long as there is some overlap
  if (x_overlap > 0) and (y_overlap > 0):
    return x_overlap * y_overlap
  else:
    return 0
    
try:
    print("\nYour overlap is ", overlaps(A,B),"\n")
except:
    print("\nI can't tell you an area because you can't have typed the inputs properly.  I think it's time you started taking this a bit more seriously\n\n\n")
