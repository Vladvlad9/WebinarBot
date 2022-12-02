from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, Message, \
    CallbackQuery

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
    async def back_ikb() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def skip_ikb(number: int) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"Пропустить",
                                         callback_data=profile_cb.new("SkipCompaniesPage", number, 0))
                ]
            ]
        )

    @staticmethod
    async def phone_kb() -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(
            resize_keyboard=True,
            one_time_keyboard=True,
            selective=True,
            keyboard=[
                [
                    KeyboardButton(text='Поделиться контактом',
                                   request_contact=True),
                    KeyboardButton(text='Пропустить', callback_data=profile_cb.new("PhoneNumber", 3, 0))
                ]
            ]
        )

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
                                         callback_data=profile_cb.new("WebinarMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"🗂 Каталог наших вебинаров",
                                         callback_data=profile_cb.new("CatalogWebinars", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def CatalogWebinars_IKB() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f"📞 Связаться с нами",
                                         callback_data=profile_cb.new("ConnectWithUsMP", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"🚀 Узнать о вебинаре",
                                         callback_data=profile_cb.new("WebinarMainPage", 0, 0))
                ],
                [
                    InlineKeyboardButton(text=f"⬅️ Назад",
                                         callback_data=profile_cb.new("MainPage", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def CatalogWebinars_text() -> str:
        text: str = "Каталог наших вебинаров:\n\n" \
                    "✅ Вебинар: Как изменился рынок Telegram Ads с сентября 2022.\n\n" \
                    "В чём преимущества Telegram Ads? Почему стоит начать уже сейчас? Как создать эффективные " \
                    "рекламные объявления, и какие изменения 2022 важны для платформы? " \
                    "Обо всём этом — в записи нашего вебинара\n\n" \
                    "..."
        return text

    @staticmethod
    async def OnlineApplication_text_LinkBot(callback: CallbackQuery):
        text = "👉 Для отправки заявки, оставьте Ваши контактные данные (3 простых шага)\n\n" \
               "1⃣ Ссылка на канал/бот: (шаг 1 из 3)"
        await callback.message.edit_text(text=text,
                                         reply_markup=await CompaniesPage.skip_ikb(number=1)
                                         )

    @staticmethod
    async def OnlineApplication_text_Budget(callback: CallbackQuery = None, message: Message = None):
        text = "Укажите бюджет на рекламную кампанию.\n" \
               "❗ Минимальный бюджет: 3000 евро"
        if callback:
            await callback.message.edit_text(text=text,
                                             reply_markup=await CompaniesPage.skip_ikb(number=2)
                                             )
        else:
            await message.answer(text=text, reply_markup=await CompaniesPage.skip_ikb(number=2)
                                 )

    @staticmethod
    async def OnlineApplication_text_Phone(message: Message):
        await message.answer(text="Контактный номер телефона: (шаг 3 из 3)",
                             reply_markup=await CompaniesPage.phone_kb()
                             )

    @staticmethod
    async def OnlineApplication_text_Finish(message: Message):
        text = "Спасибо! Мы свяжемся с Вами в течении 12 часов."
        await message.answer(text=text,
                             reply_markup=await CompaniesPage.back_ikb()
                             )
