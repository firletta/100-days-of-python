from config import PIXELA_API_TOKEN, PIXELA_API_USERNAME
from pixela import PixelaClient
import datetime as dt

PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_API_USERNAME}"
GRAPH_HEADERS = {"X-USER-TOKEN": PIXELA_API_TOKEN}


def main():
    """Main function to demonstrate Pixela API client usage."""
    client = PixelaClient(PIXELA_ENDPOINT, GRAPH_HEADERS)
    current_date = dt.datetime.now().strftime('%Y%m%d')
    response = client.update_pixel(graph_id="meditation", date="20240718", quantity="14")
    print(response)

if __name__ == "__main__":
    main() 