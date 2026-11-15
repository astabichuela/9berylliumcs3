1. Answer the following questions:

    a. What is duck typing, as explained in the video?

    "If it walks like a duck and it quacks like a duck, then it must be a duck." It is a famuos saying that is where duck typing is based on. It is a way to achieve polymorphism without relying on inheritance. It's when an object is considered compatible with a specific requirement for methods and attributes. (More Reference: https://realpython.com/duck-typing-python/)


    b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

    The Car class needs to have the required attribute and method to work inside the same loop as the Dog and Cat.


2. Create the Python code that:

    [Want to view my code for SG11 Activity 2? Click here!](quarter2/sg11_activity2-code.py)
    

3. How does the code in 2.2 demonstrate polymorphism?

    The code demonstrates polymorphism because the function start_trip() can handle objects from unrelated classes like car, boat, drone with the requirement of all having the same method, in this case move().
