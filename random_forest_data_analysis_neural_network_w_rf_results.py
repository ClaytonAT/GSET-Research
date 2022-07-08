# -*- coding: utf-8 -*-
"""Random Forest Data Analysis/Neural Network w/RF Results

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/199J1lxdTUBYInkK8fG24LVtbHIiSG_PO
"""

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
!pip install shap
import matplotlib.pyplot as plt

SpartaScore=pd.read_csv('/content/Condensed Data Set   - PCA Data Prep (2).csv')

TargetVariable=['InjuryRisk']
Predictors=['Age', 'GeneralBodyMass', 'JumpMaxChangeinAcceleration', 'JumpHeight', 'JumpMaxAcceleration', 'JumpEccentricImpulse', 'JumpConcentricImpulse',
            'JumpMaxVelocity', 'JumpMaxPower', 'JumpUnweightingTime', 'JumpEccentricTime', 'JumpConcentricTime', 'JumpTimetoTakeOff', 
            'JumpTimetoMaxAcceleration', 'JumpCountermovementDepth', 'JumpmRSIModifiedReactiveStrengthIndex', 'JumpHeight(Flight Time)', 'JumpLoad(Avg Braking RFD)', 
            'JumpExplode(Avg Relative Concentric Force)', 'JumpDrive(Relative Concentric Impulse)', 'JumpCOPxShiftStart', 'JumpCOPyShiftStart', 'JumpCOPxShiftAcceleration', 'JumpCOPyShiftAcceleration', 
            'JumpCOPxSwayVelocity', 'JumpCOPySwayVelocity', 'JumpInjuryRiskGroup', 'JumpHeightRiskGroup', 'JumpHeightGroup', 'BalanceSway(Sway Velocity Mean)', 'BalanceMultiscaleVerticalEntropy', 'BalanceMultivariateMultiscaleEntropy', 
            'BalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'BalanceCOPxShift', 'SymmBalanceSway(Sway Velocity Mean)', 'SymmBalanceMultiscaleVerticalEntropy', 'SymmBalanceMultivariateMultiscaleEntropy',
            'SymmBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'SymmBalanceCOPx Shift', 'LeftBalanceSway(Sway Velocity Mean)', 'LeftBalanceMultiscaleVerticalEntropy', 'LeftBalanceMultivariateMultiscaleEntropy', 
            'LeftBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'LeftBalanceCOPxShift', 'RightBalanceSway(Sway Velocity Mean)', 'RightBalanceMultiscaleVerticalEntropy', 'RightBalanceMultivariateMultiscaleEntropy', 
            'RightBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'RightBalanceCOPxShift', 'BalanceStabilityScore', 'BalanceSwayVelocity2Leg', 'BalanceMultivariateMultiscaleEntropy2Leg', 'BalanceMultivariateMultiscaleEntropyinXYPlane2Leg']

y=SpartaScore[TargetVariable].values
X=SpartaScore[Predictors].values


X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)


rf = RandomForestRegressor(n_estimators=50)
rf.fit(X_train, y_train)

rf.feature_importances_

plt.barh(Predictors, rf.feature_importances_)
plt.rcParams["figure.figsize"] = (30,30)

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
!pip install shap
import matplotlib.pyplot as plt

SpartaScore=pd.read_csv('/content/Condensed Data Set   - PCA Data Prep (2).csv')

TargetVariable=['InjuryRisk']
Predictors=['JumpDrive(Relative Concentric Impulse)', 'JumpConcentricImpulse', 'JumpMaxVelocity', 'JumpMaxPower', 'JumpHeight', 'Age', 'GeneralBodyMass', 'JumpMaxChangeinAcceleration', 
            'JumpMaxAcceleration', 'JumpEccentricImpulse', 
            'JumpUnweightingTime', 'JumpEccentricTime', 'JumpConcentricTime', 'JumpTimetoTakeOff', 
            'JumpTimetoMaxAcceleration', 'JumpCountermovementDepth', 'JumpmRSIModifiedReactiveStrengthIndex', 'JumpHeight(Flight Time)', 'JumpLoad(Avg Braking RFD)', 
            'JumpExplode(Avg Relative Concentric Force)', 'JumpCOPxShiftStart', 'JumpCOPyShiftStart', 'JumpCOPxShiftAcceleration', 'JumpCOPyShiftAcceleration', 
            'JumpCOPxSwayVelocity', 'JumpCOPySwayVelocity', 'JumpHeightGroup', 'BalanceSway(Sway Velocity Mean)', 'BalanceMultiscaleVerticalEntropy', 'BalanceMultivariateMultiscaleEntropy', 
            'BalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'BalanceCOPxShift', 'SymmBalanceSway(Sway Velocity Mean)', 'SymmBalanceMultiscaleVerticalEntropy', 
            'SymmBalanceMultivariateMultiscaleEntropy', 'SymmBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'SymmBalanceCOPx Shift', 'LeftBalanceSway(Sway Velocity Mean)', 
            'LeftBalanceMultiscaleVerticalEntropy', 'LeftBalanceMultivariateMultiscaleEntropy', 
            'LeftBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'LeftBalanceCOPxShift', 'RightBalanceSway(Sway Velocity Mean)', 'RightBalanceMultiscaleVerticalEntropy', 
            'RightBalanceMultivariateMultiscaleEntropy', 
            'RightBalanceControl(Multivariate Multiscale Entropy in XY Plane)', 'RightBalanceCOPxShift', 'BalanceStabilityScore', 'BalanceSwayVelocity2Leg', 
            'BalanceMultivariateMultiscaleEntropy2Leg', 'BalanceMultivariateMultiscaleEntropyinXYPlane2Leg']

