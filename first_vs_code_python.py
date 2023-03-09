import pandas as pd

my_dataset={'cars':["BMW","Volvo","Ford"],'passings':[3,7,1]}
my_var=pd.DataFrame(my_dataset)

squares = [2**n for n in range(8)]

print(squares)
print(sum(squares))

print(my_var)