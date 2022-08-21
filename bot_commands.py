from time import time
from pytube import YouTube
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


# def add(name):
#     name - name.get()
#     DLlowpres_video()

async def DLlowpres_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(Update, context)
    msg = update.message.text
    url = msg
    print(url)
    getVideo = YouTube(url)
    getVideo.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution().download('D:\GeekBrains\Python')
    print('Видео в низком качестве успешно скачалось')
    await update.message.reply_text('Видео в низком качестве успешно скачалось')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    log(Update,context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}') 

def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    log(Update,context)
    update.message.reply_text(f'time {datetime.datetime.now().time()}')

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(Update,context)
    update.message.reply_text(f'/hi\n/time\n/help')


