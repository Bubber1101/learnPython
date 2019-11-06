import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import tensorflow as tf

if __name__ == '__main__':
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

    dataset = pd.read_csv(url, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
    dataset.head()

    seaborn.pairplot(dataset, hue="species", height=2, diag_kind="hist")
    plt.show()
