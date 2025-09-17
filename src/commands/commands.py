import logging
from html import escape
from uuid import uuid4
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from src.db.database import db, User
from src.db.utils import create_interaction, create_user, user_exists
from src.utils.utils import generateGaussianDistribution, transformRandomValueResult, getRandomEmoji, names_array, emojis

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /start is issued."""
    
  chat_id = update.message.chat_id
  
  return await context.bot.send_message(
    text="Чтобы использовать бота, тэгните его, когда набираете сообщение. После нажатия на появившееся окно, бот выполнит команду указанную там.",
    chat_id=chat_id
  )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  """Send a message when the command /help is issued."""
  chat_id = update.message.chat_id
  
  return await context.bot.send_message(
    text="Чтобы использовать бота, тэгните его, когда набираете сообщение. После нажатия на появившееся окно, бот выполнит команду указанную там.",
    chat_id=chat_id
  )

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE, specific_user_id: int) -> None:
  # query = update.inline_query.query // receive what input person typed in
  db.connect(reuse_if_open=True)

  current_user = update.effective_user
  
  if not user_exists(current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, )

  value = int(generateGaussianDistribution(0, len(names_array) - 1))
  result = transformRandomValueResult(value)
  
  if user_exists(current_user.id):
    create_interaction(user_id=current_user.id, result=value)
    
  logging.info(
    f"user_id: {current_user.id}; \
    username: {current_user.username}; \
    first_name: {current_user.first_name}; \
    last_name: {current_user.last_name}; \
    language_code: {current_user.language_code}; \
    gala_resiult: {result}"
  )
  user = User.get(User.id == current_user.id)
  
  if current_user.id == specific_user_id and not user.received_discount:
    result_id = str(uuid4())

    results = [
      InlineQueryResultArticle(
            id=result_id,
            title="Что с тобой случится в 2010-х?",
            input_message_content=InputTextMessageContent(
                f"<b>Поздравляю! Ты выиграл скидку на билет на Festa& Echo. Напиши кому нибудь из организаторов! 🎉</b>",
                parse_mode=ParseMode.HTML
            ),
            url='https://t.me/edafesta', 
            description="Узнай, кто ты сегодня из 2010-х!",
            thumb_url="https://i.ibb.co/mCRJWYZT/telegram-cloud-document-2-5321245724174745216.jpg",
            thumb_width=246,
            thumb_height=303,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Festa& Echo", url="https://t.me/edafesta")
            ]])
          )
    ]
    user.received_discount = True
    user.save()
  else:
    result_id = str(uuid4())

    results = [
    InlineQueryResultArticle(
            id=result_id,
            title="Что с тобой случится в 2010-х?",
            input_message_content=InputTextMessageContent(
                f"<b>{result}</b> {getRandomEmoji(int(generateGaussianDistribution(0, len(emojis) - 1)))}",
                parse_mode=ParseMode.HTML
            ),
            url='https://t.me/edafesta', 
            description="Узнай, кто ты сегодня из 2010-х!",
            thumb_url="https://i.ibb.co/mCRJWYZT/telegram-cloud-document-2-5321245724174745216.jpg",
            thumb_width=246,
            thumb_height=303,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Festa& Echo", url="https://t.me/edafesta")
            ]])
        ),
    ]
    user.save()

  try:
    await update.inline_query.answer(results, cache_time=20, is_personal=True)
    # logging.info("Inline query answered successfully")
  except Exception as e:
    logging.error(f"Failed to answer inline query: {e}")
  db.close()

