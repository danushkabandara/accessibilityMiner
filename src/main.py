import sys
import urllib2
from collections import deque
from urlparse import urlparse
import achecker
import lxml.html
from Datumbox.DatumBox import DatumBox





TLD = ["com", "org", "net", "edu", "gov"]
MAX_QUEUE_NUM = 2000

def num_appearances_of_tag(tag_name, html):
    soup = BS(html,"lxml")
    return len(soup.find_all(tag_name))





def data_extraction(url): # use achecker to get accessibility errors
    wa_checker = achecker.Achecker()
    wa_checker.get_resource(url)
    potential = wa_checker.get_total_problems()
    likely = wa_checker.get_total_likely()
    known = wa_checker.get_total_errors()
    type_known, type_potential, type_likely = wa_checker.get_wa_type_ids()
    return potential, likely, known, type_known, type_potential, type_likely


def main():
    datum_box = DatumBox("0a7bef11dba49865675a58c4dad221da")
    
   
    #crawl(seed_url, urls)
    with open("urls.txt") as f:
    	for line in f:
	    try:
		print line,"\n"
		request = urllib2.urlopen(line)
		html = request.read()
        	page = lxml.html.fromstring(html)
		meta = page.xpath('//meta')#open meta tags and get description
        	for elem in meta:
            		if elem.get('name') == "description":
                		description = elem.get('content')
                		print "Description: " + description
            	if elem.get('name') == "keywords":
                	keywords = elem.get('content')
                	print "Keywords: " + keywords
		topic =datum_box.topic_classification(description+keywords)#put the description and keywords into datumbox api to get the topic classification 
		print "topic "+ topic 
		potential, likely, known, type_known, type_potential, type_likely = data_extraction(line) # use achecker to get the accessibility errors of url
		print potential, likely, known
		
	    except:
		e = sys.exc_info()[0]
        	print e
		continue


if __name__ == "__main__":
    sys.exit(main())
