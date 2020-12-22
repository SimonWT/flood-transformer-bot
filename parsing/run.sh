git clone https://github.com/Kosat/telegram-messages-dump.git
cd telegram-messages-dump
python -m telegram_messages_dump --chat="<chat_name>" -p <phone_number> -e csv --out="chat_history.csv"  -v -l 1000000000