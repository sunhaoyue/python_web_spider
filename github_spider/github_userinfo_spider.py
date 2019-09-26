from urllib.request import urlopen
from urllib.request import Request
import datetime
import json



if __name__ == '__main__':
    # 这里用不用转义符没差别
    url = 'http://oa.sanwant.com.cn/portal'
    req = Request(url)
    response = urlopen(req).read()
    results = json.loads(response.decode())


    #data = bs4.BeautifulSoup(results,'html.parser');
    #lidata = data.select('div#dailyList ul.daily_card li')

    f = open('ContributorsInfo4.txt', 'w')
    for item in results['items']:
        name = item['name']
        star = item['stargazers_count']
        owner = item['owner']['login']
        language = str('0')
        user = str('0')
        commits = 0
        language = item['language']
        #stats = get_statistics()
        contributor_list = []
        #count = len(stats)
        for i in range(0, count):
            #user = stats[i]['author']['login']
            #commits = stats[i]['total']
            deletions = 0
            additions = 0
            first_commit = None
            last_commit = None
            for week in stats[i]['weeks']:
                deletions += week['d']
                additions += week['a']
                # assume that weeks are ordered
                if first_commit is None and week['c'] > 0:
                    first_commit = week['w']
                if week['c'] > 0:
                    last_commit = week['w']
            contributor_list.append([name,
                                     owner,
                                     star,
                                     language,
                                     count,
                                     user,
                                     commits,
                                     additions,
                                     deletions,
                                     datetime.datetime.fromtimestamp(first_commit).strftime('%Y-%m-%d'),
                                     datetime.datetime.fromtimestamp(last_commit).strftime('%Y-%m-%d')
                                     ])
        for contributor in contributor_list:
            print(contributor, file=f)