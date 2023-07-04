# WhatsAppReplyBot

WhatsAppReplyBot is a Python script that utilizes Selenium WebDriver to automate message replying on WhatsApp Web. The bot can be customized to reply to specific messages or provide a general auto-reply for any incoming message.

## Features

- Allows auto-replying to messages on WhatsApp Web
- Supports targeting specific contacts or groups
- Can be customized to reply to specific messages or provide a default reply
- Utilizes Selenium WebDriver for browser automation

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ````
   pip install selenium
   ```
3. Download the appropriate WebDriver for your browser:
   - [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases)
4. Set the `PATH` variable in the script to the location of your browser WebDriver executable.
5. Update the `target` variable with the name of the contact or group you want to auto-reply to.
6. Customize the messages and conditions for replying, if necessary.
7. Run the script:
   ````
   python whatsapp_auto_reply_bot.py
   ```

Once the script is running, it will open WhatsApp Web and start auto-replying to messages based on your configurations.

**Note**: You will need to scan the QR code on WhatsApp Web with your phone to log in.
