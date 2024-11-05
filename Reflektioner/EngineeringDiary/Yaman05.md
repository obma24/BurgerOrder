Engineering Journal: Insights from the BurgerOrder Development Process - Yaman Alaiash

Week 1: Learning GitHub and Initial Planning

We began by setting up our development environment in GitHub, primarily because it was the client’s preference and a tool we had been recommended multiple times before. As a team, we spent significant time exploring and familiarizing ourselves with GitHub. Our goal was to understand the basics of writing and sharing code collaboratively, so we tested features like push, pull, and fetch commands. We also learned how to handle conflicts, such as when two team members accidentally modified the same file at the same time. This exercise was crucial in establishing our workflow and ensuring smooth collaboration within the team.

We also began discussing how we would approach the project as a group. Given that this was a foundational course, we decided everyone should be involved in as many parts of the project as possible, instead of specializing in specific areas. This decision helped each team member gain broad experience across different aspects of development.

Week 2: Research and Task Distribution

In the second week, our focus shifted to researching the fundamental knowledge required for our project. We evaluated different programming languages to determine which would be most suitable, with Python and Java as the main contenders. After weighing the pros and cons, we chose Python for its simplicity, readability, and the fact that most of the group was already familiar with it. This decision allowed us to move faster, as we didn’t have to learn a completely new language from scratch.

After selecting Python, we explored Flask as our web framework. Flask seemed to fit well for a project of this scale, particularly due to its flexibility and simplicity in creating web applications. By the end of the week, we had gained enough understanding of Flask to begin discussing the project structure.

At this point, we also started planning task distribution within the team. While most members focused on specific tasks, there was flexibility to switch if needed. My primary responsibility was to connect the database with Docker, while also fixing bugs that appeared in the code. Since this was new territory for me, I spent a lot of time researching online resources—primarily YouTube tutorials—to learn how to approach these tasks. I also supported the team member working on the database by providing suggestions and ideas as we moved forward.

Week 3: Learning and Overcoming Early Challenges

After three weeks, I realized I still didn’t have enough knowledge to fully dive into the project. I spent most of this week trying to bridge that gap. The example code we had was a good starting point, but with about 50% of the project still needing to be built, I had to expand my foundational knowledge before making significant progress.

Despite thorough research, I continued to struggle with setting up the database using Docker. This led me to discuss with my team and switch tasks, focusing solely on testing, debugging and adding necessary functionalities to the code. Although progress was slower than anticipated, it was essential not to rush and ensure I fully understood the concepts before moving forward.

During this week, a group member took the lead and laid the foundation for the project by setting up two separate Flask servers. Although the initial setup had minor flaws, it gave us a strong starting point. My role at this stage was to assist with debugging the code and add new functionalities where necessary. This phase was critical, as it allowed us to write core components of the application.

Week 4: Problem Solving and Code Refinement

By week four, I had a much better understanding of the technical requirements and started making substantial progress. With the basics in place, the team shifted focus to refining our Flask servers and solving several issues that had arisen during previous weeks. We spent time reviewing and improving the code, ensuring it was both functional and efficient.

One major issue I encountered was how the system handled multiple items in the cart. Initially, if a user ordered two burgers, the system generated two separate orders instead of bundling them together as a single order. This was inefficient and confusing for users. To fix this, I updated the code to ensure that all items were grouped into a single order. This involved restructuring the order logic to bundle the items together.

Additionally, I noticed there was no functionality for viewing the cart’s contents. I created a `/view_cart` endpoint to allow users to see the items in their cart, and I also added a POST endpoint for removing items from the cart via `/remove_from_cart`. These updates gave users more control over their orders, allowing them to manage their cart dynamically.

During week four, I also focused on using the debugger in VS Code to better understand and improve the code for several key functions, including the ordering and payment processes. The following steps document the debugging session I conducted:
Selecting Functionality: I chose to focus on the function for ordering a “Dripping With Lard Heartstopper” meal, as it is a core part of the app and involves multiple stages that could benefit from debugging.

Setting Breakpoints: I placed breakpoints at strategic points in the code:
At the start of the place_order function in app.py, where the order details are initially processed.
Inside the process_payment function, where the payment is handled.
On the final line of the add_to_cart function to ensure the item is correctly added to the cart.
To locate the file and functions where I needed to set these breakpoints, I reviewed the project structure in VS Code, specifically examining the app.py file, where the ordering logic is implemented.

Proceeding with Debugging and Using Debugger Tools:
I started the debugging session and used the "Continue" button to let the code run until it reached the next breakpoint.
When I reached the process_payment function, I used "Step Into" to follow each line inside the function and examine its flow.
To skip unnecessary details in functions I had already analyzed, I used "Step Over" to continue without stepping into every line.
I also used "Step Out" to exit functions where I had gathered enough information to move on.
Monitoring Variables:
I monitored the order_total variable to ensure it was calculated correctly.
In the debugger, I added order_total as a "watched variable." Initially, its value was 0, but it increased as items were added to the cart.
To detect changes in order_total, I used the “break on change” feature within watched variables, which paused the code each time the variable was modified. This allowed me to observe how the value of order_total changed step-by-step as items were added.
Exploring Different Paths:
I tested different paths through the ordering process, including placing various orders, canceling halfway through, and modifying the order in the cart.
Each path affected which parts of the code executed. For instance, canceling an order mid-way triggered error handling logic I had not originally considered.
These variations also impacted the watched variables, as values like order_total and order_items fluctuated based on the actions taken.
I repeated each step several times to ensure I understood how the debugger and its features worked. This process was invaluable for identifying and fixing issues I would have missed otherwise.


