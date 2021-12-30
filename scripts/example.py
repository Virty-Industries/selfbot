@virty.command()
async def example(ctx):
    await ctx.message.delete()
    await ctx.send("Love Virty")
    