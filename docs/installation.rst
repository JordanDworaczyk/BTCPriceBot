Installation Guide
===================
The following is a guide for setting up your own Pricebot.

.. note:: Pricebots is intended to run on either Windows or Linux. Pricebots
  does not currently work for Mac OS.

Requirements
--------------
Here is a quick bullet list of things that you will need to run your bot. This
guide will go over how to meet these requirements, however, it is not intended
to go into every single detail.

Quick List
^^^^^^^^^^
* Download Python 3.6 or greater
* Create a Twitter account
    * Create a Twitter App
    * Generate Twitter API Keys
* Download Chrome browser if you are running the bot on Windows, or download Chromium-browser if you are running the bot on Linux
* Download the latest release of the Pricebot software
* Install dependencies for running Pricebots
* Configure your Pricebot
* Run your Pricebot

Download Python 3.6 or greater
--------------------------------
In order for you to run Pricebots, you will need to install Python 3.6. You can
download Python 3.6 `here <https://www.python.org/downloads/>`_.

Create a Twitter account
---------------------------
Once you have downloaded Python 3.6 you will need to create a Twitter account
for your Pricebot. This is just a standard Twitter profile that you would use
for a personal account.

Create a Twitter App
^^^^^^^^^^^^^^^^^^^^
After you have created your Pricebot's Twitter profile, you will need to create
a Twitter App for accessing your Pricebot's account. You can create your
Twitter App `here <https://apps.twitter.com/>`_.

Generate Twitter API Keys
^^^^^^^^^^^^^^^^^^^^^^^^^
Once you have your Twitter App created and linked to your Pricebot's Twitter
account, you will be able to generate API keys.

From within your Twitter App dash, navigate to the ``Keys and Access Tokens``,
there you will be able to generate a ``Consumer Key`` and a ``Consumer Secret``
as well as an ``Access Token`` and an ``Access Secret``.

The Twitter App will allow Pricebots to access and run your Pricebot's Twitter
account. The bot uses these API keys to Tweet the price automatically.

.. warning::
  Keep your API keys secret. If somebody has access to your keys
  they will be able to use your account. If you believe you may have
  compromised your API keys, you can regenerate them, but make sure that the
  keys you are giving to the bot are the same keys that you have regenerated.

Chrome or Chromium
--------------------
The Pricebot uses the browser to create the charts that it tweets. When
creating the charts the bot expects you to have Chrome installed on Windows, or
Chromium Browser installed on Linux. The Bot will not work if you are running
it on a Mac.

If you do not have Chrome installed then you will need it for running
Pricebots. And, you will need Chromium Browser if you are running the bot on
Linux.

Download Pricebots
--------------------
Now it is time to download Pricebots. You can download the latest release of
Pricebots `here <https://github.com/JordanDworaczyk/Pricebots/releases>`_

Install All Dependencies for running Pricebots
-------------------------------------------------------
You will need to install the following Python packages that Pricebot's depends
on for creating charts and tweeting to Twitter.

The following packages are:
  * Tweepy
  * Plotly
  * PyYAML
  * Requests

In order to install these packages you will need to use Python's package
manager ``pip``.

Open the Command Terminal and enter the following commands separately:
  * ``pip install tweepy``
  * ``pip install plotly``
  * ``pip install PyYAML``
  * ``pip install requests``

.. tip:: If you are having trouble installing using ``pip``, make sure that your
  PATH variables are set correctly.

Configure your Pricebot
-------------------------
After you have ``pip installed`` your dependencies, you are ready to configure
your Pricebot. Open the ``config.yml`` file found in your Pricebot package
using Notepad.

