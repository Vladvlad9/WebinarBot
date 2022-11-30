from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.users import profile_cb


class CompaniesPage:
    @staticmethod
    async def textCompanies() -> str:
        text = "🧲 Magnetto.pro — агентство эффективного интернет-маркетинга. \n\n" \
               "Что мы умеем:\n\n" \
               "📌 Реализовывать стратегии продвижения в любых рекламных системах: " \
               "Telegram Ads, Яндекс.Директ, Google Ads, VK, email-маркетинг и другое;\n\n" \
               "..."
        return text

    @staticmethod
    async def companiesPage_ikb() -> InlineKeyboardMarkup:
        """Стартовая клавиатура главного меню

            :param:
            :return: возвращает клавиатуру
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"📞 Связаться с нами",
                                         callback_data=profile_cb.new("ConnectWithUsMP", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"🔝 Онлайн заявка",
                                         callback_data=profile_cb.new("OnlineApplication", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"🚀 Узнать о вебинаре",
                                         callback_data=profile_cb.new("LearnMoreMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"🗂 Каталог наших вебинаров",
                                         callback_data=profile_cb.new("ConnectWithUsMP", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )