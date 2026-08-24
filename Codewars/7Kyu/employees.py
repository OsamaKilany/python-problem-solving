def find_employees_role(name):
    employees = [

    {'first_name': 'Ollie', 'last_name': 'Hepburn', 'role': 'Boss'},
      {'last_name': 'Smith', 'role': 'Truck Driver'},
        {'first_name': 'Peter', 'last_name': 'Ross', 'role': 'Warehouse Manager'},
          {'first_name': 'Cal', 'last_name': 'Neil', 'role': 'Sales Assistant'},
            {'first_name': 'Jesse', 'last_name': 'Saunders', 'role': 'Admin'},
              {'first_name': 'Anna', 'last_name': 'Jones', 'role': 'Sales Assistant'},
                {'first_name': 'Carmel', 'last_name': 'Hamm', 'role': 'Admin'},
                  {'first_name': 'Tori', 'last_name': 'Sparks', 'role': 'Sales Manager'},
                    {'first_name': 'Peter', 'last_name': 'Jones', 'role': 'Warehouse Picker'},
                      {'first_name': 'Mort', 'last_name': 'Smith', 'role': 'Warehouse Picker'},
                        {'first_name': 'Anna', 'last_name': 'Bell', 'role': 'Admin'},
                          {'first_name': 'Jewel', 'last_name': 'Bell', 'role': 'Receptionist'},
                            {'first_name': 'Colin', 'last_name': 'Brown', 'role': 'Trainee'}
                            
                            ]


    
    parts = name.title().split()
    if len(parts) == 2:
        first_name, last_name = parts
        for emp in employees:
            if emp.get('first_name') == first_name and emp.get('last_name') == last_name:
                    return emp["role"]
            
    return "Does not work here!"


    
#     if  ' ' in name:
#         first_name, last_name = name.strip().title().split(' ')
#         for emp in employees:
#             if emp['first_name'] == first_name and emp['last_name'] == last_name:
#                 return emp.get("role")

#     return "Does not work here!"