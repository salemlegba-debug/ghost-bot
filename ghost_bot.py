import asyncio
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "8522204841:AAHp1ViSssIus6dti0KUClpj4yFABuoSFGQ"
CODE_PROMO = "SXM229"
LINK = "https://1w.run/?p=gByP"

# -------- SIGNAL GENERATOR --------
def generate_signal():
    target = round(random.uniform(3.00, 10.00), 2)
    safe = round(target * 0.45, 2)
    return target, safe

# -------- START --------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 SIGNAL", callback_data="signal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👻 GHOST SIGNAL BOT\n\n"
        "Clique sur 🚀 SIGNAL pour recevoir une prédiction.",
        reply_markup=reply_markup
    )

# -------- SIGNAL BUTTON --------
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    msg = await query.edit_message_text("🔍 Connexion au serveur...")
    await asyncio.sleep(0.4)

    await msg.edit_text("🎰 Analyse des données...")
    await asyncio.sleep(0.4)

    await msg.edit_text("🎯 Détection opportunité...")
    await asyncio.sleep(0.4)

    target, safe = generate_signal()

    await msg.edit_message_text(
        f"🚀 PRÉDICTION META CRASH\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📈 OBJECTIF : {target}X\n"
        f"🛡 SÉCURITÉ : {safe}X\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🎁 CODE PROMO : {CODE_PROMO}\n"
        f"🔗 {LINK}"
    )

# -------- MAIN --------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(signal, pattern="signal"))

    print("Bot lancé")
    app.run_polling()

if __name__ == "__main__":
    main()
