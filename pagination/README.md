# Pagination

## Description

This project covers different pagination techniques applied to a dataset of popular baby names. The goal is to understand how to paginate data safely and efficiently, including handling cases where data is deleted between two requests.

## Requirements

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle 2.5.*
- pymongo (for NoSQL tasks)

## Setup

Download the data file and place it at the root of the project directory:

## Files

### 0-simple_helper_function.py

Contains the function `index_range(page, page_size)` that returns a tuple with the start and end indexes corresponding to the range of indexes for the given pagination parameters. Pages are 1-indexed.

### 1-simple_pagination.py

Contains the `Server` class with a `get_page(page, page_size)` method that returns the correct page of the dataset. Uses `index_range` to compute the correct indexes. Returns an empty list if the page is out of range.

### 2-hypermedia_pagination.py

Extends the `Server` class with a `get_hyper(page, page_size)` method that returns a dictionary containing the following keys:

- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page
- `next_page`: number of the next page, or None if no next page
- `prev_page`: number of the previous page, or None if no previous page
- `total_pages`: the total number of pages in the dataset

### 3-hypermedia_del_pagination.py

Extends the `Server` class with a `get_hyper_index(index, page_size)` method that provides deletion-resilient pagination. If rows are removed from the dataset between two queries, the user will not miss any items when navigating pages. Returns a dictionary with the following keys:

- `index`: the current start index of the page
- `next_index`: the next index to query
- `page_size`: the current page size
- `data`: the actual page of the dataset

## Pagination Concepts

### Simple Pagination

Basic pagination using page number and page size. The dataset is sliced using start and end indexes computed from these two parameters.

### Hypermedia Pagination

Adds metadata to the paginated response, such as the next page, previous page, and total number of pages. This allows the client to navigate the dataset without knowing its structure.

### Deletion-Resilient Pagination

Uses indexes instead of page numbers to navigate the dataset. If items are deleted between two requests, the pagination still returns the correct items by skipping missing indexes rather than shifting the window.

## Author

Holberton School student Zimmermann Ethane