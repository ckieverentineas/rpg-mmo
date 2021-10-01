from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def keyboards(text):
    config = {
        "начать": keyboard_register,
        "профиль": keyboard_profile,
        "назад": keyboard_back,
        "+атк": keyboard_points_up,
        "+защ": keyboard_points_up,
        "+лвк": keyboard_points_up,
        "+инт": keyboard_points_up,
        "+здр": keyboard_points_up,
        "сброс": keyboard_points_up
    }
    try:
        keyboards = config[text.lower()]()
        return keyboards
    except KeyError as e:
        print(f'Not found action for {e}')
        return False

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
    keyboards.add_button('+защ', color=VkKeyboardColor.POSITIVE)
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
    keyboards.add_button('+защ', color=VkKeyboardColor.POSITIVE)
    keyboards.add_button('Назад', color=VkKeyboardColor.SECONDARY)
    return keyboards

def keyboard_back():
    keyboards = VkKeyboard(one_time=True)
    keyboards.add_button('Профиль', color=VkKeyboardColor.POSITIVE)
    keyboards.add_line()
    keyboards.add_button('Исследовать', color=VkKeyboardColor.POSITIVE)
    return keyboards