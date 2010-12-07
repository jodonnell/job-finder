import re

# The Filter class is used to filter job postings, either using excludes or includes
class Filter:
    title_filter_excludes = [
        re.compile('front[- ]?end', re.IGNORECASE),
        re.compile('(quality assurance)|(qa)', re.IGNORECASE),
        re.compile('\.net', re.IGNORECASE),
        re.compile('flex', re.IGNORECASE),
        re.compile('project manager', re.IGNORECASE),
        re.compile('information architect', re.IGNORECASE),
        re.compile('excel', re.IGNORECASE),
        re.compile('junior', re.IGNORECASE),
        re.compile('sales engineer', re.IGNORECASE),
        re.compile('product manager', re.IGNORECASE),
        re.compile('analyst', re.IGNORECASE),
        re.compile('entry[- ]level', re.IGNORECASE),
        re.compile('\bux\b', re.IGNORECASE),
        re.compile('\bflash\b', re.IGNORECASE),
        re.compile('\boracle\b', re.IGNORECASE),
        re.compile('\bsql\b', re.IGNORECASE),
        ]

    content_filter_includes =  [
        re.compile('(tdd)|(test[- ]driven[- ]development)', re.IGNORECASE),
        re.compile('\bXP\b'),
        re.compile('extreme programming', re.IGNORECASE),
        re.compile('pair programming', re.IGNORECASE),
    ]

    # The title excludes jobs based on regexes
    def title(self, title):
        for filter_out in Filter.title_filter_excludes:
            if filter_out.search(title):
                return False
        
        return True

    # The content includes jobs based on regexes
    def content(self, content):
        for keep in Filter.content_filter_includes:
            if keep.search(content):
                return True

        return False
