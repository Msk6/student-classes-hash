class HashTable:
    def __init__(self, class_limits, limit=4):
        self.limit = limit
        self.class_limits = class_limits
        self.array = [[] for i in range(limit)]
    
    def hash(self, key):

        if key["age"] >= 90:
            index = 0
            return index
        
        elif key["age"] >= 80:
            index = 1
            return index

        elif key["age"] >= 70:
            index = 2
            return index

        elif key["age"] >= 60:
            index = 3
            return index
        
        else:
            #name = key["name"]
            #score = key["age"]
            #print(f"{name} - {score}")
            pass

    def insert(self, key):
        
        index = self.hash(key)
        if type(index) == type(1):
            if len(self.array[index]) == self.class_limits:
                print("class is full")
            else:
                self.array[index].append(key)
    
    

    def print_classes(self):
        classes = ["A", "B", "C", "D"]
        for i in range(4):
            print(f"{classes[i]} ")
            for j in range(len(self.array[i])):
                student_array = self.array[i]
                student = student_array[j] 
                student_score = student["age"]
                student = student["name"]
                print(f"{student} - {student_score}")
                
                
            print("-"*40)
            

            

            

students = [
    {
        "name": "Jean-Luc Garza",
        "age": 24
    },
    {
        "name": "Teddy Munoz",
        "age": 79
    },
    {
        "name": "Georgia Ali",
        "age": 17
    },
    {
        "name": "Vicky Calhoun",
        "age": 8
    },
    {
        "name": "Awais Weaver",
        "age": 65
    },
    {
        "name": "Athena Kline",
        "age": 52
    },
    {
        "name": "Zacharia Whitaker",
        "age": 38
    },
        {
        "name": "Clarice Davenport",
        "age": 99
    },
    {
        "name": "Viktoria Flynn",
        "age": 84
    },
    {
        "name": "Ianis Crossley",
        "age": 20
    },
    {
        "name": "Johnnie Owens",
        "age": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "age": 33
    },
    {
        "name": "Adeel Nieves",
        "age": 100
    },
    {
        "name": "Dustin Villegas",
        "age": 98 
    },
    {
        "name": "Maxine Hughes",
        "age": 65
    },
    {
        "name": "Bilaal Harding",
        "age": 79
    },
    {
        "name": "Maddie Ventura",
        "age": 71
    },
    {
        "name": "Leroy Rees",
        "age": 44
    },
    {
        "name": "Wanda Frank",
        "age": 73
    },
    {
        "name": "Margaux Herbert",
        "age": 80
    },
    {
        "name": "Ali Rios",
        "age": 70
    },
    {
        "name": "Nigel Santiago",
        "age": 25
    },
    {
        "name": "Markus Greene",
        "age": 78
    },
    {
        "name": "Harlan Parrish",
        "age": 97
    },
    {
        "name": "Baran Davidson",
        "age": 43
    },
    {
        "name": "Seth Rodriguezh",
        "age": 67
    },
    {
        "name": "Diego Mayer",
        "age": 100
    },
]

number_of_student = int(input("Enter the number of students in the class: "))
table = HashTable(number_of_student)

for i in range(len(students)):
    table.insert(students[i])


print("-"*40)
table.print_classes()

