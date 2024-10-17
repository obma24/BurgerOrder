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



