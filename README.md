Сервер точного времени, который врет на указанное кол-во секунд в конфигурационном файле. 

Сервер работает по протоколу udp и прослушивает 123 порт.
Механизм работы: на любой запрос от клиента сервер отвечает сообщением в котором указана текущее время + кол-во секунд указанное в конфигурационном файле. 

Сервер запускается командой в терминале - sudo python3 time_server.py

Перед использованием измените кол-во секунд на которое будет врать сервер. 

