
# Notes for resubmission of this project

I was informed by student care and the webinair that I watched from Jo C that the projects needed to be live for a certificate to be awarded.  I had to contact the tutors as the project was not being deployed to Heroku.  The tutors helped me to set it back up to live again on Heroku.




Sean profile
Sean
Begin a Tutoring Session
Tutoring at Code Institute profile
Please confirm that you have prepared for this session as per the steps on this page: https://code-institute-org.github.io/tutoring-info/guidelines/ 
You should have:
A clear description of your issue
A list of the debugging steps and research you have carried so far 
Failure to answer all of the bots questions will result in this conversation being closed.
By clicking "I'm Prepared," you agree to these conditions.
I'm Prepared
Your tutoring usage time for this week (in minutes): 44
Tutoring at Code Institute profile
Please select one of the following which best describes what you are working on.
Portfolio Project 3
Tutoring at Code Institute profile
Please provide us with your Problem Statement. This is a clear description of the problem that you're currently facing.
At the very least, you need to tell us what should your code be doing, and what is it actually doing?
If you are getting an error, please send a screenshot.
If you are working on a particular file, which file is it, and which lines of code?
Hi tutors, I was informed by student care and the webinair I watched on migrating databases to elephant sql by jo c that we have to have our projects live for them to get a certificates. Gemma and Sean have been very kind in getting my project 5 and project 4 back up live on heroku however I am trying to get my project 3 to be live and tried the steps that sean kindly showed me yesterday but I am not sure how to link up the project 3 to heroku as this was the python project.
Tutoring at Code Institute profile
What steps have you taken so far to resolve the issue, or to address current gaps in your knowledge?
Vague answers like "searched on Slack and Google" are not sufficient here. What specific steps have you taken? What code and debugging steps have you tried? What resources have you used (e.g. provide links to StackOverflow questions you have read)?
I tried to follow the instructions from yesterday to restart the database
Tutoring at Code Institute profile
One final thing. Please share your code with us. 
If you are working on Gitpod, please set your workspace to shared, and send us the link to it. If you are working on a course challenge, please send the name of the challenge.
https://sundeepbassi-funships-jjvxjgda03o.ws-eu86.gitpod.io/
Tutoring at Code Institute profile
Thank you. We will get back to you as soon as possible. You can see how busy tutoring currently is on this page: https://code-institute-org.github.io/tutoring-info/status/
Note that if you have failed to sufficiently answer any of the above questions, tutors will have to re-ask you for the information, which will use up part of your weekly tutoring time allowance.

Sean profile
Hi Sunny, pp3 does not have a database, so there is nothing new to do with that one, is it not working for you at the moment?
Hi Sean good to hear from you when I try to open the app it does not work on Heroku

Sean profile
ok, then we likely have to scale the application again
ok Sean how would I do that ?
in the second terminal, please login to heroku
Sean profile
Remember that you need the api key instead of the password
it is giving an error shall I use the API code from yestrday that I usedto login
Sean profile
yes please
Thanks I will give it a go
Thanks Sean that worked
ok, its working again

So, you needed to restart the dyno with the command
heroku ps:scale web=1 --app  <app_name>
Sean profile
ok, seems to be running fine now, Enjoy your day and happy coding :)
1:52 pm
Thans Sean you are a star tutor always good to chat with you and thank you, do I need to add the code above ?
no, its all done
Sean profile
Im jsut telling you for future cases :)
Brilliant Sean have a great day
Sean profile
👍
Thank you this is very helpful and I appreciate your very kind support
🌟
Help Sean understand how they’re doing:
Tutoring at Code Institute profile
You rated the conversation 
Thanks for letting us know
Hi Sean I tried to write a feedback for you in the feedback box and I accidentally pressed the return key, please pass the information to your managers. Sean is an excellent tutor, Sean has helped me to be a better coder and to learn how the system operates, I have a much better understanding now and I am very grateful for Sean's amazing tutoring skills and guidance. Sean puts the fun back into learning and it helps to want to learn more.
Hi Sean I tried to write a feedback for you in the feedback box and I accidentally pressed the return key, please pass the information to your managers. Sean is an excellent tutor, Sean has helped me to be a better coder and to learn how the system operates, I have a much better understanding now and I am very grateful for Sean's amazing tutoring skills and guidance. Sean puts the fun back into learning and it helps to want to learn more.
😄

