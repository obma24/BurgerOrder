link to my diary in GitHub:
https://github.com/obma24/BurgerOrder-Grupp-11-/blob/main/Reflektioner/EngineeringDiary/hahh24.md
Engineering Diary (individual Assignment)
Name: Hazem Haj Ali
(hahh24)

Ingenjörsdagboken




Week 1:Initial Setup and Learning Git




During the first week, my team and I met to get familiar with configuration management using Git. We started by making sure everyone downloaded the correct application, as the teacher had emphasized the importance of using the right tools. We chose to use GitHub, a widely-used platform for version control and collaboration.




To better understand how GitHub works, we watched a YouTube tutorial that explained how to create a repository and the meaning of commits. Once our repository was set up, we each practiced making a commit to a shared `main.py` file. This helped us ensure that changes were being tracked correctly.




However, we encountered an issue where some commits were not successfully committed. We realised this was because two people were trying to commit changes at the same time, and the application couldn't handle the simultaneous updates. This resulted in a conflict that prevented some of the changes from being processed. After identifying the problem, we discussed it as a team and decided to take turns making commits to avoid this issue in the future. 




Overall, despite the minor setback, we successfully completed the initial setup and learned how to use Git for our project.






Reflection:




Collaboration  

Our first experience with Git showed the need for better communication. The issue with simultaneous commits taught us to coordinate more effectively, ensuring no one commits to the same file at the same time. Moving forward, we’ll use branches to manage individual tasks and avoid conflicts.




Configuration Management:

We realised the importance of understanding Git’s conflict resolution. While we avoided further issues by committing one at a time, adopting a structured branching strategy will improve our workflow and prevent future problems.








Week 2: Planning:




This week, my team and I met to plan how we would divide the work. We discussed each person’s strengths and previous coding experience to assign tasks accordingly. While we didn’t do any coding, this session was crucial for organising the project and ensuring that everyone understood their roles and responsibilities. The focus was on collaboration and planning for the upcoming tasks, allowing us to move forward efficiently in the weeks to come.






Week 3 : Implementing HTML and CSS




This week, after we finalized the division of tasks within the group, I was assigned the responsibility of implementing the HTML and CSS for the user interface. My task was to design a user-friendly interface that would make it easier for users to place their burger orders. Given my previous experience with HTML and CSS, I felt confident in my ability to handle this aspect of the project.




However, I quickly encountered a challenge: I had no prior experience connecting two different files, and I was unsure how to connect the HTML and CSS front-end with the main application. This gap in my knowledge made the task more complicated than I had anticipated. I spent a significant amount of time researching online, looking for tutorials and guides on how to connect different files. I discovered that there were multiple approaches, and the process was quite complex, involving different tools and technologies.




Some of the solutions I found required learning new programming languages or frameworks, which was initially overwhelming. After exploring several options, I realized that I needed to discuss the situation with my team. We held a meeting to talk about the different methods I had found and evaluated which one would be the most feasible for our project. Given the complexity, we decided that the best approach was to take it one step at a time. Our plan is to first establish a basic connection between the front-end and main application, then gradually add more functionality as we go along.




This experience has taught me the importance of collaboration and seeking advice when facing challenges beyond my expertise. The step-by-step approach we agreed on has helped break down the problem, making it feel more manageable and allowing us to move forward with confidence.








Reflection




Collaboration:  

This week underscored the value of teamwork. Discussing the database integration challenges with my colleagues helped simplify the task by breaking it into smaller steps. Their input made the problem more manageable.




Learning:

Researching database integration was challenging, but it taught me the importance of a step-by-step approach. By focusing on one part at a time, I was able to make progress without feeling overwhelmed.





Week 4&5: Frontend Design and Learning




Over the past weeks, I focused on learning how to connect the main application with the HTML file. This task proved to be more difficult than I anticipated. After struggling with it, my colleague and I agreed that he would handle integrating the HTML with the main application, while I shifted my focus toward learning more about databases and containers. I hoped this knowledge would help me better understand virtual machines and contribute more effectively to the project.




Meanwhile, I continued working on the front-end design. My colleague sent me a wireframe for how the website should look, which provided a clear structure and helped guide the layout of my HTML and CSS code. The wireframe simplified decisions like where to place buttons, ensuring the interface would be user-friendly. This saved me a lot of time, as I didn't have to start from scratch. The framework wasn’t too complex, which worked well because our teacher emphasized functionality over design.




As I implemented the front-end, I wrote the full HTML and CSS code, adjusting colors and adding buttons for customizing burger orders. I then committed the changes to GitHub. One challenge I faced was connecting the HTML file with the external CSS file. I knew it was best practice to keep them separate, but I struggled to make it work. After researching online, I found a solution that suggested embedding the CSS directly within the HTML file using the `<style>` tag. While this wasn’t ideal, it allowed me to proceed and ensure the design worked as intended. While this wasn’t the ideal solution, it allowed me to move forward and ensure the design looked as intended. The code I implemented looked something like this:











    <style>

        body {

            font-family: 'Arial', sans-serif;

            background-color: #f4f4f4;

            padding: 50px;

            margin: 0;

            color: #333;

        }....

</style>

Reflection:




Problem-Solving  

