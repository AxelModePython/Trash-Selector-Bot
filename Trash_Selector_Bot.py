import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

sampah_data = {
    "plastik": {"kategori": "non-organik", "waktu_terurai": "100-500 tahun"},
    "kertas": {"kategori": "organik", "waktu_terurai": "2-5 tahun"},
    "kaca": {"kategori": "non-organik", "waktu_terurai": "tidak terurai"},
    "logam": {"kategori": "non-organik", "waktu_terurai": "tidak terurai"},
    "baterai": {"kategori": "non-organik", "waktu_terurai": "tidak terurai"},
    "kayu": {"kategori": "organik", "waktu_terurai": "5-10 tahun"},
    "makanan": {"kategori": "organik", "waktu_terurai": "1-2 tahun"},
    "daun": {"kategori": "organik", "waktu_terurai": "1-2 tahun"},
    "tulang": {"kategori": "organik", "waktu_terurai": "5-10 tahun"},
    }

@bot.event
async def on_ready():
    print(f'{bot.user} telah siap!')

@bot.command(name='sampah')
async def sampah(ctx, nama_sampah):
    if nama_sampah in sampah_data:
        kategori = sampah_data[nama_sampah]["kategori"]
        waktu_terurai = sampah_data[nama_sampah]["waktu_terurai"]
        await ctx.send(f'Sampah {nama_sampah} termasuk dalam kategori {kategori} dan dapat terurai dalam waktu {waktu_terurai}.')
    else:
        await ctx.send(f'Sampah {nama_sampah} tidak ditemukan.')

@bot.command(name='kategori')
async def kategori(ctx, kategori_sampah):
    # daftar_sampah = [nama_sampah for nama_sampah, data in sampah_data.items() if data["kategori"] == kategori_sampah]
    daftar_sampah = []
    
    for nama_sampah, data in sampah_data.items():
        if data["kategori"] == kategori_sampah:
            daftar_sampah.append(nama_sampah)
    
    if daftar_sampah:
        await ctx.send(f'Daftar sampah yang termasuk dalam kategori {kategori_sampah}: {", ".join(daftar_sampah)}')
    else:
        await ctx.send(f'Tidak ada sampah yang termasuk dalam kategori {kategori_sampah}.')

bot.run("Bot Token")
