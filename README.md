# MAGIC-Gamma-Telescope-Classification
Classification of Gamma and Hadron events by training classifieres and machine learning algorithms on the MAGIC Gamma Telescope dataset.


## Table of Contents
- [MAGIC-Gamma-Telescope-Classification](#magic-gamma-telescope-classification)
  * [Data Set](#data-set)
    + [Attribute Information](#attribute-information)
  * [Data Preprocessing](#data-preprocessing)
    + [Data Balancing](#data-balancing)
    + [Data Splitting](#data-splitting)
  * [Classification Algorithms](#classification-algorithms)
    + [Decision Tree Classifier](#decision-tree-classifier)
    + [AdaBoost Classifier](#adaboost-classifier)
    + [K-Nearest Neighbors Classifier (KNN)](#k-nearest-neighbors-classifier--knn-)
    + [Random Forest Classifier](#random-forest-classifier)
    + [Naive Bayes Classifier](#naive-bayes-classifier)
    + [Neural Network](#neural-network)
  * [Classifiers Comparison](#classifiers-comparison)
  * [Remarks](#remarks)
  * [Contributers](#contributers)

## Data Set
The [MAGIC gamme telescope dataset](https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope) is generated to simulate registration of high energy gamma particles in a ground-based atmospheric Cherenkov gamma telescope using the imaging technique. The dataset consists of two classes; gammas (signal) and hadrons (background). There are 12332 gamma events and 6688 hadron events.

### Attribute Information
The dataset consists of 10 continuous features and 1 binary class label. The features are listed below:

1. fLength: continuous # major axis of ellipse [mm]
2. fWidth: continuous # minor axis of ellipse [mm]
3. fSize: continuous # 10-log of sum of content of all pixels [in #phot]
4. fConc: continuous # ratio of sum of two highest pixels over fSize [ratio]
5. fConc1: continuous # ratio of highest pixel over fSize [ratio]
6. fAsym: continuous # distance from highest pixel to center, projected onto major axis [mm]
7. fM3Long: continuous # 3rd root of third moment along major axis [mm]
8. fM3Trans: continuous # 3rd root of third moment along minor axis [mm]
9. fAlpha: continuous # angle of major axis with vector to origin [deg]
10. fDist: continuous # distance from origin to center of ellipse [mm]
11. class: g,h # gamma (signal), hadron (background)

## Data Preprocessing
The dataset isn't ready to be used for classification algorithms. It needs to be preprocessed. The preprocessing steps are listed below:

### Data Balancing
The dataset is imbalanced. There are 12332 gamma events and 6688 hadron events. The number of gamma events is much higher than the number of hadron events. This can cause the classifier to be biased towards the gamma events. To solve this problem, the dataset is balanced by downsampling the gamma events to the number of hadron events. The number of gamma events is reduced to 6688.

### Data Splitting
The dataset is split into training and testing sets. The training set is used to train the classifier. The testing set is used to test the classifier. The dataset is split into 80% training set and 20% testing set.

## Classification Algorithms
Classification algorithms are used to classify the events into gamma and hadron events. 6 classification algorithms are used in this project. The algorithms are listed below:

### Decision Tree Classifier
- No parameters are used in the classifier.

### AdaBoost Classifier
- N-estimators parameter is used in the classifier. The value of the parameter is tuned using the cross-validation method. The value of the parameter is 200.

### K-Nearest Neighbors Classifier (KNN)
- K-neighbors parameter is used in the classifier. The value of the parameter is tuned using the cross-validation method. The value of the parameter is 21.

### Random Forest Classifier
- N-estimators parameter is used in the classifier. The value of the parameter is tuned using the cross-validation method. The value of the parameter is 400.

### Naive Bayes Classifier
- No parameters are used in the classifier.

### Neural Network 
- The neural network consists of 2 hidden layers. The number of neurons in each layer is tuned using the cross-validation method. The number of neurons in the first hidden layer is 50 and the number of neurons in the second hidden layer is 90.

## Classifiers Comparison
<table align="center">
    <tr>
        <th>Algorithm</th>
        <th>Accuracy</th>
        <th>Precision</th>
        <th>Recall</th>
        <th>Average F1</th>
    </tr>
  <tr>
    <td>Decision Tree</td>
    <td>0.79</td>
    <td>0.79</td>
    <td>0.79</td>
    <td>0.79</td>
  </tr>
  <tr>
    <td>AdaBoost</td>
    <td>0.82</td>
    <td>0.82</td>
    <td>0.82</td>
    <td>0.82</td>
  </tr>
  <tr>
    <td>KNN</td>
    <td>0.77</td>
    <td>0.78</td>
    <td>0.77</td>
    <td>0.77</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>0.87</td>
    <td>0.87</td>
    <td>0.87</td>
    <td>0.87</td>
  </tr>
  <tr>
    <td>Naive Bayes</td>
    <td>0.65</td>
    <td>0.69</td>
    <td>0.65</td>
    <td>0.63</td>
  </tr>
  <tr>
    <td>Neural Network</td>
    <td>0.85</td>
    <td>0.86</td>
    <td>0.85</td>
    <td>0.85</td>
  </tr>
</table>

## Remarks

The README.md file contains an overview of the project, it is recommended to open [notebook](https://github.com/yousefkotp/MAGIC-Gamma-Telescope-Classification/blob/main/notebook.ipynb) as it contains the code and further explanation for the results.

## Contributers

1. [Yousef Kotp](https://github.com/yousefkotp)

2. [Mohamed Farid](https://github.com/MohamedFarid612)

3. [Adham Mohamed](https://github.com/adhammohamed1)
