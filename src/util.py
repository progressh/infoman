from yahoofinancials import YahooFinancials
import datetime,json,os
stock_list = '[' \
  '{"ticker":"TSLA","desc":"tesla"},' \
  '{"ticker":"ES","desc":"Eversource Energy"}' \
  ']'

def get_previous(tickerarg):
    tickers = tickerarg.split(",")
    today = datetime.date.today()
    previous = today - datetime.timedelta(days=3)
    tstr = today.strftime("%Y-%m-%d")
    lmstr = previous.strftime("%Y-%m-%d")
    yahoo_financials_banks = YahooFinancials(tickers)
    print(datetime.datetime.now().time())
    summary = yahoo_financials_banks.get_summary_data()
    print(datetime.datetime.now().time())
    attr_names = [ "previous_close", "open", "day_low", "day_high", "bid","ask", "pe","market_cap","fifty_two_week_low", "fifty_day_average","two_hundred_day_average"]
    attr_to_extract = {}
    attr_to_extract["previous_close"]="previousClose"
    attr_to_extract["open"]="open"
    attr_to_extract["day_low"]="dayLow"
    attr_to_extract["day_high"]="dayHigh"
    attr_to_extract["bid"]="bid"
    attr_to_extract["ask"]="ask"
    attr_to_extract["dividend_yield"]="dividendYield"
    attr_to_extract["pe"]="trailingPE"
    attr_to_extract["market_cap"]="marketCap"
    attr_to_extract["fifty_two_week_low"]="fiftyTwoWeekLow"
    attr_to_extract["fifty_day_average"]="fiftyDayAverage"
    attr_to_extract["two_hundred_day_average"]="twoHundredDayAverage"
    
    print(summary)
    rlt = {}
    for ticker in tickers:
        rlt[ticker] = {}
        for attr in attr_names:
          try:
            rlt[ticker][attr]=summary[ticker][attr_to_extract[attr]]
          except KeyError:
            pass
    outfile=open("out.html","w", encoding='utf8')
    outfile.write("<html><body>")
    outfile.write("<table border=\"1\">")
    outfile.write("<tr>")
    outfile.write("<td>")
    outfile.write("ticker")
    outfile.write("</td>")
    for attr in attr_names:
      outfile.write("<td>")
      outfile.write(attr)
      outfile.write("</td>")
    outfile.write("<td>")
    outfile.write("recommendation")
    outfile.write("</td>")
    outfile.write("</tr>")
    for ticker in tickers:
      outfile.write("<tr>")
      outfile.write("<td>")
      outfile.write(ticker)
      outfile.write("</td>")
      for attr in attr_names:
        outfile.write("<td>")
        outfile.write(str(rlt[ticker][attr]))
        outfile.write("</td>")
      outfile.write("<td>")
      outfile.write("")
      outfile.write("</td>")
      outfile.write("</tr>")
    outfile.write("</body></html>")

    

json_object = json.loads(stock_list)
stock_list_str=''
for item in json_object:
  if len(stock_list_str) != 0:
    stock_list_str +=','  
  stock_list_str += item['ticker']
get_previous(stock_list_str)
#print(os.getcwd()) current dir is github