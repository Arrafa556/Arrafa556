from PIL import Image, ImageDraw

img = Image.new('RGB', (64, 64), color='white')
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, 64, 64], fill='#2196F3')
draw.text((20, 14), "A", fill='white', font=None)
img.save('favicon.ico')
print("✓ favicon.ico berhasil dibuat!")