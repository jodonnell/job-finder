from sites.craigs_list import CraigsList
from job_filter import JobFilter

jf = JobFilter([CraigsList()])
jobs, bad_content_jobs, bad_titled_jobs = jf.get_todays_jobs()

for job in jobs:
    print job

print '----- bad'
for job in bad_content_jobs:
    print job

print '----- badder'
for job in bad_titled_jobs:
    print job

