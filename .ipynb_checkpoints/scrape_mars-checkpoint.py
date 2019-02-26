{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    exec_path = {'executable_path': 'chromedriver.exe'}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_info= {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_news():\n",
    "    try:\n",
    "        \n",
    "        browser = init_browser()\n",
    "        url = 'https://mars.nasa.gov/news/'\n",
    "        browser.visit(url)\n",
    "        html = browser.html\n",
    "        soup = BeautifulSoup(html, 'html.parser')\n",
    "        news_title = soup.find('div', class_='content_title').find('a').text\n",
    "        news_p = soup.find('div', class_='article_teaser_body').text\n",
    "        mars_info['news_title'] = news_title\n",
    "        mars_info['news_paragraph'] = news_p\n",
    "        \n",
    "        return mars_info\n",
    "    \n",
    "    finally:\n",
    "        browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_image():\n",
    "    try:\n",
    "        \n",
    "        browser = init_browser()\n",
    "        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "        browser.visit(image_url_featured)\n",
    "        html_image = browser.html\n",
    "        soup = BeautifulSoup(html_image, 'html.parser')\n",
    "        featured_image_url = soup.find('article')['style'].replace('background-image: url(', '').replace(');', '')[1:-1]\n",
    "        main_url = 'https://www.jpl.nasa.gov'\n",
    "        featured_image_url = main_url + featured_image_url\n",
    "        featured_image_url\n",
    "        mars_info['featured_image_url'] = featured_image_url\n",
    "        return mars_info\n",
    "    finally:\n",
    "        browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_weather():\n",
    "    try:\n",
    "        \n",
    "        browser = init_browser()\n",
    "        weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "        browser.visit(weather_url)\n",
    "        html_weather = browser.html\n",
    "        soup = BeautifulSoup(html_weather, 'html.parser')\n",
    "        latest_tweet = soup.find_all('div', class_='js-tweet-text-container')\n",
    "        for tweet in latest_tweets:\n",
    "            weather_tweet = tweet.find('p').text\n",
    "            if 'Sol' and 'pressure' in weather_tweet:\n",
    "                print(weather_tweet)\n",
    "                break\n",
    "            else:\n",
    "                pass\n",
    "            \n",
    "        mars_info['weather_tweet'] = weather_tweet\n",
    "        return mars_infor\n",
    "    finally:\n",
    "        browser.quit()\n",
    "        \n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_facts():\n",
    "    \n",
    "    facts_url = 'http://space-facts.com/mars/'\n",
    "    mars_facts = pd.read_html(facts_url)\n",
    "    mars_df = mars_facts[0]\n",
    "    mars_df.columns = ['Description', 'Value']\n",
    "    mars_df.set_index('Description', inplace = True)\n",
    "    data = mars_df.to_html()\n",
    "    mars_info['mars_facts'] = data\n",
    "    return mars_info\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_hemispheres():\n",
    "    \n",
    "    try:\n",
    "        browser = int_browser()\n",
    "        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "        browser.vist('hemispheres_url')\n",
    "        html_hemispheres = browser.html\n",
    "        soup = BeautifulSoup(html_hemispheres, 'html.parser')\n",
    "        items = soup.find_all('div', class_='item')\n",
    "        hiu = []\n",
    "        hemispheres_main_url = 'https://astrogeology.usgs.gov'\n",
    "        \n",
    "        for i in items:\n",
    "            title = i.find('h3').text\n",
    "            partial_img_url = i.find('a', class_='itemLink product-item')['href']\n",
    "            browser.visit(hemispheres_main_url + partial_img_url)\n",
    "            partial_img_html = browser.html\n",
    "            soup = BeautifulSoup(partial_img_html, 'html.parser')\n",
    "            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']\n",
    "            hiu.append({\"title\": title, \"img_url\": img_url})\n",
    "        mars_info['hiu'] = hiu\n",
    "        return mars_info\n",
    "    finally:\n",
    "        browser.quit()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
