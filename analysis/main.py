import sys
import os
sys.path.append(os.path.abspath('..'))

from preprocessing import shroom_dealer

print(shroom_dealer.get_attribute_dictionary())
