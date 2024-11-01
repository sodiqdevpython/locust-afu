from locust import HttpUser, task

class AFU(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://www.afu.uz")