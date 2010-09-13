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


# email_contents = ''
# for good_job in good_jobs:
#     email_contents += good_job.get_link() + "\n"
#     print good_job

# print ''
# print "bad jobs-------------------"

# for bad_job in bad_jobs:
#     print bad_job


# print ''
# print "FILTERED title JOBS-------------------"

# for job in filtered_jobs:
#     print job









# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText



# Create a text/plain message
msg = MIMEText(email_contents)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of mama' 
msg['From'] = 'jacobodonnell@gmail.com'
msg['To'] = 'jacobodonnell@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
# s = smtplib.SMTP()
# s.connect()
# s.sendmail('jacobodonnell@gmail.com', ['jacobodonnell@gmail.com'], msg.as_string())
# s.quit()
