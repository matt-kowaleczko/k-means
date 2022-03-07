# K-means clusters

## Summary
The repository includes a Jupyter notebook `iris_k_means.ipynb` used for experimentation and "productionised" code in `main.py` file. The algorithm uses Sklearn package and each function is well documented in both notebook and in Python files.

## Installing dependancies
All dependancies are listed in requirements.txt file. Python 3.9.1 was used for this task. To install dependancies, run `pip install -r requirements.txt`

## Running the script
The script can be ran from Jupyter notebooks by opening `iris_k_means.ipynb` or by running `main.py` from command line.

## Suggested improvements
The "productionised" code uses *number of clusters* parameters from elbow analysis done in the notebook. There are numerous other paramameters we could optimise, like *number of iterations* or *n_init*. The number of clusters could also be selected by a less arbitrary method.

Frome the coding standpoing the parameters could be passed by from command line instead of being hard coded in `main.py`

Output of the code is 
