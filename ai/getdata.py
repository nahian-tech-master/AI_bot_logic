import requests
from bs4 import BeautifulSoup

# Function to clean text
def clean_text(element):
    return element.get_text(strip=True)

# URL of the fee waiver structure page
url = 'https://ustc.ac.bd/fee-waiver-structure/'

try:
    # Make a request to the page
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the page
    title = soup.find('h1')
    if title:
        print("Page Title:", clean_text(title))

    # Find all paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print(clean_text(paragraph))

    # Find all headings for structured information
    headings = soup.find_all(['h2', 'h3'])
    for heading in headings:
        print("\n" + clean_text(heading) + ":")
        # Find the next sibling elements to get related details
        for sibling in heading.find_next_siblings():
            if sibling.name in ['h2', 'h3']:  # Stop if another heading is found
                break
            print(clean_text(sibling))

except requests.RequestException as e:
    print(f"An error occurred: {e}")
