try:
    import pefile
except ImportError:
    available = False
else:
    available = True


