from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import telegram.error

TOKEN = 'YOUR_BOT_TOKEN'  # BotFather ကနေ ရထားတဲ့ token ကို ဒီမှာ ထည့်ပါ

async def delete_message(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    chat_id = job.data['chat_id']
    message_id = job.data['message_id']
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except telegram.error.TelegramError as e:
        print(f"Delete Error: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    try:
        message = await update.message.reply_text(
            'ကျေးဇူးပြုပြီး အောက်က command တွေကို သုံးပါ:\n'
            '/daily - 📅 Daily Check-in လုပ်ရန်\n'
            '/node - 💻 Node အချက်အလက်များ\n'
            '/script - 📜 Script အချက်အလက်များ\n'
            '/testnet - 🌐 Testnet အချက်အလက်များ'
        )
        context.job_queue.run_once(
            delete_message,
            15,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Start Error: {e}")

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("📅 Check-in Pixy Farcaster", url='https://t.me/c/2309219455/115523/307585')],
        [InlineKeyboardButton("📅 Check-in Superintent", url='https://t.me/c/2309219455/115523/304648')],
        [InlineKeyboardButton("📅 Check-in Hodlher", url='https://t.me/c/2309219455/115523/302915')],
        [InlineKeyboardButton("📅 Check-in Humanoid", url='https://t.me/c/2309219455/115523/300945')],
        [InlineKeyboardButton("📅 Check-in TREX", url='https://t.me/c/2309219455/115523/195454')],
        [InlineKeyboardButton("📅 Check-in Providence", url='https://t.me/c/2309219455/33901/200301')],
        [InlineKeyboardButton("📅 Check-in Allscale", url='https://t.me/c/2309219455/115523/308644')],
        [InlineKeyboardButton("📅 Check-in Psychonaut", url='https://t.me/c/2309219455/115523/210873')],
        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update.message.reply_text('📅 နေ့စဉ် Check-in လုပ်ရန် လင့်ခ်များ:', reply_markup=reply_markup)
        context.job_queue.run_once(
            delete_message,
            30,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Daily Error: {e}")

async def node(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("✅ NODE Nexus", url='https://t.me/c/2309219455/2862/200500')],
        [InlineKeyboardButton("✅ NODE Titan", url='https://t.me/c/2309219455/2862/150612')],
        [InlineKeyboardButton("✅ NODE Namso", url='https://t.me/c/2309219455/2862/135774')],
        [InlineKeyboardButton("✅ NODE Siexpence", url='https://t.me/c/2309219455/2862/113509')],
        [InlineKeyboardButton("✅ NODE Interlink", url='https://t.me/c/2309219455/2862/75993')],
        [InlineKeyboardButton("✅ NODE IDOS", url='https://t.me/c/2309219455/43/203455')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update.message.reply_text('Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
        context.job_queue.run_once(
            delete_message,
            25,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Node Error: {e}")

async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("📜 Script ARCfaucet", url='https://t.me/c/2309219455/43/311168')],
        [InlineKeyboardButton("📜 Script polarisfaucet", url='https://t.me/c/2309219455/43/310390')],
        [InlineKeyboardButton("📜 Script polaris", url='https://t.me/c/2309219455/43/310393')],
        [InlineKeyboardButton("📜 Script Humanoid", url='https://t.me/c/2309219455/43/300946')],
        [InlineKeyboardButton("📜 Script Wallet Drainer Script", url='https://t.me/c/2309219455/43/298934')],
        [InlineKeyboardButton("📜 Script X1", url='https://t.me/c/2309219455/43/298724')],
        [InlineKeyboardButton("📜 Script Psychonaut", url='https://t.me/c/2309219455/43/214805')],
        [InlineKeyboardButton("📜 Script IDOS", url='https://t.me/c/2309219455/43/203455')],
        [InlineKeyboardButton("📜 Script Dawn", url='https://t.me/c/2309219455/43/18365')],
        [InlineKeyboardButton("📜 Script Titan", url='https://t.me/c/2309219455/43/152040')],
        [InlineKeyboardButton("📜 Script Sixpence", url='https://t.me/c/2309219455/43/113510')],
        [InlineKeyboardButton("📜 Script Tunkey", url='https://t.me/c/2309219455/43/93850')],
        [InlineKeyboardButton("📜 Script Interlink", url='https://t.me/c/2309219455/43/76403')],
        [InlineKeyboardButton("📜 Script Teneo", url='https://t.me/c/2309219455/43/14021')],
        [InlineKeyboardButton("📜 Script Stork", url='https://t.me/c/2309219455/43/12769')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update.message.reply_text('Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
        context.job_queue.run_once(
            delete_message,
            25,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Script Error: {e}")

async def testnet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("🌐 Testnet ARC", url='https://t.me/c/2309219455/25180/311021')],
        [InlineKeyboardButton("🌐 Testnet Hotstuff", url='https://t.me/c/2309219455/25180/308522')],
        [InlineKeyboardButton("🌐 Testnet Polaris", url='https://t.me/c/2309219455/25180/307484')],
        [InlineKeyboardButton("🌐 Testnet X1Ecochain", url='https://t.me/c/2309219455/25180/298723')],
        [InlineKeyboardButton("🌐 Testnet Syntetika", url='https://t.me/c/2309219455/25180/165558')],
        [InlineKeyboardButton("🌐 Testnet Tunkey", url='https://t.me/c/2309219455/25180/93849')],
        [InlineKeyboardButton("🌐 Testnet Pharos", url='https://t.me/c/2309219455/25180/60397')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update.message.reply_text('Testnet နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
        context.job_queue.run_once(
            delete_message,
            25,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Testnet Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("daily", daily)) # Daily Check-in အတွက်
    app.add_handler(CommandHandler("node", node))
    app.add_handler(CommandHandler("script", script))
    app.add_handler(CommandHandler("testnet", testnet))
    
    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == '__main__':
    main()
