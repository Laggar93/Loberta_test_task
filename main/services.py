import requests


class StatusCheckService:

    def call(self, data):
        url = data['url']

        try:
            response = requests.get(url=url)
            status = response.status_code

        except requests.HTTPError as e:
            status = e.response.status_code
        except requests.ConnectionError:
            status = None

        return {
            "url": url,
            "status": status
        }