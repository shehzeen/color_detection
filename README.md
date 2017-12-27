# color_detection

The program allows you to create classification files using cv2 library.

Step 1: 
The first program to run is the PythonTraining.py program which creates the text File with mean and variance of every class (Color class, Color Like class and Non Color class). It generates a text File called Output_Mean_Cov.text. 

Please change the directory inside this file by changing the varPath variable.

varPath ='...'
os.chdir(varPath)


Step 2: 

Next we need to run GaussianModel.py program. In GaussianModel.py please change the variable folder to the desired folder where test images are placed. Next we use the generated output from program 1 PythonTraining.py that is Output_Mean_Cov.text as the input to my second program GaussianModel.py. This is also provided as a text file but you can regenerate the means and covariances that are shown here for each of the classes from PythonTraining.py


