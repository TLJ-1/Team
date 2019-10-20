import numpy as np


def generate(sample_size, num_classes, diff, regression=False):
    np.random.seed(10)
    mean = np.random.randn(2)
    cov = np.eye(2)

    # len(diff)
    samples_per_class = int(sample_size / num_classes)

    X0 = np.random.multivariate_normal(mean, cov, samples_per_class)
    Y0 = np.zeros(samples_per_class)

    for ci, d in enumerate(diff):
        X1 = np.random.multivariate_normal(mean + d, cov, samples_per_class)
        Y1 = (ci + 1) * np.ones(samples_per_class)

        X0 = np.concatenate((X0, X1))
        Y0 = np.concatenate((Y0, Y1))
        # print(X0, Y0)

    if regression == False:  # one-hot  0 into the vector "1 0
        Y0 = np.reshape(Y0, [-1, 1])
        # print(Y0.astype(np.int32))
        Y0 = onehot(Y0.astype(np.int32), 0, num_classes)
        # print(Y0)
    X, Y = shuffle(X0, Y0)
    # print(X, Y)
    return X, Y


np.random.seed(10)
input_dim=2   #[[0] [1]]
num_classes=4   #[0 1][1 0][1 1][0 0]
X,Y=generate(320,num_classes,[[3.0,0],[3.0,3.0],[0,3.0]],regression=True)
Y=Y%2   #为什么要取余运算？


xr=[]
xb=[]
for (l,k) in zip(Y[:],X[:]):
    if l==0.0:
        xr.append(k[0],k[l])
    else:
        xb.append(k[0],k[l])

xr=np.array(xr)
xb=np.array(xb)
plt.scatter(xr[:,0],xr[:,1],c='r',marker='+')
plt.scatter(xb[:,0],xb[:,1],c='b',marker='o')
plt.show()

