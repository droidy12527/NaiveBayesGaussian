from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
weather_main = ['overcast', 'rainy', 'sunny']
play_main = ['No','Yes']
temp_main = ['cool','hot','mild']
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
weather_ip = input('Tell me weather condition: Sunny / Overcast / Rainy: ')
weather_ip = weather_main.index(weather_ip.lower())
temp_ip = input('Tell me temperature: Hot / Mild / Cool: ')
temp_ip = temp_main.index(temp_ip.lower())
prediction = int(gaussian.predict([[weather_ip,temp_ip]]))
print('The prediction is: '+play_main[prediction])
