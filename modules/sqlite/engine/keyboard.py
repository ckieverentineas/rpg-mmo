from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def keyboards(text):
    config = {
        "начать": keyboard_register,
        "профиль": keyboard_profile,
        "назад": keyboard_back,
        "+ур": keyboard_back,
        "-ур": keyboard_back,
        "+атк": keyboard_points_up,
        "+фзащ": keyboard_points_up,
        "+мзащ": keyboard_points_up,
        "+лвк": keyboard_points_up,
        "+инт": keyboard_points_up,
        "+здр": keyboard_points_up,
        "сброс": keyboard_points_up,
        "исследовать": keyboard_battle,
        "атака": keyboard_battle,
        "руна": keyboard_rune,
        "надеть": keyboard_rune,
        "снять": keyboard_rune,
        "сломать": keyboard_altar,
        "+руна": keyboard_rune,
        "-руна": keyboard_rune,
        "++руна": keyboard_altar,
        "--руна": keyboard_altar,
        "wipe": keyboard_profile,
        "алтарь": keyboard_altar,
        "создать": keyboard_altar,
        "изменить руну": keyboard_altar_rune_rerol,
        "~+руна": keyboard_altar_rune_rerol,
        "~-руна": keyboard_altar_rune_rerol,
        "~атк": keyboard_altar_rune_rerol,
        "~фзащ": keyboard_altar_rune_rerol,
        "~мзащ": keyboard_altar_rune_rerol,
        "~лвк": keyboard_altar_rune_rerol,
        "~инт": keyboard_altar_rune_rerol,
        "~здр": keyboard_altar_rune_rerol,
        "+ур10": keyboard_back,
        "-ур10": keyboard_back,
        "+ур100": keyboard_back,
        "-ур100": keyboard_back,
        "спелл": keyboard_battle,
        "инвентарь": keyboard_back
    }
    try:
        keyboards = config[text.lower()]()
        return keyboards
    except KeyError as e:
        print(f'Not found action for {e}')
        return False

def keyboard_lvl():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('-ур10', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+ур10', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('-100', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+100', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('-ур', color=VkKeyboardColor.SECONDARY)
    keyboards.add_button('+ур', color=VkKeyboardColor.SECONDARY)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_register():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Профиль', color=VkKeyboardColor.NEGATIVE)
    return keyboards

def keyboard_profile():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('+атк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+здр', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('+лвк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+инт', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('+фзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+мзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('СБРОС', color=VkKeyboardColor.NEGATIVE)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_points_up():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Профиль', color=VkKeyboardColor.PRIMARY)
    keyboards.add_line()
    keyboards.add_button('+атк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+здр', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('+лвк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+инт', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('+фзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('+мзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_back():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Профиль', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('Инвентарь', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('Алтарь', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('Руна', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('Исследовать', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('-ур', color=VkKeyboardColor.SECONDARY)
    keyboards.add_button('+ур', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_battle():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Атака', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('Спелл', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('Исследовать', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('-ур', color=VkKeyboardColor.SECONDARY)
    keyboards.add_button('+ур', color=VkKeyboardColor.SECONDARY)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_rune():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Надеть', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('Снять', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('-Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_button('+Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_altar():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Изменить руну', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('СОЗДАТЬ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('--Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_button('++Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_line()
    keyboards.add_button('СЛОМАТЬ', color=VkKeyboardColor.NEGATIVE)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_altar_rune_rerol():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('~атк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('~здр', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('~лвк', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('~инт', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('~фзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('~мзащ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('~-Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_button('~+Руна', color=VkKeyboardColor.PRIMARY)
    keyboards.add_line()
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards