# phoney
## The mouse and keyboard you always have one you

You can use your phone as a mouse and keyboard, no applications needed. 

Run phoney on your PC or laptop and connect to you PC from your phone. Phoney uses websockets to connect your phone to your computer, providing smooth HID movement.

Currently the keyboard functionality uses 'pyautogui'. In future I would like to change this, but for now that is how it is. Unfortunately, this means you will need 'python3-xlib'.

I have added nothing in the way of Windows support so far. Please feel free to do that :)

NOTE: This is a proof of concept right now. There are and should be obvious security concerns. The Flask server currently has no authentication, and as such any connection to this server basically has direct and full access to your computer's mouse and keyboard.
