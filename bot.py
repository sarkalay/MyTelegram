from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes
import telegram.error

TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    try:
        await update.message.reply_text(
            'ကျေးဇူးပြုပြီး အောက်က command တွေကို သုံးပါ:\n'
            '/node - Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်\n'
            '/script - Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်'
        )
    except telegram.error.BadRequest as e:
        print(f"Start Error: {e}")

async def node(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("âœ… NODE Dria", url='https://t.me/airdropbombnode/9/17013')],
        [InlineKeyboardButton("âœ… NODE Gaianet", url='https://t.me/airdropbombnode/9/4780')],
        [InlineKeyboardButton("âœ… NODE T3rn", url='https://t.me/airdropbombnode/9/16160')],
        [InlineKeyboardButton("âœ… NODE Danom", url='https://t.me/airdropbombnode/9/14178')],
        [InlineKeyboardButton("âœ… NODE Dill", url='https://t.me/airdropbombnode/9/12163')],
        [InlineKeyboardButton("âœ… NODE 0glabs", url='https://t.me/airdropbombnode/9/9152')],
        [InlineKeyboardButton("âœ… NODE Ink", url='https://t.me/airdropbombnode/9/2368')],
        [InlineKeyboardButton("âœ… NODE PipeNetwork", url='https://t.me/airdropbombnode/43/9324')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await update.message.reply_text('Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
    except telegram.error.BadRequest as e:
        print(f"Node Error: {e}")

# /script command အတွက် function
async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return
    keyboard = [
        [InlineKeyboardButton("ðŸ“œ Script Blockscout", url='https://t.me/airdropbombnode/43/20603')],
        [InlineKeyboardButton("ðŸ“œ Script Parasail", url='https://t.me/airdropbombnode/43/20225')],
        [InlineKeyboardButton("ðŸ“œ Script Billion", url='https://t.me/airdropbombnode/43/19955')],
        [InlineKeyboardButton("ðŸ“œ Script Coresky", url='https://t.me/airdropbombnode/43/19892')],
        [InlineKeyboardButton("ðŸ“œ Script InkGM", url='https://t.me/airdropbombnode/43/19785')],
        [InlineKeyboardButton("ðŸ“œ Script Voltix", url='https://t.me/airdropbombnode/43/19216')],
        [InlineKeyboardButton("ðŸ“œ Script Oogies", url='https://t.me/airdropbombnode/43/18482')],
        [InlineKeyboardButton("ðŸ“œ Script Dawn", url='https://t.me/airdropbombnode/43/18365')],
        [InlineKeyboardButton("ðŸ“œ Script Beamable Quest", url='https://t.me/airdropbombnode/43/17632')],
        [InlineKeyboardButton("ðŸ“œ Script Beamable Daily", url='https://t.me/airdropbombnode/43/15814')],
        [InlineKeyboardButton("ðŸ“œ Script Flow3 Daily", url='https://t.me/airdropbombnode/43/16702')],
        [InlineKeyboardButton("ðŸ“œ Script Flow3 Auto Ref", url='https://t.me/airdropbombnode/43/17004')],
        [InlineKeyboardButton("ðŸ“œ Script Magic Newton", url='https://t.me/airdropbombnode/43/16179')],
        [InlineKeyboardButton("ðŸ“œ Script 0glabs Auto Swap", url='https://t.me/airdropbombnode/43/16116')],
        [InlineKeyboardButton("ðŸ“œ Script Hipin", url='https://t.me/airdropbombnode/43/15328')],
        [InlineKeyboardButton("ðŸ“œ Script Despeed", url='https://t.me/airdropbombnode/43/14321')],
        [InlineKeyboardButton("ðŸ“œ Script XOX", url='https://t.me/airdropbombnode/43/14140')],
        [InlineKeyboardButton("ðŸ“œ Script Teneo", url='https://t.me/airdropbombnode/43/14021')],
        [InlineKeyboardButton("ðŸ“œ Script Arichain", url='https://t.me/airdropbombnode/43/13244')],
        [InlineKeyboardButton("ðŸ“œ Script Bless", url='https://t.me/airdropbombnode/43/13207')],
        [InlineKeyboardButton("ðŸ“œ Script Stork", url='https://t.me/airdropbombnode/43/12769')],
        [InlineKeyboardButton("ðŸ“œ Script OpenSci", url='https://t.me/airdropbombnode/43/12381')],
        [InlineKeyboardButton("ðŸ“œ Script MinionLab", url='https://t.me/airdropbombnode/43/11864')],
        [InlineKeyboardButton("ðŸ“œ Script InfinityGround", url='https://t.me/airdropbombnode/43/11774')],
        [InlineKeyboardButton("ðŸ“œ Script HanaNetwork", url='https://t.me/airdropbombnode/43/9586')],
        [InlineKeyboardButton("ðŸ“œ Script HAHA Wallet", url='https://t.me/airdropbombnode/43/9454')],
        [InlineKeyboardButton("ðŸ“œ Script MultipleNetwork", url='https://t.me/airdropbombnode/43/9231')],
        [InlineKeyboardButton("ðŸ“œ Script NodeGo", url='https://t.me/airdropbombnode/43/8044')],
        [InlineKeyboardButton("ðŸ“œ Script GoKiteAI", url='https://t.me/airdropbombnode/43/6850')],
        [InlineKeyboardButton("ðŸ“œ Script Naoris Protocol", url='https://t.me/airdropbombnode/43/6242')],
        [InlineKeyboardButton("ðŸ“œ Script Kaleido", url='https://t.me/airdropbombnode/43/5903')],
        [InlineKeyboardButton("ðŸ“œ Script Taker", url='https://t.me/airdropbombnode/43/4369')],
        [InlineKeyboardButton("ðŸ“œ Script MyGate", url='https://t.me/airdropbombnode/43/4075?single')],
        [InlineKeyboardButton("ðŸ“œ Script Openloop", url='https://t.me/airdropbombnode/43/3633')],
        [InlineKeyboardButton("ðŸ“œ Script GAEA", url='https://t.me/airdropbombnode/43/2987')],
        [InlineKeyboardButton("ðŸ“œ Script Kaisar", url='https://t.me/airdropbombnode/43/2970')],
        [InlineKeyboardButton("ðŸ“œ Script Titan", url='https://t.me/airdropbombnode/43/2765')],
        [InlineKeyboardButton("ðŸ“œ Script Depined", url='https://t.me/airdropbombnode/43/2612')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await update.message.reply_text('Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)
    except telegram.error.BadRequest as e:
        print(f"Script Error: {e}")
# Main function မှာ command handler တွေ ထည့်ပေးပါ
def main():
    app = Application.builder().token(TOKEN).build()

    # Command handler တွေ ထည့်ပါ
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("node", node))
    app.add_handler(CommandHandler("script", script))

    # Bot ကို စတင်ပါ
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == '__main__':
    main()
