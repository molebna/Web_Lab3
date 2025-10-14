from groq import Groq
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKENTG = "8375222529:AAHiWfibtBqjW7vc9qdPnmLGeHwrKxHOhEM"
TOKENGPT = "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"

chatbot = Groq(api_key=TOKENGPT)

menu_buttons = [
    [KeyboardButton("Student")],
    [KeyboardButton("IT-technologies")],
    [KeyboardButton("Contacts")],
    [KeyboardButton("Chat GPT")]
]
reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)

isAIChosen = 0

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Обери команду з меню",
        reply_markup=reply_markup
    )

async def chatgpt_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    if user_message == None:
        return

    global isAIChosen

    if user_message == "Student":
        await update.message.reply_text("Molebna Maria IP-24")
        isAIChosen = 0
    elif user_message == "IT-technologies":
        await update.message.reply_text("Web technologies")
        isAIChosen = 0
    elif user_message == "Contacts":
        await update.message.reply_text("molebna.maria@lll.kpi.ua")
        isAIChosen = 0
    elif user_message == "Chat GPT":
        await update.message.reply_text("You chose an AI assistant. Please write your prompt")
        isAIChosen = 1
    elif isAIChosen == 1:
        chat_completion = chatbot.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "Ти саркастичний асистент, який відповідає різко, але не образливо. В кожному повідомленні називай співрозмовника лагідним словом Зіще"},
                {"role": "user", "content": user_message},
            ]
        )

        reply = chat_completion.choices[0].message.content
        await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKENTG).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply))

print("Bot started...")
app.run_polling()
