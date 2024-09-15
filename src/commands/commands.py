import logging
import asyncio
from html import escape
from uuid import uuid4
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from src.db.database import db
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

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
  
  result_id = str(uuid4())

  # list_of_bots = """1. <b>Личностный тест</b> - @five_factor_model_bot\n2. <b>Бросаться снежками</b> - @throw_snowball_bot\n3. <b>Last.FM bot</b> - @lastfm_tgbot\n\nПо интересующим вопросам, @keeeparis"""
    
  results = [
    # InlineQueryResultPhoto(
    #         id=str(uuid4()),
    #         photo_url="https://i.ibb.co/0qKyhfG/festa-x-dsba.jpg",
    #         thumb_url="https://i.ibb.co/0qKyhfG/festa-x-dsba.jpg",
    #         title="Кто ты сегодня с Met Gala?",
    #         caption=f"<b>{result}</b>",
    #         parse_mode=ParseMode.HTML,
    #         reply_markup=InlineKeyboardMarkup([[
    #             InlineKeyboardButton("Открыть Met Gala", url="https://t.me/metgalaposvyat")
    #         ]])
        # ),
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
    # InlineQueryResultArticle(
    #   id=str(uuid4()),
    #   title="Список ботов",
    #   input_message_content=InputTextMessageContent(
    #     f"{list_of_bots}", parse_mode=ParseMode.HTML
    #   ),
    #   url='https://seesaw.kz',
    #   description="⬇️ Клик ⬇️",
    # ),
  ]
  context.user_data['inline_results'] = {result_id: result}
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
    # try:
    #     await asyncio.sleep(60)
    #     await context.bot.edit_message_text(
    #         inline_message_id=inline_message_id,
    #         text=f"<b>{result}</b>",
    #         parse_mode="HTML"
    #     )
    #     # logging.info(f"Message with inline_message_id {inline_message_id} edited successfully")
    # except Exception as e:
    #     logging.error(f"Failed to edit message: {e}")

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