import sys
import time
import pytesseract
from PIL import ImageGrab, Image
import pyperclip
import keyboard

HOTKEY = "ctrl+alt+o"
QUIT_HOTKEY = "ctrl+alt+q"
LANG = "eng"
PSM = 6

def ocr_from_clipboard():
    """
    1) Read the current clipboard
    2) If it holds an image, OCR it
    3) Copy recognized text back to clipboard
    """
    try:
        clip = ImageGrab.grabclipboard()

        if isinstance(clip,Image.Image):
            pil_img = clip
        
        config = f"--oem 3 --psm {PSM}"
        text = pytesseract.image_to_string(pil_img, lang=LANG, config=config)

        cleaned = text.strip()
        if cleaned:
            pyperclip.copy(cleaned)
            print(f"\ntext has been copied!")
    except Exception as e:
        print(e)

def main():
    print(f"OCR Clipboard tool running!")
    print(f"Take a screenshot (e.g., Win+Shift+S on Windows), then press {HOTKEY} to OCR.")

    keyboard.add_hotkey(HOTKEY, ocr_from_clipboard)
    
    keyboard.wait(QUIT_HOTKEY)
    print(f"Exiting...")
    sys.exit(0)

if __name__ == "__main__":
    main()
