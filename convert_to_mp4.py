from pdf2image import convert_from_path
import os

def pad(n, digits):
    return f"{'0' * digits}{n}"[-digits:]

images = convert_from_path('frames.pdf', dpi=600)

for i, img in enumerate(images):
    img.save(f"img/frame{pad(i, 3)}.png")

os.system(
    "ffmpeg -f image2 -r 25 -pattern_type glob -i 'img/frame*.png' "
    "-vcodec libx264 -crf 22 video.mp4"
)
