import sys, os, time
import requests
import yaml as yaml
from Pricebot import Pricebot
from Configure import Configure
from subprocess import Popen

WEEK = 604800
DAY = 86400
HOUR = 3600
MINUTE = 60
EPSILON = MINUTE * 2

def main():
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

            # creates a pricebot for each configuration setting
            for bot in cfg:
                config = Configure(cfg, str(bot))
                pricebot = Pricebot(config)

                total_coins =  config.getAllCoins()
                for coin in total_coins:
                    print(coin)
                    pricebot.plotTweet(coin)

                pricebot.updateTweet()

        except Exception as err:
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

if __name__ == '__main__':
    main()
