from src.handlers import bot


def main() -> None:
    """
    Main function to run the bot and handle updates.

    Prints "Bot successfully launched! Waiting for updates..."

    Returns:
        None
    """
    print("Bot successfully launched! Waiting for updates...")

    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")


if __name__ == "__main__":
    main()
