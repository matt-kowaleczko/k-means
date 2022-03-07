from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def elbow_method(x, maxiter):
    """
        Generating elbow plot to identify the best number of clusters for k-means
        Input:
            - Elbow 
    """
    iterations = 10
    wcss = []

    for i in range(1, iterations+1):
        kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = maxiter, random_state = 1)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, iterations+1), wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS') 
    plt.show()

def cluster(x, nclusters, maxiter):
    """Clusters dataframe

    Args:
        x (_type_): dataframe of features
        nclusters (_type_): number of clusters for k-means
        maxiter (_type_): number of iterations for k-means

    Returns:
        _model (k-means model): model object
        _prediction (np array): array of predictions
    """
    _model = KMeans(n_clusters = nclusters, init = 'k-means++', max_iter = maxiter, random_state = 1)
    _prediction = _model.fit_predict(x)
    return _model, _prediction