# Servier

## Predict basic properties of a molecule

Flask API predicting P1 for any given smile

### Preprocessing
training input: csv file containing P1, model_id, smiles
predict input: any smile as string
output: predicted P1 for the provided smile

### Requirements
bash commands to run before launching application
conda init
conda activate servier
conda install -c conda-forge rdkit
pip install pandas
pip install scikit-learn
pip install numpy
python setup.py install

### Application
#### Data preprocessing
Extract features from smiles
Transform extracted features to array
Create a dummy variable for each feature
Data is highly unbalanced (20/80): Oversampling of the minority class

### Train / Prediction model
##### train/test split
Split the dataset into train (70%) and test (30%) datasets (Given the number of observations we won't split into train/test/validation

#### model
After investigation we found that the Support Vector Model was best permorfer for our case.
We tested Logistic regression, K Nearest neighbors, Gaussian Binomial, and Random Forest.

##### train task
Train the model using the fit function SVC().fit() scikit-learn function

##### evaluate task
Model performance was evaluated using accuracy, specificity and sensitivity.
Assuming that the business don't want to launch extensive studies on molecules that could fail on clinical phases we selected the model that minimised type-II errors (non-rejection of false).

#### room for improvement
With more time we could perform a grid search for each model to find the best hyperparameters and run a Principal Component Analysis or a Recursive Feature Elimination algorithm to reduce the number of features and minimise the noise.

##### predict
Please speicify the smile you want to analyze when running the application.
e.g predict 'Cc1cccc(N2CCN(C(=O)C34CC5CC(CC(C5)C3)C4)CC2)c1C'
or bin/predict.py 'Cc1cccc(N2CCN(C(=O)C34CC5CC(CC(C5)C3)C4)CC2)c1C'


##### setup.py
We created a setup.py file to install the application.
Entry points allow to predict the output for any given smile using the application.
First run 'train-evaluate dataset_single.csv' to train and evaluate your model
Once you trained your model you can run prediction using 'predict your-smile'


### Flask API
We failed to set up a flask API for the application.
Using the flask run command leads to a rdkit module not found error while the package is well installed.
To be investigated.

### Docker
We created the dockerfile that allowed us to build the docker image.
However, when we tried to run the docker image we faced an package import error.
The mentioned is well installed.
To be investigated.





