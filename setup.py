from setuptools import setup, find_packages

setup(
    name='hand-star',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'mediapipe',
    ],
    entry_points={
        'console_scripts': [
            'hand-star-demo = hand_star.hand_star:main'
        ]
    },
    author='Sumit Kumar Singh',
    author_email='sumitsingh9441@gmail.com',
    description='Handstar using Mediapipe and OpenCV Making Handdetection Easy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/RAJPUTRoCkStAr/hand-star',
)
