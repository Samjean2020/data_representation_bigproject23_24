# data_representation_bigproject23_24
                                                Big Project

                                                Description:

Write a program that demonstrates that you understand creating and consuming RESTful APIs. If you cannot think of a project to do: Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables. You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data. Assessment strategy for Project Type A: You have flexibility as to what you do for this project. 

                                                Scripts on the server
This project includes two files: drbigproject23_24.py and drbigproject23_24.py.ipynb.   Download both files. Run drbigproject23_24.py on Visual Studio Code (VSC). Run drbigproject23_24.py.ipynb on Jupyter Notebook. Boolean expression is = True, on the function app.run(debug=True) under the if __name__== ‘__main__’: construct for the file to be run on VSC. Whereas, in the script to be run on Jupyter Notebook, the Boolean expression must be = False, as app.run(debug=False) if not, an error will occur. The same code alteration applies in pythonanywhere hosting. drbigproject23_24.py run on VSC will display dataset sample in JSON format straightforward.
Pandas df() function reads the dataset CSV file (United Nations Women dataset). Notwithstanding, do not concurrently run Pandas and RESTful API. The server will stop running if you do so. Start with the cell containing the RESTfull API script in order to get the output in JSON format. The Pandas DataFrames df() function shows the source of data incorporated in the RESTful API, how to access the dataset, and make data visualisation. Use your localhost or the following link, http://127.0.0.1/5000, and then: http://127.0.0.1/5000/GCdataset in the browser’s address bar and hit the ENTER button. The links will display the welcoming message from the server and the dataset output sample in JSON format. This applies to both scripts to be run on VSC and Jupyter Notebook.  Follow comments included on both scripts. Moreover, to run the python script file drbigproject23_24.py on python anywhere host.

                                                Project Hosting on Python Anywhere
Go to: http://jsbb.pythonanywhere.com, click on PythonAnywhere on the welcoming message page. Log-in using jsbb as username and Papamama2025 as password, and then click on home/jsbb/drbigproject23_24.py. Update the IP port localhost default 5000 to 5354 as http://127.0.0.1/5354 or any other compatible ESTABLISHED ports, if not a Traceback(most recent call last)error will occur, and the server will not run accordingly.

                                                Virtual Environment and Client URL
Use Cmder terminal to create a virtual environment (venv) in order to connect the server to your device and exchange data under the Client URL (curl) command line tool, as below. On Cmder command line: 
Python  -m venv venv
.\venv\Scripts\activate.bat
(venv) λ pip freeze

(venv) λ pip install Flask
(venv) λ ls # make sure to download the drbigproject23_24.py on your local machine.
(venv) λ python drbigproject23_24.py

                                              Create, Read, Update and Delete (CRUD) Operations
When your localhost or the default one pops up (http://127.0.0.1/5000) use it to access the dataset incorporated on the server and perform CRUD operations as per comments on the script: drbigproject23_24.py
