import os
import re

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ms-ai-pack",  # 用自己的名替換其中的 YOUR_USERNAME
    version="0.0.1",  # 包版本號，便於維護版本
    author="Sai Ling",  # 作者，可以寫自己的姓名
    author_email="author@example.com",  # 作者聯繫方式，可寫自己的郵箱地址
    description="A small example package",  # 包的簡述
    long_description=long_description,  # 包的詳細介紹，一般在 README.md 文件內
    long_description_content_type="text/markdown",
    url="https://github.com/Sai-ComfyUI/ms_ai_pack",  # 自己項目地址，比如 GitHub 的項目地址
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.0',  # 對 Python 的最低版本要求
)