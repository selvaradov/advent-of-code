import sys
import requests
import os
from dotenv import load_dotenv

NOTEBOOK_CONTENT = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
"""

if len(sys.argv) != 2:
    print("Run from command line!\n usage: python make_day.py <day_number>")
    sys.exit(1)

# Load environment variables from .env file
load_dotenv()
aoc_cookie = os.environ.get('AOC_COOKIE')

# Get the day number from the command line
day = sys.argv[1]
folder_path = f'day_{day}'

# check if data for this day already exists
if os.path.exists(os.path.join(folder_path, 'input.txt')):
    print(f"Data for day {day} already exists.")
    sys.exit(1)

# Make the GET request
base_url = f'https://adventofcode.com/2023/day/{day}'
url = base_url + '/input'
print(f"Making GET request based on {base_url}")

headers = {'Cookie': f'session={aoc_cookie}'}
response = requests.get(url, headers=headers)

# Check if the request was successful, save the text file
if response.status_code == 200:
    folder_path = f'day_{day}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(os.path.join(folder_path, 'input.txt'), 'w', encoding='utf-8') as file:
        file.write(response.text)

    print("Request successful. Text file saved in the output folder.")

    # Create the solution notebook
    if not os.path.exists(os.path.join(folder_path, 'solution.ipynb')):
        with open(os.path.join(folder_path, 'solution.ipynb'), 'w', encoding='utf-8') as file:
            file.write(NOTEBOOK_CONTENT)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)