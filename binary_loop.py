import pandas as pd

my_dataset={'cars':["BMW","Volvo","Ford"],'passings':[3,7,1]}
my_var=pd.DataFrame(my_dataset)

squares = [2**n for n in range(8)]

print()
print(f'2^(0,1,2,3,4,5,6,7,8): { squares }')
print()
print("Sum of Squares")
print(sum(squares))
print()
print(my_var)
