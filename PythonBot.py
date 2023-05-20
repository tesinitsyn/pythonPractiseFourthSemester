import praw
import telebot

# Reddit API credentials
reddit_client_id = 'qpGWB5-xcmXI9_wybBp5Og'
reddit_client_secret = 'pR4GjgQ4cvF5YV1UTaKWvZNMHWN4Aw'
reddit_username = 't1mmm7'
reddit_password = 'sinitsyn021224'

# Telegram bot token
telegram_token = '6056997727:AAFDWHzzSmRs30UlrhaxV6LiGlNckusNfFs'

# Subreddit to fetch hot topics from
subreddit_name = ''

# Initialize Reddit API
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     username=reddit_username,
                     password=reddit_password,
                     user_agent='TelegramBot')

# Initialize Telegram bot
bot = telebot.TeleBot(token=telegram_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Send a welcome message when the /start command is issued."""
    bot.reply_to(message, 'Hi! I will send you the hottest topics from /r/{}.'.format(subreddit_name))


@bot.message_handler(commands=['s'])
def get_subreddit(message):
    global subreddit_name
    subreddit_name = message.text[3:]
    bot.reply_to(message, subreddit_name)




@bot.message_handler(commands=['hot_topics'])
def send_hot_topics(message):
    """Fetch and send the hottest topics from the specified subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    hot_posts = subreddit.new(limit=5)
    for post in hot_posts:
        message_text = '{}\n{}\n{}'.format(post.title, post.url, post.score)
        bot.send_message(chat_id=message.chat.id, text=message_text)


# Start the bot
bot.polling()
