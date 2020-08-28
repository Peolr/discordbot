import sqlite3
import discord


class BotDB:
    def __init__(self):
        self.conn = sqlite3.connect("main.db")
        c = self.conn.cursor()

        c.execute('''
        CREATE TABLE IF NOT EXISTS servers (
            servername text,
            guild_id int64 PRIMARY KEY,
            added DATETIME DEFAULT CURRENT_TIMESTAMP
        );''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS polls (
            servername text,
            guild_id int64 PRIMARY KEY,
            added DATETIME DEFAULT CURRENT_TIMESTAMP
        );''')
        self.conn.commit()

    def checkserver(self, g : discord.Guild):
        c = self.conn.cursor()

        c.execute(f"SELECT servername FROM servers WHERE guild_id=?;", (g.id,))
        result = c.fetchone()
        if result is None:
            c.execute(f"INSERT INTO servers (servername, guild_id) VALUES (?, ?); ", (g.name, g.id))
        elif result[0] != g.name:
            c.execute(f"UPDATE servers SET servername=? WHERE guild_id=?", (g.name, g.id))

        self.conn.commit()
