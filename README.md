# Crypto-Pub

RSICrossOver.py is for Double RSI Crossover Strategy; for example you can choose rsi1 argument as 7-day RSI, and rsi2 as 21-day. It works for machine learning performance as a feature for my model. So cheers, try it.

DateFeatureExtractor.py takes np.datetime64 array as input and extracts features as the current year, month, day of the year, whether it is a business day, hour of the day, day of the week and categorized hour as a period(am or pm). Those features are especially useful for machine learning models, especially working with time series data. 
