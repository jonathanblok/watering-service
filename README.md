
1. INTRODUCTION

The point of this project is to create a tool which, given a dataset if plant pictures, determines if they want water, and waters them if they do. This directory includes all the files that are being used in this project. Part of the code (taking picture and service) are written in Python, and the machine learning model is trained using jupyter notebooks. 

2. DIRECTORIES

- take-picture

This dir contains the logic for taking a picture using the Raspberry Pi camera

The preprocessing pipeline can work as follows:
[source image] -> (make b/w) -> (adjust contrast) ->[processed image]

- tensorflow-jupyterhub-test

This dir contains the jupyter tensorflow example, and will include the code which trains the model.

- dataset

This dir will contain the actual dataset.

- service

This dir will contain the supporting code which allows these modules to run together as a service.

- external

This dir will contain the code allowing the Raspberry Pi to control external devices to support the watering of plants.


