"""Exact screen mask for the phone cutout of ep. 002 (owner, 25 Nov 2026: the app drawn on the phone spilled
over the metal rim at the right end and the near edge).
The screen is the grey glass of the photo: low saturation, lighter than the black bezel. We take the largest
grey region (opened, so the thin rim highlights drop out), its convex hull, and keep only the grey pixels near it;
the notch and the home bar stay dark, as on a real phone. The old mask is kept as c_b11_phone_screen_mask_v1.png.
Usage: python3 scripts/phone_screen_mask_ep002.py
"""
import os
import cv2
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D = os.path.join(ROOT, "illustrations/ep002/cutouts")


def main():
    c = np.asarray(Image.open(os.path.join(D, "c_b11_phone_nightstand.png")).convert("RGBA")).astype(np.float32)
    rgb, al = c[..., :3], c[..., 3]
    lum, sat = rgb.mean(2), rgb.max(2) - rgb.min(2)
    cand = ((lum > 70) & (sat < 40) & (al > 200)).astype(np.uint8)
    op = cv2.morphologyEx(cand, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    n, lab, st, _ = cv2.connectedComponentsWithStats(op, 8)
    m = (lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    hull = np.zeros_like(m)
    cv2.fillPoly(hull, [cv2.convexHull(cnts[0])], 1)
    grey = ((lum > 60) & (sat < 45)).astype(np.uint8)
    near = cv2.dilate(m, np.ones((5, 5), np.uint8))
    mk = (hull & grey & near).astype(np.uint8)
    ff = mk * 255
    h, w = mk.shape
    cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 255)
    holes = (ff == 0) & (lum > 48)          # small holes filled; the dark home bar / notch stay out
    mk = ((mk > 0) | holes).astype(np.uint8) * 255
    mk = cv2.GaussianBlur(mk, (3, 3), 0)
    Image.fromarray(mk).save(os.path.join(D, "c_b11_phone_screen_mask.png"))
    print("screen mask:", int((mk > 128).sum()), "px")


if __name__ == "__main__":
    main()
