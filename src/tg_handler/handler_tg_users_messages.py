import logging
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler, Updater
from config_files import Settings
from uuid import uuid4
from NASA_api_handler import handler_NASA_API
from datetime import time, datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "This is a 'Don't Look Up' bot.\nWe provide you with interesting NASA updates.\nYou can choose theme and the time of the day you wish to get the news"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Use the job queue for the scheduled messages for user
# this function looks fine for this
#run_daily(callback, time, days=(0, 1, 2, 3, 4, 5, 6), data=None, 
# name=None, chat_id=None, user_id=None, job_kwargs=None)[source]
# use new command with conext.args for getting time from the user
# DOCUMENTATION:
# https://docs.python-telegram-bot.org/en/stable/telegram.ext.jobqueue.html

# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
async def pod(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    message_data = handler_NASA_API.get_nasa_data()
    title = message_data['title']
    explanation = message_data['description']
    image = message_data['image']
    message = f"Today we will talk about {title}."
    await context.bot.send_message(job.chat_id, text=f"{message} \n {explanation} \n {image}")


def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def set_time_pod(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id
    try:
        # Parse the time input in HH:MM format
        time_str = context.args[0]
        hour, minute = map(int, time_str.split(':'))
        due = datetime.combine(datetime.now().date(), time(hour=hour, minute=minute))
        print(due)

        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_daily(pod, due, days=(0, 1, 2, 3, 4, 5, 6), chat_id=chat_id, name=str(chat_id), data=due)

        text = "Time for receiving the news is set."
        if job_removed:
            text += " Old one was removed."
        await update.effective_message.reply_text(text)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Usage: /set_time_pod <seconds>")


async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Receiving news for that time is cancelled!" if job_removed else "You have no active time news."
    await update.message.reply_text(text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def pod_inline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    message_data = handler_NASA_API.get_nasa_data()
    title = message_data['title']
    explanation = message_data['description']
    image = message_data['image']
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=title,
            input_message_content=InputTextMessageContent(f"{explanation} - {image}")
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


def main():
    application = ApplicationBuilder().token(Settings.TOKENkey).build()
    
    start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    POD_handler = InlineQueryHandler(pod_inline)

    application.add_handler(start_handler)
    # application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(POD_handler)
    application.add_handler(CommandHandler("set", set_time_pod))
    application.add_handler(CommandHandler("unset", unset))

    application.run_polling()


if __name__ == '__main__':
    main()