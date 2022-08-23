from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("dl_low", DLlowest_video))
app.add_handler(CommandHandler("dl_hight", DLhighest_video))
app.add_handler(CommandHandler("dl_audio", DL_audio))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))

print('server start')

app.run_polling()