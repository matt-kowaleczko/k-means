import pandas as pd
from sklearn.datasets import load_iris

def get_iris_data():
    """
        Getting and preparing Iris data from sklearn.datasets repository

        Returns:
            _X (dataframe): features dataframe
            _y (dataframe): labels dataframe
            _df (dataframe): combined features and labels dataframe
            _data (dictionary): output of load_iris function from sklearn
    """        
    _data = load_iris()
    _X = pd.DataFrame(_data.data)
    _y = pd.DataFrame(_data.target)
    _y = _y.apply(lambda x: _data.target_names[x])

    _df = pd.concat([_X, _y], axis=1)
    labels = _data.feature_names + ['species']
    _df.columns = labels
    return _X, _y, _df, _data

def box_plots(data):
    """
        Creating boxplots for each feature
    """
    for f in data.feature_names:
        sns.boxplot(x="species",y=f,data=df)
        plt.show()