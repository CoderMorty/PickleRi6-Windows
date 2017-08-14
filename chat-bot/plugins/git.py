from plugin import Plugin
import random

class Git(Plugin):

    fancy_name='Git Repo'

    async def get_commands(self, server):
        commands = [
            {
                'name': '!git',
                'description': 'Links to Mee6\'s Github page.'
            },
        ]
        return commands

    async def on_message(self, message):

        flavortext = [
            "Wubba lubba dub dub! Here is my source-code!",
            "Make sure you grab me the screwdriver while you're in there.",
            "Don't mess anything up.",
            "If you must know, here is my source-code."
            ]

        if message.content == '!git':
            await self.mee6.send_message(
                message.channel,
                '{}\nhttps://github.com/Bourbbbon/PickleRi6/'.format(
                random.choice(flavortext)
                )
             )
