# PYCNet Mailbox Scraper
A webscraper project I did within two days for fun, tested on a fellow friend's school website.

### Requirements

- Python 3 ([Download Here (Windows)](https://www.python.org/downloads/))
- Selenium Python ([Download Guide](https://selenium-python.readthedocs.io/installation.html))
- Chrome WebDriver ([Downloads](https://chromedriver.chromium.org/downloads/version-selection))

  [Minor Note: It is possible to use other browser drivers, however I myself have not tested whether it would work as well as it does with Google Chrome, so do your research :)]

### Description & Notes

The main thing this scraper *should* do is:
1. Login for you
2. Fetch the first page of your Inbox
3. Relay it back to you and save the data into a .txt file.

Unfortune-fucking-ly, there's some issues with this 6-hour project:

1. The relay isn't formatted, it doesn't really matter, but its a gripe I have
2. Chinese characters are displayed as unknown characters, this is due to the codec encoding, but I haven't found a workaround that would allow me to display these characters in the command window without triggering another error.
3. Only saves the data of the last mail on the page into the .txt file

While I will work to resolve these problems, I am still learning my way around these controls, so do expect the fix to be veeeeerrrryyyy far into the future. At large, the scraper will work.

Plus this project is really just something to keep my Python skills kicking (aka, having too much fun and not writing or drawing) , so ignore the shitty barf code, and if you wish, feel free to improve on it :D
