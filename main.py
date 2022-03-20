import discord
import time


class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("정상작동")

        await client.change_presence(status=discord.Status.online, activity=game)

        print("준비된")

    async def on_message(self, message):
        if message.author.bot:
            return None
        
        if message.content == "~채굴":
            channel = message.channel
            msg = "다이아몬드가 채굴되었습니다"
            await channel.send(msg)
            return None
        
        if message.content == "~도움":
            channel = message.channel
            msg = "```다이아몬드 인공지능의 도움말 (v0.1)\n~도움 : 도움말을 봅니다\n~채굴 : 채굴을 합니다\n~끝말잇기 : 끝말잇기를 합니다\n~tos : tos를 알려줍니다\n~주제 : 이 봇이 주제를 생각합니다 \n~움짤 : Tenor에서 움짤을 불러옵니다\n~비트박스 : 봇이 비트박스를 합니다.```"
            await channel.send(msg)
            return None

        if message.content == "~끝말잇기":
            channel = message.channel
            msg = "`봵`으로 시작하는 단어를 10초 이내로 사용하세요"
            await channel.send(msg)
            time.sleep(10)
            msg = "너님은`봵`으로 시작하는 단어를 입력하지 않았으므로 게임이 종료됩니다"
            await channel.send(msg)
            return None

        if message.content == "~tos":
            channel = message.channel
            msg = "https://discord.com/terms"
            await channel.send(msg)
            return None

        if message.content == "~주제":
            channel = message.channel
            msg = "주제를 생각하는 중입니다"
            await channel.send(msg)
            return None

        if message.content == "~움짤":
            channel = message.channel
            msg = "https://c.tenor.com/D1hkdg_7xzEAAAAS/%EC%9D%98%EC%82%AC%EC%96%91%EB%B0%98-%ED%8F%AD8.gif"
            await channel.send(msg)
            return None

        if message.content == "~비트박스":
            channel = message.channel
            msg = "연습 중인 비트박스에요. 북치기 박치기 북치기 박치기 박치기 북치기 박치기 북치기 "
            await channel.send(msg)
            return None

            
        
if __name__ == "__main__":
    client = chatbot()
    client.run("토큰")
