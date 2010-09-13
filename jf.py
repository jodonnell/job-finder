# get todays links for all job sites
# filter out bad title ones
# get content for remaining jobs
# filter based on content
# email

import urllib2
from BeautifulSoup.BeautifulSoup import BeautifulSoup

from filter import Filter
from job import Job
from job_site_soup_parser import JobSiteSoupParser
from sites.craigs_list import CraigsList

def beautiful_soupify_url(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html)

filter = Filter()
craigs_list = CraigsList()
jssp = JobSiteSoupParser(craigs_list)

list_soup = beautiful_soupify_url(craigs_list.get_job_listing_url())

jobs = jssp.get_todays_links(list_soup)

# collect all jobs


get_posting_jobs = []
filtered_jobs = []
for job in jobs:
    if filter.title(job.get_title()):
        get_posting_jobs.append(job)
    else:
        filtered_jobs.append(job)
        
good_jobs = []
bad_jobs = []
for job in get_posting_jobs:
    content_soup = beautiful_soupify_url(job.get_link())
    content = jssp.parse_content(content_soup)
    job.set_content(content)

    if filter.content(job.get_content()):
        good_jobs.append(job)
    else:
        bad_jobs.append(job)


email_contents = ''
for good_job in good_jobs:
    email_contents += good_job.get_link() + "\n"
    print good_job

print ''
print "bad jobs-------------------"

for bad_job in bad_jobs:
    print bad_job


print ''
print "FILTERED title JOBS-------------------"

for job in filtered_jobs:
    print job

