"""CoronaVirus LookUp
Syntax: .coronavirus <country>"""
from covid import Covid
from telethon import events
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


from telebot import CMD_HELP


@telebot.on(admin_cmd(pattern="coronavirus (.*)"))
@telebot.on(sudo_cmd(pattern="coronavirus (.*)", allow_sudo=True))
async def _(event):
    covid = Covid()
    data = covid.get_data()
    country = event.pattern_match.group(1)
    country_data = get_country_data(country, data)
    output_text = ""
    for name, value in country_data.items():
        output_text += "`{}`: `{}`\n".format(str(name), str(value))
    await eor(
        event,
        "**CoronaVirus Info in {}**:\n\n{}".format(country.capitalize(), output_text),
    )


def get_country_data(country, world):
    for country_data in world:
        if country_data["country"].lower() == country.lower():
            return country_data
    return {"Status": "No information yet about this country!"}


CMD_HELP.update(
    {
        "coronavirus": ".coronavirus <country name>\nUse - Get covid status of that country"
    }
)
"""CoronaVirus LookUp
Syntax: .coronavirus <country>"""
from covid import Covid
from telethon import events
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from telebot import CMD_HELP

@telebot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@telebot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "`📊Collecting data...........`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n☹️New Deaths : <code>{country_data['new_deaths']}</code>"
        await catevent.edit(
            "<b>Corona Virus Info of {}. By: [💛 🇧 🇷 🇺 🇨 🇪  🇱🇰💛](t.me/BruceSL)\n{}</b>".format(country, data),
            parse_mode="html",
        )
    
    


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n**Syntax : **`.covid <country name>`\
        \n**Function :** __Get an information about covid-19 data in the given country.__\
        \n\n**Syntax : **`.covid <state name>`\
        \n**Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
