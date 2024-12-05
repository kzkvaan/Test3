
def count_letters(main_str):
    main_str = main_str.lower()
    letter_count = {}
    for char in main_str:
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1

    return letter_count

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())  # суммируем все значения в словаре
    frequency_dict = {}
    for letter, count in letter_count.items():
                frequency = count / total_letters
                frequency_dict[letter] = f"{frequency:.2f}"  # Принудительно 2 знака после запятой

    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_counts = count_letters(main_str) # словарь с подсчетом букв

letter_frequencies = calculate_frequency(letter_counts) # словарь частот по букве

for letter, frequency in (letter_frequencies.items()): #letter - как ключ (буква) frequency как значение (частоты
    print(f"{letter}: {frequency}")

# TODO Распечатайте в столбик букву и её частоту в тексте
