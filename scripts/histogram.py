import pandas as pd
import sys
import matplotlib.pyplot as plt

args = sys.argv[1:]

print(args)

if args[0].startswith('-f'):
    column_id = int(args[0][-1])
    filename = sys.argv[2]
    df = pd.read_csv(filename)
   
else:
    column_id = 1
    filename = sys.argv[1]
    df = pd.read_csv(filename)

# print(df.iloc[:,column_id])
df.iloc[:,column_id].hist()
plt.savefig(filename + '.png')
