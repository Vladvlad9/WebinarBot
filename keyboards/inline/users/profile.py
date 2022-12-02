from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest

from keyboards.inline.users import ConnectWithUsMP
from keyboards.inline.users import LearnMorePage
from keyboards.inline.users import WebinarPage
from keyboards.inline.users import profile_cb
from keyboards.inline.users.companiesPage import CompaniesPage
from keyboards.inline.users.mainPage import MainPage
from loader import bot
from states.users import RegistrationUser


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

                # ###########4 Главные кнопки меню #########
                elif data.get("target") == "WebinarMainPage":
                    await callback.message.edit_text(text=await WebinarPage.textWebinarPage(),
                                                     reply_markup=await WebinarPage.WebinarPageIKB())

                elif data.get("target") == "CompaniesMainPage":
                    await callback.message.edit_text(text=await CompaniesPage.textCompanies(),
                                                     reply_markup=await CompaniesPage.companiesPage_ikb())

                elif data.get("target") == "LearnMoreMainPage":
                    await callback.message.edit_text(text=await LearnMorePage.LearnMorePage_text(),
                                                     reply_markup= await LearnMorePage.LearnMorePage_IKB())

                elif data.get("target") == "ConnectWithUsMP":
                    await callback.message.edit_text(text=await ConnectWithUsMP.ConnectWithUsMP_text(),
                                                     reply_markup=await ConnectWithUsMP.ConnectWithUsMP_IKB())
                ################################################

                elif data.get("target") == "RegistrationUser":
                    await callback.message.edit_text(text=await WebinarPage.registration_user_text())
                    await RegistrationUser.LName.set()

                elif data.get("target") == "CatalogWebinars":
                    await callback.message.edit_text(text=await CompaniesPage.CatalogWebinars_text(),
                                                     reply_markup=await CompaniesPage.CatalogWebinars_IKB())

                elif data.get('target') == "OnlineApplication":
                    await CompaniesPage.OnlineApplication_text_LinkBot(callback=callback)
                    await RegistrationUser.LinkBOT.set()

                elif data.get('target') == "SkipCompaniesPage":
                    number = int(data.get('id'))
                    if number == 1:
                        await CompaniesPage.OnlineApplication_text_Budget(callback=callback)
                        await RegistrationUser.Budget.set()
                    elif number == 2:
                        await callback.message.delete()
                        await callback.message.answer(text="Контактный номер телефона: (шаг 3 из 3)",
                                                      reply_markup=await CompaniesPage.phone_kb()
                                                      )
                        await RegistrationUser.Phone.set()

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
                if await state.get_state() == "RegistrationUser:LName":
                    await state.update_data(name=message.text)
                    await message.answer(text=await WebinarPage.email_text())
                    await RegistrationUser.Email.set()

                elif await state.get_state() == "RegistrationUser:Email":
                    email = await WebinarPage.validate_email(message.text)
                    if email is not None:
                        await message.answer(text="Спасибо! Вы успешно зарегистрированы на вебинар. Мы "
                                                  "отправим дополнительное письмо со ссылкой на вебинар на ваш email",
                                             reply_markup=await WebinarPage.back_mainMenu())
                    else:
                        await message.answer(text="Введен не верный email")

                    await state.update_data(email=message.text)

                elif await state.get_state() == "RegistrationUser:LinkBOT":
                    await state.update_data(linkbot=message.text)
                    await CompaniesPage.OnlineApplication_text_Budget(message=message)
                    await RegistrationUser.Budget.set()

                elif await state.get_state() == "RegistrationUser:Budget":
                    await state.update_data(budget=message.text)

                    await message.answer(text="Контактный номер телефона: (шаг 3 из 3)",
                                         reply_markup=await CompaniesPage.phone_kb()
                                         )
                    await RegistrationUser.Phone.set()

                elif await state.get_state() == "RegistrationUser:Phone":
                    if message.content_type == "contact":
                        await state.update_data(phone=message.contact.phone_number)
                        await CompaniesPage.OnlineApplication_text_Finish(message=message)
                        await state.finish()
                    elif message.text == "Пропустить":
                        await CompaniesPage.OnlineApplication_text_Finish(message=message)
                        await state.finish()
                    else:
                        await state.update_data(phone=message.text)
                        await state.finish()