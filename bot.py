from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# သင့်ရဲ့ Bot Token ကို ဒီနေရာမှာ ထည့်ပါ
TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
    await update.message.reply_text('ကျေးဇူးပြုပြီး သင်လိုချင်တဲ့ node ကို ရွေးပါ:', reply_markup=reply_markup)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