This week was challenging as I struggled with connecting the HTML and CSS files. Even though best practice suggests keeping them separate, I had to adapt by embedding the CSS directly into the HTML file to keep moving forward. This taught me that sometimes a temporary workaround is necessary to make progress, even if it’s not the ideal solution.




Learning and Adaptation: 

Although I couldn’t complete the integration of the HTML with the main application, I gained valuable insight into database structures and containers, which will be useful for future tasks. I also realised that I need to improve my understanding of how different parts of an application connect.




Collaboration: 

Discussing the integration issue with my colleague helped us divide the work based on our strengths. Handing over the task of connecting the files to him allowed me to focus on other areas like design and learning about virtual machines. This collaboration helped us maintain progress without getting stuck on one task.






Week 6 - Final Debugging




During the final week of our project, much of my time was dedicated to debugging and fine-tuning the kitchen view to ensure it displayed new orders in real-time. We noticed that the kitchen view wasn’t automatically updating after each new order; instead, we had to refresh the page manually to see the latest information. My colleague and I decided to investigate the cause, and we modified specific JavaScript variables to implement automatic updates.

The fetchOrders() function was central to the solution, as it periodically requests updated order data from the server. This function uses two key variables: orders and ordersContainer. These variables required close monitoring to ensure they received and displayed the new data correctly.

The orders variable holds the list of current orders. Inside fetchOrders(), orders is assigned the server response via xhr.responseText, which is parsed into a JavaScript array. While observing orders, we noticed it sometimes returned as an empty array [], especially when no orders were available. This discrepancy suggested that the XMLHttpRequest wasn’t always returning data as expected. To address this, we added a conditional check to handle cases when orders is empty, displaying a “No orders yet” message in ordersContainer if no data is returned.

The ordersContainer variable, accessed using document.getElementById('ordersContainer'), represents the HTML element where orders are displayed. Initially, we observed that ordersContainer.innerHTML wasn’t updating dynamically, leading to a static view of the orders. To fix this, we cleared ordersContainer.innerHTML at the beginning of each fetchOrders() call to ensure that old data was removed before appending new entries. Observing this variable in the console confirmed that each time fetchOrders() ran, ordersContainer.innerHTML was reset, preventing duplicate entries.

Within the fetchOrders() function, we used forEach() loops to display each order’s details. The orderHTML variable within these loops builds the HTML structure, showing each burger’s name and its customizations. Initially, we noticed some data alignment issues, where customizations didn’t display correctly alongside their respective burgers. After monitoring orderHTML, we made adjustments to ensure each burger’s customizations appeared consistently, verifying that the details were formatted correctly.

Finally, we set the fetchOrders() function to run every five seconds using setInterval (fetchOrders, 5000);, ensuring the kitchen view updates in real-time. This adjustment confirmed that the ordersContainer now refreshes automatically, showing the latest order information without manual intervention. The debugging process allowed us to achieve a functional, real-time order display, improving the overall user experience.









Problem-Solving and Debugging

This week emphasised the importance of thorough testing and debugging. While my initial HTML and CSS worked well, it took careful review and collaboration to fix the issue with the kitchen view. It showed me that even small errors can have significant impacts on the overall functionality, and I’ve learned the value of revisiting and refining my work.




Collaboration 

Working closely with my colleagues was essential to solving the final problem. When we encountered the issue while refreshing the page, my colleague’s research and our teamwork helped resolve it quickly.




Improvement

One lesson I’ve taken away is the need for continuous testing throughout development. Early testing might have caught the kitchen view issue sooner. Going forward, I’ll aim to integrate testing as part of my development process to avoid last-minute fixes.





Overall reflection:





Collaboration  

Throughout the project, collaboration was a key aspect of our success. Early on, we encountered issues with Git and learned the importance of coordinating commits to avoid conflicts. By adopting a more structured approach to commits and branching, we managed to streamline our workflow. As we progressed, our teamwork became even more crucial, particularly when tackling challenges that individual members couldn’t solve alone, such as integrating the HTML with the main application. The consistent communication and division of tasks based on strengths allowed us to maintain steady progress, even when facing complex problems.




Configuration Management  

From the beginning, we utilized Git for version control, and our understanding of configuration management improved over time. Initially, we encountered issues with simultaneous commits, but as we incorporated a branching strategy, we became more efficient. This helped prevent further conflicts and allowed us to work independently while keeping the project organized. Our experience with Git has reinforced the importance of a well-planned configuration management system in collaborative projects.




Problem-Solving and Learning  

Each week presented new challenges, from connecting HTML and CSS to working with databases and debugging. The project reinforced the idea that learning is continuous, especially in a fast-paced, collaborative environment. We often faced problems that required immediate solutions, and by breaking tasks down into manageable steps, we were able to move forward. The ability to adapt, research, and seek help from teammates was essential to overcoming these obstacles.




Reflective Practice and Improvements  

One area for improvement identified during the project was the need for continuous testing. Many issues, such as the problem with the kitchen view, could have been resolved earlier with more frequent testing throughout development. Moving forward, I plan to integrate testing as a regular part of my development process to catch potential issues sooner and reduce the need for last-minute fixes.





Feedback:




We received additional feedback regarding the tests, which we had completely missed earlier. To address this, we gathered as a team and created two new test files. With focus and persistence, we conducted thorough testing using pytest, working together to identify and resolve any issues that arose. We didn’t stop until every test finally passed successfully, leaving us with a strong sense of achievement and improvement in our work.