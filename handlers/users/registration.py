from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import BadRequest

from keyboards import MainPage
from keyboards.inline.users.profile import profile_cb, Profile
from loader import dp, bot
from states.users import RegistrationUser


@dp.message_handler(commands=["start"])
async def registration_start(message: types.Message):
    await message.delete()
    for entity in message.entities:
        if entity.type in ["url", "text_link"]:
            await message.delete()
        try:
            await bot.delete_message(
                chat_id=message.from_user.id,
                message_id=message.message_id - 1
            )
        except BadRequest:
            pass
    Greetings_text: str = "🤖Привет! Я бот-помощник Magnetto, помогу вам с регистрацией на вебинар и познакомлю с " \
                          "нашей компанией. Добро пожаловать! "
    await message.answer(text=Greetings_text,
                         reply_markup=await MainPage.mainPage_ikb())


@dp.callback_query_handler(profile_cb.filter())
@dp.callback_query_handler(profile_cb.filter(), state=RegistrationUser.all_states)
async def process_callback_reg(callback: types.CallbackQuery, state: FSMContext = None):
    await Profile.process_profile(callback=callback, state=state)


@dp.message_handler(state=RegistrationUser.all_states, content_types=["text", "contact"])
async def process_message_reg(message: types.Message, state: FSMContext):
    await Profile.process_profile(message=message, state=state)