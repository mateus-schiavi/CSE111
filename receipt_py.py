import csv
from datetime import datetime


def main():
    try:
        products_list = read_dict('products.csv', 0)
        print('\n\n----- PYTHONS FUNCTIONS STORE -----\n\n')
        
        request = {}
        
        with open("request.csv","rt") as file:
            reader = csv.reader(file)
            
            
            next(reader)
            
            sub_total = 0
            
            for row in reader:
                value = row[0]
                value_quantity = row[1]
                value_quantity = float(value_quantity)
                
                items_order = products_list[value]
                name_product = items_order[1]
                product_price = items_order[2]
                product_price = float(product_price)
                
                sub_total += product_price * value_quantity
                
                print(f'{name}:    |{value_quantity}|  ${product_price}')
            print(" ")
            print(f'Subtotal: ${sub_total:.2f}')
            
            sale_tax_rate = sub_total * 0.06
            sale_tax_rate = float(sale_tax_rate)
            print(f'Sales Tax: ${sale_tax_rate:.2f}')
            
            total_computed = sub_total + sale_tax_rate
            total_computed = float(total_computed)
            print(f'Total Computed: ${total_computed:.2f}')
            
            print('\n\n\n ----- HAVE A NICE DAY -----\n\n\n')
            
            current_date_and_time = datetime.now()
            print('\n\n\n\n')
            print(f'{current_date_and_time: %A %I %M %P}')
            
    except(FileNotFoundError, PermissionError) as error:
        print('error found')
        print('Please, try to open another file')
        
    except ValueError as val_err:
        print('Error found at {val_err}. The value you want must be compoused by numbers. In need of assistance, please call 123-456-789')
        
    except KeyError as key_error:
        print(f'Error at line {reader.line_num} of {file.name} is formatted incorrecty.')
        
def read_dict(filename, key_column_index):
    
    products = {}
    
    with open(filename, "rt") as file:
        
        reader = csv.reader(file)
        
        next(reader)
        
        for row in reader:
            key_value = row[0]
            value_name = row[1]
            value_price = row[2]
            
            products[key_value] = [key_value, value_name, value_price]
            
    return products

def read_request():
    requests = {}
    
    with open("request.csv", "rt") as file:
        
        reader = csv.reader(file)
        
        next(reader)
        
        for row in reader:
            key_number = row[0]
            quantity = row[1]
            
            requests[key_number] = [key_number, quantity]
            print(requests[key_value])
            
    return requests

if __name__ == "__main__":
    main()
            