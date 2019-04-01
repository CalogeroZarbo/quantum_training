import numpy as np
from sklearn.datasets import load_breast_cancer
import os

wisc = load_breast_cancer()

idx = np.arange(len(wisc.target))
np.random.shuffle(idx)

# train on a random 2/3 and test on the remaining 1/3
idx_train = idx[:2*len(idx)//3]
idx_test = idx[2*len(idx)//3:]

X_train = wisc.data[idx_train]
X_test = wisc.data[idx_test]

y_train_binary= wisc.target[idx_train]  
y_test_binary = wisc.target[idx_test]

if not os.path.exists('./data/'):
    os.makedirs('./data/')

train_ds_binary = open('./data/train_wisc_binary.csv', 'w')
for i,line in enumerate(X_train):
    lbl_bin = [str(y_train_binary[i])]
    line = [str(x) for x in line]

    line_out_bin = lbl_bin
    line_out_bin.extend(line)
    train_ds_binary.write(','.join(line_out_bin)+'\n')
train_ds_binary.close()

test_ds_binary = open('./data/test_wisc_binary.csv', 'w')
for i,line in enumerate(X_test):
    lbl_bin = [str(y_test_binary[i])]
    line = [str(x) for x in line]

    line_out_bin = lbl_bin
    line_out_bin.extend(line)
    test_ds_binary.write(','.join(line_out_bin)+'\n')
test_ds_binary.close()
