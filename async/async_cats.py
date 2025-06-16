import requests  # requests - make requests via python
import time
import uuid


def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(time_end - time_start)

    return wrapper()


def get_res(url):
    # get_res(url) — sends an HTTP request to a URL and receives a response with an image.

    """
    requests.get() is a function from the requests library that sends an HTTP GET request to the specified URL.
    url=url is an argument that contains the address to which the request should be made.
    allow_redirects=True is a statement that if the server responds with a redirect (for example, with HTTP status 301 or 302), the library will automatically follow this redirect and get the final response.
    """
    return requests.get(url=url, allow_redirects=True)


def write_files(res: requests.Response):
    # write_file(res) — accepts this response, generates a unique file name and saves the image contents (res.content is the file bytes) to disk.

    file_name = str(uuid.uuid4()) + '.jpg'

    with open(file_name, 'wb') as f:
        f.write(res.content)


@time_decorator
def main():
    # In the main() function — downloads an image 50 times in a row and saves it to a separate file with a unique name.

    url = 'https://loremflickr.com/320/240/dog'
    for _ in range(10):
        write_files(get_res(url))


main()
