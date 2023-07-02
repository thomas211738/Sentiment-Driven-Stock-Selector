# Sentiment-Driven-Stock-Selector
This project was created by @thomas211738 and @joshleeds

This project collects daily headlines for each company in the S&P 500 and performs sentiment analysis on them. It collects 100 headlines for each company and then gives a polarity score to the five most relevant headlines. Then, it calculates a polarity score for each company based on the average of the 5 headline scores. After, it compares the scores with the percentage change in the stock price from yesterday's closing price to today's open price. 

By collecting data each day for a month, we were able to create a graphical representation of each company's sentiment score versus percentage change and show the correlation between both variables for each company. 

Here is an example for the company Cardinal Health Inc:
<img width="631" alt="Screenshot 2023-07-02 at 2 50 08 PM" src="https://github.com/thomas211738/Sentiment-Driven-Stock-Selector/assets/134543664/62d22314-b297-44a2-b7ae-168e3ea70d64">

As you can see, Cardinal Health Inc has a positive correlation between headline polarity score and percent change of a stock price. Out of all the companies in the S&P 500, our project concluded that around 60 companies have a strong positive correlation. Although this project should not solely be used to make investment decisions, it can still be taken into account when investing.

This project allows the user to see the graph of any company in the S&P 500.
