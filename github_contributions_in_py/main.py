from github_contributions import GithubUser
import datetime

user = GithubUser('hdmtp')
contribs = user.contributions()

print(contribs.days[0])
# prints the first date the user made a contribution in his/her account

contribs_2021 = user.contributions(start_date='2021-11-14', end_date=str(datetime.date.today()))
print(sum([day.count for day in contribs_2021.days]))

streak = user.current_streak()
print(len(streak))
