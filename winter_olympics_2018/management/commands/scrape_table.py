from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests
from winter_olympics_2018.models import Country


class Command(BaseCommand):
    '''one time script used for scraping data from the wiki table'''
    def handle(self, *args, **options):
        url = "https://en.wikipedia.org/wiki/2018_Winter_Olympics_medal_table"
        web = requests.get(url)
        soup = BeautifulSoup(web.content, 'html.parser')
        table_row_list = soup.find('table', {"class": "wikitable sortable plainrowheaders"})\
            .find_all('tr') #find all countries table
        country_list = list()
        for index,row in enumerate(table_row_list):

            try:
                if index==0: #to skip table header
                    continue

                #logic to scrape data if multiple countries have same rank
                no_of_col = len(row.find_all('td'))

                if no_of_col==5:

                    rank = int(row.find_all('td')[0].string)
                    gold = int(row.find_all('td')[1].string)
                    silver = int(row.find_all('td')[2].string)
                    bronze = int(row.find_all('td')[3].string)
                    total = int(row.find_all('td')[4].string)
                    noc = row.find('th').find('a').string.strip()
                    short = row.find('th').find('span').string.split('(')[1].split(')')[0]

                elif no_of_col==4:

                    if len(table_row_list[index-1].find_all('td'))==5:
                        rank = int(table_row_list[index-1].find_all('td')[0].string)
                    else:
                        rank = int(table_row_list[index-2].find_all('td')[0].string)

                    gold = int(row.find_all('td')[0].string)
                    silver = int(row.find_all('td')[1].string)
                    bronze = int(row.find_all('td')[2].string)
                    total = int(row.find_all('td')[3].string)
                    noc = row.find('th').find('a').string.strip()
                    short = row.find('th').find('span').string.split('(')[1].split(')')[0]

                else:
                    #else
                    continue

                obj = Country()
                obj.rank = rank
                obj.gold = gold
                obj.silver = silver
                obj.bronze = bronze
                obj.total = total
                obj.noc = noc
                obj.short = short

                country_list.append(obj)

            except:
                #do something
                pass

        for obj in country_list:
            try:
                obj.save() #saving object in database
            except:
                #do something
                pass
        print('creation success -------------------------')