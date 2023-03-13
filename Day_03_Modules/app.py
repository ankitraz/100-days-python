# importing sales module here

# from sales import calc_shipping,calc_tax   # if you press ctrl + space you will get all the function defined in sales module

import sys
from ecommerce import customer
print(dir(customer))
# import sales   # import entire module as an object so that you can use their functions with a dot operator just like i did in line 14

# from sales import * # this will import everything from a module, which is a bad practice.



# calc_shipping()
# calc_tax()

print(sys.path) # this will return a list of directory that python will look at to find a module.

# sales.calc_shipping()




# whenever we run this program, we will get a compiled version of the sales module. i.e., __pycache__
# this is basically done to speed up program




#==========================================================
# now importing sales.py from ecommerce package
# import ecommerce.sales

# using it
# ecommerce.sales.calc_tax()


# # better apprach to import modules from a package
# from ecommerce.sales import calc_tax,calc_shipping
# # using it
# calc_tax()
# calc_shipping()


# # import sales.py as an object from a module
# from ecommerce import sales
# # using it
# sales.calc_shipping()
# sales.calc_tax


# ==================================================================

# using a module from subpackage

# from ecommerce.shopping import sales




