from user_class import User
from admin_class import Admin, Privileges

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