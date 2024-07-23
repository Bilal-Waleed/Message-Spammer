import pyautogui
import time
import threading

stop_flag = False

def send_whatsapp_message(message, count):
    global stop_flag
    for _ in range(count):
        if stop_flag:
            print("Stopped by user.")
            break
        pyautogui.typewrite(message)  
        pyautogui.press("enter")      
        time.sleep(0.3)              

def stop_sending():
    global stop_flag
    input("Press Enter to stop...")
    stop_flag = True

# Message to send
message = "How are you..."
message_count = 100


print("You have 10 seconds to switch to WhatsApp Web and open the chat...")
stop_thread = threading.Thread(target=stop_sending)
stop_thread.start()
time.sleep(10)

send_whatsapp_message(message, message_count)

print("Messages sent or stopped.")
