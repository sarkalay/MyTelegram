from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# သင့်ရဲ့ Bot Token ကို ဒီနေရာမှာ ထည့်ပါ
TOKEN = 'YOUR_BOT_TOKEN'

# /start command အတွက် function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'ကျေးဇူးပြုပြီး အောက်က command တွေကို သုံးပါ:\n'
        '/node - Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်\n'
        '/script - Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်တွေ ကြည့်ရန်'
    )

# /node command အတွက် function
async def node(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ NODE MULTIPLE NETWORK", url='https://example.com/node-multiple-network')],
        [InlineKeyboardButton("✅ NODE SPHERON NETWORK FIZZ", url='https://example.com/spheron-network-fizz')],
        [InlineKeyboardButton("✅ NODE VOLARA MAINNET", url='https://example.com/volara-mainnet')],
        [InlineKeyboardButton("✅ NODE IntiVerse (INI Chain)", url='https://example.com/intiverse')],
        [InlineKeyboardButton("✅ NODE ATLAS NETWORK", url='https://example.com/atlas-network')],
        [InlineKeyboardButton("✅ NODE MULTIPLE **MultiGrow Testnet**", url='https://example.com/multigrow-testnet')],
        [InlineKeyboardButton("✅ NODE - OPEN LEDGER", url='https://example.com/open-ledger')],
        [InlineKeyboardButton("✅ NODE MULTIPLE NETWORK | CHROME EXTENSION", url='https://example.com/multiple-network-chrome')],
        [InlineKeyboardButton("✅ NODE TITAN NETWORK - CASSINI TESTNET", url='https://example.com/titan-network')],
        [InlineKeyboardButton("✅ NODE - GAIANET", url='https://example.com/gainet')],
        [InlineKeyboardButton("✅ NODE - PRIVASEA", url='https://example.com/privasea')],
        [InlineKeyboardButton("✅ NODE - zkVerify TUTORIAL", url='https://example.com/zkverify')],
        [InlineKeyboardButton("✅ NODE - NodeGo (DePIN)", url='https://example.com/nodego')],
        [InlineKeyboardButton("✅ NODE - OG LABS", url='https://example.com/og-labs')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Node နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)

# /script command အတွက် function
async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📜 Script 1: Basic Automation", url='https://example.com/script1')],
        [InlineKeyboardButton("📜 Script 2: Advanced Bot Script", url='https://example.com/script2')],
        [InlineKeyboardButton("📜 Script 3: Data Scraping", url='https://example.com/script3')],
        [InlineKeyboardButton("📜 Script 4: API Integration", url='https://example.com/script4')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Script နဲ့ ပတ်သက်တဲ့ အချက်အလက်များ:', reply_markup=reply_markup)

# Main function မှာ command handler တွေ ထည့်ပေးပါ
def main():
    app = Application.builder().token(TOKEN).build()

    # Command handler တွေ ထည့်ပါ
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("node", node))
    app.add_handler(CommandHandler("script", script))

    # Bot ကို စတင်ပါ
    app.run_polling()

if __name__ == '__main__':
    main()
