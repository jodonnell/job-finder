
# A simple class that holds the title, link and contents of a job.
class Job:
    def __init__(self, title, link):
        self._title = title
        self._link = link
       
    def __str__(self):
        return self._title

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

    def get_link(self):
        return self._link
