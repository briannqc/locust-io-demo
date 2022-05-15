import time

from locust import HttpUser, between, task


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    headers = {}

    def on_start(self):
        """
        on_start method will be called once for each simulated user when they start.
        """
        self.client.post(
            url="/login",
            json={"username": "foo", "password": "bar"}
        )

    @task(3)
    def posts_albums(self):
        """
        Methods marked with @task are the core of your locust file. For every running user, Locust creates a greenlet
        (micro-thread) that will call those methods: def posts_albums(self) and def view_todos(self). When
        QuickstartUser runs, it’ll pick one of the declared tasks and execute it. Tasks are picked at random,
        but you can give them different weights. After completing the execution, the user will then sleep during the
        waiting time (in our example it is 1 to 5 seconds), after which it will select a new method marked @task and
        continue repeating the sequence. Note that only methods marked with  @task  will be picked, so you can define
        your own internal helper methods any way you like.
        """
        self.client.get(
            url="/posts",
        )
        self.client.get(
            url="/albums",
        )

    @task(3)
    def view_todos(self):
        for user_id in range(10):
            self.client.get(
                url=f"/todos?userId={user_id}",
                name="/todos"
            )
            time.sleep(0.5)
