from filter import Filter
import urllib2
from BeautifulSoup.BeautifulSoup import BeautifulSoup

from job import Job


class JobFilter(object):
    
    def __init__(self, sites):
        self._sites = sites
        self._jobs = []
        self._bad_titled_jobs = []
        self._bad_content_jobs = []

        self._filter = Filter()

    def get_todays_jobs(self):
        self._get_todays_links()
        self._filter_on_titles()
        self._get_postings_content()
        self._filter_on_content()
        return (self._jobs, self._bad_content_jobs, self._bad_titled_jobs)

    def _get_todays_links(self):
        for site in self._sites:
            list_soup = self._beautiful_soupify_url(site.get_job_listing_url())
            links = site.get_todays_links(list_soup)

            jobs = []
            for link in links:
                jobs.append(Job(link.string, link['href'], site))

        self._jobs = jobs

    def _filter_on_titles(self):
        get_posting_jobs = []
        for job in self._jobs:
            if self._filter.title(job.get_title()):
                get_posting_jobs.append(job)
            else:
                self._bad_titled_jobs.append(job)

        self._jobs = get_posting_jobs
    
    def _get_postings_content(self):
        for job in self._jobs:
            content_soup = self._beautiful_soupify_url(job.get_link())
            job.set_content(content_soup)

    def _filter_on_content(self):
        good_jobs = []
        for job in self._jobs:
            if self._filter.content(job.get_content()):
                good_jobs.append(job)
            else:
                self._bad_content_jobs.append(job)

        self._jobs = good_jobs

    def _beautiful_soupify_url(self, url):
        html = urllib2.urlopen(url).read()
        return BeautifulSoup(html)
