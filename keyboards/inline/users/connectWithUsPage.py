from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.users import profile_cb


class ConnectWithUsMP:
    @staticmethod
    async def ConnectWithUsMP_text() -> str:
        text: str = "📲 Мы всегда на связи. Будем рады ответить на все ваши вопросы!"
        return text

    @staticmethod
    async def ConnectWithUsMP_IKB() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

                            :param:
                            :return: возвращает клавиатуру
                        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"Телеграмм канал",
                                         callback_data=profile_cb.new("pass", 0, 0),
                                         url=""),
                    InlineKeyboardButton(text=f"Сайт",
                                         callback_data=profile_cb.new("pass", 0, 0),
                                         url="")
                ],
                [
                    InlineKeyboardButton(text=f"📞 Оставить заявку",
                                         callback_data=profile_cb.new("OnlineApplication", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"Написать консультанту",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )