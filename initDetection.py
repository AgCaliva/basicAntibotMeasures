from pynput import keyboard

# Define the LLKHF_INJECTED flag value (hex 0x10)
LLKHF_INJECTED = 0x10


def win32_event_filter(msg, data):
  # data is a pointer/structure containing the KBDLLHOOKSTRUCT flags
  is_injected = bool(data.flags & LLKHF_INJECTED)

  if is_injected:
    print(f'[!] Fake/Injected input detected! (Flags: {data.flags:#x})', flush=True)
  else:
    print(f'[x] Physical hardware input (Flags: {data.flags:#x})', flush=True)

  # Return True to process normally, or False to swallow/ignore event
  return True


def on_press(key):
  pass  # Handle standard press events here


# Attach the filter to the listener
with keyboard.Listener(
    on_press=on_press, win32_event_filter=win32_event_filter
) as listener:
  listener.join()
