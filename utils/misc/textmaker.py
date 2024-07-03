def makeUser(users):
    text = ""
    for user in users:
        text+=f"userID: {user.id}\n"
        text+=f"To'liq ismi: {user.fullname}\n"
        if user.username:
            text+=f"Foydalanuvchi nomi: @{user.username}\n"
        else:
            text+=f"Foydalanuvchi nomi: {user.username}\n"
        if user.is_admin:
            text+=f"Status: 👨‍💻 Admin\n"
        else:
            text+=f"Status: 👤 Oddiy foydalanuvchi\n"
        
        text+=f"Sana (UZB vaqti): {user.date_joined}\n\n"
    with open("data/users/users.txt", "w+", encoding='utf-8') as file:
        file.write(text)
    return text

def makeService(services):
    text = ""
    for service in services:
        text += f"<b>ID</b>: {service.id}\n"
        text += f"<b>Nomi</b>: {service.name}\n"
        text += f"<b>Xizmat uchun foiz</b>: {service.percent}%\n\n"
    return text

def makeChannel(channels):
    text = ""
    for channel in channels:
        text += f"<b>ID</b>: <code>{channel.id}</code>\n"
        text += f"<b>Nomi</b>: {channel.name}\n"
        text += f"<b>Sana (UZB vaqti)</b>: {channel.date}\n"
    return text