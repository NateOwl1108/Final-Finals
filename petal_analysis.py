
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import pandas as pd
df = pd.read_csv('titanic/train.csv')
independent = df[["SepalLengthCm","SepalWidthCm","PetalLengthCm"]]
dependent = df[["PetalWidthCm"]]

reg = LinearRegression().fit(independent, dependent)
rss = 0
predictions = []
row = [i for in range(len(df['PetalWidthCm']))]
for i in range(len(df['PetalWidthCm'])):
  prediction = reg.predict(independent[i])
  predictions.append(prediction)
  rss += (dependent[i] - prediction) **.5

plt.plot(row,predictions)
plt.xlabel("row")
plt.ylabel("prediction")
plt.savefig('petal analysis .png')



