# Script designed to detect if a module is available for import

try:
    import pefile

#    module_to_test = input("Enter the module to see if available you chump:\n", )
#    import module_to_test
# except ImportError:

except ImportError:
    available = False
    print("Module not present you pheasant")
else:
    available = True
    print("Module is locked and loaded")

# print("Module check to see if string is correct:", module_to_test)



