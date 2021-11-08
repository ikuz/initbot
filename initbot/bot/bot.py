from discord.ext.commands import Bot  # type: ignore

from discord import opus

from .config import CFG
from .commands import commands

bot = Bot(command_prefix="$")

OPUS_LIBS = [
    "libopus-0.x86.dll",
    "libopus-0.x64.dll",
    "libopus-0.dll",
    "libopus.so.0",
    "libopus.0.dylib",
]


def load_opus_lib():
    if opus.is_loaded():
        print("opus is loaded")
        return True

    print("opus not yet loaded")

    for opus_lib in OPUS_LIBS:
        try:
            opus.load_opus(opus_lib)
            return True
        except OSError:
            pass

        raise RuntimeError(
            "Could not load an opus lib."  # " Tried %s" % (", ".join(OPUS_LIBS))
        )


@bot.event
async def on_ready():
    print("Logged in")  # as {0.user}".format(bot))


def run():
    load_opus_lib()
    if not opus.is_loaded():
        print("Opus is not loaded")
    else:
        print("Opus is loaded")
    for cmd in commands:
        bot.add_command(cmd)
    bot.run(CFG.token)
