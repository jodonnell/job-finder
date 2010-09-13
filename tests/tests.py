import unittest
import datetime

from sites.craigs_list import CraigsList
from BeautifulSoup.BeautifulSoup import BeautifulSoup

good_post_content = u"\n Senior Ruby on Rails Developer \n \n San Francisco, New York City, and Boulder \n \n \r\nIf you're looking for somewhere to do serious agile development, and serious Rails development, Pivotal Labs is the place. We're looking for brilliant Rails developers to join our star team in San Francisco, New York, and Boulder offices. If you want to share your knowledge while learning from others, work sustainably, and work on some serious projects, we think you'll have a blast working with us.\r\n \n \r\nJob Summary:\r\n \n \r\n    * Developing Ruby on Rails applications for a variety of leading clients\r\n \r\n    * Test and Behaviour Driven Development\r\n \r\n    * Pair Programming\r\n \r\n    * Aggressive Refactoring\r\n \r\n    * Working directly with clients to manage requirements\r\n \n \n \r\nAdditional Skills desired:\r\n \n \r\n    * Experience with testing frameworks, from RSpec to Cucumber and Jasmine\r\n \r\n    * Ability to communicate with both technical and non-technical clients\r\n \r\n    * SQL\r\n \r\n    * JavaScript, Flash\r\n \r\n    * HTML, CSS\r\n \n \r\nWhy join us?\r\n \n \r\n   1. We're agile. That means test-driven development with tools like RSpec, Test::Unit, JUnit, JsUnit, Jasmine, Cucumber, and Selenium. It means pair-programming, refactoring, and state-of-the-art continuous integration, build, and deployment infrastructure.\r\n \r\n   2. We've got a real culture. We share it by rotating developers between projects. With us, you may work on five, six, or even more projects in a single year.\r\n \r\n   3. We're good, and always improving. We have daily stand-up meetings and regular retrospectives. We figure out what we're doing wrong, so we can fix it, and what we're doing right, so we can make it even better. Working here means you get better at what you already do well, every day. \r\n \n \r\nWe've got multiple teams of Rails and Java developers working on a variety of products at our labs in downtown San Francisco, New York City, and Boulder, and at some very well known companies around the Bay Area and beyond. If you're a talented developer who's enthusiastic about agile and interested in a unique and challenging environment, get in touch with us.\r\n \n \r\nInterested? Email us. Please specify the location of the position you are applying for.   START CLTAGS  \n \n Principals only. Recruiters, please don't contact this job poster.\n Please, no phone calls about this job!\n Please do not contact job poster about other services, products or commercial interests. \n  END CLTAGS  \n \n \n \n \n \n \n \n \n \n \n"


class TestCraigsList(unittest.TestCase):
    def setUp(self):
        self.craigs_list = CraigsList()

    def get_test_file_to_soup(self, file):
        cl_test_file = open(file)
        cl_test_soup = BeautifulSoup(cl_test_file.read())
        cl_test_file.close()
        return cl_test_soup

    def test_get_links(self):
        cl_list_soup = self.get_test_file_to_soup('cl_list_test.html')

        test_date = datetime.date(2010, 9, 11)
        todays_links = self.craigs_list._get_days_links(cl_list_soup, test_date)

        self.assertEqual(todays_links[0].__str__(), 
                         '<a href="http://newyork.craigslist.org/mnh/sof/1950616953.html">Software Engineer (Hadoop)</a>')

    def test_parse_content(self):
        cl_post_soup = self.get_test_file_to_soup('cl_good_job.html')
        content = self.craigs_list.parse_content(cl_post_soup)
        self.assertEqual(content, good_post_content)

if __name__ == '__main__':
    unittest.main()
