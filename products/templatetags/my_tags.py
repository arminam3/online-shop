from django import template

register = template.Library()

@register.filter(name='e2f')
def english_numbers_convertor(number):
    persian_num = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in persian_num.items():
        # global f_number
        number = str(number).replace(e, p)

    triple = (len(number) - 1) // 3
    f_number_list = list(number)

    jobran = 0
    for i in range(triple):
        f_number_list.insert(-((i+1)*3) + jobran, ',')
        jobran -= 1
    # f_number_list.reverse()

    number_splited = ''
    for j, index in enumerate(f_number_list):
        number_splited += f_number_list[j]

    return number_splited