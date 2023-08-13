from heic2png import HEIC2PNG

if __name__ == '__main__':
    heic_img = HEIC2PNG('heic/20230802_114152.heic')
    heic_img.save() # it'll show as `test.png`