# Quiz Wizard
## Video Demo:  <https://youtu.be/XmJ1d2KHPCE>
### Description:

This is project is a fully working quiz website having functionalities <br/>
**register**: you can register the website by giving username and password & again typing the password you will be successfully registered to the quiz wizard web app and being redirected to the home page of the website<br/>
**log in**:after you registered if you want to visit again you can just type the username then password and again being redirected to the home page of the website<br/>
**log out**: if you want to log in or register to another account you can by just clicking log out on the web page <br/>
**The homepage**: in which all the instruction of what,why,how are given in discriptive but yet simple language <br/>
**dashboard**: you can see which quiz you palyed how many times <br/>
**quiz**: in this section there are five quiz's you can paly those are <br/>
* pyhton <br/>
* C <br/>
* SQL <br/>
* web frontPack <br/>
* trivia <br/>
**solution**: in this section there are only solution of 4 quiz's those are <br/>
* pyhton <br/>
* C <br/>
* SQL <br/>
* web frontPack <br/>
you might be thinking that why not trivia because it's trivia means no meaning of it, just for fun & time pass <br/>
**history**: in history you can see the name of quiz, attempt, time when you played that means 3 column's <br/>

#### The project directory:
> The project directory is consist of
static directory - 1 file
templates directory - 18 files ,
1 app.py,
1 database and requirement.txt as well<br/>

**the structure of the project is as follows**
* project
    - static
        - styles.css
    - templates
        - apology.html
        - c_quiz.html
        - c_solution.html
        - dasnboard.html
        - history.html
        - index.html
        - layout.html
        - login.html
        - python_quiz.html
        - python_solution.html
        - quiz.html
        - register.html
        - solution.html
        - sql_quiz.html
        - sql_solution.html
        - trivia_quiz.html
        - web_frontPack_quiz.html
        - wed_frontPack_solution.html
    - app.py
    - quiz.db
    - README.md
    - requirements.txt

##### static:
in this directory there is one styles.css<br/>
where we mainly changed the button, solution-text, other style for naviation<br/>
##### templates:
1. apology.html
in this one will return apology if the user do something wrong<br/>
2. c_quiz.html
in this we managed to get only one input of one qestion in mcq format, if correct then the background color will change to green then feedback come's that it's correct else means the question is wrong then backgorund color will change to red then feedback come's that it's incorrect <br/>
after submiting the quiz the page get redirect to home page and a flash message pop up that you completed the quiz and the record will be saved in the quiz database in quizy table<br/>
3. c_solution.html
in this html page all solution will be avaliable of all the questions that were asked in the c_quiz.html<br/>
in a format that first that question then it's solution in blue color the classic way of writting answer<br/>
4. dasnboard.html
in this section of the web app the user have it's own records of what the quiz and how many times that quiz he/she played that. <br/>
she/he also will have the username in the dashboard<br/>
5. history.html
in this section of the web app the user will have the history in short to say about <br/>
what the quiz he/she played & number of attempt & when they played that in proper datetime format<br/>
6. index.html
this is the page which represent homepage<br/>
7. layout.html
this the the block of code which we used again and again in the all the remaning html pages in short we can say that it is the standard format in which all the page's primary structure is defined<br/>
8. login.html
this will have a input for username and password<br/>
9. python_quiz.html
this page have same function as the c_quiz.html page have the only difference is this time it's the quiz of python, and every statement run in the reference of python<br/>
10. python_solution.html
this page have same function as the c_solution.html page have the only difference is this time it's the solution of python quiz, and every statement run in the reference of python<br/>
11. quiz.html
in this html page we can access the all avaiable quiz to paly by clicking in the play button<br/>
12. register.html
this will have a input for username and password and again password varifiaction<br/>
13. solution.html
in this html page we can access the all avaiable solution to see by clicking in the solution button<br/>
14. sql_quiz.html
this page have same function as the c_quiz.html page have the only difference is this time it's the quiz of SQL, and every statement run in the reference of SQL<br/>
15. sql_solution.html
this page have same function as the c_solution.html page have the only difference is this time it's the solution of SQL quiz, and every statement run in the reference of SQL<br/>
16. trivia_quiz.html
this page have same function as the c_quiz.html page have the only difference is this time it's the quiz of triva, and every statement run in the reference of trivia but the only catch is that it do not have solution<br/>
17. web_frontPack_quiz.html
this page have same function as the c_quiz.html page have the only difference is this time it's the quiz of web frontPack, and every statement run in the reference of web_frontPack, this pack is consist of css, html, javascript<br/>
18. wed_frontPack_solution.html
this page have same function as the c_quiz.html page have the only difference is this time it's the solution of web frontPack quiz, and every statement run in the reference of web_frontPack<br/>
19. app.py
this is the main backend the all routes are established here which ended up controling all the html pages of the dirctory templates<br/>
20. quiz.db
this is the database where the records of histroy is stored it's a sqlite3 database.<br/>
21. README.md
this is the file which i am writing all this thing<br/>
22. requirements.txt
this is the text file where we write all the dependences of this project

### Conclusion
> This web app is Build in MVC arcitecture
> Model is quiz.db
> View is templates
> Controller is app.py

## That's All!
# "Just Play to outperform"
