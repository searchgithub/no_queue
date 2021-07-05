import keyboard
import pyautogui, win32gui, time, random, json

# x,y = pyautogui.locateCenterOnScreen("entergame.png")
# print(x,y)
# pyautogui.click(x,y)
loop_flag = True


def set_loop_flag():
    global loop_flag
    loop_flag = False


def reg_hotkey():
    keyboard.add_hotkey('ctrl+y', set_loop_flag)


def open_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        config_json = json.load(f)
        print(json.dumps(config_json, indent=2))
        return config_json


def loop_aciton():
    # Get the config
    config_json = open_config()
    window_list = []
    while True:
        window = win32gui.FindWindow(None, config_json['caption'])
        if window == 0:
            print("There is no windows founding! exit.")
            break
        else:
            window_list.append(window)
            win32gui.SetWindowText(window, "TempWindowName")
    # Set window name back to original
    for i, win in enumerate(window_list):
        print(f"第{i + 1}个窗口:")
        win32gui.SetWindowText(win, config_json['caption'])
    # Loop the click action for the windows
    while True:
        for i, win in enumerate(window_list):
            print("beg" + "=" * 10)
            print(f"第{i + 1}个窗口:")
            win32gui.SetForegroundWindow(win)
            pyautogui.moveTo(20 + 200 * i, 30 + 200 * i)
            for act in config_json['action_list']:
                print(act['key'])
                print_str = act['key']
                if print_str == " ":
                    print_str = "SPACE"
                print("Do the action:" + print_str)
                pyautogui.press(act['key'])
                step_sleep_sec = config_json['step_base_second'] + random.randint(
                    config_json['step_random_start'] * 1000,
                    config_json[
                        'step_random_end'] * 1000) / 1000
                time.sleep(step_sleep_sec)
            print("end" + "=" * 10)
        window_sleep_sec = config_json['window_base_second'] + random.randint(config_json['window_random_start'] * 1000,
                                                                              config_json[
                                                                                  'window_random_end'] * 1000) / 1000
        if loop_flag == False:
            print("The loop_flag is False, break!")
            break
        print("Window sleep sec is :", window_sleep_sec)
        time.sleep(window_sleep_sec)


if __name__ == '__main__':
    reg_hotkey()
    loop_aciton()
