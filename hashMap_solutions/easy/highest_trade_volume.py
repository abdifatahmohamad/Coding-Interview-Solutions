'''
We notice that out servers are expecting increased traffic due to large trade volumes of a popular stock.

We need to create a report for our CEO to show which stock has the highest trade volume(number of shares traded).

Unfortunately, the data we received from the server is not aggregated. It's given to us as list of strings.
Each string contains the ticker symbol and the number of shares traded separated by space.
Ticker symbols are always exactly 3 characters.


Please aggregate this data to report the CEO which stock has the highest trade volume.


Example 1:
["ABC 9", "XYZ 2"] ==> "ABC

Example 2: 
["ABC 9", "XYZ 7", "HIJ 10", "XYZ 5"] ==> "XYZ
'''

# Handful approach
from typing import List


def highest_trade_volume(trade: List[str]) -> str:
    mapping = {}
    max_trade = float("-Inf")
    max_ticker = ""
    for data in trade:
        ticker, trade_val = data.split(" ")
        trade_val = int(trade_val)

        # if ticker in mapping:
        #     mapping[ticker] += int(trade_val)
        # else:
        #     mapping[ticker] = int(trade_val)

        # Short version of above if else statement
        mapping[ticker] = mapping.get(ticker, 0) + trade_val

        if mapping[ticker] > max_trade:
            max_trade = mapping[ticker]
            max_ticker = ticker

    return max_ticker


# My approach
def highest_trade_volume(trade: List[str]) -> str:
    mapping = {}
    max_trade = float("-Inf")
    for data in trade:
        ticker, trade_val = data.split(" ")
        trade_val = int(trade_val)

        mapping[ticker] = mapping.get(ticker, 0) + trade_val

        max_trade = max(max_trade, mapping.get(ticker))

    for t in mapping:
        if max_trade == mapping[t]:
            return t


print(highest_trade_volume(["ABC 9", "XYZ 7", "HIJ 10", "XYZ 5"]))


def test():
    assert highest_trade_volume(["ABC 9", "XYZ 3"]) == "ABC"
    assert highest_trade_volume(["ABC 9", "XYZ 7", "HIJ 10", "XYZ 5"]) == "XYZ"
