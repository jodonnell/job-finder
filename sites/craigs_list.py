import datetime
import sys
import re

class CraigsList:
    def __init__(self):
        self._job_listings_url = 'http://newyork.craigslist.org/sof/'

    def get_job_listing_url(self):
        return self._job_listings_url

    def get_todays_links(self, job_list_soup):
        test_date = datetime.date(2010, 9, 11)
#        self._get_days_links(job_list_soup, datetime.today())
        return self._get_days_links(job_list_soup, test_date)

    def _get_days_links(self, job_list_soup, day):
        dates = job_list_soup.findAll("h4", {"class":"ban"})

        today = None

        yesterday = day - datetime.timedelta(1) #- timedelta(1)
        for day in dates:
            yesterday_regex = str(yesterday.day) + '$'
            if re.search(yesterday_regex, day.string):
                today = day

        try:
            first_post_from_today = today.previousSibling.previousSibling.findAll("a", href=re.compile('^http://newyork.craigslist.org/.*?/sof/\d+.html$'))[0]
        except IndexError:
            sys.exit('No posts yet today')
        all_posts = job_list_soup.findAll("a", href=re.compile('^http://newyork.craigslist.org/.*?/sof/\d+.html$'))
        
        i = 0
        for post in all_posts:
            if post['href'] == first_post_from_today['href']:
                break
            i += 1

        return all_posts[0:i+1]


    def parse_content(self, content_soup):
        content_list = content_soup.find('div', id="userbody").findAll(text=True)
        content = ' '.join(content_list)
        return content
