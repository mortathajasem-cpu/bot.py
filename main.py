import telebot
from telebot import types

# ---------------------------------------------------------
# التوكين الخاص بك
TOKEN = "8259361246:AAHJuWJkoZShk5MJU46JgTsQndqVYP7oUZU"
# ---------------------------------------------------------

bot = telebot.TeleBot(TOKEN)

user_answers = {}

# قائمة الأسئلة
questions = [
    {"id": 1, "text": "في اجتماع، قاطعك أحدهم بصوت عالٍ. ردة فعلك؟", "options": {"A": {"text": "أصمت وأرتبك", "score": 1}, "B": {"text": "أنتظر بخجل", "score": 2}, "C": {"text": "أسكت للمشاكل", "score": 3}, "D": {"text": "أعترض بحزم", "score": 4}, "E": {"text": "أوقفه بقوة", "score": 5}}},
    {"id": 2, "text": "شاهدت شخصاً يُظلم في الشارع. ماذا تفعل؟", "options": {"A": {"text": "أهرب فوراً", "score": 1}, "B": {"text": "أحزن وأمشي", "score": 2}, "C": {"text": "أراقب فقط", "score": 3}, "D": {"text": "أبحث عن شرطي", "score": 4}, "E": {"text": "أتدخل بنفسي", "score": 5}}},
    {"id": 3, "text": "عُرضت عليك وظيفة في مدينة بعيدة. قرارك؟", "options": {"A": {"text": "أرفض فوراً", "score": 1}, "B": {"text": "أتردد وأرفض", "score": 2}, "C": {"text": "أقبل بشرط", "score": 3}, "D": {"text": "أقبل بقلق", "score": 4}, "E": {"text": "أقبل بحماس", "score": 5}}},
    {"id": 4, "text": "طلب منك صديق طلباً فوق طاقتك. هل تقول لا؟", "options": {"A": {"text": "مستحيل أرفض", "score": 1}, "B": {"text": "أوافق خجلاً", "score": 2}, "C": {"text": "أختلق عذراً", "score": 3}, "D": {"text": "أعتذر بلطف", "score": 4}, "E": {"text": "أقول لا بوضوح", "score": 5}}},
    {"id": 5, "text": "حدثت مشكلة مفاجئة وكبيرة. أول ردة فعل؟", "options": {"A": {"text": "أصاب بالذعر", "score": 1}, "B": {"text": "أبكي وأشكو", "score": 2}, "C": {"text": "أتوتر جداً", "score": 3}, "D": {"text": "أقلق وأفكر", "score": 4}, "E": {"text": "أهدأ وأديرها", "score": 5}}},
    {"id": 6, "text": "مدى اهتمامك برأي الناس في قراراتك؟", "options": {"A": {"text": "يغير قراري", "score": 1}, "B": {"text": "يقلقني جداً", "score": 2}, "C": {"text": "أعدل لإرضائهم", "score": 3}, "D": {"text": "أسمع للنقد", "score": 4}, "E": {"text": "لا أهتم إطلاقاً", "score": 5}}},
    {"id": 7, "text": "ارتكبت خطأً فادحاً. كيف تتصرف؟", "options": {"A": {"text": "أنكر تماماً", "score": 1}, "B": {"text": "ألوم الظروف", "score": 2}, "C": {"text": "أعترف لو كُشفت", "score": 3}, "D": {"text": "أعترف وأعتذر", "score": 4}, "E": {"text": "أعترف وأصلح", "score": 5}}},
    {"id": 8, "text": "دورك المفضل في فرق العمل؟", "options": {"A": {"text": "منفذ صامت", "score": 1}, "B": {"text": "مساعد", "score": 2}, "C": {"text": "عضو فعال", "score": 3}, "D": {"text": "نائب قائد", "score": 4}, "E": {"text": "القائد", "score": 5}}},
    {"id": 9, "text": "غريب طلب مالاً لقصة مأساوية. ردة فعلك؟", "options": {"A": {"text": "أعطيه كل شيء", "score": 1}, "B": {"text": "أعطيه الكثير", "score": 2}, "C": {"text": "مبلغ رمزي", "score": 3}, "D": {"text": "أطلب إثباتاً", "score": 4}, "E": {"text": "أتجاهله", "score": 5}}},
    {"id": 10, "text": "تصديق الأخبار على السوشيال ميديا؟", "options": {"A": {"text": "أصدق وأنشر", "score": 1}, "B": {"text": "أصدق المشهور", "score": 2}, "C": {"text": "أشك وأنشر", "score": 3}, "D": {"text": "أصدق الموثوق", "score": 4}, "E": {"text": "أبحث عن المصدر", "score": 5}}},
    {"id": 11, "text": "قراراتك المصيرية تعتمد على؟", "options": {"A": {"text": "العاطفة فقط", "score": 1}, "B": {"text": "رأي الناس", "score": 2}, "C": {"text": "خليط", "score": 3}, "D": {"text": "منطق وعاطفة", "score": 4}, "E": {"text": "عقلانية تامة", "score": 5}}},
    {"id": 12, "text": "شخص خذلك مرتين. فرصة ثالثة؟", "options": {"A": {"text": "أوافق فوراً", "score": 1}, "B": {"text": "أوافق بقلق", "score": 2}, "C": {"text": "تحت الضغط", "score": 3}, "D": {"text": "أوافق بحذر", "score": 4}, "E": {"text": "أقطع علاقتي", "score": 5}}},
    {"id": 13, "text": "خطتك للسنوات الخمس القادمة؟", "options": {"A": {"text": "لا توجد", "score": 1}, "B": {"text": "أحلام فقط", "score": 2}, "C": {"text": "أفكار عامة", "score": 3}, "D": {"text": "أهداف سنوية", "score": 4}, "E": {"text": "خطة مكتوبة", "score": 5}}},
    {"id": 14, "text": "مزاح ثقيل ومهين أمام الناس. ردك؟", "options": {"A": {"text": "أخجل وأسكت", "score": 1}, "B": {"text": "أضحك مجاملة", "score": 2}, "C": {"text": "أنزعج بصمت", "score": 3}, "D": {"text": "رد مبطن", "score": 4}, "E": {"text": "أوقفه بجدية", "score": 5}}},
    {"id": 15, "text": "هل يستغل الناس طيبتك؟", "options": {"A": {"text": "دائماً (ضحية)", "score": 1}, "B": {"text": "كثيراً", "score": 2}, "C": {"text": "أحياناً", "score": 3}, "D": {"text": "نادراً", "score": 4}, "E": {"text": "مستحيل", "score": 5}}},
    {"id": 16, "text": "دفع فاتورة العشاء مع الأصدقاء؟", "options": {"A": {"text": "أتهرب", "score": 1}, "B": {"text": "أنتظر غيري", "score": 2}, "C": {"text": "أدفع حصتي", "score": 3}, "D": {"text": "أعرض مجاملة", "score": 4}, "E": {"text": "أدفع للجميع", "score": 5}}},
    {"id": 17, "text": "استعارة غرض عزيز عليك؟", "options": {"A": {"text": "أرفض بشدة", "score": 1}, "B": {"text": "أكذب وأرفض", "score": 2}, "C": {"text": "أوافق بقلق", "score": 3}, "D": {"text": "أوافق وأنبه", "score": 4}, "E": {"text": "فداك", "score": 5}}},
    {"id": 18, "text": "شراء الهدايا للمناسبات؟", "options": {"A": {"text": "أرخص شيء", "score": 1}, "B": {"text": "متوسطة", "score": 2}, "C": {"text": "جيدة ومعقولة", "score": 3}, "D": {"text": "قيمة وجودة", "score": 4}, "E": {"text": "الأغلى والأفخم", "score": 5}}},
    {"id": 19, "text": "فلسفة الإنفاق على نفسك؟", "options": {"A": {"text": "أكتنز (بخل)", "score": 1}, "B": {"text": "بحذر وذنب", "score": 2}, "C": {"text": "توازن", "score": 3}, "D": {"text": "بسخاء للتطوير", "score": 4}, "E": {"text": "بلا حساب", "score": 5}}},
    {"id": 20, "text": "طعام كثير متبقي بعد وليمة؟", "options": {"A": {"text": "أخزنه لنفسي", "score": 1}, "B": {"text": "أعطي للخدم", "score": 2}, "C": {"text": "أوزع للأقارب", "score": 3}, "D": {"text": "أعلبه للفقراء", "score": 4}, "E": {"text": "أوصله بنفسي", "score": 5}}},
    {"id": 21, "text": "كرم المشاعر والمدح؟", "options": {"A": {"text": "بخيل جداً", "score": 1}, "B": {"text": "مجاملة فقط", "score": 2}, "C": {"text": "للمستحق", "score": 3}, "D": {"text": "كريم للمقربين", "score": 4}, "E": {"text": "غني ومبتسم", "score": 5}}},
    {"id": 22, "text": "دفع مبلغ كبير لشيء ضروري؟", "options": {"A": {"text": "ألم وشكوى", "score": 1}, "B": {"text": "انزعاج", "score": 2}, "C": {"text": "عدم رضا", "score": 3}, "D": {"text": "تقبل كواجب", "score": 4}, "E": {"text": "رضا وحمد", "score": 5}}},
    {"id": 23, "text": "آخر كتاب قرأته بالكامل؟", "options": {"A": {"text": "لا أذكر", "score": 1}, "B": {"text": "رواية قديمة", "score": 2}, "C": {"text": "مقالات فقط", "score": 3}, "D": {"text": "كل بضعة أشهر", "score": 4}, "E": {"text": "قارئ نهم", "score": 5}}},
    {"id": 24, "text": "5 ساعات فراغ بمفردك؟", "options": {"A": {"text": "نوم وملل", "score": 1}, "B": {"text": "تيك توك", "score": 2}, "C": {"text": "أفلام", "score": 3}, "D": {"text": "هواية مفيدة", "score": 4}, "E": {"text": "تعلم وإبداع", "score": 5}}},
    {"id": 25, "text": "حديثك المفضل في المجالس؟", "options": {"A": {"text": "فضائح الناس", "score": 1}, "B": {"text": "الشكوى", "score": 2}, "C": {"text": "رياضة/موضة", "score": 3}, "D": {"text": "أخبار العالم", "score": 4}, "E": {"text": "أفكار وفلسفة", "score": 5}}},
    {"id": 26, "text": "المحتوى في هاتفك؟", "options": {"A": {"text": "مقالب تافهة", "score": 1}, "B": {"text": "رقص وأغاني", "score": 2}, "C": {"text": "منوعات", "score": 3}, "D": {"text": "أخبار وسياسة", "score": 4}, "E": {"text": "تعليمي وثائقي", "score": 5}}},
    {"id": 27, "text": "طبيعة هواياتك؟", "options": {"A": {"text": "لا توجد", "score": 1}, "B": {"text": "استهلاكية", "score": 2}, "C": {"text": "ترفيهية", "score": 3}, "D": {"text": "بدنية/ذهنية", "score": 4}, "E": {"text": "إبداعية منتجة", "score": 5}}},
    {"id": 28, "text": "تعلم مهارة جديدة مجاناً؟", "options": {"A": {"text": "لا أختار", "score": 1}, "B": {"text": "شيء سهل", "score": 2}, "C": {"text": "تفيد عملي", "score": 3}, "D": {"text": "لغة جديدة", "score": 4}, "E": {"text": "برمجة/AI", "score": 5}}},
    {"id": 29, "text": "هدفك من السفر؟", "options": {"A": {"text": "التباهي", "score": 1}, "B": {"text": "التسوق", "score": 2}, "C": {"text": "الاستجمام", "score": 3}, "D": {"text": "السياحة", "score": 4}, "E": {"text": "استكشاف ثقافات", "score": 5}}},
    {"id": 30, "text": "تعريف النجاح؟", "options": {"A": {"text": "المال", "score": 1}, "B": {"text": "الشهرة", "score": 2}, "C": {"text": "السلطة", "score": 3}, "D": {"text": "الاستقرار", "score": 4}, "E": {"text": "الأثر والعلم", "score": 5}}}
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_answers[message.chat.id] = {"score": 0, "current_q": 0}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("ابدأ الاختبار 📝"))
    bot.send_message(message.chat.id, "أهلاً بك في محلل الشخصية!\nاضغط الزر بالأسفل للبدء.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "ابدأ الاختبار 📝")
def start_quiz(message):
    ask_question(message.chat.id, 0)

def ask_question(chat_id, index):
    if index >= len(questions):
        show_result(chat_id)
        return
    
    q = questions[index]
    markup = types.InlineKeyboardMarkup(row_width=1)
    for k, v in q['options'].items():
        markup.add(types.InlineKeyboardButton(f"{k}) {v['text']}", callback_data=f"ans_{v['score']}_{index}"))
    
    bot.send_message(chat_id, f"سؤال {q['id']}/30:\n\n{q['text']}", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def answer_handler(call):
    _, score, index = call.data.split('_')
    chat_id = call.message.chat.id
    
    if chat_id not in user_answers: user_answers[chat_id] = {"score": 0, "current_q": 0}
    user_answers[chat_id]['score'] += int(score)
    
    try: bot.delete_message(chat_id, call.message.message_id)
    except: pass
    
    ask_question(chat_id, int(index) + 1)

def show_result(chat_id):
    score = user_answers[chat_id]['score']
    
    # تحديد التحليل التفصيلي بناءً على النقاط
    if score <= 60:
        title = "🌱 الشخصية الطيبة الحذرة"
        desc = """
        أنت شخص مسالم جداً، تميل لتجنب المشاكل مهما كلف الأمر.
        قلبك طيب ولكنك قد تتردد في أخذ حقك خوفاً من المواجهة.
        تحتاج لتعزيز ثقتك بنفسك وقول "لا" في المواقف الصعبة.
        الناس يحبونك لكن البعض قد يطمع في طيبتك، فاحذر.
        """
    elif score <= 90:
        title = "⚖️ الشخصية المتوازنة الواقعية"
        desc = """
        أنت شخص تمسك العصا من المنتصف. لديك وعي جيد ولا تنجرف بسهولة.
        تحسب حساباً كبيراً لرأي الناس والمخاطر قبل أي خطوة.
        لست متهوراً ولكنك لست مغامراً كبيراً أيضاً.
        تفضل الاستقرار والهدوء على المخاطرة والمجد.
        """
    elif score <= 120:
        title = "🦁 الشخصية القوية الطموحة"
        desc = """
        تمتلك صفات القيادة والكرم بشكل واضح.
        أنت مثقف وتعرف ماذا تريد، ولا تخاف من المواجهة إذا لزم الأمر.
        لديك توازن رائع بين العقل والعاطفة، وتخطط لمستقبلك جيداً.
        شخصية يُعتمد عليها في الأزمات.
        """
    else:
        title = "👑 الشخصية القيادية النادرة (الزعيم)"
        desc = """
        أنت تمتلك كاريزما عالية جداً وشجاعة نادرة.
        كريم، مثقف، ولا تهزك الأزمات.
        الناس يعتمدون عليك في القرارات الصعبة ويرونك قائداً بالفطرة.
        طموحك ليس له حدود، وتترك أثراً في كل مكان تذهب إليه.
        """
        
    final_text = f"""
    ✅ النتيجة النهائية للاختبار:
    
    🏆 مجموع النقاط: {score} من 150
    
    🏷 نوع الشخصية: {title}
    
    📊 التحليل التفصيلي:
    {desc}
    """
    
    bot.send_message(chat_id, final_text)
    del user_answers[chat_id]

bot.infinity_polling()