Write a reply…


- I would like to say the support and encouragement from my mentor Miguel Martinez has been exceptionally outstanding. Miguel has never given up on me and I feel his support got me through a lot of stress and anxiety when I was doing this project.  I am forever touched with Miguels kindness and empathy and he has taught me the true meaning of dedication and commitment.  Miguel is a brilliant mentor and a great teacher.

- I would also like to say thank you to all of the tutor support team for spending time with me to try and get the correct code to work.  There were times when I did not understand and the tutors were patient with me and helped me to work through the issues.

- This project is being resubmitted as it only failed on one point in the criteria.

- The point it failed on is 2.1	Write code that handles empty or invalid input data.

- The above has now been rectified with the support of my mentor and the tutors.

- I have added two extra sections that explain how the code was rectified and where the problem needed to be rectified. I am grateful to the assessors for pointing out in the report that the data to be entered was to be between 1-9 and that 0 and -1 had been inputted and accepted by the code.  This problem has now been rectified and thoroughly tested and no invalid data is being processed.

- The two sections added to the readme are:

    - Bugs and Invalid Data Rectified From Submission of First Project

    - 2.1	Write code that handles empty or invalid input data. 

- I have also done an updated pep8 online check that passed without any faults and this can be found in the validator testing section of this readme. As I had submitted new code I wanted to ensure that it was checked properly by pep8 online checker.

## Fun-Ships

- Fun-Ships is a noughts and crosses game (tik tak toe in American) designed on the original paper played game.

