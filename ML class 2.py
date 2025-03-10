import matplotlib as pd
import numpy as np
import pandas as pd

dataset = pd.read_csv(r"C:\Users\navee\DS class files\ML class files\24 and 26 dec\24th- ML\2.Training,Testing & Model\Data.csv")


x = dataset.iloc[:, :-1].values

y = dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer()

imputer = imputer.fit(x[:,1:3])

x[:,1:3] = imputer.transform(x[:,1:3])


from sklearn.preprocessing import LabelEncoder

labelencoder_x = LabelEncoder()

labelencoder_x.fit_transform(x[:,0])
x[:,0] = labelencoder_x.fit_transform(x[:,0])


labelencoder_y = LabelEncoder()

y = labelencoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2, random_state=0)