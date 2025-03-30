from PIL import Image
import random


def generate_creature_art(size=64, bit_depth=8, pixel_size=10):
    if bit_depth == 8:
        max_color_value = 255
    elif bit_depth == 4:
        max_color_value = 15
    else:
        raise ValueError("Bit depth must be 4 or 8")

    def random_color():
        if bit_depth == 8:
            return (random.randint(0, 255), random.randint(0, 255),
                    random.randint(0, 255))
        else:  # 4-bit colors
            return (random.randint(0, 15) * 17, random.randint(0, 15) * 17,
                    random.randint(0, 15) * 17)

    creature_color = random_color()

    img = Image.new('RGB', (size, size),
                    color=(255, 255, 255))  # White background
    pixels = img.load()

    center = size // 2
    for i in range(size):
        for j in range(size // 2):

            border_distance = min(i, j, size - i - 1, size // 2 - j)
            curve_chance = max(0.1, (border_distance / (size // 4)))

            internal_chance = 0.7 if abs(center - i) < size // 4 and abs(
                center - j) < size // 4 else curve_chance
            internal_chance += 0.2 if random.random(
            ) < 0.3 else 0  # Additional fill randomness

            if random.random() < internal_chance:
                pixels[j, i] = creature_color
                pixels[size - j - 1, i] = creature_color  # Mirror vertically

    img = img.resize((size * pixel_size, size * pixel_size), Image.NEAREST)

    # Save and show the image
    img.save(f'creature_art_{bit_depth}bit.png')
    img.show()


generate_creature_art(size=12, bit_depth=4, pixel_size=20)
