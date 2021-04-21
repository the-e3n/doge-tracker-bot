# DOGE-tracker-telegram-bot
Basic DOGE CryptoCurrency Price tracker/alarm, checks the price of api at a specific interval, defined by update interval.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic DOGE CryptoCurrency Price tracker/alarm, checks the price of api at a specific interval, defined by update interval.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.

# Sample Bot
On Telegram
@doge_tracker_bot // Please Unset after a testing time to avoid rate limiting

# Usage
1. Send `/start` to start the bot.
2. Send `/set <price>` to set an alert based on price.
3. Send `/unset` to remove alert.
4. Send `/help` to get help.
