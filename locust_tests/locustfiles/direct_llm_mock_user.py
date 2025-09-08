from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def mock_llm_chat(self):
        self.client.post(url="/api/chat",
                         json={
                             "model": "llama3.2:3b",
                             "messages":
                                 [{
                                     "role": "user",
                                     "content": "What's Kong Gateway?"
                                 }],
                             "stream": "false"
                         })