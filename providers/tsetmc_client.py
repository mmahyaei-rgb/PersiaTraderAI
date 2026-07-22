import requests


class TSETMCClient:

    BASE_URL = "https://cdn.tsetmc.com/api"

    def get(self, endpoint):

        url = f"{self.BASE_URL}/{endpoint}"

        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("Response:")
        print(response.text[:1000])   # فقط 1000 کاراکتر اول

        return None
    