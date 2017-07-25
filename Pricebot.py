# Jordan Dworaczyk
# jordan.dwo@gmail.com
# --------------------
# The following code is designed to run mutliple instances of twitter bots.
# The purpose of these twitter bots is to tweet the price data of different
# cyrpto markets. The price data includes a 24hr market summary as well as a
# candle stick OHCL chart of the past week.

import os, sys
import time, datetime
import requests
import plotly.offline as offline
import plotly.graph_objs as go
import tweepy

WEEK = 604800
DAY = 86400
HOUR = 3600
MINUTE = 60
EPSILON = MINUTE * 2

class Pricebot(object):

    def __init__(self, config):
        self.config = config

        self.consumer_key = self.config.getKey('consumer_key')
        self.consumer_secret = self.config.getKey('consumer_secret')
        self.access_key =self.config.getKey('access_key')
        self.access_secret = self.config.getKey('access_secret')

        self.charts = []
        self.download_folder = self._findDownLoadsFolder()

        self.browser = self._findBrowser()

    def plotTweet(self, use_coin):
        coin_symbol = self.config.getSymbol(use_coin)
        candlestick = self.config.getDuration(use_coin)

        # for getting interval of OHLC data from cyrptowatch
        now =  int(time.time())

        # parameters for grabbing specific content form cyrptowatch
        params = {}
        duration = 0
        if candlestick == 'hourly':
            date = int(time.time() - ( 2 * WEEK ))
            duration = HOUR
            params = {'after': date, 'before': now, 'periods': duration }
        elif candlestick == 'daily':
            date = int(time.time() - ( DAY * 365 ))
            duration = DAY
            params = {'after': date, 'before': now, 'periods': duration }

        # grabs OHCL contents from cryptowatch
        url = "https://api.cryptowat.ch/markets/gdax/" + coin_symbol +"usd/ohlc"

        # makes request to cryptowatch for data
        r = requests.get(url, params=params)
        print('retrieving data from : ' + url )

        data = r.json()

        self.buildPlot(use_coin, data, candlestick, duration, coin_symbol)

    def buildPlot(self, use_coin, data, candlestick, duration, coin_symbol):
        increasing_color = self.config.getColor(use_coin, 'increasing_color')
        decreasing_color = self.config.getColor(use_coin, 'decreasing_color')
        full_name = self.config.getName(use_coin)

        titleX_axis = ''
        candlestick_dur = ''
        if candlestick == 'hourly':
            titleX_axis = 'Past 14 Days (UTC Time)'
            candlestick_dur = ' Hour '
        elif candlestick =='daily':
            titleX_axis = 'Past Year (UTC Time)'
            candlestick_dur = ' Day '

        # puts json data into list with each element being a candle
        data = data['result'][str(duration)]

        # initializing lists for OHCL data
        dates = list()
        open_data = list()
        high_data = list()
        low_data = list()
        close_data = list()
        volume_data = list()

        # reading data form each candle into OHCL lists
        for candle in data:
            #puts day for each candle into datetime for plotting
            day = candle[0]
            day = datetime.datetime.fromtimestamp(day).strftime('%Y-%m-%d %H:%M:%S')
            dates.append(day)

            open_data.append(candle[1])
            high_data.append(candle[2])
            low_data.append(candle[3])
            close_data.append(candle[4])
            volume_data.append(candle[5])

        # traces the data for plot
        trace_candlestick = go.Candlestick(x=dates,
            open=open_data,
            high=high_data,
            low=low_data,
            close=close_data,
            increasing=dict(name='<i>Bullish' + candlestick_dur + '</i>',
                line=dict(color= increasing_color)
            ),
            decreasing=dict(name='<i>Bearish' + candlestick_dur + '</i>',
                line=dict(color= decreasing_color)
            ),
            showlegend = False
        )

        # candlestick plots in plotly do not have an attribute for circle
        # legends. So, we have to make a scatter plot that in
        # order to use its legend which is circular. This is what is
        # happening with `legend_increasing` and `legend_decreasing`. We make
        # the sctter plot invisible so that it does not show up on the chart
        legend_increasing = {
            'x':[0],
            'y':[0],
            'visible': 'legendonly',
            'legendgroup' : 'group',
            'name': '<i>Bullish' + candlestick_dur + '</i>',
            'mode': 'markers',
            'marker': {
                'color': increasing_color
            },
            'showlegend': True,
            'opacity': 1
        }

        legend_decreasing= {
            'x':[0],
            'y':[0],
            'visible': 'legendonly',
            'legendgroup' : 'group',
            'name': '<i>Bearish' + candlestick_dur + '</i>',
            'mode': 'markers',
            'marker': {
                'color': decreasing_color
            },
            'showlegend': True,
            'opacity': 1
        }

        data = [trace_candlestick, legend_increasing, legend_decreasing]

        # attributes for plot
        layout = go.Layout(
            title = 'GDAX: Price of ' + full_name,
            titlefont=dict(
                family='Helvetica',
                size=34,
                color='#7f7f7f'
                ),
            xaxis=dict(
                rangeslider=dict(
                    visible=False
                ),
                title= titleX_axis + '<br>',
                showgrid= True,
                titlefont=dict(
                    family='Helvetica',
                    size=24,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='USD',
                titlefont=dict(
                    family='Helvetica',
                    size=24,
                    color='#7f7f7f'
                ),
                side='right'
            ),
            paper_bgcolor= '#ffffff',
            plot_bgcolor= '#ffffff',
            legend = dict(
                x = -.1,
                y = -.25,
                font=dict(
                    family='Helvetica',
                    size=12,
                    color='#7f7f7f'
                ),
            ),
            images=[dict(
                source= 'https://raw.githubusercontent.com/JordanDworaczyk/EthPriceBot/master/' + coin_symbol + 'watermark.png',
                xref='paper', yref='paper',
                x=.95, y=-.4,
                sizex=0.2, sizey=0.2,
                opacity=0.1,
                xanchor='left', yanchor='bottom'
            )]
        )

        # combines data and layout into figure
        fig = go.Figure(data=data, layout=layout)

        total_coins = self.config.getAllCoins()
        img_width = 0
        img_height = 0
        if len(total_coins) == 1:
            img_width = 800
            img_height = 600
        elif len(total_coins) == 2 or len(total_coins) == 4:
            img_width = 600
            img_height = 600

        #plots figure, saves as html, saves pic of chart into downloads folder
        offline.plot(fig,
        filename=use_coin + '.html',
        image='png',
        image_filename = coin_symbol + use_coin + 'plot',
        auto_open=True,
        image_width = img_width,
        image_height = img_height
        )

    def updateTweet(self):
        # authenticates with twitter account using tweepy
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)

        # creates string for tweet
        tweet_time = self.config.getTimesToTweet()
        tweet = ''
        use_coins = []
        for times in tweet_time:
            coins = self.config.getCoinsToTweet(times)
            status = self.config.getStatus(times)
            use_coins = coins

            if status == '24hMarketTweet':
                use_coin = coins[0]

                coin_symbol = self.config.getSymbol(use_coin)
                full_name = self.config.getName(use_coin)

                tweet = self._create24hTweet(use_coin, coin_symbol, full_name)
            elif status == 'TotalMarketSummary':
                pass # create TotalMarketSummary()

        self._findChartPictures(coins)
        # upload images and get media_ids
        media_ids = []
        for filename in self.charts:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)

        # tweets with status and pictures
        api.update_status(media_ids=media_ids, status=tweet)

        # removes picture from file after tweeted
        for filename in self.charts:
            os.remove(filename)

        #prints tweet data to console
        now = datetime.datetime.now()
        print('\n---------------------------------\n')
        print("Last tweet sent:" + now.strftime('%Y/%m/%d/ %I:%M:%p'))
        print("Just tweeted:\n" +str(tweet))
        print('\n---------------------------------\n')

    def _create24hTweet(self, coin, coin_symbol, full_name):
        #grabs contents from cryptowatch
        r=requests.get("https://api.cryptowat.ch/markets/gdax/" + coin_symbol + "usd/summary")
        data = r.json()

        #finds data in contents
        last = data['result']['price']['last']
        high = data['result']['price']['high']
        low = data['result']['price']['low']
        percentage = data['result']['price']['change']['percentage']
        absolute_change = data['result']['price']['change']['absolute']
        volume = data['result']['volume']

        #puts into percentage format
        percentage = percentage * 100
        volume = volume * last
        volume = "{:,}".format(volume)

        #turns data into string format
        last = "Last: $%5.2f\n" % last
        high = "High: $%5.2f\n" % high
        low = "Low: $%5.2f\n" % low
        percentage = "Change: %3.2f%%" % percentage
        absolute_change = " | $%3.2f\n" % absolute_change
        volume = "Volume: $%.17s\n" % volume

        #creates string for tweet
        tweet = "#"+ coin_symbol.upper() +" 24hr Summary:\n" + last + high + low + percentage \
            + absolute_change + volume + "$"+coin_symbol.upper()+" #"+full_name+" #Pricebots"

        return tweet

    def _findDownLoadsFolder(self):
        name_of_operating_system = os.name

        #creates download_folder's path based off of os
        if name_of_operating_system == 'nt':
            print('The operating System is Windows.')
            download_folder = os.path.expanduser('~') + '\Downloads\\'
            print('The downloads folder is '+ download_folder)
        else:
            print('The operating System is Linux')
            download_folder = os.path.expanduser('~') + '/Downloads/'
            print('The downloads folder is '+ download_folder)
        return download_folder

    def _findBrowser(self):
        name_of_operating_system = os.name

        #creates download_folder's path based off of os
        if name_of_operating_system == 'nt':
            print('The operating System is Windows.')
            browser = 'chrome.exe'
            print('The browser is ' + browser)
        else:
            print('The operating System is Linux')
            browser = 'chromium-browser'
            print('The browser is ' + browser)
        return browser

    def _waitToDownload(self, coin, filename):
        #sleeps to allow time for plot.png to be downloaded into folder
        coin_symbol = self.config.getSymbol(coin)

        while os.path.exists(filename) == False:
            print('Picture of chart is not yet downloaded')
            print('Looking for ' + filename )
            time.sleep(5)
        print('Picture of chart has been downloaded')

    def _findChartPictures(self, coins):
        self.charts = []
        for coin in coins:
            coin_symbol = self.config.getSymbol(coin)
            filename = self.download_folder + coin_symbol + coin + 'plot.png'
            self.charts.append(filename)
            self._waitToDownload(coin, filename)

        return self.charts

if __name__ == "__main__":
    main()
