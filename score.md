
	# Nov-3rd_week_codes

- [x] 1. **15th Nov**

  - mCoding(_mCoding.LLC_)
    > [GitHub](https://github.com/mCodingLLC) [YouTube](youtube.com/c/mCodingWithJamesMurphy) [Patreon](https://www.patreon.com/mCoding)
    - excellent Python coder and mentor. His name is `James Murphy`

- [x] 2. **16th Nov**

  - GitHub __Actions__
    > [Learn GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)
    - ![Tests](https://github.com/hdmtp-s-basement/Nov-3rd_week_codes/actions/workflows/github_action.yml/badge.svg)

- [x] 3. **17th Nov**

  - `from youtube_dl import YoutubeDL`
    > [youtube_dl](https://pypi.org/project/youtube_dl/)

  - GitHub __Actions__
    > [Learn GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)
    - ![Tests](https://github.com/hdmtp-s-basement/Nov-3rd_week_codes/actions/workflows/python-script.yml/badge.svg)

- [ ] 4. **18th Nov** - ~~_NULL_~~
- [x] 5. **19th Nov**

  -  ![Tests](https://github.com/hdmtp-s-basement/Nov-3rd_week_codes/actions/workflows/main.yml/badge.svg)

- [x] 6. **20th Nov**

  -  GitHub Contribution Fetcher in `python`
      > pip install [githubcontributions](https://github.com/bcongdon/github_contributions)
      
``` python
from github_contributions import GithubUser
import datetime
user = GithubUser('hdmtp')
contribs = user.contributions()
contribs_2021 = user.contributions(start_date='2021-11-14', end_date=str(datetime.date.today()))
print(sum([day.count for day in contribs_2021.days]))
```
 

   - ![Tests](https://github.com/hdmtp-s-basement/Nov-3rd_week_codes/actions/workflows/score.yml/badge.svg)
     > [Source](https://canovasjm.netlify.app/2020/11/29/github-actions-run-a-python-script-on-schedule-and-commit-changes/) 


<hr>
<div align="center">

Day      | Score
:--------------:|:----------------:
**15th Nov** | **0.5**
**16th Nov** | **0.5**
**17th Nov** | **0.5**
**18th Nov** | **0**
**19th Nov** | **0.5**
**20th Nov** | **0.5 + 1**
***Total***     | ***3.5***
     
</div>
<hr>
<!--Below part needs to be edited-->

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].  

You can also use words, to fit your writing style more closely[^note].

[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.

Score : 49
Day      | Score
:--------------:|:----------------:
**2021-11-20** | **49**
     
Day      | Score
:--------------:|:----------------:
**2021-11-20** | **51**
     
**2021-11-20** | **53**
