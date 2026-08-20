# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation means bundling data and methods together inside a class. In the sari-sari store, we can create a "Product" class that contains properties such as name, price, and quantity, along with methods like update_stock() or calculate_total(). This keeps product-related information secure and organized, preventing direct manipulation of variables outside the class.

### 2. Abstraction
Abstraction hides unnecessary details and shows only the essential features. For example, the store owner doesn’t need to know how the system calculates totals internally; they only need to call a method like get_total_sales(). By abstracting complex operations into simple methods, the system becomes easier to use and maintain. This reduces confusion and keeps the focus on what the user needs rather than how the process works.

### 3. Inheritance
Inheritance allows new classes to reuse properties and methods from existing ones. In the sari-sari store, we might have a base "Product" class, and then create specialized classes like PerishableProduct (with an expiry_date property) or NonPerishableProduct. This avoids code duplication and makes it easier to extend the system when new product types are introduced.

### 4. Polymorphism
Polymorphism lets different classes respond to the same method in different ways. For example, both PerishableProduct and NonPerishableProduct have a method called display_info(), but the perishable version could also show the expiry date while the non-perishable one does not. This makes the system flexible, as the same interface can handle different product types seamlessly. It improves design by allowing uniform handling of diverse objects.

## Reflection
Among the four pillars of OOP, for me, Encapsulation would be most useful in improving the sari-sari store inventory system. By grouping product data and methods together, the store owner can manage inventory more securely and consistently. It ensures that updates to stock, pricing, or sales are done through controlled methods, reducing errors and making the system easier to maintain as the store grows.
