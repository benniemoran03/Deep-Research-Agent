import os

def ensure_dirs():
    os.makedirs("data/reports", exist_ok=True)
    os.makedirs("data/cache", exist_ok=True)
