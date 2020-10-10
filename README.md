# DL_stockmarket
Obj  - To train a Machine Learning Model that can 'play' around in the simulated market and achieve a reasonable accuracy.

Current Progress : 
* Completed making a ML model that takes only the price action into account. 
* Collected Data From : https://www.kaggle.com/hk7797/stock-market-india
* Only considered bank stocks
* Aprrox 1.6 million data points
* The ML model used is DQN with The CNN hidden layers as the main idea is to capture short term price pattern when doing intraday trading

Challenges : 
* only price action doesn't give a whole lot of picture , may require live sentiment analysis to further improve the accuracy
* The training is lot slower due to large I/O overhead. Can we train data in bigger batches? --- Done
* Tweaking required in the main model
* Require better optimization technique for better convegence since this is very high entropy data. Is this a random walk?
* Apply and compare with Policy Gradient Method
