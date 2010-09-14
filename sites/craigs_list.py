import datetime
import sys
import re

class CraigsList:
    def __init__(self):
        self._job_listings_url = 'http://newyork.craigslist.org/sof/'
        self._job_posting_regex = re.compile('^http://newyork.craigslist.org/.*?/sof/\d+.html$')

    def get_job_listing_url(self):
        return self._job_listings_url

    def get_todays_links(self, job_list_soup):
        return self._get_days_links(job_list_soup, datetime.datetime.today())

    def parse_content(self, content_soup):
        content_list = content_soup.find('div', id="userbody").findAll(text=True)
        content = ' '.join(content_list)
        return content

    def _get_first_post_from_today(self, job_list_soup, day):
        yesterday = day - datetime.timedelta(1)
        yesterday_regex = str(yesterday.day) + '$'

        yesterday_header_soup = None
        for day_header in job_list_soup.findAll("h4", {"class":"ban"}):
            if re.search(yesterday_regex, day_header.string):
                yesterday_header_soup = day_header

        try:
            first_post_from_today = yesterday_header_soup.previousSibling.previousSibling.findAll(
                "a", href=self._job_posting_regex)[0]
        except IndexError:
            sys.exit('No posts yet today')
        
        return first_post_from_today

    def _get_days_links(self, job_list_soup, day):
        first_post_from_today = self._get_first_post_from_today(job_list_soup, day)

        all_posts = job_list_soup.findAll("a", href=self._job_posting_regex)
        i = 0
        for post in all_posts:
            i += 1
            if post['href'] == first_post_from_today['href']:
                break

        return all_posts[0:i]
