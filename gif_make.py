import imageio
from pathlib import Path

png_path = Path('png')
images = []
for filename in png_path.iterdir():
    images.append(imageio.imread(filename))
imageio.mimsave('results.gif', images, duration=1)