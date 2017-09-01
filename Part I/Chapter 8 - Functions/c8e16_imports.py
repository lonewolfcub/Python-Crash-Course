import c8e3_t_shirt
c8e3_t_shirt.make_shirt("large", "I love Python!")

from c8e3_t_shirt import make_shirt
make_shirt("medium", "No, really, I love Python!")

from c8e3_t_shirt import make_shirt as ms
ms('small', 'Me too!')

import c8e3_t_shirt as t
t.make_shirt('extra small', 'Me Three!')

from c8e3_t_shirt import *
make_shirt('extra large', 'This has gotten far too silly!')
