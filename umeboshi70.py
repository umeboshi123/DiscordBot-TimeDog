import discord  # 1.0.1
import datetime

client = discord.Client()
pretime_dict = {}


@client.event
async def on_voice_state_update(member, before, after):
    if(before.channel is None):
        pretime_dict[member.name] = datetime.datetime.now()
        reply_text = str(member.name) + "  " + \
            str(after.channel.name) + ":Enter"
    elif(after.channel is None):
        duration = (datetime.datetime.now()-pretime_dict[member.name]).total_seconds()
        time_hour = int(duration/3600)
        time_min = int((duration-time_hour*3600)/60)
        time_s = int(duration-time_hour*3600-time_min*60)

        reply_text = str(member.name) + "  " + str(before.channel.name) + \
            ":Exit   Duration:" + str(time_hour) + \
            "h"+str(time_min)+"m"+str(time_s)+"s"
    print(reply_text)
    channel = client.get_channel("input voice channel ID")
    await channel.send(reply_text)
client.run("Input your bot TOKEN")
