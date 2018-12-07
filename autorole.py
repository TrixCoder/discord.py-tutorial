@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='rolename here')
    await client.add_roles(member, role)
