# Jordan Dworaczyk
# jordan.dwo@gmail.com
# -----------------------
# The following code is designed to run mutliple instances of twitter bots.
# The purpose of these twitter bots is to tweet the price data of different
# cyrpto markets. The price data includes a 24hr market summary as well as a
# candle stick OHCL chart of the past week.

import requests
import time, datetime, threading, tweepy
import plotly.offline as offline
import plotly.graph_objs as go
import os
import yaml as yaml
from subprocess import Popen
import sys

WEEK = 604800
DAY = 86400
HOUR = 3600
MINUTE = 60
EPSILON = MINUTE * 2

class PriceBot(object):
    """The following code is designed to run mutliple instances of twitter bots.
    The purpose of these twitter bots is to tweet the price data of different
    cyrpto markets. The price data includes a 24hr market summary as well as a
    candle stick OHCL chart of the past week.

    Attributes:
        CONSUMER_KEY: Twitter API Key.
        CONSUMER_SECRET: Twitter API Key.
        ACCESS_KEY: Twitter API Key.
        ACCESS_SECRET: Twitter API Key.
        coin_name: Name of coin that bot is tweeting about. Such as, BTC, ETH,
                   LTC, ETC, etc..
        download_folder: Folder to place picture of chart.
    """

    def __init__(self,
                    consumer_key, consumer_secret,
                    access_key, access_secret,
                    coin_name, full_name, download_folder,
                    increasing_color, decreasing_color):
        """Return a PriceBot object with the coin_name of *coin_name* with the
            given API keys."""
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_key = access_key
        self.access_secret = access_secret
        self.coin_name = coin_name
        self.download_folder = download_folder
        self.full_name = full_name
        self.increasing_color = increasing_color
        self.decreasing_color = decreasing_color

    @classmethod
    def plotTweet(self):
        # for getting interval of OHLC data from cyrptowatch
        now =  int(time.time())
        date = int(time.time() - WEEK)

        # prints out to console
        print("Last week:  %9.0f" % date)
        print(datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S'))
        print("\nNow: %9.0f" % now)
        print(datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S'))
        print()

        # parameters for grabbing specific content form cyrptowatch
        params = {'after': date, 'before': now, 'periods': HOUR}

        # grabs OHCL contents from cryptowatch
        r = requests.get("https://api.cryptowat.ch/markets/gdax/" + coin_name + "usd/ohlc",
                        params=params)
        data = r.json()

        # puts json data into list with each element being a candle
        data = data['result'][str(HOUR)]

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
                               increasing=dict(name='<i>Bullish Hour</i>',
                                    line=dict(color= increasing_color)
                                    ),
                               decreasing=dict(name='<i>Bearish Hour</i>',
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
            'name': 'Bullish Hour',
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
            'name': 'Bearish Hour',
            'mode': 'markers',
            'marker': {
                'color': decreasing_color
            },
            'showlegend': True,
            'opacity': 1
        }

        data = [trace_candlestick, legend_increasing, legend_decreasing]

        # attributes for plot
        cwd = os.getcwd()
        layout = \
            go.Layout(
            title = 'GDAX: Price of ' + full_name,
            titlefont=dict(
                family='Helvetica',
                size=34,
                color='#7f7f7f'
                )
            ,
            xaxis=dict(
                rangeslider=dict(
                    visible=False
                ),
                title='Past Seven Days (UTC Time)<br>',
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
                source= 'https://raw.githubusercontent.com/JordanDworaczyk/EthPriceBot/master/' + coin_name + 'watermark.png',
                xref='paper', yref='paper',
                x=.95, y=-.4,
                sizex=0.2, sizey=0.2,
                opacity=0.1,
                xanchor='left', yanchor='bottom'
            )]
        )

        print(cwd)

        # combines data and layout into figure
        fig = go.Figure(data=data, layout=layout)

        #plots figure, saves as html, saves pic of tweet into downloads folder
        offline.plot(fig, image='png',image_filename=coin_name + 'plot',auto_open=True)
    @classmethod
    def getTotalMarketStatus(self):
        url = 'https://api.coinmarketcap.com/v1/ticker/'
        r = requests.get(url + full_name + '/')
        data = r.json()

        print(data)

        last = data[0]['price_usd']
        volume = data[0]['24h_volume_usd']
        marketcap = data[0]['market_cap_usd']
        change = data[0]['percent_change_24h']

        status = "#"+ coin_name.upper() + " 24hr Total Market Summary:\n"
        last = "Last: $" + last + "\n"
        change = "Change: " + change + "%\n"
        volume = "Volume: $" + volume + "\n"
        marketcap = "Marketcap: $" +  marketcap + "\n"

        status = status + last + change + volume + marketcap
        status = status + "$" + coin_name.upper() + " #" + full_name + " #Pricebots"

        print(status)
        return status
    @classmethod
    def getMarketSummary(self):
        #grabs contents from cryptowatch
        r=requests.get("https://api.cryptowat.ch/markets/gdax/" + coin_name + "usd/summary")
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

        #turns data into string format
        last = "Last: $%5.2f\n" % last
        high = "High: $%5.2f\n" % high
        low = "Low: $%5.2f\n" % low
        percentage = "Change: %3.2f%%" % percentage
        absolute_change = " | $%3.2f\n" % absolute_change
        volume = "Volume: $%9.2f\n" % volume

        #creates string for tweet
        tweet = "#"+ coin_name.upper() +" 24hr Summary:\n" + last + high + low + percentage \
            + absolute_change + volume + "$"+coin_name.upper()+" #"+full_name+" #coinbase"

        return tweet

    @classmethod
    def updateTweet(self, tweet):

        now = datetime.datetime.now()

        #sleeps to allow time for plot.png to be downloaded into folder
        while os.path.exists( download_folder +coin_name+ 'plot.png' ) == False:
            print('Picture of chart is not yet downloaded')
            time.sleep(5)
        print('Picture of chart has been downloaded')

        #tweets to twitter with picture and tweet status
        api.update_with_media(download_folder+ coin_name+ 'plot.png',
        status=tweet)

        # removes picture from file after tweeted
        os.remove(download_folder+coin_name+'plot.png')

        #prints data to console
        print("Last tweet sent:" + now.strftime('%Y/%m/%d/ %I:%M:%p'))
        print("Just tweeted:\n" +str(tweet))
        print()

def _findDownLoadsFolder():
    name_of_operating_system = os.name

    #creates download_folder's path based off of os
    if name_of_operating_system == 'nt':
        print('The operating System is Windows.')
        download_folder = os.path.expanduser('~')+'\Downloads\\'
        print('The downloads folder is '+ download_folder)
        browser = 'The browser is chrome.exe'
        print(browser)
    else:
        print('The operating System is Linux')
        download_folder = os.path.expanduser('~')+'/Downloads/'
        print('The downloads folder is '+download_folder)
        browser = 'The browser is chromium-browser'
        print(browser)
    return download_folder

def _findBrowser():
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

if __name__ == "__main__":
    arg = sys.argv[1]
    when = sys.argv[2]

    browser = _findBrowser()

    if arg == 'test':
        desktop_path = os.path.expanduser('~')+'\Desktop\\'
        config_file = desktop_path + 'test.yml'
    elif arg == 'run':
        config_file = 'config.yml'

    if when == 'hourly':
         time_to_tweet = HOUR
    elif when == 'now':
        time_to_tweet = MINUTE

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)

    while True:
        try:
            now = time.time()
            round(now)

            #forces tweet to initiate on the hour
            while now % time_to_tweet > EPSILON:
                print('Waiting to tweet.')
                now = time.time()
                round(now)
                time.sleep(MINUTE / 2)

            for bot in cfg:
                consumer_key = cfg[bot]['consumer_key']
                consumer_secret = cfg[bot]['consumer_secret']
                access_key = cfg[bot]['access_key']
                access_secret = cfg[bot]['access_secret']
                coin_name = cfg[bot]['coin_name']
                full_name = cfg[bot]['full_name']
                download_folder = _findDownLoadsFolder()
                increasing_color = cfg[bot]['increasing_color']
                decreasing_color = cfg[bot]['decreasing_color']

                print(cfg)

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_key, access_secret)
                api = tweepy.API(auth)

                bot = PriceBot(consumer_key, consumer_secret, access_key,
                    access_secret, coin_name, full_name, download_folder,
                    increasing_color, decreasing_color)

                bot.plotTweet()
                bot.updateTweet()

        except KeyError as err:
            print(err)
        finally:
            time.sleep( time_to_tweet / 2 )
            #clears chrome window to avoid openning too many tabs and crashing system
            if browser == 'chrome.exe':
                Popen(['taskkill ', '/F',  '/IM', browser], shell=False)
            elif browser == 'chromium-browser':
                os.system('killall ' + browser)
            else:
                print('Cannot find browser to kill.')
                print(browser)
