#!/usr/bin/env python
#-*-coding:utf8;-*-

from googlesearch import search
from datetime import datetime
import time
import re


#figure out the results number issue!!


class gSearch:

	def  __init__(self):

		self.time_start = time.process_time()
		self.urls = []
		self.index = 1

	def g_data_input(self):

		for retry in range(5):
			self.query = input(self.g_data_bold("#-") + " What kinda shit do you want to Google?\n" + self.g_data_bold("#-") + " Type your bullshit here: " )
			if  self.query:
				break
			else:
				if retry <= 5:
						if retry == 4:
							self.g_data_single_output(self.g_data_bold("#- ERROR") + ": IMPROPER INPUT: 5 Fails! BYE!")
							exit(0)
						else:
							self.g_data_single_output(self.g_data_bold("#- ERROR") + ": IMPROPER INPUT: Must enter a query (SOMETHING) you idiot!")
		for retry1 in range(5):
			self.result_limit = input(self.g_data_bold("#-") + " How many damn results do you want? ")
			if self.result_limit.isdigit():
				self.result_limit = int(self.result_limit)
				self.result_limit += 1
				break
			else:
				if retry1 <= 5:
					if retry1 == 4:
						self.g_data_single_output(self.g_data_bold("#- ERROR") + ": IMPROPER INPUT: 5 Fails! BYE!")
						exit(0)
					else:
						self.g_data_single_output(self.g_data_bold("#- ERROR") + ": IMPROPER INPUT: Must enter a number!")
		for retry2 in range(5):
			safe_option = input(self.g_data_bold("#-") + " Enable Safe Search (No Porn)? ")
			if safe_option.lower() in ["yes", "y"]:
				safe_search = True
				self.g_data_single_output("\n")
				break
			elif safe_option.lower() in ["no", "n"]:
				safe_search = False
				self.g_data_single_output("\n")
				break
			else:
				if retry2 <= 5:
					if retry2 == 4:
						self.g_data_single_output(self.g_data_bold("ERROR") + ": IMPROPER INPUT! 5 Fails! BYE!" ) 

						safe_search = None
						self.g_data_single_output("\((n")
						exit()
					else:
						self.g_data_single_output(self.g_data_bold("ERROR") + ": IMPROPER INPUT! Use [\"yes\", \"y\"] or [\"no\", \"n\"]" )
						
		self.g_data_request(self.query,  self.result_limit, safe_search)

	def g_data_request(self, query, result_limit, safe_search):
		
		if safe_search:
			request = list(search(query, num_results=result_limit, advanced=True))
			#request = search(query, num_results=result_limit, advanced=True)
		else:
			request = list(search(query, num_results=result_limit, safe=None, advanced=True))
			#request = search(query, num_results=result_limit, safe=None, advanced=True)
			
		self.g_data_arrange(request)
		
	def g_data_arrange(self, request):

		for result in request:
			
			dt = datetime.now()
			search_result_str = str(result)
			url = re.search(r"url=(.*?),", search_result_str).group(1)
			title = re.search(r"title=(.*?),", search_result_str).group(1)
			description = re.search(r"description=(.*)", search_result_str).group(1)
			
			search_time = dt.strftime("%m/%d/%Y - %I:%M:%S%p")
			#self.g_data_output(search_time)
			self.g_data_output(url,  title, description, search_time)
			#self.g_data_output(search_time)
			
	def g_data_bold(self, text):
		
		return f"\033[1m{text}\033[0m"

	def g_data_single_output(self, output):
		
		output_line = output
		print(output_line)
		
	def g_data_output(self, url,  title, description, search_time):
		
		if url not in self.urls:
			g_time = time
			r_limit = int(self.result_limit) - 1
			if self.index == 1:
				print(self.g_data_bold("#-") + " Here are your" + " (" + self.g_data_bold(str(r_limit)) + ")"  + " results for \"" + self.query + "\"" + self.g_data_bold(" FUCKER") + ":\n\n")
			print(self.g_data_bold("RESULT " + str(self.index) + ":\n\n"))
			print(self.g_data_bold("TITLE: ") + title)
			print(self.g_data_bold("DESCRIPTION:"), description)
			print(self.g_data_bold("URL: ") + url)
			print(self.g_data_bold("SEARCH TIME:"), search_time)
			self.time_end = time.process_time()
			self.time_run = round((self.time_end - self.time_start), 4)
			if self.time_run < 1:
				trace_output = self.g_data_bold("TRACE TIME: ") + str(self.time_run) + " sec"
			else:
				trace_output = self.g_data_bold("TRACE TIME: ") + str(self.time_run) + " min"
			print(trace_output + "\n\n")
			self.urls.append(url)
			self.index += 1
			
		if  self.index == self.result_limit:
			exit()


if __name__ == '__main__':

	gSearch().g_data_input()
