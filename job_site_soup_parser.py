
#
class JobSiteSoupParser:
    def __init__(self, soup, site):
        self._soup = soup
        self._site = site


    def get_todays_links(self):
        return self._site.get_todays_links(self._soup)
