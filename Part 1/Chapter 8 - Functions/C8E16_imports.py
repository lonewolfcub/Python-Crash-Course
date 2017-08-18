import C8E3_t_shirt
C8E3_t_shirt.make_shirt("large", "I love Python!")

from C8E3_t_shirt import make_shirt
make_shirt("medium", "No, really, I love Python!")

from C8E3_t_shirt import make_shirt as ms
ms('small', 'Me too!')

import C8E3_t_shirt as t
t.make_shirt('extra small', 'Me Three!')

from C8E3_t_shirt import *
make_shirt('extra large', 'This has gotten far too silly!')
