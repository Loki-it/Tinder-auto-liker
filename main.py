import pyautogui
from PIL import ImageGrab
import time
import random

target_color = (0, 207, 110)  # RGB del verde di Tinder
tolerance = 30  # Tolleranza per le variazioni di colore

def color_match(color1, color2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def find_and_click_heart():
    while True:
        screenshot = ImageGrab.grab()
        width, height = screenshot.size
        for x in range(width):
            for y in range(height):
                pixel_color = screenshot.getpixel((x, y))
                if color_match(pixel_color, target_color, tolerance):
                    # Muovi e cliccaaa
                    pyautogui.moveTo(x, y)
                    pyautogui.click()
                    print(f"Cuore verde trovato e cliccato! ({x}, {y})")
                    return
        print("Cuore verde non trovato. Riprovo...")

def auto_like(interval):
    try:
        while True:
            find_and_click_heart()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Script interrotto dall'utente.")

if __name__ == "__main__":
    interval = random.randrange(0,1) # Qui imposta il tempo che vuoi
    print("Avvio dello script di auto-like. Premi Ctrl+C per interrompere.")
    auto_like(interval)
