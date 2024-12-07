
# Copywrite reserved @2024 Ahmad Zubair Amini

pashto_to_english = {
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
}

english_to_pashto = {
    '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
}

def convert_to_english(num):
    result = ""
    for char in str(num):
        if char in pashto_to_english:
            result += pashto_to_english[char]
        else:
            result += char  
    return result


def convert_to_pashto(num):
    result = ""
    for char in str(num):
        if char in english_to_pashto:
            result += english_to_pashto[char]
        else:
            result += char  
    return result

def num_to_pashto(num, level=0):
    if num is None:
        return ""
    
    if isinstance(num, str):
        num = float(convert_to_english(num))

    if num.is_integer():
        num = int(num)

    if num < 0:
        num = -num
        return "منفی " + num_to_pashto(num, level)
    
    if num == 0:
        return "صفر" if level == 0 else ""
 
    result = ""
    yekan = ["یو", "دوه", "دری", "څلور", "پينځه", "شپږ", "اوه", "اته", "نه"]
    dahgan = ["شل", "دیرش", "څلویښت", "پنځوس", "شپیته", "اویا", "اتیا", "نوی"]
    sadgan = ["سل", "دوه سوه", "دری سوه", "څلور سوه", "پنځه سوه", "شپږ سوه", "اوه سوه", "اته سوه", "نه سوه"]
    dah = ["لس", "یوولس", "دولس", "دیارلس", "څوارلس", "پنځلس", "شپاړلس", "اوه لس", "اتلس", "نولس"]
    
    if num < 10:
        result += yekan[int(num) - 1]
    elif num < 20:
        result += dah[int(num) - 10]
    elif num < 100:
        units = int(num) % 10
        tens = int(num) // 10
        if tens == 2:
            if units == 0:
                result += "شل"
            else:
                result += yekan[units - 1] + " " + "ویشت"
        else:
            if units != 0:
                result += yekan[units - 1] + " " + dahgan[tens - 2]
            else:
                result += dahgan[tens - 2]
    elif num < 1000:
        if num // 100 == 1:
            result += "یو سل"
        else:
            result += sadgan[num // 100 - 1]
        if num % 100 != 0:
            remainder = num % 100
            result += " و " + num_to_pashto(remainder, level + 1)
    elif num < 100000:
        result += num_to_pashto(num // 1000, level + 1) + " زره"
        if num % 1000 != 0:
            result += " و " + num_to_pashto(num % 1000, level + 1)
    elif num < 10000000:
        result += num_to_pashto(num // 100000, level + 1) + " لکه"
        if num % 100000 != 0:
            result += " و " + num_to_pashto(num % 100000, level + 1)
    elif num < 1000000000:
        result += num_to_pashto(num // 10000000, level + 1) + " میلیون"
        if num % 10000000 != 0:
            result += " و " + num_to_pashto(num % 10000000, level + 1)
    else:
        result += num_to_pashto(num // 1000000000, level + 1) + " میلیارد"
        if num % 1000000000 != 0:
            result += " و " + num_to_pashto(num % 1000000000, level + 1)


    if '.' in str(num):
        whole, fractional = str(num).split('.')
        whole_part = num_to_pashto(int(whole))
        result = whole_part + " اعشاریه"
        for digit in fractional:
            result += " " + yekan[int(digit) - 1]
    
    return result.strip()



