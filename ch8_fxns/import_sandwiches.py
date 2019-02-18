
import sandwich_module

sandwich_module.sandwiches_fxn('wheat', 'cheese', 'meat')

from sandwich_module import sandwiches_fxn

sandwiches_fxn('white', 'cheese', 'meat')

from sandwich_module import sandwiches_fxn as sf

sf('challah', 'egg', 'yolk')

import sandwich_module as sm

sm.sandwiches_fxn('flatbread', 'tuna', 'mayo')

from sandwich_module import *

sandwich_module.sandwiches_fxn('kaiser roll', 'chicken cutlet')
