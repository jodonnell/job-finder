
# Interface for site parsing, uses delegation to use appropriate strategy for the different job sites
class JobSiteSoupParser:
    def __init__(self, site):
        self._site = site

    def get_todays_links(self, list_soup):
        return self._site.get_todays_links(list_soup)

    def parse_content(self, content_soup):
        return self._site.parse_content(content_soup)