- For more information about noughts and crosses check out [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

- Funships is coded in python and the code is outputted in the terminal the game is also deployed to Heroku.

- The game is designed to be played by a single person against the computer.

- The objective of the game is for the player to place  3 X's on the grid board in a line to win.


## How To Play

- The player has to input a number from 1 to 9.

- Then the player is prompted to enter another number.

- X represents the players symbol on the grid.

- O represents the computer symbol on the grid.

- The player must try to get three x's in a line.

- The Computer will try to block the player.

- The player and the computer can start the game.

## Features



### Existing Features

- The screenshot below is the game displayed on various screens.

- [Game On Various Screens](assets/screenshots/multiscreen.png)

- There ia a grid board for the player to play the game.

- The player is greeted with a welcome.

- The player is given an option to input a number value for the grid board from 1 - 9.

- The screenshot below shows the start of the game.

- [Start The Game](assets/screenshots/startgames.png)

- The player is prompted again to input a numnber and this will continue until either the player or computer wins, 
  loses or there is a draw.

- If both sides score a draw the player will be notified as shown in the draw screenshot below.

- [There is a draw](assets/screenshots/draw.png)

- If the player loses the game this will be displayed in the terminal as seen in the screenshot below.

- [Player has lost the game](assets/screenshots/lost.png)

- If the player inputs letters, symbols or an empty return the following message will be displayed by the computer.

- [Message For Incorrect Inputs](assets/screenshots/inputreq.png)

- The screenshot below displays the response when the player inputs the wrong number

- [Wrong Number](assets/screenshots/wrongnum.png)


### Future Features

- Allow player to have the opportunity to play against someone else.


###  Data Model
 
The model that I am using for this project is based on a grid board function.

The grid board function contains both the players turn and the computers turn.

The grid board functions are, define the board, who goes first, print the board, is the board full, check if there is a winner,
is a space free, place a marker on the board, who goes first, player turn, create a copy of the board, computer turn, check if player can win, if computer plays first, and run the game.

There is a choice to put in a number between 1 to 9.

###  Testing

- I did manual testing on the project by:

- Putting the code into the Pep8 linter validator testing check.  The code was passed without any problems and errors.

- I also did tests on the inputs to see what would happen if I inputted a number above 9. The function works because 
  the player is prompted to input a number between 1 and 9.

  I did a test with my mentor to see what would happen if I inputted a letter, a symbol and an empty space.  A bug was removed. The output for this test was working and informed the player to select the correct input required to play the game (numbers between 1-9)

- The code was also tested on the local terminal and in Heroku. 



###  Bugs

- There were bugs in the code that inhibited it from running properly.  I had to contact tutor support and reach out to the slack community for support. The bugs were related to the nesting of the code in the loops.

The bugs were removed and it was the tutorial from Knowledge Mavens that helped to do checks.

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


### Bugs and Invalid Data Rectified From Submission of First Project
- Through the assessors kind feedback of the project it was noted in the assessment that in criteria 2.1 had failed as the allowance of invalid data entry causes the function to go wrong.  Through the support of my mentor and the tutor support we managed to locate the specific issue of why the game was allowing 0 to be accepted as an input.  This was rectified with the code being made more specific to what input was allowed to be run. 

- The assessor also kindly noted in the feedback that " The input range of the game is 1-9, however, the program takes 0 as input and proceeds. Moreover, when the user gives input of -1 the program does not raise error, accepts the user input." 

- Through the kind support of the tutors I was able to rectify the above issue by adding the code below to ensure that only the specified integers could be accepted from 1-9.  The game will not accept 0 as an input now. The -1 problem was resolved I also checked with +1 and this was not accepted.  

- The code that I used to rectify this is re.match(r'^\d+$', str(position)):
I also had to put import re at the top.  The tutors at the Code Institute helped me with this.

- The code that was inputting the incorrect data entry value was located in player turn.  
The code was rectified and the code now works and invalid data entry is not permitted. My mentor Miguel Martinez and the tutors at code institute helped me with this.  I am very grateful to them for their kind support.


### 2.1	Write code that handles empty or invalid input data. 

- The code that was causing the input of invalid data has now been rectified.

- The screenshot below was taken on the 13th of February 2002 and it shows the code that was rectified to stop the invalid input of data.  My mentor and the tutors supported me into checking the code thoroughly and to input the correct code to ensure that invalid data could not be inputed into the game by the user.

 ![Screenshot of code rectified for player turn](assets/screenshots/playerturn.png)


- The screenshot below was taken on the 13th of February 2002 and it shows that the input data has been checked.

 ![Screenshot of checking data input](assets/screenshots/datacheck.png)
 

 - The screenshot below was taken on the 13th of February 2002 and it shows input data for symbols on a keyboard and empty spaces were rejected as invalid data.

  ![Screenshot of checking data input](assets/screenshots/seconddatacheck.png)

 - The screenshot below was taken on the 13th of February 2002 and it shows what happens when a player inputs a number that has already been inputted, it states this position is not free, please try again.

   ![Screenshot of position not free](assets/screenshots/notfree.png)


###  Remaining Bugs

No remaining bugs

###  Validator Testing


- pep8
       - No errors were returned from pep8online.com.

 - The screenshot below is the most updated Pep 8 online check done taken on the 12 of February 2022 for 
 - the resubmission of this project.
 
 ![Pep 8 online updated passed screenshot taken on the 12 February 2022](assets/screenshots/pep8updated.png)

- The screenshot below is the one that was submitted on the first submission of this project in October 2021.

- Removed errors from code after checking in pep8 mainly indentation errors were removed. 24/10/21.

 ![Pep 8 online passed screenshot](assets/screenshots/peppass.png)


###  Deployment
- The project was deployed using the code Instiutes mock terminal for Heroku.

  - Steps for deployment:
      - Fork or clone this repository
      - Creat a new Heroku app
      - Set the build blocks to Python and Nodejs in that order 
      - Link the Heroku app to the repository
      - Click on **Deploy**
      
      - https://fun-ships.herokuapp.com/

      - As I had to resubmit this project, I redeployed the project on the 13th of February 2022.

      - I did  manual deployment using the deploy branch button on Heroku. I also cheecked with the tutors to see if I needed to do anything else as I had done my first deployment in October and the tutors informed me as long as the code was working in the Heroku terminal then everything would be good.

      - The screenshot below is the Heroku App stating the deployment is successful.

      ![Screenshot of deployment successful on Heroku](assets/screenshots/depsucces.png)


      - The screenshot below is the deployed site on the Heroku App.

       ![Screenshot of the deployed site on Heroku](assets/screenshots/deployed.png)






      



###  Credits

- Data modelling information from Database Design 2nd Edition

- [Database Design](https://opentextbc.ca/dbdesign01/chapter/chapter-4-types-of-database-models/)

- [Database Design](https://opentextbc.ca/dbdesign01/chapter/chapter-5-data-modelling/)

- The code for adding the import random is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for adding playerLetter and the computerLetter with values is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for define the board is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the print_board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the is_full function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the check_win function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the is_free function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.


- The code for the place_marker function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the who_goes_first function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- Credits to the tutor support and slack community for supporting me with bug fixes and 
  resolving errors in the code.

- The bug and errors in the code were resolved by checking with the Youtube tutorial from:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The other resources to sort the bugs were:

- [Stack overflow](https://stackoverflow.com/questions/52809455/nested-loops-in-python)

- [Geeks for Geeks](https://www.geeksforgeeks.org/loops-in-python/)

- The code for the player_turn function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the duplicate _board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the computer_turn function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the check if the player can win function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the if computer plays first function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the run the game function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- The code for the start the game function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=oe0kIt3kE2g&t=3s) Youtube Tutorial.

- To add the # noqa: E501 at the end of line 112 is accredited to the tutors at the Code Institute 
  for helping me to rectify this warning in pep 8 online validation checker.

- To remove the white trailing spaces from the code is accredited to fellow students on Slack and 
  the tutor support team.

- In my mentoring session my mentor highlighted the need to check my code thoroughly for bugs and errors.  My mentor has really
  empowered me to find solutions with debugging the code, thinking about what the code is doing and keeping focused with the 
  project. My mentor is an excellent support for me in helping me to code better.

- My mentor also identified a bug on line 62 onwards and he empowered me to try and find a solution into how this could rectified.
  we had to look at using the Whilst true, Try, Break and Except code to get the bug and error removed.

- I was informed by tutor support to use print() under lines of code to try to identify errors and bugs in why the code
  is not working.

- Tutor support also advised me to use the collapable arrows on the side of the code line so as to check if specific sections of 
  a loop are aligned correctly.

- Fellow students on slack showed me how to use the debugger in the python file and how to try to find bugs in the code.

- One thing that I really learnt with python is the importance of indentation in the code and how incorrect indentation can make 
  the code inoperative.

- A very good resource for helping with code structurtes with python.
  [tutorialspoint](https://www.tutorialspoint.com/python/python_continue_statement.htm)




The credits below were used for the design of previous projects,  I decided to keep them in the credits for both reference and research purposes.

- HIDDEN_BOARD and GUESS_BOARD is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- These functions code used in the project, def board():, def make_ships():, def bring_ship_place():, def count_attacked_ships():,
are all accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the print_board function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The random function import is accredited to both:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code institute python essentials information.

- The code added to the make_ships function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The comment added at the top of the code file for the legend is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the bring_ships_place function is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the count_attacked_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the make_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The information on constructing and checking the readme for the battleships game is accredited to the Code Institute
Battleships game readme.

- My Mentor Miguel Martinez helped me to align the grid with spaces, and the lines.  Better visibility for the player.

- Martin also helped me to insert line breaks for the input sections for the numbers and the letters.

- The code below is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.


- LENGTH_OF_SHIPS = [2, 3, 3, 4, 5]
- PLAYER_BOARD = [[" "] * 8 for i in range(8)]
- COMPUTER_BOARD = [[" "] * 8 for i in range(8)]
- PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
- COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
- LET_TO_NUM = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

- The code added to the print_board function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The import random is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

- The code added to the place_ships function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.


- The code added to the check_ship_fit  function  is accredited to:

- [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=66s) Youtube Tutorial.

### Disclaimer

- The contents of this project are solely for the purposes of education and research.  
- All of  the information and code that has been used from outside resources has be accredited to that person or organisation.

### Acknowledgements

I would like to thank my mentor Miguel Martinez for being an excellent mentor anf guiding me with the project.  Miguel's insights, experince and knowledge have empowered me to try to do my best and not to give up.

I would like to thank fellow students from slack and Matt Bodden the 5p lead in encouraging me to do my best.

I would like to thank Scott and Ed from the tutor support team to find good solutions whislt working with my code.

I would like to thank the whole of the tutor support for helping me with coding issues.

I would like to thank the student care team, Alex, Kieron and Aoife for listening to me and pointing me in the right direction.

I would like to thank my friends Claire and Holly for believing in me and checking on me when I was stressed with the course work and the project.

I would like thank Claire's pets, Bodhi (dog), Lass (dog), Mitzy (dog), Kiddy (cat) and Rabsie (rabbit), for sitting with me whilst I was doing my work and the endless support they gave me.  The dog walks helped me to get fresh air into my brain cells.

























    
























