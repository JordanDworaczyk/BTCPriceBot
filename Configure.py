class Configure:

    def __init__(self, cfg, bot):
        self.cfg = cfg[bot]

    def getBotConfig(self):
        summary = '\nThis is a summary of the bots configuration. \n'
        raw = '\nRaw:'
        raw += '\n----\n' + str(self.cfg) + '\n'

        summary += raw

        keys = '\nThese are the keys provided:'
        keys += '\n----------------------------\n'
        for key, value in self.cfg['api_keys'].items():
            keys = keys + key + ': ' + value + '\n'

        summary += keys

        settings = '\nThese are the settings for this bot\n'
        settings += '\n------------------------------------\n'
        times_to_tweet = self.getTimesToTweet()
        settings += 'Times to Tweet: ' + str(times_to_tweet)
        for status in times_to_tweet:
            tweet = self.getStatus(status)
            settings += '\nTweet ' + status + ': '
            settings += tweet

        summary += settings
        currencies = '\nCoins/Currencies for this Bot:\n'
        currencies +='--------------------------------\n'
        for currency in self.cfg['currencies']:

            coin = str(currency)
            name = self.getName(coin) + ', '
            symbol = self.getSymbol(coin)
            increasing_color = self.getColor(coin, 'increasing_color')
            decreasing_color = self.getColor(coin, 'decreasing_color')

            details = coin + '\n'
            details += 'Name: ' + name + symbol + '\n'
            details += 'Increasing Color:' + increasing_color + '\n'
            details += 'Decreasing Color: ' + decreasing_color + '\n'

            currencies += details + '\n'
        summary += currencies

        return summary

    def getKey(self, key) :
        return self.cfg['api_keys'][key]

    def getDetails(self, coin):
        return self.cfg['currencies'][coin]['details']

    def getCandleSticks(self, coin):
        return self.cfg['currencies'][coin]['candlesticks']

    def getSymbol(self, coin):
        details = self.getDetails(coin)
        symbol = details['name']
        return symbol

    def getName(self, coin):
        details = self.getDetails(coin)
        name = details['full_name']
        return name

    def getColor(self, coin, stick):
        candlesticks = self.getCandleSticks(coin)
        color = candlesticks[stick]
        return color

    def getAllCoins(self):
        all_coins = []
        times_to_tweet = self.getTimesToTweet()
        for time in times_to_tweet:
            all_coins = self.getCoinsToTweet(time)
        return all_coins


        for coin in self.cfg['currencies']:
            all_coins.append(coin)

        return all_coins

    def getSettings(self):
        settings = self.cfg['settings']
        return settings

    def getTimesToTweet(self):
        times = self.getSettings()

        times_to_tweet = []
        for time in times:
            times_to_tweet.append(time)

        return times_to_tweet

    def getStatus(self, time):
        settings = self.getSettings()
        status = settings[time]['status']

        return status

    def getCoinsToTweet(self, time):
        settings = self.getSettings()
        coins_to_tweet = settings[time]['coins']

        return coins_to_tweet

    def getDuration(self, coin):
        candlesticks = self.getCandleSticks(coin)
        duration = candlesticks['duration']
        return duration
