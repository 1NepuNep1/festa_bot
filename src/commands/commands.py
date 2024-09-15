import logging
import asyncio
from html import escape
from uuid import uuid4
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from src.db.database import db, User
from src.db.utils import create_interaction, create_user, user_exists
from src.utils.utils import generateGaussianDistribution, transformRandomValueResult, getRandomLink, getRandomEmoji

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

  value = int(generateGaussianDistribution(0, 42))
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
            title="Кто ты сегодня с Met Gala?",
            input_message_content=InputTextMessageContent(
                f"<b>Поздравляю! Ты выиграл скидку на билет на Met Gala Posvyat. Напиши кому нибудь из организаторов!</b>"
                f"<a href='https://i.ibb.co/0Cpg6xv/aap-rocky-attends-the-2023-met-gala-celebrating-karl-lagerfeld-a-line-of-beauty-1714429223233.jpg'> 🎉</a>",
                parse_mode=ParseMode.HTML
            ),
            url='https://t.me/metgalaposvyat', 
            description="Узнай, какая ты celebrity с Met Gala сегодня!",
            thumb_url="https://i.ibb.co/0qKyhfG/festa-x-dsba.jpg",
            thumb_width=246,
            thumb_height=303,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Met Gala Posvyat", url="https://t.me/metgalaposvyat")
            ]])
          )
    ]
    context.user_data['inline_results'] = {result_id: "Поздравляю! Ты выиграл скидку на билет на Met Gala Posvyat. Напиши кому нибудь из организаторов!"}
    user.received_discount = True
    user.save()
  else:
    result_id = str(uuid4())

    results = [
    InlineQueryResultArticle(
            id=result_id,
            title="Кто ты сегодня с Met Gala?",
            input_message_content=InputTextMessageContent(
                f"<b>{result}</b>"
                f"<a href='{getRandomLink(value)}'> {getRandomEmoji(int(generateGaussianDistribution(0, 42)))}</a>",
                parse_mode=ParseMode.HTML
            ),
            url='https://t.me/metgalaposvyat', 
            description="Узнай, какая ты celebrity с Met Gala сегодня!",
            thumb_url="https://i.ibb.co/0qKyhfG/festa-x-dsba.jpg",
            thumb_width=246,
            thumb_height=303,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Met Gala Posvyat", url="https://t.me/metgalaposvyat")
            ]])
        ),
    ]
    context.user_data['inline_results'] = {result_id: result}
    user.save()

  try:
    await update.inline_query.answer(results, cache_time=20, is_personal=True)
    # logging.info("Inline query answered successfully")
  except Exception as e:
    logging.error(f"Failed to answer inline query: {e}")
  db.close()


async def chosen_inline_result(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # logging.info("chosen_inline_result function called")
    
    chosen_result = update.chosen_inline_result
    result_id = chosen_result.result_id  # Получаем result_id
    # logging.info(f"Chosen result: {chosen_result}")

    inline_message_id = chosen_result.inline_message_id
    result = context.user_data.get('inline_results', {}).get(result_id, "Фото больше недоступно.")
    # logging.info(f"Editing message with inline_message_id: {inline_message_id}")

    asyncio.create_task(edit_message_later(inline_message_id, context, result))

async def edit_message_later(inline_message_id: str, context: ContextTypes.DEFAULT_TYPE, result: str) -> None:
    try:
        await asyncio.sleep(60)
        await context.bot.edit_message_text(
            inline_message_id=inline_message_id,
            text=f"<b>{result}</b>",
            parse_mode="HTML"
        )
        # logging.info(f"Message with inline_message_id {inline_message_id} edited successfully")
    except Exception as e:
        logging.error(f"Failed to edit message: {e}")