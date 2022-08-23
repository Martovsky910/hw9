from time import time
from pytube import YouTube
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *


async def DLlowest_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    url = msg
    print(url)
    getVideo = YouTube(url)
    getVideo.streams.get_lowest_resolution().download('D:\GeekBrains\Python') #.get_lowest_resolution().download('D:\GeekBrains\Python')
    print('Видео в низком качестве успешно скачалось')
    await update.message.reply_text('Видео в низком качестве успешно скачалось')


async def DLhighest_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    url = msg
    print(url)
    getVideo = YouTube(url)
    getVideo.streams.get_highest_resolution().download('D:\GeekBrains\Python') #.filter(progressive=True, file_extension='mp4')
    print('Видео в высоком качестве успешно скачалось')
    await update.message.reply_text('Видео в высоком качестве успешно скачалось')


async def DL_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    url = msg
    print(url)
    getAudio = YouTube(url)
    getAudio.streams.get_audio_only().download(output_path='D:\GeekBrains\Python', filename='audio.mp3')
    print('Аудио успешно скачалось')
    await update.message.reply_text('Аудио успешно скачалось')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    log(Update,context)
    await update.message.reply_text(f'hi {update.effective_user.first_name}') 


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(Update,context)
    await update.message.reply_text(f'/hi\n/time\n/dl_low\n/dl_hight\n/dl_audio\n/help')