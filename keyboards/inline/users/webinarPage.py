from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.users import profile_cb


class WebinarPage:
    @staticmethod
    async def textWebinarPage():
        text = "✅Всё больше и больше компаний выбирают в Telegram Ads как основной рекламный инструмент. \n\n" \
               "⌨️Почему? Как начать продвижение в Telegram и увеличить трафик?\n\n" \
               "Об этом и многом другом вы узнаете на нашем вебинаре, который мы проведём совместно " \
               "с Synergy CRM — цифровой платформой для увеличения продаж с помощью автоматизации процессов. \n\n" \
               "💬На вебинаре вы узнаете:\n\n" \
               "✔️Что такое Telegram Ads. Особенности этого рекламного канала.\n" \
               "✔️Преимущества. Что важно знать перед стартом? Основные правила модерации.\n\n" \
               "Регистрация по ссылке ниже ⬇️ ⬇️ ⬇️"
        return text

    @staticmethod
    async def WebinarPageIKB() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

                    :param:
                    :return: возвращает клавиатуру
                """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"✅ Зарегистрироваться",
                                         callback_data=profile_cb.new("Registration", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )