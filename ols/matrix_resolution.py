import pandas as pd
import numpy as np


# This will be the Matrix Resolution of Ordinary Least Squares
# A = (X'X)^-1 * X'Y
# Y = X * B + e
# e = Y(hat) - X * B

e = './ols/e_matrix1.csv'
df_main = pd.read_csv(e, header=0)

matrix_y = df_main['Y1'].to_numpy()
print(matrix_y)

