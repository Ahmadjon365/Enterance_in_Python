"""Template"""

"""
1. 
  "Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
    info() - (brand, model, type) ni print qilib beradi.

  "Notebooks" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
    more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.
    
  "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
    more_info() - (brand, model, type, size, display) ni print qilib beradi.
  
  "Smartphones" child klassi bor. Unda konstruktirida (size, sim_count) parametrlari bor.
    more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.
    
    
2.
  "Transport" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
    info() - (brand, model, type) ni print qilib beradi.
    
  "ElentroCars" - child klassi bor. Unda konstruktirida qo'shimcha (battery_life, chargin_time).
    more_info() - (brand, model, type, battery_life, chargin_time) ni print qilib beradi.

  "SportCars" - child klassi bor. Unda konstruktirida qo'shimcha (motor, color).
    more_info() - (brand, model, type, motor, color) ni print qilib beradi.
    
  "Truck" - child klassi bor. Unda konstruktirida qo'shimcha (motor, height, long, wieght).
    more_info() - (brand, model, type, height, long, wieght) ni print qilib beradi.

3.1
  "University" - parent klass. Konstruktorida esa (university) parametrlari bor.
    info() - (university) ni print qilib beradi.
    
  "Staff" - child klass. Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
    staff_info() - (university, first_name, last_name, age) ni print qilib beradi.
  
  "Student" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (group) parametrlari bor.
    more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.
    
  "Teacher" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
    more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
  
  "OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position) parametrlari bor.
    more_info() - (university, first_name, last_name, position,) ni print qilib beradi.

3.2
"Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
    object_info() - (university, name) ni print qilib beradi.
  
  "Computer" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
    object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
    
  "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
    object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.
"""