from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5780455225:AAFPoFkl0R9mjm91VweO7cZziVtL3QcUcZE").build()

app.add_handler(CommandHandler("hi", DLlowpres_video))
# app.add_handler(CommandHandler("time", time_command))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(CommandHandler("sum", sum_command))

print('server start')

app.run_polling()