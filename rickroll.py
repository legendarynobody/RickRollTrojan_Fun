import win32gui
import win32api
import win32ui
import win32con
import time
import webbrowser


def draw_text(x, y, text, color, font, text_size):
    hdc = win32gui.GetDC(0)
    red, green, blue = color
    win32gui.SetBkMode(hdc, win32con.TRANSPARENT)  # Make the background transparent
    win32gui.SetTextColor(hdc, win32api.RGB(red, green, blue))
    
    # Create a LOGFONT structure to set the text size
    lf = win32gui.LOGFONT()
    lf.lfHeight = text_size  # Set the negative height to specify pixel size
    lf.lfFaceName = font  # Set the desired font name
    
    custom_font = win32gui.CreateFontIndirect(lf)  # Create the custom font
    
    win32gui.SelectObject(hdc, custom_font)  # Select the custom font
    
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    win32gui.DrawText(hdc, text, -1, (0, 0, screen_width, screen_height), win32con.DT_CENTER | win32con.DT_VCENTER)

    win32gui.ReleaseDC(0, hdc)

def goThroughList(texts):
    for text in texts:
        if text[0] == "open":
            webbrowser.open(text[1])
            time.sleep(50)
            continue
        win32gui.FillRect(hdc, (0, 0, screen_width, screen_height), 0x000000)
        timeUp = False
        start_time = time.time()
        while timeUp != True:
            draw_text(text_width, text_height, text, (red_text, green_text, blue_text), font, text_size)
            if time.time() - start_time > 3:
                timeUp = True

if __name__ == "__main__":
    hdc = win32gui.GetDC(0)
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # make empty screen
    #get device username
    username = win32api.GetUserName()
    
    blue_text = 50
    green_text = 0
    red_text = 0
    texts = [
        "Hello, " + username + "!",
        "I guess this\nis you, right?",
        "Wanna get 💰?",
        "Obviously: YES 👍",
        "Ok, listen " + username + ":\nI can help",
        "Visit:\nyoutube.com/watch\n?v=xvFZjo5PgG0",
        ["open", "https://www.youtube.com/watch?v=xvFZjo5PgG0"]
    ]
    texts += ["oh, almost forgot:\n\nJust Leave It..."] * 100
    font = "MS Sans Serif"  # Set the desired font name
    text_size = 200  # Set the desired text size in pixels
    
    text_width = screen_width // 2
    text_height = screen_height // 2
    goThroughList(texts)
