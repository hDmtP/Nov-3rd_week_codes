from github_contributions import GithubUser
import datetime

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(start_date='2021-11-14', end_date=str(datetime.date.today()))
#print(sum([day.count for day in contribs_2021.days]))


sc = f'''
Day      | Score
:--------------:|:----------------:
**{datetime.date.today()}** | **{sum([day.count for day in contribs_2021.days])}**
     '''

f = open("score.md", "a")
f.write(sc)
f.close()
