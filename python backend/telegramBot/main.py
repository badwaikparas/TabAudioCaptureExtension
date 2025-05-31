from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7755884178:AAGPX3w-l4Dc-iK-oawEw3-pErWXUpmrApc'
BOT_USERNAME = 'tested_13Bot'

# Commmands
async def start_command(update, context):
    await update.message.reply_text('Hello! Thanks for chatting with me ! I am a Banana')
async def help_command(update, context):
    await update.message.reply_text('I am a Banana please type something so i can respond')
async def custom_command(update, context):
    await update.message.reply_text('this is a custom command')
    
# Handle responses

def handle_response(text):
    processed = text.lower()
    
    if 'hello' in processed:
        return 'Hey There!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'i love python' in processed:
        return 'I love it too!'
    
    return 'I dont unserstand what you wrote...'

async def handle_message(update, context):
    message_type = update.message.chat.type
    text = update.message.text
    
    print(f'User ({update.message.chat.id}) in  {message_type}: "{text}"')
    
    # response only when bot is tagged
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME,"").strip()
            response = handle_response(new_text)
            
        else:
            return 
        
    else:
        response = handle_response(text)
        
    print("Bot: ", response)
    await update.message.reply_text(response)
    
async def error(update, context):
    print(f'Update {update} caused error {context.error}')
    
    
    
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Errors
    app.add_error_handler(error)
    
    #polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)