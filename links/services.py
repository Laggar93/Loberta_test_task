import requests


class StatusCheckService:
    def call(self, url):
        try:
            response = requests.get(url=url)
            status = response.status_code
        except requests.HTTPError as e:
            status = e.response.status_code
        except requests.ConnectionError:
            status = None
        return status


status_check_service = StatusCheckService()
