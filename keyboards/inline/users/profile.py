from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest

from keyboards.inline.users import LearnMorePage
from keyboards.inline.users import WebinarPage
from keyboards.inline.users import profile_cb
from keyboards.inline.users.companiesPage import CompaniesPage
from keyboards.inline.users.mainPage import MainPage
from loader import bot


class Profile:
    @staticmethod
    async def process_profile(callback: CallbackQuery = None, message: Message = None,
                              state: FSMContext = None) -> None:

        if callback:
            if callback.data.startswith('profile'):
                data: dict = profile_cb.parse(callback_data=callback.data)

                if data.get("target") == "MainPage":
                    Greetings_text: str = "🤖Привет! Я бот-помощник Magnetto, помогу вам с регистрацией на " \
                                          "вебинар и познакомлю с нашей компанией. Добро пожаловать! "
                    await callback.message.edit_text(text=Greetings_text,
                                                     reply_markup=await MainPage.mainPage_ikb())

                elif data.get("target") == "WebinarMainPage":
                    await callback.message.edit_text(text=await WebinarPage.textWebinarPage(),
                                                     reply_markup=await WebinarPage.WebinarPageIKB())

                elif data.get("target") == "CompaniesMainPage":
                    await callback.message.edit_text(text=await CompaniesPage.textCompanies(),
                                                     reply_markup=await CompaniesPage.companiesPage_ikb())

                elif data.get("target") == "LearnMoreMainPage":
                    await callback.message.edit_text(text=await LearnMorePage.LearnMorePage_text(),
                                                     reply_markup= await LearnMorePage.LearnMorePage_IKB())


        if message:
            await message.delete()

            try:
                await bot.delete_message(
                    chat_id=message.from_user.id,
                    message_id=message.message_id - 1
                )
            except BadRequest:
                pass

        if state:
            pass