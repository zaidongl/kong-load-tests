from locust import HttpUser, task, between, tag


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @tag("no_plugin")
    @task
    def mock_llm_chat(self):
        self.client.post(url="/api/load-tests/chat",
                         json={
                             "model": "llama3.2:3b",
                             "messages":
                                 [{
                                     "role": "user",
                                     "content": "What's Kong Gateway?"
                                 }],
                             "stream": "false"
                         })

    @tag("decorator")
    @task
    def mock_llm_chat_with_decorator(self):
        self.client.post(url="/api/load-tests/decorator/chat",
                         json={
                             "model": "llama3.2:3b",
                             "messages":
                                   [{
                                       "role": "user",
                                       "content": "What's Kong Gateway?"
                                   }],
                             "stream": "false"
                         })

    @tag("guard")
    @task
    def mock_llm_chat_with_guard(self):
        self.client.post(url="/api/load-tests/guard/chat",
                         json={
                             "model": "llama3.2:3b",
                             "messages":
                                 [{
                                     "role": "user",
                                     "content": "What's Kong Gateway?"
                                 }],
                             "stream": "false"
                         })

    @tag("decorator_guard")
    @task
    def mock_llm_chat_with_decorator_guard(self):
        self.client.post(url="/api/load-tests/decorator-guard/chat",
                         json={
                             "model": "llama3.2:3b",
                             "messages":
                                 [{
                                     "role": "user",
                                     "content": "What's Kong Gateway?"
                                 }],
                             "stream": "false"
                         })