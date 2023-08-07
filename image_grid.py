from PIL import Image
import matplotlib.pyplot as plt


def split_image_into_pieces(image, piece_width, piece_height):
    pieces = []
    for y in range(0, image.height, piece_height):
        for x in range(0, image.width, piece_width):
            piece = image.crop((x, y, x + piece_width, y + piece_height))
            pieces.append(piece)
    return pieces


def show_image_pieces(image_pieces, num_rows, num_cols):
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 10))
    for i, ax in enumerate(axs.flatten()):
        if i < len(image_pieces):
            ax.imshow(image_pieces[i])
        ax.axis("off")
    plt.show()


# Görüntüyü yükle
image_path = "C:/Users/UCAR/Desktop/Inovako/Image_Grid/sunset.jpg"
image = Image.open(image_path)

# Parça boyutları
piece_width = 960
piece_height = 600

# Görüntüyü parçalara ayır
image_pieces = split_image_into_pieces(image, piece_width, piece_height)

# Parçaları bir kare üzerinde göster
num_rows = image.height // piece_height
num_cols = image.width // piece_width
show_image_pieces(image_pieces, num_rows, num_cols)
