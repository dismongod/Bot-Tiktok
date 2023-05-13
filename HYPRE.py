import interactions
import sys
import os
import time
import requests as ru
import requests
from re import search
from requests import Session, post, get
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs
from re import search
from user_agent import generate_user_agent
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed


guild_id = 999 #ไอดีเซิฟเวอร์ที่จะใช้งานบอท
threading = ThreadPoolExecutor(max_workers=int(100000))
client = interactions.Client("โทเค่นบอท", intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)

@client.event
async def on_start():
	print('Online !')
	
@client.command(name="views", description="ปั๊มวิว tiktok ", scope=guild_id)
async def views(ctx: CommandContext):
	modal = Modal(
		custom_id="start-view",
		title="TIKTOK AUTO VIEWS",
		components=[
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-1",
				label=f"URL",
				placeholder="https://vt.tiktok.com/",
			),
		],
	)
	await ctx.popup(modal)
	
@client.command(name="follows", description="ปั๊มฟอล tiktok ", scope=guild_id)
async def follows(ctx: CommandContext):
	modal = Modal(
		custom_id="start-foll",
		title="TIKTOK AUTO FOLLOWS",
		components=[
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-1",
				label=f"URL",
				placeholder="https://www.tiktok.com/",
			),
		],
	)
	await ctx.popup(modal)
	
@client.command(name="share", description="ปั๊มแชร์ tiktok ", scope=guild_id)
async def share(ctx: CommandContext):
	modal = Modal(
		custom_id="start-share",
		title="TIKTOK AUTO SHARE",
		components=[
			TextInput(
				style=TextStyleType.SHORT,
				custom_id="text-input-1",
				label=f"URL",
				placeholder="https://vt.tiktok.com/",
			),
		],
	)
	await ctx.popup(modal)
	
@client.modal("start-share")
async def share(ctx: CommandContext, one):
	data = one
	if "https://vt.tiktok.com/" in one:
		cvb(data)
		embed = interactions.Embed(
			title="successfully",
			description="รอรับยอดแชร์..",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)
	else:
		embed = interactions.Embed(
			title="⚠️ ข้อมูลของคุณผิดพลาด",
			description="เนื่องจากคุณระบุลิงก์ไม่ถูกต้อง",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)
		
@client.modal("start-foll")
async def foll(ctx: CommandContext, one):
	action = one
	if "https://www.tiktok.com/" in one:
		ceng(action)
		embed = interactions.Embed(
			title="successfully",
			description="รอรับยอดฟอล..",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)
	else:
		embed = interactions.Embed(
			title="⚠️ ข้อมูลของคุณผิดพลาด",
			description="เนื่องจากคุณระบุลิงก์ไม่ถูกต้อง",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)


	
@client.modal("start-view")
async def cum(ctx: CommandContext, one):
	url = one
	if "https://vt.tiktok.com/" in one:
		letGoo(url)
		embed = interactions.Embed(
			title="successfully",
			description="รอรับยอดวิว..",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)
	else:
		embed = interactions.Embed(
			title="⚠️ ข้อมูลของคุณผิดพลาด",
			description="เนื่องจากคุณระบุลิงก์ไม่ถูกต้อง",
			color=0xfcfc03
		)
		await ctx.send(embeds=embed)


def cang(url):
	requests.post('https://iplusview.store/api', json={"key": "8f39e0660e829f2dbea6cd7d55026d17","action": "add","service": "1367","link": url,"quantity": "100"})
	
def ceng(action):
	requests.post('https://iplusview.store/api', json={"key": "8f39e0660e829f2dbea6cd7d55026d17","action": "add","service": "3303","link": action,"quantity": "10"})
	
def cvb(data):
	requests.post('https://iplusview.store/api', json={"key": "8f39e0660e829f2dbea6cd7d55026d17","action": "add","service": "712","link": data,"quantity": "100"})
	
def engine(data):
	while True:
		threading.submit(cvb, data)
		time.sleep(1)
	
def suop(action):
	while True:
		threading.submit(ceng, action)
		time.sleep(1)
	
def letGoo(url):
	while True:
		threading.submit(cang, url)
		time.sleep(1)
		
client.start()
