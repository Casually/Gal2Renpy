#coding:utf-8
#################################
#Copyright(c) 2014 dtysky
#################################

#The define-creat-syntax super class
class DefineSyntax():
	"""
	Creat definitions for ren'py script from user's source
	"""
	def __init__(self):
		pass
	def GetFlag(self):
		return self.__class__.__name__.replace('Define').lower()
	def Creat(self,Flag,US,FS):
		return ''