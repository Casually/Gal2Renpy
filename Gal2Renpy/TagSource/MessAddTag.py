#coding:utf-8
#################################
#Copyright(c) 2014 dtysky
#################################
import G2R

class MessAddTag(G2R.TagSource):
	def Get(self,Flag,US):
		tags={'m':{}}
		for m in US.Args['ch']:
			if m not in ['Common','Tag']:
				tags['m'][m]=US.Args['ch'][m]['Name']
		return tags