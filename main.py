from PIL import Image, ImageDraw
from sort_functions import selection_sort, quicksort_iterative
from search_functions import binary_search_sub
from pixel_functions import compare_pixels, store_pixels, pixels_to_image, pixels_to_points, grayscale

def main():
    IMG_NAME = 'monkey'

    with Image.open(IMG_NAME + '.jpg') as im:
        pixels = store_pixels(im)
        print("stored")

        threshold = 200
        choice = input("Input threshold to use: ")
        try:
            threshold = int(choice)

        except ValueError:
            print("Did not use an int, using 200")

        subi = binary_search_sub([r[0][0] for r in sorted_pixels],
                                 0 len(sorted_pixels) -1, threshold)
        print(f"Sublist of reds starts at {subi:}")
        grayscale(im, pixels)

if __name__ == "__main__":
    main()

