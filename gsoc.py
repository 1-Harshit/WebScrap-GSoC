# all fancy imports
from bs4 import BeautifulSoup
import requests
import json
import csv

def main():
    # a link that contains all 1292 results and file where it all will be strored
    url = "https://summerofcode.withgoogle.com/api/program/current/project/?page_size=20"
    filename = 'gsoc2021.csv'
    i = 0
    # Write something to clear/create the file
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Organization", "Project"])

    print("Let's begin!")

    # loop
    while True:
        # get the json file
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        data = json.loads(soup.text)
        project = data['results']

        # to store output on this page
        output = []

        for entry in project:
            # required variables
            name = entry['student']['display_name']
            org = entry['organization']['name']
            title = entry['title']
            # save this entry
            tuple_entry = tuple((name, org, title))
            output.append(tuple_entry)

            # Beautify
            i = i + 1
            if i%200 == 0:
                print("{} projects loaded. More loading...".format(i))
        
        # print this page
        with open('gsoc2021.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerows(output)

        # if there's next page
        if data['next'] is None:
            print("Done! {} projects loaded and saved to {}".format(i, filename))
            break
        else:
            url = data['next']

# driver code
if __name__ == '__main__':
    main()