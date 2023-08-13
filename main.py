import PIL.Image
import pillow_heif

heif_file = pillow_heif.read_heif("heic/20230802_114152.heic")
image = Image.frombytes(
    heif_file.mode,
    heif_file.size,
    heif_file.data,
    "raw",

)

image.save("png/20230802_114152.png", format("png"))