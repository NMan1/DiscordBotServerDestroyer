from discord.ext import commands
from authority import auth


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return
        # elif isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.MissingPermissions):
        #     print("Missing Perms Error...")
        #     if ctx.command.qualified_name == 'm':
        #         print("Came from 'member' command")
        #         return
        #     elif ctx.command.qualified_name == 'c':
        #         print("Came from 'channel' command")
        #         return
        #     elif ctx.command.qualified_name == 'r':
        #         print("Came from 'run' command")
        #         return
        # elif isinstance(error, commands.BadArgument):
        #     if ctx.command.qualified_name == 'm':
        #         print("Came from 'member' command")
        #         return
        #     elif ctx.command.qualified_name == 'c':
        #         print("Came from 'channel' command")
        #         return
        #     elif ctx.command.qualified_name == 'r':
        #         print("Came from 'run' command")
        #         return
        else:
            print(error)
            if ctx.command.qualified_name == 'm':
                print("Came from 'member' command\n")
                return
            elif ctx.command.qualified_name == 'c':
                print("Came from 'channel' command\n")
                return
            elif ctx.command.qualified_name == 'r':
                print("Came from 'run' command\n")
                await auth.run(ctx=ctx)

            return


def setup(client):
    client.add_cog(CommandErrorHandler(client))
