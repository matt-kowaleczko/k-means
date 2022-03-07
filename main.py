from preprocessing import get_iris_data
from kmeans import cluster
import numpy as np
import os

def main():
    """The function pulls data from sklearn Iris set and clusters it. The output is then being saved in the Output folder
    """
    X, y, df, data = get_iris_data()
    model, predictions = cluster(X, 3, 300)

    path = os.path.join('output','output.csv')
    np.savetxt(path, predictions, delimiter=",")

if __name__ == "__main__":
    main()
