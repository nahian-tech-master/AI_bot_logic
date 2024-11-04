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

    # Find all department sections (assumed structure)
    # Adjust the selectors based on the actual HTML structure
    department_sections = soup.find_all(['h2', 'h3'])  # Adjust selectors based on the actual content structure

    for section in department_sections:
        # Print the section title
        print("\nDepartment:", clean_text(section))
        
        # Collect related information
        for sibling in section.find_next_siblings():
            if sibling.name in ['h2', 'h3']:  # Stop if another heading is found
                break
            # Print the sibling text
            print(clean_text(sibling))

except requests.RequestException as e:
    print(f"An error occurred: {e}")
