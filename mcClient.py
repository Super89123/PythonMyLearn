from mcproto import Connection, Buffer
from mcproto.packets import Packet, PacketDirection, PacketState
from mcproto.packets.handshaking import Handshake, NextState
from mcproto.packets.login.clientbound import LoginSuccess
from mcproto.packets.login.serverbound import LoginStart
from mcproto.packets.status.clientbound import StatusResponse
from mcproto.packets.status.serverbound import StatusRequest
from mcproto.packets.play.clientbound import ChatMessagePacket
from mcproto.packets.play.serverbound import ChatMessageServerboundPacket

# Подключение к серверу
def connect_to_server(host: str, port: int, username: str):
    # Создаем соединение
    conn = Connection((host, port))

    # Шаг 1: Handshake
    handshake = Handshake(
        protocol_version=757,  # Версия протокола (например, 757 для 1.18.1)
        server_address=host,
        server_port=port,
        next_state=NextState.LOGIN
    )
    conn.write_packet(handshake)

    # Шаг 2: Login Start
    login_start = LoginStart(username=username)
    conn.write_packet(login_start)

    # Шаг 3: Ожидание ответа от сервера
    while True:
        packet = conn.read_packet()
        if isinstance(packet, LoginSuccess):
            print("Успешный вход на сервер!")
            break

    # Переход в состояние PLAY
    conn.state = PacketState.PLAY

    # Шаг 4: Отправка сообщения в чат
    chat_message = ChatMessageServerboundPacket(message="Привет, это Python клиент!")
    conn.write_packet(chat_message)

    # Шаг 5: Чтение сообщений из чата
    while True:
        packet = conn.read_packet()
        if isinstance(packet, ChatMessagePacket):
            print(f"Сообщение из чата: {packet.message}")

if __name__ == "__main__":
    connect_to_server("localhost", 25565, "PythonUser")