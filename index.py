import requests

if __name__ == "__main__":
    # r =requests.get('https://xkcd.com/1906/')
    # print r.status_code
    receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')
    with open(r'./image5.png', 'wb') as f:
        f.write(receive.content)