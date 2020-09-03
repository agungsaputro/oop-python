data = [
    {
	    "id" : 1,
        "fullname" : "ratna putri",
        "address" : "jakarta",
        "salary" : 5000000,
        "phone" : '099903'
    },
    {
	    "id" : 2,
        "fullname" : "hamish daud",
        "address" : "jakarta",
        "salary" : 2000000,
        "phone" : '34232949'
    },
]

class Employee:

    # init method initializes the name and id attributes
    def __init__(self,data):
        self.data =data
    
    # read all 
    def read(self):
        return self.data
    
    
    

emp = Employee(data)
print(emp.read())