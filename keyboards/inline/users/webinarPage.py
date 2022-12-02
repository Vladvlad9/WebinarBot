import re

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
    async def back_mainMenu() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

                            :param:
                            :return: возвращает клавиатуру
                        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )

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
                                         callback_data=profile_cb.new("RegistrationUser", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def registration_user_text() -> str:
        text: str = "Записаться на вебинар\n" \
               "👉 Для записи на вебинар оставьте ваши контактные данные (2 простых шага - Имя и Email)\n\n" \
               "1⃣ Ваше имя (шаг 1 из 2):"

        return text

    @staticmethod
    async def email_text() -> str:
        text: str = "2⃣ Ваш email (шаг 2 из 2):"
        return text

    @staticmethod
    async def validate_email(get_email: str) -> str:
        email = get_email

        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        if re.match(pattern, email) is not None:
            print("Проверка пройдена")
            return email
        else:
            email = None
            return email


