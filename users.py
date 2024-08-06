import random
dishs=[]
dish = ""
name=''
weight = ''
rost=''
text = """🖤 Ешьте больше овощей и фруктов. Они содержат много клетчатки, которая помогает чувствовать себя сытым дольше.
🖤 Пейте больше воды. Вода помогает ускорить метаболизм и уменьшить аппетит.
🖤 Уменьшите потребление сахара и жиров. Эти продукты содержат много калорий, но мало питательных веществ.
🖤 Занимайтесь физическими упражнениями регулярно. Это поможет сжечь лишние калории и укрепить мышцы.
🖤 Следите за размерами порций. Не переедайте, чтобы избежать переедания и лишних калорий.
🖤 Избегайте быстрых диет и экстремальных методов похудения. Они могут привести к негативным последствиям для здоровья.
🖤 Получайте достаточно сна каждый день. Недостаток сна может привести к увеличению веса.
🖤 Обратитесь к врачу или диетологу, если у вас есть проблемы со здоровьем или вы не знаете, как правильно питаться.
🖤 Не забывайте про мотивацию и поддержку близких людей. Похудение может быть трудным процессом, поэтому важно иметь поддержку и мотивацию для достижения цели.
"""
#infotexts
def get_sovet():
    soveti = [
        "Увеличить физическую активность. Регулярные тренировки помогут сжигать калории и укреплять мышцы.",
        "Сократить потребление калорий. Необходимо следить за количеством потребляемых калорий и стараться не превышать дневную норму.",
        "Употреблять больше белка. Белок помогает сохранять мышечную массу и ускоряет обмен веществ.",
        "Пить больше воды. Вода помогает ускорить метаболизм и уменьшить аппетит.",
        "Избегать перекусов между основными приемами пищи. Перекусы могут привести к избыточному потреблению калорий.",
        "Следить за размерами порций. Не переедайте, чтобы избежать переедания и лишних калорий.",
        "Избегать быстрых диет и экстремальных методов похудения. Они могут привести к негативным последствиям для здоровья.",
        "Получать достаточно сна каждый день. Недостаток сна может привести к увеличению веса.",
        "Обратиться к врачу или диетологу, если у вас есть проблемы со здоровьем или вы не знаете, как правильно питаться.",
        "Не забывать про мотивацию и поддержку близких людей. Похудение может быть трудным процессом, поэтому важно иметь поддержку и мотивацию для достижения цели."
    ]
    sovet = random.randint(0,9)
    return soveti[sovet]

