from ..utils import admin_cmd
@borg.on(admin_cmd(pattern="drink", outgoing=True))
async def _(event):
    a = await bot.get_me()
    phune = a.phone
    await bot.send_message(event.chat_id, phune)
