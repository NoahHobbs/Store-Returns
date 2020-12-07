# Store-Returns
Making a program to quickly sort Amazon and Kohl's returns and learning how to use Py Simple GUI.
This was made as a final project for my CIS164 class.
I included quite a lot of comments but if something is not clear please comment or reach out!
Formalized Proposal
Kohl’s should be able to get both their own returns as well as Amazon’s and organize these quickly and efficiently. As it is now, Kohl’s employees must go through each return and split them depending on where they are from, this is horribly inefficient and can be improved greatly.  I will add them to a queue based linked list and to organize them on whether they are a Kohl’s item or an item from Amazon. I will keep the number of items a customer returns in an array. The sorting algorithm will be a selection sort which organizes the returns based off of how many items have been returned.

 	Next week, I will start by planning the logic and doing some pseudocode to help myself understand the program. During the first sprint I will lay the framework, on the second sprint I will begin by implementing my data structures and adding items to the queue, on the third sprint, I will implement my sorting algorithm. During the final sprint I will add my GUI and fix any errors or logic issues that have arrived.

Time/Change Logs

The program changed throughout my development, but the overall idea stayed relatively the same. 
•	During the first sprint I planned my logic and began setting up the general frame for my project
•	Second sprint, I made my classes and methods. I made an example of the data that the program will use
•	Third sprint, I finished the classes and methods for my program.
•	Fourth sprint, I had to redo a good chunk of my methods to include an Amazon front and a Kohl’s front so my sorting would be much easier. I added the sorting this week so that when the return is processed, they’re sorted based on how large they are
•	Fifth sprint, I added my GUI and learned how to use PySimpleGUI and added comments

Lessons Learned

I am happy with the project I chose, and I don’t think the scope was overwhelming. I really just wanted to learn how to create a project without a ton of instruction and I am very happy with the results. If I were to do this again, I think I would use Tkinter instead of PySimpleGUI, even though it was very simple the documentation was scattered, and I found it difficult to find helpful resources online that explained the issues I was having. I think Tkinter is slightly less user friendly but offers more through their methods and documentation.

With a program this size and one that goes for as long as this one did, you will always run into life blockers! During this project there were many blockers in my personal life. I also ran into a few issues with trying to deepen my knowledge of Python and learning Python 3.
•	The election which captivated most of the country for more than a week
•	Thanksgiving week and trying to balance family time with school time
•	Syntax issues that I spent time researching
•	As stated above, some confusing documentation for my GUI
•	Most of my blockers were resulting from other classes being packed to the brim which led me to working through several late nights and weekends for this project.

Conclusion/Summary
Modularity is used through my program, I used classes and methods to accomplish my goals because this is the way I’ve been taught from OOP principles. I tried to make my program as efficient as possible so that it can scale when I add new features. I added some error handling for when the user tries to process without entering something in the text box. I think I made the program very easy to understand and the GUI is very user friendly. The string in parentheses helps understand that you can add more than one value. For readability I added a ton of comments throughout and tried to use good variable names throughout. Using Python is great for elegance! I think the code looks very clean and the spacing makes everything look structured.

The project went well, and I think that the GUI turned out really good! With any program that you make there is always extra stuff you want to add but I decided this was a good point to submit because I accomplished the goals I set at the start of the project. The tough part about the program was the logic and planning as this is a real-world problem I was solving; it isn’t a concept that can be searched for and researched online.

In the future, I could add some way to send the returns to a file or to connect it to a database so that they can be organized. I think this would be a really cool way to learn more about file I/O or connecting to a database using Python which I have no experience with. From that I could then output the file to my GUI with a show past returns button.


	
