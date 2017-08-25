from admin import User, Admin, Privileges

admin1 = Admin('Bad',
               'Admin',
               'admin1',
               100001,
               'employee',
               'admin1@fictiouscompany.com',
               'root',
               True,
               False)

admin1.privileges.show_privileges()