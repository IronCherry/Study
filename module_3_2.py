my_message = input("Введите сообщения для отправления : ")
my_recipient = input('Укажите адресс для отправления : ')
count_sender = "university.help@gmail.com"


def send_email(message, recipient, *, sender):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    if '@' not in recipient or (".com" not in recipient and ".ru" not in recipient and ".net" not in recipient):
        print(f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}.')
    if '@' not in sender or (".com" not in sender and ".ru" not in sender and ".net" not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email(my_message, my_recipient, sender="urban.info@gmail.com")
