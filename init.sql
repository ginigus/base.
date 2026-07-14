-- Удаляем старые таблицы, если они вдруг уже были созданы, чтобы не было ошибок
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Создаем таблицы заново строго по заданию
CREATE TABLE customers (
    id         INTEGER PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    city       VARCHAR(50),
    created_at DATE NOT NULL
);

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    title    VARCHAR(100) NOT NULL,
    category VARCHAR(50)  NOT NULL,
    price    DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INT NULL REFERENCES customers(id),
    order_date  DATE NOT NULL,
    status      VARCHAR(20) NOT NULL
);

CREATE TABLE order_items (
    order_id   INT NOT NULL REFERENCES orders(id),
    product_id INT NOT NULL REFERENCES products(id),
    qty        INT NOT NULL,
    price      DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

-- Наполняем таблицы оригинальными данными
INSERT INTO customers VALUES
(1, 'Иванов Пётр',    'Москва',         '2025-01-10'),
(2, 'Сидорова Анна',  'Санкт-Петербург','2025-02-15'),
(3, 'Кузнецов Олег',  'Москва',         '2025-03-01'),
(4, 'Попава Мария',   'Казань',         '2025-03-20'),
(5, 'Смирнов Игорь',  'Москва',         '2025-05-05'),
(6, 'Волкова Дарья',  NULL,             '2025-05-20');

INSERT INTO products VALUES
(1, 'Клавиатура',  'Периферия',   2500.00),
(2, 'Мышь',        'Периферия',   1200.00),
(3, 'Монитор 24"', 'Мониторы',   15000.00),
(4, 'Монитор 27"', 'Мониторы',   22000.00),
(5, 'Веб-камера',  'Периферия',   3500.00),
(6, 'Кабель HDMI', 'Аксессуары',   500.00);

INSERT INTO orders VALUES
(1,  1,    '2025-03-05', 'shipped'),
(2,  1,    '2025-04-10', 'shipped'),
(3,  2,    '2025-04-12', 'cancelled'),
(4,  3,    '2025-04-20', 'paid'),
(5,  2,    '2025-05-01', 'shipped'),
(6,  4,    '2025-05-15', 'new'),
(7,  1,    '2025-06-01', 'paid'),
(8,  NULL, '2025-06-05', 'shipped'),
(9,  6,    '2025-06-10', 'paid'),
(10, 3,    '2025-06-15', 'shipped');

INSERT INTO order_items VALUES
(1, 1, 1,  2500.00),    
(1, 2, 2,  1200.00),
(2, 3, 1, 15000.00),
(3, 4, 1, 22000.00),
(4, 2, 1,  1100.00),
(4, 6, 3,   500.00),
(5, 5, 1,  3500.00),
(5, 6, 2,   450.00),
(6, 4, 1, 22000.00),
(7, 1, 1,  2400.00),
(8, 2, 2,  1200.00),
(10, 6, 0,  500.00),
(10, 5, 1, -3500.00);