Inside your ``config.yml`` file you should see this::

  bot1:
    settings:
      1hour:
        status: 24hMarketTweet
        coins:
          - coin1
    api_keys:
      consumer_key: secret
      consumer_secret: secret
      access_key: secret
      access_secret: secret
    currencies:
      coin1:
        details:
          name: eth
          full_name: Ethereum
        candlesticks:
          duration: daily
          increasing_color: "#19cf86"
          decreasing_color: "#cf1962"
  bot2:
    settings:
      1hour:
        status: 24hMarketTweet
        coins:
          - coin1
    api_keys:
      consumer_key: secret
      consumer_secret: secret
      access_key: secret
      access_secret: secret
    currencies:
      coin1:
        details:
          name: btc
          full_name: Bitcoin
        candlesticks:
          duration: daily
          increasing_color: "#187ae7"
          decreasing_color: "#e78518"
  bot3:
    settings:
      1hour:
        status: 24hMarketTweet
        coins:
          - coin1
    api_keys:
      consumer_key: secret
      consumer_secret: secret
      access_key: secret
      access_secret: secret
    currencies:
      coin1:
        details:
          name: ltc
          full_name: Litecoin
        candlesticks:
          duration: daily
          increasing_color: "#5dbcd2"
          decreasing_color: "#d2735d"

You configure the settings for your bot by modifying this configuration
file. The Pricebot's software is able to run multiple instances of Twitter
bots, and can tweet daily and hourly charts. You can modify the colors of the
increasing and decreasing candles by changing the hexadecimal values. You will
replace the words ``secret`` with the corresponding API keys that you have
generated.

Here is an example of a Twitter bot that tweets four charts in one tweet. The
charts consist of a hourly Ethereum, daily Ethereum, hourly Bitcoin, and daily
Bitcoin charts::

  bot1:
    settings:
      1hour:
        status: 24hMarketTweet
        coins:
          - coin1
          - coin2
          - coin3
          - coin4
    api_keys:
      consumer_key: secret
      consumer_secret: secret
      access_key: secret
      access_secret: secret
    currencies:
      coin1:
        details:
          name: eth
          full_name: Ethereum
        candlesticks:
          duration: daily
          increasing_color: "#19cf86"
          decreasing_color: "#cf1962"
      coin2:
        details:
          name: btc
          full_name: Bitcoin
        candlesticks:
          duration: hourly
          increasing_color: "#187ae7"
          decreasing_color: "#e78518"
      coin3:
        details:
          name: eth
          full_name: Ethereum
        candlesticks:
          duration: hourly
          increasing_color: "#19cf86"
          decreasing_color: "#cf1962"
      coin4:
        details:
          name: btc
          full_name: Bitcoin
        candlesticks:
          duration: daily
          increasing_color: "#187ae7"
          decreasing_color: "#e78518"

.. note:: Since Pricebots only has support for cryptowat.ch's API, it is only
  able to tweet cryptocurrencies that are on cryptowat.ch. See the available
  coins that you can tweet `here <https://cryptowat.ch/>`_.

Run your Pricebot
-------------------
Finally, you will be able to run your bot.

Open the Command Terminal and ``cd`` to your Pricebot package.

Run the following command: ``python main.py run now``

This command will immediately run your Pricebot and keep tweeting constantly
about every minute. This is for testing to see if you configured your Pricebot
correctly. If your bot fails to run, then please submit an issue with the error
message `here <https://github.com/JordanDworaczyk/Pricebots/issues>`_.

Otherwise, if everything looks good, then use this command to run your bot to
tweet on the hour every hour: ``python main.py run hourly``

If everything went right you should see your tweets on twitter at the
start of every hour.

.. note:: Pricebots uses the browser to create charts. Every time that a chart
  is tweeted a tab is opened and the chart gets made inside of that tab.
  So, Pricebots terminates the browser session 30min after every
  tweet in order to prevent an infinite amount of tabs from being opened. This
  will cause your chrome or chromium browser to close itself automatically.
  Therefore, it is advised that you run Pricebots on a machine that you do not
  use often, or that you do your browsing on a separate browser that is not
  Chrome or Chromium.

.. centered:: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
  EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
  OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
  DEALINGS IN THE SOFTWARE.