y=SpartaScore[TargetVariable].values
X=SpartaScore[Predictors].values


X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)


rf = RandomForestRegressor(n_estimators=150)
rf.fit(X_train, y_train)

rf.feature_importances_

plt.barh(Predictors, rf.feature_importances_)
plt.rcParams["figure.figsize"] = (50,30)

import matplotlib.pyplot as plt
from sklearn import tree

fn=Predictors
cn=TargetVariable

fig, axes = plt.subplots (nrows = 1, ncols = 1, figsize = (4,4), dpi=800)
tree.plot_tree(rf.estimators_[0], 
               feature_names = fn,
               class_names=cn, 
               filled=True);
fig.savefig('rf_OneTree.png')

# Commented out IPython magic to ensure Python compatibility.
from keras.metrics import MAPE
import pandas as pd
import numpy as np

SpartaScore=pd.read_csv('/content/Condensed Data Set   - RandomForestSelectedData.csv')

TargetVariable=['InjuryRisk']
Predictors=['JumpDrive(Relative Concentric Impulse)', 'JumpConcentricTime', 'JumpMaxVelocity', 'JumpMaxPower', 'JumpHeight']
#add variable
X=SpartaScore[Predictors].values
y=SpartaScore[TargetVariable].values

from sklearn.preprocessing import StandardScaler
PredictorScaler=StandardScaler()
TargetVariableScaler=StandardScaler()

PredictorScalerFit=PredictorScaler.fit(X)
TargetVariableScalerFit=TargetVariableScaler.fit(y)

X=PredictorScalerFit.transform(X)
y=TargetVariableScalerFit.transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#import two, test with separate data set
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

!pip install tensorflow
!pip install keras

from keras.models import Sequential
from keras.layers import Dense

model = Sequential() 

model.add(Dense(units=5, input_dim=5, kernel_initializer='normal', activation='relu'))

model.add(Dense(units=4, kernel_initializer='normal', activation='tanh'))

model.add(Dense(1, kernel_initializer='normal'))

model.compile(loss='mean_squared_error', optimizer= 'adam')

model.fit(X_train, y_train, batch_size=15, epochs = 30, verbose=1)

