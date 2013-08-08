#-*- coding:utf-8 -*-

import Image
import os
import uuid
#图片缩略图生成函数
#创建Mpicture时，并不会生成缩略图。Mpicture有方法thumbnail，调用此辅助函数生成并保存缩略图
#图片大小，无上限，有下限。下限在form验证里面做验证
#TODO 不同APP的图片处理，分开做
def ssthumbnail(path, short, ratio):
	pix = Image.open(path)

	w1 = pix.size[0]
	h1 = pix.size[1]

	#这里生成正方形缩略图
	if ratio == 1.0:
		if w1 <= h1:
			delta = (int)((h1 - w1) / 2)
			box = (0, delta, w1, h1 - delta)
		else:
			delta = (int)((w1 - h1) / 2)
			box = (delta, 0, w1 - delta, h1)
		pix = pix.crop(box)
		pix = pix.resize((short, short), Image.ANTIALIAS)
		return pix

	#这里生成图片查看页面的大图
	#首先将图裁剪到比例内
	if w1 <= h1:
		if h1 > w1 * ratio:
			delta = (int)((h1 - w1 * ratio) / 2)
			box = (0, delta, w1, h1 - delta)
			pix = pix.crop(box)

	#再按比例调整图大小
	if short > w1:
		short = w1
	w2 = short
	h2 = pix.size[1] * short / w1
	pix = pix.resize((w2, h2), Image.ANTIALIAS)
	return pix

def ssuserlogo(path, short, ratio):
	pix = Image.open(path)

	w1 = pix.size[0]
	h1 = pix.size[1]

	#这里生成正方形缩略图
	if ratio == 1.0:
		if w1 <= h1:
			delta = (int)((h1 - w1) / 2)
			box = (0, delta, w1, h1 - delta)
		else:
			delta = (int)((w1 - h1) / 2)
			box = (delta, 0, w1 - delta, h1)
		pix = pix.crop(box)
		pix = pix.resize((short, short), Image.ANTIALIAS)
		return pix

	#这里生成图片查看页面的大图
	#首先将图裁剪到比例内
	if w1 <= h1:
		if h1 > w1 * ratio:
			delta = (int)((h1 - w1 * ratio) / 2)
			box = (0, delta, w1, h1 - delta)
			pix = pix.crop(box)

	#再按比例调整图大小
	if short > w1:
		short = w1
	w2 = short
	h2 = pix.size[1] * short / w1
	pix = pix.resize((w2, h2), Image.ANTIALIAS)
	return pix


#生成彩妆缩略图
def shiselogo(path, size):
	pix = Image.open(path)
	w1 = pix.size[0]
	h1 = pix.size[1]
	w = size
	h = size

	#首先将图裁剪到比例内
	if w1 >= h1:
		#横图，左右裁剪
		delta = (int)((w1 - h1) / 2)
		box = (delta, 0, w1-delta, h1)
		pix = pix.crop(box)
	else:
		#竖图，上下裁剪
		delta = (int)((h1 - w1) / 2)
		box = (0, delta, w1, h1-delta)
		pix = pix.crop(box)

	#缩放
	pix = pix.resize((w, h), Image.ANTIALIAS)
	return pix

def generate_logoori_name(filename):
	f, ext = os.path.splitext(filename)
	ext = ".jpg"
	logooriname =  '%s%s' %(uuid.uuid4().hex[:8], ext)
	return logooriname



def generate_userlogoori_name(instance, filename):
	logooriname = generate_logoori_name(filename)
	return '/'.join(['userlogo', logooriname])


def generate_shiselogoori_name(instance, filename):
	pic_oriname = generate_logoori_name(filename)
	return '/'.join(['shiselogo', pic_oriname])
