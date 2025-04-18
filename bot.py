from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import telegram.error

TOKEN = 'YOUR_BOT_TOKEN'  # BotFather ကနေ ရထားတဲ့ token ကို ဒီမှာ ထည့်ပါ

async def delete_message(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    chat_id = job.data['chat_id']
    message_id = job.data['message_id']
    print(f"Attempting to delete message: chat_id={chat_id}, message_id={message_id}")
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        print(f"Message deleted successfully: chat_id={chat_id}, message_id={message_id}")
    except telegram.error.TelegramError as e:
        print(f"Delete Error: {e}, chat_id={chat_id}, message_id={message_id}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        print("No message found in start command")
        return
    try:
        message = await update.message.reply_text(
            'ကျေးဇူးပြုပြီး အောက်က command တွေကို သုံးပါ:\n'
            '/node - Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်\n'
            '/script - Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်'
        )
        print(f"Scheduling deletion for message: chat_id={update.message.chat_id}, message_id={message.message_id}")
        context.job_queue.run_once(
            delete_message,
            30,
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Start Error: {e}")

async def node(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        print("No message found in node command")
        return
    keyboard = [
        [InlineKeyboardButton("✅ NODE Eclipse", url='https://t.me/c/2309219455/9/30346')],
        [InlineKeyboardButton("✅ NODE Dria", url='https://t.me/c/2309219455/9/17013')],
        [InlineKeyboardButton("✅ NODE Gaianet", url='https://t.me/c/2309219455/9/4780')],
        [InlineKeyboardButton("✅ NODE T3rn", url='https://t.me/c/2309219455/9/16160')],
        [InlineKeyboardButton("✅ NODE Danom", url='https://t.me/c/2309219455/9/14178')],
        [InlineKeyboardButton("✅ NODE Dill", url='https://t.me/c/2309219455/9/12163')],
        [InlineKeyboardButton("✅ NODE 0glabs", url='https://t.me/c/2309219455/9/9152')],
        [InlineKeyboardButton("✅ NODE Ink", url='https://t.me/c/2309219455/9/2368')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update.message.reply_text('Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
        print(f"Scheduling deletion for message: chat_id={update.message.chat_id}, message_id={message.message_id}")
        context.job_queue.run_once(
            delete_message,
            30,  # 30 စက္ကန့်အဖြစ် ပြောင်းလဲ
            data={'chat_id': update.message.chat_id, 'message_id': message.message_id}
        )
    except telegram.error.BadRequest as e:
        print(f"Node Error: {e}")

async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        print("No message found in script command")
        return
    keyboard = [
        [InlineKeyboardButton("📜 Script Anime", url='https://t.me/c/2309219455/43/32714')],
        [InlineKeyboardButton("📜 Script 3dos", url='https://t.me/c/2309219455/43/25616')],
        [InlineKeyboardButton("📜 Script Prior Testnet", url='https://t.me/c/2309219455/43/25405')],
        [InlineKeyboardButton("📜 Script openledger", url='https://t.me/c/2309219455/43/24282')],
        [InlineKeyboardButton("📜 Script Blockscout", url='https://t.me/c/2309219455/43/20603')],
        [InlineKeyboardButton("📜 Script Parasail", url='https://t.me/c/2309219455/43/20225')],
        [InlineKeyboardButton("📜 Script Billion", url='https://t.me/c/2309219455/43/19955')],
        [InlineKeyboardButton("📜 Script Coresky", url='https://t.me/c/2309219455/43/19892')],
        [InlineKeyboardButton("📜 Script InkGM", url='https://t.me/c/2309219455/43/19785')],
        [InlineKeyboardButton("📜 Script Voltix", url='https://t.me/c/2309219455/43/19216')],
        [InlineKeyboardButton("📜 Script Oogies", url='https://t.me/c/2309219455/43/18482')],
        [InlineKeyboardButton("📜 Script Dawn", url='https://t.me/c/2309219455/43/18365')],
        [InlineKeyboardButton("📜 Script Magic Newton", url='https://t.me/c/2309219455/43/16179')],
        [InlineKeyboardButton("📜 Script 0glabs Auto Swap", url='https://t.me/c/2309219455/43/16116')],
        [InlineKeyboardButton("📜 Script Hipin", url='https://t.me/c/2309219455/43/15328')],
        [InlineKeyboardButton("📜 Script Despeed", url='https://t.me/c/2309219455/43/26159')],
        [InlineKeyboardButton("📜 Script XOX", url='https://t.me/c/2309219455/43/14140')],
        [InlineKeyboardButton("📜 Script Teneo", url='https://t.me/c/2309219455/43/14021')],
        [InlineKeyboardButton("📜 Script Arichain", url='https://t.me/c/2309219455/43/13244')],
        [InlineKeyboardButton("📜 Script Stork", url='https://t.me/c/2309219455/43/12769')],
        [InlineKeyboardButton("📜 Script OpenSci", url='https://t.me/c/2309219455/43/12381')],
        [InlineKeyboardButton("📜 Script MinionLab", url='https://t.me/c/2309219455/43/11864')],
        [InlineKeyboardButton("📜 Script InfinityGround", url='https://t.me/c/2309219455/43/11774')],
        [InlineKeyboardButton("📜 Script HanaNetwork", url='https://t.me/c/2309219455/43/9586')],
        [InlineKeyboardButton("📜 Script HAHA Wallet", url='https://t.me/c/2309219455/43/9454')],
        [InlineKeyboardButton("📜 Script MultipleNetwork", url='https://t.me/c/2309219455/43/9231')],
        [InlineKeyboardButton("📜 Script NodeGo", url='https://t.me/c/2309219455/43/8044')],
        [InlineKeyboardButton("📜 Script GoKiteAI", url='https://t.me/c/2309219455/43/13565')],
        [InlineKeyboardButton("📜 Script Naoris Protocol", url='https://t.me/c/2309219455/43/6242')],
        [InlineKeyboardButton("📜 Script Kaleido", url='https://t.me/c/2309219455/43/5903')],
        [InlineKeyboardButton("📜 Script Taker", url='https://t.me/c/2309219455/43/4369')],
        [InlineKeyboardButton("📜 Script MyGate", url='https://t.me/c/2309219455/43/4075')],
        [InlineKeyboardButton("📜 Script Openloop", url='https://t.me/c/2309219455/43/3633')],
        [InlineKeyboardButton("📜 Script GAEA", url='https://t.me/c/2309219455/43/2987')],
        [InlineKeyboardButton("📜 Script Kaisar", url='https://t.me/c/2309219455/43/2970')],
        [InlineKeyboardButton("📜 Script Titan", url='https://t.me/c/2309219455/43/2765')],
        [InlineKeyboardButton("📜 Script Depined", url='https://t.me/c/2309219455/43/2612')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        message = await update
