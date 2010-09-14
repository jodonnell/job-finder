
# A simple class that holds the title, link and contents of a job.
class Job:
    def __init__(self, title, link, site):
        self._title = title
        self._link = link
        self._site = site
       
    def __str__(self):
        return self._title

    def set_content(self, content_soup):
        self._content = self._site.parse_content(content_soup)

    def get_content(self):
        return self._content

    def get_link(self):
        return self._link

    def get_title(self):
        return self._title
