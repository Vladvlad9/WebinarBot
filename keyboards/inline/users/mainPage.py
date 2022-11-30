from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.users import profile_cb


class MainPage:
    @staticmethod
    async def mainPage_ikb() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

            :param:
            :return: возвращает клавиатуру
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"🚀 О Вебинаре",
                                         callback_data=profile_cb.new("WebinarMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"❤️ О компании",
                                         callback_data=profile_cb.new("CompaniesMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"📈 Узнать больше",
                                         callback_data=profile_cb.new("LearnMoreMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"📞 Связаться с нами",
                                         callback_data=profile_cb.new("ConnectWithUsMP", 0, 0))
                ]
            ]
        )