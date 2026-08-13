import pyautogui
import time

# 1. Safety and Configuration
# Disable the fail-safe (moving mouse to corner to abort) if desired
# pyautogui.FAILSAFE = False

# 2. Mouse Control
# Get screen size and current mouse position
screen_width, screen_height = pyautogui.size()
current_x, current_y = pyautogui.position()
print(f"Screen size: {screen_width}x{screen_height}, Current position: ({current_x}, {current_y})")

# Move mouse to specific coordinates (e.g., center of screen)
center_x, center_y = screen_width // 2, screen_height // 2
pyautogui.moveTo(center_x, center_y, duration=1) # duration=1 moves over 1 second

# Click and double-click
pyautogui.click() # Click at current position
pyautogui.doubleClick() # Double-click at current position

# 3. Keyboard Control
# Type text with a delay between keystrokes
pyautogui.write('Hello, PyAutoGUI!', interval=0.1)

# Simulate key presses (e.g., press En   