# Sentiment-Driven-Stock-Selector
This project was created by @thomas211738 and @joshleeds

This project collects daily headlines for each company in the S&P 500 and performs sentiment analysis on them. It collects 100 headlines for each company and then gives a polarity score to the five most relevant headlines. Then, it calculates a polarity score for each company based on the average of the 5 headline scores. After, it compares the scores with the percentage change in the stock price from yesterday's closing price to today's open price. 

By collecting data each day for a month, we were able to create a graphical representation of each company's sentiment score versus percentage change and show the correlation between both variables for each company. 

Here is an example for the company Cardinal Health Inc:
<img width="631" alt="Correlation Pic" src="Screenshot 2023-07-02 at 2.50.08 PM.png">

As you can see, Cardinal Health Inc has a positive correlation between headline polarity score and percent change of a stock price. Out of all the companies in the S&P 500, our project concluded that around 60 companies have a strong positive correlation. Although this project should not solely be used to make investment decisions, it can still be taken into account when investing.

This project allows the user to see the graph of any company in the S&P 500.


MIT License

Copyright (c) 2023 Thomas Yousef

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