def FunctionFindBestParams (X_train, y_train, X_test, y_test):
  batch_size_list=[5, 10, 15, 20, 25]
  epoch_list = [5, 10, 50, 100]

  import pandas as pd
  SearchResultsData=pd.DataFrame(columns=['JumpDrive(Relative Concentric Impulse)', 'JumpConcentricTime', 'JumpMaxVelocity', 'JumpMaxPower', 'JumpHeight'])
  
  TrialNumber=0
  for batch_size_trial in batch_size_list:
    for epochs_trial in epoch_list:
      TrialNumber+=1
      model = Sequential ()
      model.add(Dense(units=5, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu'))
      model.add(Dense(units=4, kernel_initializer='normal', activation='relu'))
      model.add(Dense(1, kernel_initializer='normal'))
      model.compile(loss='mean_squared_error', optimizer='adam')
      model.fit(X_train, y_train, batch_size=batch_size_trial, epochs=epochs_trial, verbose=0)
      MAPE = np.mean(100*(np.abs(y_test-model.predict(X_test))/y_test))
      print(TrialNumber, 'Parameters:', 'batch_size', batch_size_trial, '-', 'epochs:', epochs_trial, 'Accuracy:', 100-abs(MAPE))
      SearchResultsData=SearchResultsData.append(pd.DataFrame(data=[[TrialNumber, str(batch_size_trial)+'-'+str(epochs_trial), 100-MAPE]], columns=['TrialNumber', 'Parameters', 'Accuracy'] )) 
  return (SearchResultsData)

ResultsData=FunctionFindBestParams(X_train, y_train, X_test, y_test)

# %matplotlib inline
ResultsData.plot(x='Parameters', y='Accuracy', figsize=(15,4), kind='line')


model.fit(X_train, y_train, batch_size=15, epochs = 5, verbose=0)

Predictions=model.predict(X_test)

Predictions=TargetVariableScalerFit.inverse_transform(Predictions)

y_test_orig=TargetVariableScalerFit.inverse_transform(y_test)

Test_Data=PredictorScalerFit.inverse_transform(X_test)

TestingData=pd.DataFrame(data=Test_Data, columns=Predictors) 

TestingData['InjuryRisk']=y_test_orig
TestingData['Predicted InjuryRisk']=Predictions
TestingData.head()

APE=100*(abs(TestingData['InjuryRisk']-TestingData['Predicted InjuryRisk'])/TestingData['InjuryRisk'])
TestingData['APE']=APE

print('The Acccuracy of ANN Model IS:', 100-np.mean(APE))
print(TestingData)

!pip install ann_visualizer
from ann_visualizer.visualize import ann_viz;

ann_viz(model, view = True, filename='Neural Network from Random Forest', title = "Trained Neural Network Using Variables from Random Forest Machine Learning")

"""MSK Health"""

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
!pip install shap
import matplotlib.pyplot as plt

SpartaScore=pd.read_csv('/content/Condensed Data Set   - MSK health prediction.csv')

TargetVariable=['MSK Health']
Predictors=['Sparta score', 'Load t-score', 'Explode t-score', 'Drive t-score',
            'Jump height (in)', 'Weight (lb)']

y=SpartaScore[TargetVariable].values
X=SpartaScore[Predictors].values


X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.3, random_state=42)


rf = RandomForestRegressor(n_estimators=150)
rf.fit(X_train, y_train)

rf.feature_importances_

plt.barh(Predictors, rf.feature_importances_)
plt.rcParams["figure.figsize"] = (40,25)

# Commented out IPython magic to ensure Python compatibility.
from keras.metrics import MAPE
import pandas as pd
import numpy as np

SpartaScore=pd.read_csv('/content/Condensed Data Set   - MSK health prediction.csv')

TargetVariable=['MSK Health']
Predictors=['Explode t-score', 'Weight (lb)', 'Jump height (in)']
#add variable
X=SpartaScore[Predictors].values
y=SpartaScore[TargetVariable].values

from sklearn.preprocessing import StandardScaler
PredictorScaler=StandardScaler()
TargetVariableScaler=StandardScaler()

PredictorScalerFit=PredictorScaler.fit(X)
TargetVariableScalerFit=TargetVariableScaler.fit(y)

X=PredictorScalerFit.transform(X)
y=TargetVariableScalerFit.transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#import two, test with separate data set
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

!pip install tensorflow
!pip install keras

from keras.models import Sequential
from keras.layers import Dense

model = Sequential() 

model.add(Dense(units=3, input_dim=3, kernel_initializer='normal', activation='relu'))

model.add(Dense(units=3, kernel_initializer='normal', activation='tanh'))

model.add(Dense(1, kernel_initializer='normal'))

model.compile(loss='mean_squared_error', optimizer= 'adam')

model.fit(X_train, y_train, batch_size=15, epochs = 30, verbose=1)

def FunctionFindBestParams (X_train, y_train, X_test, y_test):
  batch_size_list=[5, 10, 15, 20, 25]
  epoch_list = [5, 10, 50, 100]

  import pandas as pd
  SearchResultsData=pd.DataFrame(columns=['JumpDrive(Relative Concentric Impulse)', 'JumpConcentricTime', 'JumpMaxVelocity', 'JumpMaxPower', 'JumpHeight'])
  
  TrialNumber=0
  for batch_size_trial in batch_size_list:
    for epochs_trial in epoch_list:
      TrialNumber+=1
      model = Sequential ()
      model.add(Dense(units=5, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu'))
      model.add(Dense(units=4, kernel_initializer='normal', activation='relu'))
      model.add(Dense(1, kernel_initializer='normal'))
      model.compile(loss='mean_squared_error', optimizer='adam')
      model.fit(X_train, y_train, batch_size=batch_size_trial, epochs=epochs_trial, verbose=0)
      MAPE = np.mean(100*(np.abs(y_test-model.predict(X_test))/y_test))
      print(TrialNumber, 'Parameters:', 'batch_size', batch_size_trial, '-', 'epochs:', epochs_trial, 'Accuracy:', 100-abs(MAPE))
      SearchResultsData=SearchResultsData.append(pd.DataFrame(data=[[TrialNumber, str(batch_size_trial)+'-'+str(epochs_trial), 100-MAPE]], columns=['TrialNumber', 'Parameters', 'Accuracy'] )) 
  return (SearchResultsData)

ResultsData=FunctionFindBestParams(X_train, y_train, X_test, y_test)

# %matplotlib inline
ResultsData.plot(x='Parameters', y='Accuracy', figsize=(15,4), kind='line')


model.fit(X_train, y_train, batch_size=15, epochs = 5, verbose=0)

Predictions=model.predict(X_test)

Predictions=TargetVariableScalerFit.inverse_transform(Predictions)

y_test_orig=TargetVariableScalerFit.inverse_transform(y_test)

Test_Data=PredictorScalerFit.inverse_transform(X_test)

TestingData=pd.DataFrame(data=Test_Data, columns=Predictors) 

TestingData['InjuryRisk']=y_test_orig
TestingData['Predicted InjuryRisk']=Predictions
TestingData.head()

APE=100*(abs(TestingData['InjuryRisk']-TestingData['Predicted InjuryRisk'])/TestingData['InjuryRisk'])
TestingData['APE']=APE

print('The Acccuracy of ANN Model IS:', 100-np.mean(APE))
print(TestingData)