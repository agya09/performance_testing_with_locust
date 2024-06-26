from locust import HttpUser, TaskSet, task, between
import csv

class UserBehavior(TaskSet):
    urls = []

    @staticmethod
    def load_urls_from_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            UserBehavior.urls = [row[0] for row in reader]

    def on_start(self):
        self.load_urls_from_csv('Data/urls.csv')

    @task
    def load_product_pages(self):
        for url in self.urls:
            self.client.get(url)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks
