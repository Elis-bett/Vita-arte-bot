import logging
import random

from telegram.ext import Application, MessageHandler, filters, ConversationHandler, ContextTypes, CallbackQueryHandler
from config import BOT_TOKEN
from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup, Update, InlineKeyboardButton
from telegram import ReplyKeyboardRemove
from admin import message, photo1, photo2, photo3, photo4, photo5, sogl, photo6, photo7
from keyboards import markup, markup1, markup2, markup3
from test import tests
from data import db_session
from data.users import User
from password_maker import password

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        "Привет от команды онлайн школы Vita-arte! &#128075; \n "
        "Наш бот поможет Вам узнать больше о нас, определиться с направлением а так же записаться к нам. \n"
        " Успехов в учебе &#128156;",
        reply_markup=markup
    )
    await update.message.reply_html(
        "&#11088;Чтобы узнать больше информации о школе используйте команду /info\n"
        "&#11088;Чтобы записаться на обучение используйте команду /reg \n"
        "&#11088;Хотите рисовать, но не можете определиться с направлением? &#128533;"
        " Мы поможем вам, проведя небольшое тестирование, для этого используйте команду /test \n"
        "&#11088;Если остались вопросы, всегда можно обратиться к администратору &#128222;, используйте команду /help\n"
        "&#11088;Если хотите убрать клавиатуру, используйте команду /close",
        reply_markup=markup
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_html("Если возникли проблемы, всегда можно обратиться к нашему администратору:"
                                    "@Betty_Ionina")


async def info_command(update, context):
    """Отправляет сообщение когда получена команда /info"""
    await update.message.reply_html("&#128231;Онлайн-школа Vita arte - проект, в рамках которого все желающие и имеющие"
                                    " трудности с получением художественного образования смогут легко получить его. \n"
                                    "&#127775;Особенности Vita arte&#127775; \n"
                                    "&#128396; все курсы созданы на базе академических программ художественных ВУЗов\n"
                                    "&#128396; форматы самостоятельного обучения или с прямой связью с педагогом\n"
                                    "&#128396; занятия ведут только профессиональные художники с опытом преподавания\n"
                                    "&#128396; наличие прямой связи с ведущими художественными ВУЗами, позволяющая "
                                    "заранее определиться с выбором\n"
                                    "&#128396; большой выбор направлений")
    await update.message.reply_html("Наша онлайн-школа решает следующие проблемы:\n"
                                    "&#127979; поступление в ВУЗы, СУЗы без художественного образования\n"
                                    "&#127979; отсутствие возможности получить качественное художественное образование\n"
                                    "&#127979; отсутствие возможности учиться в очном формате")
    await update.message.reply_html('Если мы вас заинтересовали, вы можете узнать больше о каждом из направлений:\n'
                                    '&#127912;живопись\n'
                                    '&#127912;графика\n'
                                    '&#127912;дизайн\n'
                                    '&#127912;роспись\n'
                                    'выбрав их на клавиатуре &#128521;', reply_markup=markup1)


async def registration_command(update, context):
    """Отправляет сообщение когда получена команда /reg"""
    await update.message.reply_html('Спасибо, что выбрали нас&#128156;\n'
                                    'Напишите полностью свою фамилию, имя и отчество (если есть)&#129303;',
                                    reply_markup=markup3)
    return 11


async def test_command(update, context):
    """Отправляет сообщение когда получена команда /test"""
    await update.message.reply_html('Наш тест поможет Вам определиться с направлением&#128156;\n'
                                    'За каждый ответ будет начисленно определенное количество баллов\n'
                                    'В конце введите ваши баллы\n'
                                    'Пожалуйста, напишите свое имя и фамилию')
    return 1


async def age(update, context):
    await update.message.reply_html('Напишите, пожалуйста, свой возраст')
    return 2


# далее - вопросы для теста
async def qw1(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[0]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[0]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[0]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[0]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo1(update.message.chat_id)
    await update.message.reply_html(tests[0]['question'], reply_markup=reply_markup)
    return 3


async def qw2(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[1]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[1]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[1]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[1]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo2(update.message.chat_id)
    await update.message.reply_html(tests[1]['question'], reply_markup=reply_markup)
    return 4


async def qw3(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[2]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[2]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[2]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[2]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo3(update.message.chat_id)
    await update.message.reply_html(tests[2]['question'], reply_markup=reply_markup)
    return 5


async def qw4(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[3]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[3]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[3]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[3]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo4(update.message.chat_id)
    await update.message.reply_html(tests[3]['question'], reply_markup=reply_markup)
    return 6


async def qw5(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[4]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[4]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[4]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[4]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    photo5(update.message.chat_id)
    await update.message.reply_html(tests[4]['question'], reply_markup=reply_markup)
    return 7


async def qw6(update, context):
    keyboard = [
        [InlineKeyboardButton(tests[5]['answer'][0], callback_data='1 балл')],
        [InlineKeyboardButton(tests[5]['answer'][1], callback_data='2 балла')],
        [InlineKeyboardButton(tests[5]['answer'][2], callback_data='3 балла')],
        [InlineKeyboardButton(tests[5]['answer'][3], callback_data='4 балла')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_html(tests[5]['question'], reply_markup=reply_markup)
    return 8


# просит ввести баллы
async def end_test(update, context):
    await update.message.reply_html(f'Введите Ваш результат: ')
    return 9


# результаты тестирования
async def ending_test(update, context):
    if update.message.text.isdigit():
        if int(update.message.text) in range(6, 14):
            await update.message.reply_html('Вероятнее всего вам подходит направление Живопись')
        elif int(update.message.text) in range(14, 20):
            await update.message.reply_html(f'Вероятнее всего вам подходит направление Графика')
        elif int(update.message.text) in range(20, 27):
            await update.message.reply_html(f'Вероятнее всего вам подходит направление Дизайн')
        elif int(update.message.text) in range(27, 36):
            await update.message.reply_html(f'Вероятнее всего вам подходит направление Роспись')
        else:
            await update.message.reply_html(f'Пожалуйста, пересчитайте баллы, возможно вы ошиблись&#128565;')
        await update.message.reply_html(f'Спасибо за участие в тестировании&#128519;\n'
                                        f'Надеемся, что помогли вам определиться&#128156;')
    else:
        await update.message.reply_html(f'Пожалуйста, пересчитайте баллы, возможно вы ошиблись&#128565;')
        await update.message.reply_html(f'Спасибо за участие в тестировании&#128519;\n'
                                        f'Надеемся, что помогли вам определиться&#128156;')
    return ConversationHandler.END


# возвращение на исходную клавиатуру
async def back_command(update, context):
    """Отправляет сообщение когда получена команда /back"""
    await update.message.reply_html('Пожалуйста, выберите, что вас интересует&#128522;', reply_markup=markup)


# команда для остановки диалога
async def stop(update, context):
    """Отправляет сообщение когда получена команда /stop"""
    await update.message.reply_text("Всего доброго!", reply_markup=markup)
    return ConversationHandler.END


# команда для закрытия клавиатуры
async def close_keyboard(update, context):
    """Отправляет сообщение когда получена команда /close"""
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


# завершение регистрации
async def end_reg(update, context):
    passw = password()
    message(f" Новый зарегистрированный пользователь @{update.message.from_user.username} \n"
            f"email: {update.message.text}")
    email = "email@email.ru"
    await update.message.reply_html("Спасибо за оставленную заявку! Администратор свяжется с вами позже")
    user = User()
    user.name = context.user_data['name']
    user.email = update.message.text
    user.hashed_password = passw
    await update.message.reply_html(f"Ваш пароль: {passw} \n"
                                    f"Ваш логин: ваша эллектронная почта\n"
                                    "Для завершения регистрации, нажмите команду /stop", reply_markup=markup3)
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    return ConversationHandler.END


# выбор курса при регистрации
async def course(update, context):
    context.user_data['name'] = update.message.text
    keyboard = [
        [
            InlineKeyboardButton("живопись", callback_data="живопись"),
            InlineKeyboardButton("графика", callback_data="графика"),
        ],
        [
            InlineKeyboardButton("дизайн", callback_data="дизайн"),
            InlineKeyboardButton("роспись", callback_data="роспись"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Выберите пожалуйста направление:", reply_markup=reply_markup)
    return 12


async def end_registration(update, context):
    await update.message.reply_html('Пожалуйста заполните следующие согласия и пришлите сюда')
    sogl(update.message.chat_id)
    await update.message.reply_html('Так же пришлите пожалуйста свою электронную почту')
    return 13


# бот реагирует на выбранную кнопку на inline клавиатуре
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    await query.edit_message_text(text=f"Вы выбрали: {query.data}\n"
                                       f"Пожалуйста, напишите 'ок'")


# ответы на самые распространенные фразы от пользователей
async def echo(update, context):
    if update.message.text.lower() in ['живопись', 'графика', 'дизайн', 'роспись']:
        await update.message.reply_html(f'Информация о курсах пока разрабатывается', reply_markup=markup2)
    elif 'привет' in update.message.text.lower() or 'здравствуйте' in update.message.text.lower():
        await update.message.reply_html(
            random.choice(['Привет от команды Vita-arte	&#128075;', 'Доброго времени суток',
                           'Вас приветствует команда Vita-arte&#128156;']),
            reply_markup=markup)
    elif 'направления ' in update.message.text.lower() or 'курсы' in update.message.text.lower():
        await update.message.reply_html(f'Информация о курсах пока разрабатывается', reply_markup=markup2)
    elif 'педагог ' in update.message.text.lower() or 'учител' in update.message.text.lower():
        await update.message.reply_html(f'Наши учителя:', reply_markup=markup)
        photo6(update.message.chat_id)
    elif 'регистр ' in update.message.text.lower():
        await update.message.reply_html(f'Для регистрации воспользуйтесь командой /reg', reply_markup=markup)
    elif 'бот ' in update.message.text.lower():
        await update.message.reply_html(random.choice(['Я здесь&#9995;', 'Жду ваших вопросов&#128526;',
                                                       'Я на связи']), reply_markup=markup)
    elif 'админ ' in update.message.text.lower():
        await update.message.reply_html(f'Вам всегда поможет наш администратор @Betty_Ionina', reply_markup=markup)
    elif 'тест' in update.message.text.lower():
        await update.message.reply_html(f'Если вы хотите пройти тестирование, воспользуйтесь командой /test',
                                        reply_markup=markup)
    elif 'школ' in update.message.text.lower():
        await update.message.reply_html(f'Вы можете узнать более подробную информацию, нажав команду /info',
                                        reply_markup=markup)
        photo7(update.message.chat_id)
    else:
        await update.message.reply_html(f'Извините, я вас не понимаю&#128533;\n'
                                        f'Воспользуйтесь командами на клавиатуре', reply_markup=markup)


# сценарий диалога для регистрации
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('reg', registration_command)],

    states={
        11: [MessageHandler(filters.TEXT & ~filters.COMMAND, course)],
        12: [MessageHandler(filters.TEXT & ~filters.COMMAND, end_registration)],
        13: [MessageHandler(filters.TEXT & ~filters.COMMAND, end_reg)]
    },

    fallbacks=[CommandHandler('stop', stop)]
)

# сценарий диалога для тестирования
conv_handler1 = ConversationHandler(
    entry_points=[CommandHandler('test', test_command)],

    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, age)],
        2: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw1)],
        3: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw2)],
        4: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw3)],
        5: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw4)],
        6: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw5)],
        7: [MessageHandler(filters.TEXT & ~filters.COMMAND, qw6)],
        8: [MessageHandler(filters.TEXT & ~filters.COMMAND, end_test)],
        9: [MessageHandler(filters.TEXT & ~filters.COMMAND, ending_test)]
    },

    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conv_handler)
    application.add_handler(conv_handler1)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("test", test_command))
    application.add_handler(CommandHandler("reg", registration_command))
    application.add_handler(CommandHandler('back', back_command))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(CallbackQueryHandler(button))
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    db_session.global_init("db/blogs.db")
    application.run_polling()


if __name__ == '__main__':
    main()
