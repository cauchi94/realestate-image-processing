# realestate_image_processing  
A trained deep learning model that is able to identify and classify the type of rooms found in real estates such as a living room, kitchen, bedroom, or bathroom from an image.
  
## Libraries

In order to be able to replicate the model these libraries need to be installed and imported succesfully:
- simple_image_download: https://github.com/RiddlerQ/simple_image_download
- os: allows us to interact with operating system
- shutil: to copy all files from different directories into one folder
- difPy: removes duplicated images
- pandas: data analysis and manipulation tool
- splitfolders: to split images into training and test set
- tensorflow: tools to process and load data for end-to-end machine learning
- tqdm: used for creating Progress Meters or Progress Bars
- matplotlib: for creating static, animated, and interactive visualizations
- keras: powerful and easy-to-use free open source Python library for developing and evaluating deep learning models

## How to Use

Make sure that you follow the steps in _**realestate_image_processing.ipynb**_ and is in the same folder of visual_interface.py in your local OS.
Once you have a saved outout of the model in _**.pb**_ format and then run the _**visual_interface.py**_ and select an image.
When done, the model will return the output of highest probability based on the room types trained with the model.
