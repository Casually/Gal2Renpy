#coding:utf-8
#################################
#Copyright(c) 2014 dtysky
#################################
import G2R

class HpcTag(G2R.TagSource):
	def Get(self,Flag,US):
		chs={}
		for m in US.Args['ch']:
			if m not in ['Common','Tag']:
				chs[m]=US.Args['ch'][m]['Name']
		tags={}
		tags['mm']={'PC':'PC','Phone':'Phone'}
		tags['ms']={'Call':'Call','Message':'Message','Web':'Web'}
		tags['o']=chs
		tags['l']=US.Args['hpc']['Position']
		tags['t']=US.Args['hpc']['Transition']
		return tags