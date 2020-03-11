from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
label = preprocessing.LabelEncoder()
weather_en = label.fit_transform(weather)
temp_en = label.fit_transform(temp)
play_en = label.fit_transform(play)
features =list(zip(weather_en, temp_en))
gaussian = GaussianNB()
gaussian.fit(features, play_en)
print(gaussian.predict([[0,2]]))