class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def display_info(self):
        print(f"Car Make: {self.make}, Model:{self.model},year: {self.year}")
        
    def start_engine(self):
        print(f" the engine of the {self.make}, Model:{self.model},year: {self.year} is running ")
        
car1=Car("honda","civic",2021)
car1.display_info()
car1.start_engine()
        
car2=Car("honda","civic",2024)
car2.display_info()
car2.start_engine()
