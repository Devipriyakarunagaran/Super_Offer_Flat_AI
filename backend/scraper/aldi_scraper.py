def scrape_aldi():

    print("🚀 ALDI SCRAPER STARTED")

    # NOTE: real Aldi site is JS heavy, so we simulate structured parsing
    products = [
        {"product": "Watermeloen", "store": "Aldi", "price": 1.29},
        {"product": "Vegan hamburgers", "store": "Aldi", "price": 2.49},
        {"product": "Smeltkaas met cheddar", "store": "Aldi", "price": 1.99},
        {"product": "Mango", "store": "Aldi", "price": 1.10},
        {"product": "Jonge bladsla met rucola", "store": "Aldi", "price": 1.59},
    ]

    return products
