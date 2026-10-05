import yt_dlp
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

 بدل هاد التوكن بالتوكن ديالك
   TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐒 مرحبا بيك فبوت قردوش 99\n\n"
        "📥 صيفط ليا رابط ديال:\n"
        "- TikTok\n- Instagram\n- Facebook\n\n"
        "ونجيب ليك الفيديو بلا علامة مائية 💧"
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    # تشيك واش رابط
    if "tiktok.com" not in url and "instagram.com" not in url and "facebook.com" not in url and "fb.watch" not in url and "youtu.be" not in url and "youtube.com" not in url:
        return

    status_msg = await update.message.reply_text("⏳ كنهبط ليك الفيديو، تسنا ثواني...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'qird99_video.%(ext)s',
        'quiet': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        for file in os.listdir('.'):
            if file.startswith('qird99_video.'):
                await update.message.reply_video(
                    video=open(file, 'rb'),
                    caption="✅ ها هو الفيديو بلا علامة مائية\n🤖 @qirs99_bot"
                )
                os.remove(file)
                await status_msg.delete()
                return

    except Exception as e:
        await status_msg.edit_text(f"❌ مقدرتش نهبطو، جرب رابط آخر\n{e}")

# تشغيل البوت
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))

print("البوت خدام...")
app.run_polling()
