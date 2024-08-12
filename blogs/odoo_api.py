import xmlrpc.client
from bs4 import BeautifulSoup
from datetime import datetime
import time
import logging

from django.utils.dateformat import format
from django.conf import settings

logger = logging.getLogger(__name__)


class OdooAPI:
    def __init__(self):
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USERNAME
        self.password = settings.ODOO_PASSWORD
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common")
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object")


    def search_read(self, model, domain, fields, limit=0, retries=5):
        for attempt in range(retries):
            try:
                result = self.models.execute_kw(
                    self.db,
                    self.uid,
                    self.password,
                    model,
                    "search_read",
                    [domain],
                    {"fields": fields, "limit": limit}
                )
                if result is None:
                    logger.warning(f"search_read returned None for model: {model}, domain: {domain}, fields: {fields}")
                return result
            except Exception as e:
                logger.error(f"Error in search_read (attempt {attempt + 1}/{retries}): {e}")
                if attempt < retries - 1:
                    time.sleep(1)  # Wait before retrying
                else:
                    return None
    

    def soup_the_image_url(self, post):
        soup = BeautifulSoup(post["content"], "html.parser")
        first_image_url = None
        
        for image in soup.find_all("img"):
            if image["src"].startswith("/"):
                image["src"] = self.url + image["src"]
                if first_image_url is None:
                    first_image_url = image["src"]

        post["content"] = str(soup)
        post["image_url"] = first_image_url

        return post


    def get_posts(self):
        domain = [["is_published", "=", True]]
        fields =["id", "name", "content", "author_name", "published_date"]
        posts = self.search_read("blog.post", domain, fields)

        for post in posts:
            if ',' in post.get('author_name', ''):
                post['author_name'] = post['author_name'].split(', ', 1)[1]

            if isinstance(post['published_date'], str):
                post['published_date'] = datetime.strptime(post['published_date'], '%Y-%m-%d %H:%M:%S')
            post['published_date'] = format(post['published_date'], 'M d, Y')

            post = self.soup_the_image_url(post)

        return posts


    def get_post(self, post_id):
        domain = [["id", "=", post_id]]
        fields =["id", "name", "content"]
        posts = self.search_read("blog.post", domain, fields)
        if not posts:
            return None
        post = posts[0]
        post = self.soup_the_image_url(post)
        return post
