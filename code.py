'''
Ashley Pak
SI 201
Project 1

'''

import csv 

def load_data(csv_file):
    data = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
def get_sales(data, state = None, region = None, category = None):
    total_sales = []
    for row in data:
        if (state is None or row['State'] == state) and \
           (region is None or row['Region'] == region) and \
           (category is None or row['Category'] == category):
            try:
                total_sales.append(float(row['Sales']))
            except ValueError:
                continue
    return total_sales

def avg_sales_ny(data):
    total_sales = 0
    count = 0
    for row in data:
        if row['State'] == 'New York':
            try:
                total_sales += float(row['Sales'])
                count += 1
            except ValueError:
                continue
    return total_sales / count if count > 0 else 0

def percent_east_sales(data):
    east_total = 0
    art_orders = 0
    for row in data:
        if row["Region"] == "East":
            east_total += 1
            if "art" in row["Category"].lower(): 
                art_orders += 1

    if east_total == 0:
        return 0
    return (art_orders / east_total) * 100

def write_results(ave_ny, pct_art):
    with open('results.txt', 'w') as file:
        file.write(f"Average sales in New York: ${ave_ny:.2f}\n")
        file.write(f"Percentage of art orders in East region: {pct_art:.2f}%\n")

def test_avg_sales():
    data = [
        {"State": "New York", "Sales": "200"},
        {"State": "New York", "Sales": "100"},
        {"State": "California", "Sales": "50"},
    ]
    result = round(avg_sales_ny(data), 2)
    assert result == 150.00  

    data = [
        {"State": "New York", "Sales": "99.99"},
        {"State": "New York", "Sales": "0.01"},
        {"State": "Texas", "Sales": "500.00"},
    ]
    result = round(avg_sales_ny(data), 2)
    assert result == 50.00  

    data = [
        {"State": "California", "Sales": "10"},
        {"State": "Texas", "Sales": "20"},
    ]
    assert avg_sales_ny(data) == 0  
     
    data = [
        {"State": "New York", "Sales": "abc"},
        {"State": "New York", "Sales": "300"},
    ]
    result = round(avg_sales_ny(data), 2)
    assert result == 300.00

def test_pct_art_sales():
    data = [
        {"Region": "East", "Category": "Art"},
        {"Region": "East", "Category": "Furniture"},
        {"Region": "West", "Category": "Art"},
    ]
    result = round(percent_east_sales(data), 2)
    assert result == 50.00  

    data = [
        {"Region": "East", "Category": "art supplies"},
        {"Region": "East", "Category": "Technology"},
        {"Region": "East", "Category": "ART"},
    ]
    result = round(percent_east_sales(data), 2)
    assert result == 66.67

    data = [
        {"Region": "West", "Category": "Art"},
        {"Region": "South", "Category": "Art"},
    ]
    assert percent_east_sales(data) == 0  

    data = [
        {"Region": "East", "Category": "  Art  "},
        {"Region": "East", "Category": ""},
        {"Region": "East"},
    ]
    result = round(percent_east_sales(data), 2)
    assert result == 33.33

    
def main():
    data = load_data('SampleSuperstore.csv')
    ave_ny = avg_sales_ny(data)
    pct_art = percent_east_sales(data)
    write_results(ave_ny, pct_art)

if __name__ == "__main__":
    main()

