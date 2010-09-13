import unittest
import datetime

from sites.craigs_list import CraigsList
from BeautifulSoup.BeautifulSoup import BeautifulSoup


class TestCraigsList(unittest.TestCase):
    def setUp(self):
        self.craigs_list = CraigsList()

    def test_get_links(self):
        cl_list_file = open('cl_list_test.html')
        cl_list_soup = BeautifulSoup(cl_list_file.read())
        cl_list_file.close()

        test_date = datetime.date(2010, 9, 11)
        todays_links = self.craigs_list._get_days_links(cl_list_soup, test_date)

        self.assertEqual(todays_links[0].__str__(), '<a href="http://newyork.craigslist.org/mnh/sof/1950616953.html">Software Engineer (Hadoop)</a>')



if __name__ == '__main__':
    unittest.main()
