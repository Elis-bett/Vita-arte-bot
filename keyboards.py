from telegram import ReplyKeyboardMarkup

course_keyboard = [['/back'],
                   ['/help']]
info_keyboad = [['живопись', 'графика'],
                ['дизайн', 'роспись'],
                ['/back']]
reply_keyboard = [['/info', '/test'],
                  ['/reg', '/help']]
back_keyboard = [['/back'],
                 ['/stop']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup1 = ReplyKeyboardMarkup(info_keyboad, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(course_keyboard, one_time_keyboard=False)
markup3 = ReplyKeyboardMarkup(back_keyboard, one_time_keyboard=False)