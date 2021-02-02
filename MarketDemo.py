import os

CATALOG_FILENAME = 'products.txt'

class Product:
    isin = ''
    title = ''
    price = 0.0
    count = 0

    def __init__(self, isin, title, price, count):
        self.isin = isin
        self.title = title
        self.price = price
        self.count = count

    def display_info(self):
        print(f'[ISIN: {self.isin}; title: {self.title};', end='')
        print(f'price: {self.price}; count: {self.count}]')


class MarketCatalog:
    catalog = []

    # Добавили параметр self
    def load_from_file(self):
        if not os.path.exists(CATALOG_FILENAME):
            # Убрали return None
            return

        with open(CATALOG_FILENAME, encoding='utf-8') as file:
            for line in file:
                isin, title, price, count = line.split(';')
                # Используем конструктор класса Product
                # Вызываем метод add_product через self
                # Убрали параметр product_catalog
                self.add_product(Product(isin, title, float(price), int(count)))

    # Добавили параметр self и убрали парметр product_catalog
    def add_product(self, product):
        # Получаем каталог через self
        self.catalog.append(product)
    
    def save_catalog_to_file(self):
        with open(CATALOG_FILENAME, 'w', encoding='utf-8') as file:
            for product in self.catalog:
                # Получаем данные из полей объекта типа Product
                file.write(';'.join([product.isin, product.title, str(product.price), str(product.count)]) + '\n')


def create_product():
    isin = input('Enter the isin: ')
    title = input('Enter the title: ')
    price = float(input('Enter the price: '))
    count = int(input('Enter the count of product: '))

    return Product(isin, title, price, count) # Список поменяли на создание объекта типа Product


def main():
    product_catalog = MarketCatalog()
    product_catalog.load_from_file()
    # product = create_product()
    # add_product(product_catalog, product)
    product_catalog.save_catalog_to_file()

    product = Product('2134124', 'Хлеб черный', 32.90, 2400)
    product.display_info()
    

main()
