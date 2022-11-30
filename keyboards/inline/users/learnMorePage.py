from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.users import profile_cb


class LearnMorePage:
    @staticmethod
    async def LearnMorePage_text() -> str:
        text: str = "Telegram Ads сегодня - это уникальный инструмент привлечения пользователей и " \
                    "клиентов для любого бизнеса.\n\n" \
                    "✔️ 70+ млн пользователей в России.\n" \
                    "✔️ Более 250 тысяч каналов для размещения рекламы.\n" \
                    "✔️ Самый быстрорастущий мессенджер и контент-площадка.\n\n" \
                    "Хотите попробовать Telegram Ads? Оставьте заявку и наш менеджер свяжется с вами"
        return text

    @staticmethod
    async def LearnMorePage_IKB() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

                    :param:
                    :return: возвращает клавиатуру
                """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"🔝 Заказать услугу",
                                         callback_data=profile_cb.new("OrderServiceLMP", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"📞 Связаться с нами",
                                         callback_data=profile_cb.new("ConnectWithUsMP", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )