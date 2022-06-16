from breeze.utils import gen_random_string
from locust import between
from locust import HttpUser
from locust import task


class LoadTest(HttpUser):

    wait_time = between(0, 1)

    @task
    def get_homepage(self):
        self.client.get("/")

    @task
    def get_login(self):
        self.client.get("/login")

    @task
    def get_register(self):
        self.client.get("/u/register")

    @task
    def register_user(self):
        self.client.post(
            "/register",
            data={
                "username": gen_random_string(30),
                "email": gen_random_string(30) + "@gmail.com",
                "password": "123456",
                "confirm_password": "123456",
            },
        )

    @task
    def create_post(self):
        self.client.post(
            "/p/new",
            data={
                "content": gen_random_string(30),
            },
        )

    @task
    def get_profile(self):
        self.client.get("/u/profile")

    @task
    def get_logout(self):
        self.client.get("/logout")
