#
# Nomad Diskmag - CLIPARTS
# Rendering images generated by code.
#
# E-zine on a 1.44 floppy tailored made on Raspberry Pi computer.
# Created by Krzysztof Krystian Jankowski
# https://krzysztofjankowski.com/nomad-diskmag
#

import pygame
from pygame.locals import *
import time
import math

class Clipart:
	def __init__(self, mag, clip, pos, transparent="white", palette=("#b21cb0", "#e532e2", "#e5b7e4")):
		self.Mag = mag
		self.clip = clip
		self.pos = pos
		self.pal_shift = 0
		self.transparent = transparent
		self.palette = palette
		self.Mag.scene.add(self)
		self.timer = 0

	def draw(self):
		if self.clip == 'cover_0':
			self.draw_cover_0(self.pos)
		if self.clip == 'floppy':
			self.draw_floppy(self.pos, p=self.palette)
		if self.clip == 'rainbow':
			self.draw_rainbow(self.pos)
		if self.clip == 'pi':
			self.draw_pi(self.pos)
		if self.clip == 'fake_game':
			self.draw_fake_game(self.pos)
	
	def draw_cover_0(self, pos):
		x, y = pos
		y = y - 80 + math.sin(time.time()) * 80
		
		drive_x = self.pos[0] - 4
		drive_y = self.pos[1] - 30

		btn_x = drive_x + 170
		btn_y = drive_y

		pygame.draw.rect(self.Mag.screen, Color("#dddddd"), (drive_x-53, drive_y+20, 270, 10))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-53, drive_y-20, 270, 40))

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 14))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x, drive_y+12, 164, 2))

		self.draw_floppy((x,y), self.palette)

		pygame.draw.rect(self.Mag.screen, Color("#222222"), (drive_x, drive_y, 164, 2))
		pygame.draw.rect(self.Mag.screen, Color("#cccccc"), (drive_x-53, drive_y-20, 270, 20))
		pygame.draw.rect(self.Mag.screen, Color("#eeeeee"), (drive_x-53, drive_y-180, 270, 160))
		pygame.draw.rect(self.Mag.screen, Color("#222222"), (btn_x, btn_y, 20, 12))

	def draw_floppy(self, pos, p):
		x, y = pos
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+4, y+4, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x, y, 152, 160))
		pygame.draw.rect(self.Mag.screen, Color("#eaeaea"), (x+(152*0.5-40), y, 80, 50))
		pygame.draw.rect(self.Mag.screen, Color(p[1]), (x+84, y+7, 21, 40))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+5, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(p[0]), (x+139, y+142, 8, 8))
		pygame.draw.rect(self.Mag.screen, Color(self.transparent), (x+141, y+144, 6, 6))
		pygame.draw.rect(self.Mag.screen, Color(p[2]), (x+20, y+67, 110, 94))
		
	def draw_rainbow(self, pos):
		x, y = pos
		y = y - 180 + math.sin(time.time() * 0.5) * 80
		rows = 7
		pal = [(249, 65, 68),(243, 114, 44),(248, 150, 30),(249, 199, 79),(144, 190, 109),(67, 170, 139),(87, 117, 144)]
		for i in range(rows):
			r,g,b = pal[i][0],pal[i][1],pal[i][2]
			pygame.draw.rect(self.Mag.screen, Color(r,g,b), (x, (y+160*i)+math.sin(i*8)*60, 1280, 320))

	def draw_pi(self, pos):
		x, y = pos
		# green pcb, metal, black chip, yellow rings, 
		pal = [(22,135,92), (159,143,143), (48, 42, 56), (243, 208, 104)]
		r,g,b = pal[0]
		pygame.draw.rect(self.Mag.screen, Color(r,g,b), (x,y,250,200))


	def draw_fake_game(self, pos):
		x, y = pos
		s = self.Mag.screen
		pal = [
			(72,72,72),
			(72,72,72),
			(58,58,58),
			(58,58,58),
			(58,58,58),
			(46,46,46),
			(46,46,46),
			(46,46,46),
			(58,58,58),
			(58,58,58),
			(58,58,58)]
		pal_green = [
			(25,146,32),
			(71,168,78),
			(108,185,113),
			(71,168,78)]
		speed = 0.25
		max_z = 22
		fat = 1
		last_y = 0
		w = 32
		shift_x = x
		self.timer += speed*0.1
		max_w = 512
		car_w, car_l = 64,24
		pygame.draw.rect(s,Color(191,230,255), (x-max_w*0.5,y-32,max_w,64))
		for z in range(max_z):
			f = fat + ( z * 1.5)
			last_y += f - z*0.5
			w += z * 2
			shift_x = x + math.sin(self.timer + (max_z-z)*0.1) * (max_z-z)*4
			shift_y = y + (1+math.sin((max_z-z)*0.25)) * 32

			# sky
			pygame.draw.rect(s, self.get_shifted_color(pal_green, max_z-z), (x-max_w*0.5,shift_y+last_y, max_w, f+6))
			
			# landscape
			
			# road
			pygame.draw.rect(s, self.get_shifted_color(pal, max_z-z), (shift_x-w/2,shift_y+last_y, w, f+6))

		# car
		cx = math.sin(self.timer)*24
		pygame.draw.rect(s, Color(204,0,0), (x-car_w*0.5+cx,shift_y+last_y, car_w, car_l))
			
			
			
			

		self.pal_shift += speed

	def get_shifted_color(self, pal, id):
		target, max = int(self.pal_shift) + id, len(pal)
		if target >= max:
			target = target % max
		r,g,b = pal[target]
		return Color(r,g,b)