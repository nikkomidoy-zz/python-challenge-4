import requests

from bs4 import BeautifulSoup


class TwitterSimpleScrape(object):
    """
    Simple class object that handles scraping twitter accounts
    """
    def __init__(self, url):
        self.url = url
        self.name = ''

    def get_follower_count(self):
        """
        Return number of followers of specific twitter url
        """
        page_data = requests.get(self.url)
        scraper = BeautifulSoup(page_data.text, 'html.parser')

        follower_div = scraper.find(
            'li', {'class': 'ProfileNav-item ProfileNav-item--followers'}
        )
        temp = follower_div.find('a')
        followers = temp.find('span', {'class': 'ProfileNav-value'})

        follower_div = scraper.find('h1', 'ProfileHeaderCard-name')
        self.name = follower_div.find('a').text
        self.follower_count = followers.get('data-count')

        return '{:,}'.format(int(self.follower_count))


if __name__ == '__main__':
    try:
        twitter_url = input('Enter twitter url: ')
        twitter_scrape = TwitterSimpleScrape(twitter_url.strip())
        number_of_followers = twitter_scrape.get_follower_count()
        print('Twitter name: {}'.format(twitter_scrape.name))
        print('Number of followers: {}'.format(number_of_followers))
    except:
        raise Exception('Enter valid URL.')
