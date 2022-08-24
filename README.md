# Language Translator
	ABSTRACT:-
              This project defines a web-based language translator using Machine learning and Python. Translation enables communication between people from different regions. It provides meaningful communication from one language to another language. A language translator or text translator is a tool to translate text, words, and phrases from one language to any other language. It is like a dictionary where we can translate the text. 

•	KEYWORD:- python, googletrans, streamlit.

•	OBJECTIVE:- 
The objective of this project is to translate text from one language to any other language in real-time with a button click. This project will be built using the streamlit, googletrans libraries. In this project, the user enters text in any language and get it translated in any other language by selecting the output language.

•	INTRODUCTION:-

In this project, a web-based language translator application is created. A language translator or text translator is a tool to translate text, words and phrases from one language to any other language. It is like a dictionary where we can translate the text. To implement this project, we will use the basic concepts of Python, streamlit, and googletrans libraries. 
Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. We can instantly develop web apps and deploy them easily using Streamlit. Streamlit allows us to write an app the same way we write a python code. Streamlit makes it seamless to work on the interactive loop of coding and viewing results in the web app.
Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate. We import the Translator from googletrans, which is used to do translations. We also import LANGUAGES from googletrans which lists all supported languages in a Python dictionary.


•	Tools & Environment:-

Application	 		:	Language Translator Web based Application
Operating System  		:	Windows 10
Python IDE			:	Spyder IDE
Command Prompt  		:	MS-DOS


•	METHODOLOGY:-

Steps to build the web-based Language Translator application Python project:

1.	install the library
2.	import required modules
3.	create an instance of Translator class to use Google Translate ajax API
4.	define function
5.	define selectbox to select destination language
6.	input source language text in textarea 
7.	translate text from source language to destination language
8.	show text in destination language












    1.	install the library
           To install the library, we use pip install to the command prompt:
    •	    pip install googletrans

googletrans is a module to translate text. We import the Translator from googletrans, which is used to do translations. We also import LANGUAGES from googletrans which lists all supported languages in a Python dictionary.

 

•	pip install streamlit

Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. We can instantly develop web apps and deploy them easily using Streamlit.

 

2.	import required modules

•	import streamlit


 

•	import googletrans

 

3.	create instance of Translator class

Translator is a Google Translate ajax API implementation class. We have to create an instance of Translator to use this API.

 

4.	define Function

	val is the destination language

	key is the abbreviation of language for eg. value = 'hindi', key = 'hi'

	items get all the languages and its abbreviation from 'LANGUAGE' dictionary that is present in googletrans library  where key = abbrev. & value = language.

	if val == value then key is returned.

 

5.	select destination language

	the required destination language is selected from the selectbox which contains all the languages present in googletrans library.
	values get all the languages from the 'LANGUAGE' dictionary.

 

6.	input text in source language

    input text, words and phrases in source language from the user.

 

7.	translation

	translator is used to create a Translator class object.
	translate() function generally converts the text in source language to the text in destination language. It contains two arguments, first is source language text and second is destination language in which text is to be translated

 

8.	show result

	to print resulted text, words or phrases in destination language write method is called

 

•	RUN LANGUAGE TRANSLATOR:-

To run this project, we first open command prompt go to the specified directory where our program file "language_translator_NITRR.py" file is stored and used command 'streamlit run'.
 

 
•	CONCLUSION:-

This project will be beneficial for students in learning algorithms and programming languages like Python. In this project, a basic approach to translate text, words, and phrases into specific language is described. We have discussed how to translate text to the desired language using Googletrans library. Googletrans library also has the feature to detect the language of the text. We can extend it to the next level by adding some of the algorithms such as speech recognition, speech to text, text to speech, etc. By this project, we are encouraged to practice the API, as well as learn and understand to use it in real-life applications.