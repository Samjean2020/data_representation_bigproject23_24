# data_representation_bigproject23_24
                                                Big Project

                                                Description
Write a program that demonstrates that you understand creating and consuming RESTful APIs. If you cannot think of a project to do: Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables. You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data. Assessment strategy for Project Type A: You have flexibility as to what you do for this project. 

                                                Scripts on the server
This project includes two files to be run on local machine browser and virtual environment(venv) under Client URL(curl). These are: drbigproject23_24.py and drbigproject23_24.py.ipynb.   Download both files. Run drbigproject23_24.py on Visual Studio Code (VSC). Run drbigproject23_24.py.ipynb on Jupyter Notebook. Boolean expression is = True, on the function app.run(debug=True) under the if __name__== ‘__main__’: construct for the file to be run on VSC. Whereas, in the script to be run on Jupyter Notebook, the Boolean expression must be = False, as app.run(debug=False) if not, an error will occur. drbigproject23_24.py run on VSC will display dataset sample in JSON format straightforward.
Pandas df() function reads the dataset CSV file (United Nations Women dataset). Notwithstanding, do not concurrently run Pandas and RESTful API. The server will stop running if you do so. Start with the cell containing the RESTfull API script in order to get the output in JSON format. The Pandas DataFrames df() function shows the source of data incorporated in the RESTful API, how to access the dataset, and make data visualisation. Use your localhost or the following link, http://127.0.0.1/5000, and then: http://127.0.0.1/5000/GCdataset in the browser’s address bar and hit the ENTER button. The links will display the welcoming message from the server and the dataset output sample in JSON format. This applies to both scripts to be run on VSC and Jupyter Notebook.  Follow comments included on both scripts.

I have included a web page file in HTML with a datatable to perform CRUD operations. This is available at this link: https://www.pythonanywhere.com/user/jsbb/files/home/jsbb/ajax.cssUN%20WomenData.html?
                                               
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

                                                Project Hosting on Python Anywhere
Go to: http://jsbb.pythonanywhere.com, click on PythonAnywhere on the welcoming message page. Log-in using jsbb as username and Papamama2025 as password, and then click on home/jsbb/drbigproject23_24.py while on Dashboard and run when the script is displayed or click on Files and select the RESTful API server file: drbigproject23_24.py. Update the IP port localhost default 5000 to 5354 as http://127.0.0.1/5354 or any other compatible ESTABLISHED ports, if not a Traceback(most recent call last)error will occur, and the server will not run accordingly. The debug = False while running the RESTful API server on Python Anywhere. I have also included a web page file: ajax.css UNWomenData.html for CRUD operations. This can be run on a local machine browser via this webpage link:https://www.pythonanywhere.com/user/jsbb/files/home/jsbb/ajax.cssUN%20WomenData.html?.  See also Consoles MySQL file: jsbb$drProject2324 to access the database called “jsbb$drProject2324”. The tablename is ”drproject2324". CRUD operations can be carried out on Python Anywhere MySQL prompt.

                                                Documentation
                                                  
                                                  REST API 
REST stands for Representation State Transfer. It is an architectural approach relating to distributed hypermedia structure. It is widely utilised for building web-based APIs (Application Programming Interfaces). REST does not fit on a protocol framework as HTTP. REST has six guiding principles including Uniforme Interface, Client-Server, Stateless, Cacheable, Layered Systems and Code on Demand. Refer to REST API Tutorial for further details on each principle [https://restfulapi.net/].
                                                  
                                                  
                                                  Flask
                                                  
Flask is a web framework and Python module dedicating for the development of web application. There is no ORM (Object Relational Manager) related to it, as it is a micro framework. A Web Framework or Web Application encapsulates libraries and packages relevant for the writing of applications regardless of protocol or thread management. Armin Ronacher, Pooco (an international Python Team) leader developed Flask based on Werkzeug, WSGI (Web Server Gateway Interface), and Jinja2 template engine [https://pythonbasics.org/what-is-flask-python/].
Flask facilitates the execution of the framework with a development server via a run command. An interactive debugger is available on Flask and enables to reload in case of code alteration while in debug mode. To avoid interference with CLI (Command Line-Interface) command while using the Flask.run() command, set the debug=True For further details on Flask Python and its attributes, see[https://pythonbasics.org/what-is-flask-python/]. 

                                                  Curl
                                                  
Curl is command line tool and library for transferring data with URLs. It is used in Command lines or scripts to transfer data. HTTP Cookies, HTTP/2, HTTP3, URL Syntax and WebSocket are some of protocols and formats used by Curl (curl.se, 2024). For more info: [https://curl.se/docs/] ; [https://curl.se/docs/]

                                                  PythonAnywhere
                                                  
PythonAnywhere can be defined as a web-based Python development environment that can be used and accessed from any device by means of a browser [https://www.pythonanywhere.com/about/company_details/]


                                                References
[1] Curl (2024) “Curl". Available at: https://curl.se/(Accessed on 01/01/2024)                                                 
[2] Curl (2024) “Documentation Overview”. Available at: https://curl.se/docs/(Accessed on 01/01/2024)                                                
[3]Pythonanywhere.com (2023) “About US”. Available at: https://www.pythonanywhere.com/about/company_details/ (Accessed on 31/12/2023)
[4]Pythonbasics.org (2023)” Python Tutorial, What is Flask Python”. Available at: https://pythonbasics.org/what-is-flask-python/ (Accessed on 31/12/2023)
[5]Restful API (2023) “REST API Tutorial”. Available at:  https://restfulapi.net/  (Accessed on 31/12/2023)



