"""Remove stray cyan accent dots that the Z-Image style suffix left in a few ep. 002 stills
(a cyan dot in the night sky, cyan deck lights on the cargo ship, a cyan glint under the table).
CPU only: OpenCV inpaint (TELEA) on small discs. Originals kept as <name>_raw.jpg (first run)."""
import os, shutil
import cv2
import numpy as np

IMG = os.path.join(os.path.dirname(__file__), "..", "illustrations", "ep002", "img")
SPOTS = {
    "b01_empty_trading_office": [(504, 182, 9)],
    "b31_wall_clock_quiet": [(774, 1019, 12)],
}
for name, spots in SPOTS.items():
    path = os.path.join(IMG, name + ".jpg")
    raw = os.path.join(IMG, name + "_raw.jpg")
    if not os.path.exists(raw):
        shutil.copy(path, raw)
    im = cv2.imread(raw)
    m = np.zeros(im.shape[:2], np.uint8)
    for x, y, r in spots:
        cv2.circle(m, (x, y), r, 255, -1)
    out = cv2.inpaint(im, m, 10, cv2.INPAINT_TELEA)
    cv2.imwrite(path, out, [cv2.IMWRITE_JPEG_QUALITY, 95])


# cargo ship: a row of cyan deck lights and their reflection; turn them into plain warm-white
# deck lights instead of erasing them (lights belong on a ship)
name = "b36_cargo_ship_dawn"
path = os.path.join(IMG, name + ".jpg")
raw = os.path.join(IMG, name + "_raw.jpg")
if not os.path.exists(raw):
    shutil.copy(path, raw)
im = cv2.imread(raw)
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cy = ((h > 75) & (h < 105) & (s > 60) & (v > 60)).astype(np.uint8)
box = np.zeros_like(cy)
box[600:830, 250:1200] = 1
m = cv2.dilate(cy * box, np.ones((7, 7), np.uint8)).astype(np.float32)
m = cv2.GaussianBlur(m, (0, 0), 2.0)
h2 = np.where(m > 0.05, 18, h).astype(np.uint8)          # warm hue
s2 = (s * (1 - 0.7 * m)).astype(np.uint8)
out = cv2.cvtColor(cv2.merge([h2, s2, v]), cv2.COLOR_HSV2BGR)
cv2.imwrite(path, out, [cv2.IMWRITE_JPEG_QUALITY, 95])
