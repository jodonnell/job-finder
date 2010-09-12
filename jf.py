import urllib2, re, sys
from BeautifulSoup.BeautifulSoup import BeautifulSoup
from datetime import datetime, timedelta

class Job:
    def __init__(self, title, contents, link):
        self.title = title
        self.contents = contents
        self.link = link
       
    def __str__(self):
        return self.title


front_end = re.compile('front[- ]?end', re.IGNORECASE)
qa = re.compile('(quality assurance)|(qa)', re.IGNORECASE)
dot_net = re.compile('\.net', re.IGNORECASE)
flex = re.compile('flex', re.IGNORECASE)
pm = re.compile('project manager', re.IGNORECASE)
ia = re.compile('information architect', re.IGNORECASE)
excel = re.compile('excel', re.IGNORECASE)
junior = re.compile('junior', re.IGNORECASE)
sales_engineer = re.compile('sales engineer', re.IGNORECASE)

tdd = re.compile('(tdd)|(test[- ]driven[- ]development)', re.IGNORECASE)

class Filter:
    def title(self, title):
        if front_end.search(title):
           return False

        if qa.search(title):
           return False

        if dot_net.search(title):
           return False

        if flex.search(title):
           return False

        if pm.search(title):
           return False

        if ia.search(title):
           return False

        if excel.search(title):
           return False

        if junior.search(title):
           return False

        if sales_engineer.search(title):
            return False
        
        return True


    def content(self, content):
        if tdd.search(content):
            return True

        return False

class JobSiteSoupParser:
    def __init__(self, soup):
        self.soup = soup


    def get_todays_links(self):
        dates = soup.findAll("h4", {"class":"ban"})

        today = None

        yesterday = datetime.today() - timedelta(2) #- timedelta(1)
        for day in dates:
            yesterday_regex = str(yesterday.day) + '$'
            if re.search(yesterday_regex, day.string):
                today = day

        try:
            first_post_from_today = today.previousSibling.previousSibling.findAll("a", href=re.compile('^http://newyork.craigslist.org/.*?/sof/\d+.html$'))[0]
        except IndexError:
            sys.exit('No posts yet today')
        all_posts = self.soup.findAll("a", href=re.compile('^http://newyork.craigslist.org/.*?/sof/\d+.html$'))
        
        i = 0
        for post in all_posts:
            if post['href'] == first_post_from_today['href']:
                break
            i += 1

        return all_posts[0:i+1]



def beautiful_soupify_url(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html)
    


soup = beautiful_soupify_url('http://newyork.craigslist.org/sof/')
jssp = JobSiteSoupParser(soup)

#print soup.prettify()

links = jssp.get_todays_links()


filter = Filter()

jobs = []
filtered_jobs = []
for link in links:
    if filter.title(link.string):
        jobs.append(Job(link.string, '', link['href']))
    else:
        filtered_jobs.append(Job(link.string, '', link['href']))


good_jobs = []
bad_jobs = []
for job in jobs:
    soup = beautiful_soupify_url(job.link)
    content_list = soup.find('div', id="userbody").findAll(text=True)

    content = ' '.join(content_list)
    if filter.content(content):
        good_jobs.append(job)
    else:
        bad_jobs.append(job)



email_contents = ''
for good_job in good_jobs:
    email_contents += good_job.link + "\n"
    print good_job

print ''
print "bad jobs-------------------"

for bad_job in bad_jobs:
    print bad_job


print ''
print "FILTERED title JOBS-------------------"

for job in filtered_jobs:
    print job









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
s = smtplib.SMTP()
s.connect()
s.sendmail('jacobodonnell@gmail.com', ['jacobodonnell@gmail.com'], msg.as_string())
s.quit()
