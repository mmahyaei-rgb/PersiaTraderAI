import requests


class APIClient:

    def get(self, url):

        try:

            response = requests.get(

                url,

                timeout=20,

                headers={

                    "User-Agent":
                    "Mozilla/5.0"

                }

            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(e)

            return None
        