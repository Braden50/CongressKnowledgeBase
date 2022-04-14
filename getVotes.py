import requests


def main():
    getVoteCSV(134)

def getVoteCSV(senateVoteNumber):
    url = f'https://www.govtrack.us/congress/votes/117-2022/s{senateVoteNumber}/export/csv'
    r = requests.get(url)
    with open(f'senate_117_2022_s{senateVoteNumber}.csv', 'wb') as f:
        f.write(r.content)


if __name__=="__main__":
    main()
