import dogehouse
import requests as r
import environ
import os
import keep_alive
import json

token = os.environ.get('TOKEN')
refresh_token = os.environ.get('REFRESH_TOKEN')


class Client(dogehouse.DogeClient):
    @dogehouse.event
    async def on_ready(self):
        print(f"Logged on as {self.user.username}")
        await self.create_room("Bot Room || Jokes || Facts & more..")
        # await self.join_room("1fbb7d1e-d3b1-43ae-9854-06cd9231fe50")
        print("Joined")

    @dogehouse.event
    async def on_message(self, message):
        # if message.author.id == self.user.id:
        #     return

        if message.content.startswith("hi"):
            await self.send("sup , how are ya")

    @dogehouse.command
    async def help(self, ctx):
        whisper_that_g = [ctx.author.id]
        await self.send(message="Cmds -> !hanimal , !hcryptog , !hjoke",
                        whisper=whisper_that_g)

    @dogehouse.command
    async def hanimal(self, ctx):
        whisper_that_g = [ctx.author.id]
        await self.send(
            message=
            "!catfact, !dogfact, !pandafact, !foxfact, !birdfact, !koalafact",
            whisper=whisper_that_g)

    @dogehouse.command
    async def hcryptog(self, ctx):
        whisper_that_g = [ctx.author.id]
        await self.send(message="!encode <msg>, !decode <msg>",
                        whisper=whisper_that_g)

    @dogehouse.command
    async def hjoke(self, ctx):
        whisper_that_g = [ctx.author.id]
        await self.send(message="!joke", whisper=whisper_that_g)

    @dogehouse.command
    async def hello(self):
        await self.send("Hello!")

    # @dogehouse.command
    # async def ping(self, ctx):
    #     await self.send(f"Hello {ctx.author.mention}")

    @dogehouse.command
    async def catfact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/cat").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def dogfact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/dog").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def pandafact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/panda").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def foxfact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/fox").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def birdfact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/bird").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def koalafact(self, ctx):
        resp = r.get("https://some-random-api.ml/facts/koala").json()
        await self.send(message=f"{resp['fact']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def encode(self, ctx, *, encode_msg="no_msg"):
        resp = r.get(
            f"https://some-random-api.ml/base64?encode={encode_msg}").json()
        await self.send(message=f"->  {resp['base64']}",
                        whisper=[ctx.author.id])

    @dogehouse.command
    async def decode(self, ctx, *, decode_msg="bm8gbXNn"):
        resp = r.get(
            f"https://some-random-api.ml/base64?decode={decode_msg}").json()
        await self.send(message=f"->  {resp['text']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def joke(self, ctx):
        resp = r.get(f"https://v2.jokeapi.dev/joke/Any?type=single").json()
        await self.send(message=f"{resp['joke']}", whisper=[ctx.author.id])

    @dogehouse.command
    async def reg(self, ctx, *, act):
        with open("currentAct.json", "r") as f:
            reg = json.load(f)
        reg['Activity'] = act
        with open("currentAct.json", "w+") as f:
            json.dump(reg, f, indent=4)
            await self.send(message=f"Done!!, Actvity Changed To -> {act}",
                            whisper=[ctx.author.id])

    @dogehouse.command
    async def what_we_doin(self, ctx):
        with open("currentAct.json", "r") as f:
            reg = json.load(f)
            actv = reg['Activity']

            await self.send(message=f'->  {actv}', whisper=[ctx.author.id])

    @dogehouse.command
    async def source(self, ctx):
        url = 'https://github.com/DHRUV-CODER/DogeHouse-Bot'
        await self.send(message=f'->  {url}', whisper=[ctx.author.id])

    # @dogehouse.event
    # async def on_error(self,error):
    #     await self.send(f"oops -> {error}")
    #     print(f"-> {error}")

    @dogehouse.event
    async def on_user_join(self, user):
        userNameToWhisper = [user.id]
        await self.send(
            message=
            f"welcome `{user.username}` !! , Pls Type `!help` For More Info & Btw If Udk What We Doin Type -> `!what_we_doin`",
            whisper=userNameToWhisper)

    # @dogehouse.event
    # async def on_user_leave(self,user):
    #     await self.send(f"{user.username} Just Left")


keep_alive.keep_alive()

if __name__ == "__main__":
    Client(token, refresh_token, prefix="!").run()
