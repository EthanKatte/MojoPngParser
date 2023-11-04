from python import Python

def main():
    # This is equivalent to Python's `import numpy as np`
    Python.add_to_path('./')
    let parser = Python.import_module("kaitaiParser")
    let png_obj = parser.get_png("./dinosaur.png")
    let png_str = parser.unwrap_object(png_obj)
    print(png_str)