Week 5: Further Development and Optimizations

With most foundational issues resolved, we spent week five focusing on improving the user experience and streamlining the project’s functionality. The goal was to ensure that all the features we had implemented worked smoothly together.

During testing, I found that orders were not being correctly transmitted to the kitchen service. I implemented a function that used an HTTP POST request to send the order to the kitchen via `/kitchen/orders`. I also added error handling, ensuring that any issues with the request were logged and that the system would continue running without crashing.

Previously, each item in the cart was sent as a separate order, which was inefficient and created unnecessary load on the kitchen service. To address this, I updated the `/place_order` function so that the entire cart would be sent as a single order. I also modified the `kitchen.py` code to process multiple items from a single order. This significantly streamlined communication between the user interface and the kitchen service, making the system more efficient.

Week 6: Final Touches and Documentation

In the final week, I concentrated on polishing all aspects of the project. I reviewed the entire codebase, made any necessary adjustments, and ensured that everything was working as expected.

As part of the final tasks, I updated the `README.md` file to include a step-by-step guide on how to set up and run the application using Docker. This documentation was essential for any future developers or users who wanted to contribute to or test the project. I also added links in the documentation for both the BurgerOrderer interface and the KitchenView, making it easy for users to access both the customer-facing and kitchen-facing sides of the application.

Additionally, I went through the code and added comments to parts that weren’t well-documented, helping future developers understand the logic behind certain functions and making the code easier to maintain.

Reflection

The best part of this project was that it made both me and my colleagues more familiar with GitHub, a tool crucial for our future careers as software engineers. Working on BurgerOrder also boosted my Python skills and gave me valuable experience in integrating databases with Docker. Learning how to containerize our application added another important skill to my toolkit.



Problem-Solving and Debugging:

Debugging became a central part of my workflow, not just for fixing bugs, but for improving the project’s efficiency and scalability. I’ve come to realize that debugging requires a lot of coding experience. Although I managed most issues on my own, I sometimes needed help from more experienced students. There were also moments when we asked for advice from a teacher in a different course (the Python course), since the project involved Python. This collaboration was essential in overcoming some of the more complex challenges.

Team Collaboration:

Collaboration was another crucial aspect. Initially, managing the codebase on GitHub led to several conflicts. However, as we refined our workflow and improved communication, teamwork became much smoother. Clear communication helped us avoid misunderstandings, especially when multiple people worked on different parts of the project. When group members were unable to meet in person, we seamlessly switched to Discord calls with screen-sharing. This allowed us to stay on track and avoid delays in the project.

What Could Be Improved:

One major improvement would have been to work more effectively with Git branches. Instead of waiting for each other to finish changes before starting new tasks, we could have used individual branches to work in parallel. This would have allowed for smoother collaboration, reduced downtime, and minimized the risk of conflicting changes.

While relying on YouTube tutorials and online documentation was helpful, it would have been far more effective to plan our questions ahead of time and bring them to the lecture sessions. This would have allowed us to ask the teacher directly and get immediate, targeted feedback. Additionally, the lack of branch usage likely contributed to this issue. If we had been coding simultaneously using branches, we would have encountered more questions and challenges earlier, giving us more opportunities to seek help from the instructor during class time. (This excludes the initial phase when we were still gaining foundational knowledge.)

Conclusion:

The most difficult part of this project was overcoming the initial sense of being completely overwhelmed. When we were first introduced to the project, my programming knowledge was limited to basic concepts like while- and for-loops. We had no clear idea of how to begin, and it seemed impossible to complete the project on time. However, despite the challenges, it gradually became more manageable.

Having five members in the group certainly made things easier, as we could divide the workload and support each other. It took considerable time and effort to overcome the technical obstacles, but with guidance from the teacher, help from fellow students, and countless hours spent on YouTube tutorials, we made steady progress.

One of the key lessons I learned from working on BurgerOrder was the importance of stepping back and reflecting on the code. Taking the time to think about what we were doing and planning the next steps carefully helped us avoid possible mistakes and move forward more efficiently.



	Correcting mistakes:
Upon reviewing the assignment, the teacher pointed out that pytest tests were missing. In response, we arranged a meeting to add the necessary tests to the "app.py" file for the KitchenView app. I did therefore the following commit:

In the "app.py" file for the KitchenView app, I ran some tests to see if I could cancel orders correctly. The first test checked if I could cancel an order and if the order list would update after that. At first, this test failed because the order I thought I canceled was still in the list, which caused an error.

The second test was supposed to check what happens when I try to cancel an order that doesn’t exist. Instead of getting a 404 error, it returned a 200 status, meaning the app wasn’t handling that situation properly.

To fix the problems, I changed how the orders are stored. Instead of using a simple list (orders = []), I made it part of the Flask app itself (app.orders = []). This way, the same order list is used throughout the app, and it’s easier to reset for testing. I also updated the code to use app.orders everywhere instead of the standalone list.

After making these changes, I ran the tests again. The first test passed, confirming that I could cancel an order and the order list was empty afterward. The second test also passed, returning the expected 404 status when trying to cancel an order that didn’t exist. Overall, these fixes made the app better at handling order.
