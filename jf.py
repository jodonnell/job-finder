from sites.craigs_list import CraigsList
from job_filter import JobFilter

jf = JobFilter([CraigsList()])
jf.get_todays_links()
jf.filter_on_titles()
jf.get_postings_content()
jf.filter_on_content()

for job in jf._jobs:
    print job

print '----- bad'
for job in jf._bad_content_jobs:
    print job

print '----- badder'
for job in jf._bad_titled_jobs:
    print job

