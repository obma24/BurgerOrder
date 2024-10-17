Engineering Diary (Individual Assignment):
Name: Baraa Msaddi
(bams24 / Baraamsaddi)

Copied from google docs: 

Week 1: Setting up the project and getting started 
In the first week, we laid the groundwork for our project. We created a shared GitHub repository where everyone on the team could access and work together. This was a really important step to make sure our collaboration went smoothly. I made my own branch in the repository to work on specific parts of the project without messing up the main code. This way, I could test and make changes safely without worrying about breaking anything.
We also started talking about how the website would look and function. We had several team meetings where I shared ideas and helped brainstorm how the website should be structured. I made sure to write everything down so we could stay organized and consistent. Looking back, I could have been more forward-thinking about how our early design choices would affect the project down the line. This might have made it easier for me when I started developing features.
Collaboration: The team worked well together when setting up the repository. However, it would have been better if we had clearer communication about who was doing what tasks.
Configuration Management: I used Git branches to separate the features I was working on, which kept things organized. Going forward, I want to use better names for the branches to make it even easier for everyone to follow.
Implementation & Documentation: I documented the setup process, but I can improve by planning ahead to see how these decisions will affect future tasks.
Testing & Debugging: We didn’t do much testing this week because we were mostly focused on planning. I plan to set up a testing framework in the coming weeks.

Week 2: Getting Into the Technical Side 
This week, the team spent more time than expected choosing the programming language. We finally decided on Python. I spent a lot of time refining how we use GitHub for our project, focusing on how we create and merge branches. By playing around with branches, I realized that using more detailed and descriptive branch names would help us keep track of progress more easily.
We divided the work among team members and set milestones. My main responsibility was to work on the website’s ordering system. In hindsight, I think I could have worked more closely with my teammates, especially when I ran into technical challenges.
Collaboration: Dividing tasks helped make things clearer, but working more closely with my teammates would have made it easier to solve some of the technical issues we faced early on.
Configuration Management: I continued working with Git branches and merging them. I see that using clearer, more specific branch names would make it easier to follow progress.
Implementation & Documentation: I started learning the tools and frameworks needed to build the ordering system. Looking back, I should have taken more time to document what I was learning.
Testing & Debugging: We didn’t do a lot of testing this week, but I realized how important it is to plan out test cases early to avoid problems later.

Week 3: Learning and Starting Work on the Kitchen System 
This week, I switched my focus to working on the kitchen side of the project. I spent a lot of time learning new things by watching YouTube tutorials and using resources like Discord, Python.org, and W3Schools. These were really helpful for gaining the skills I needed.
Collaboration: I mostly studied and worked on my own this week. I probably could have communicated more with my teammates to update them on what I was doing.
Configuration Management: I kept using Git branches but didn’t document where I was learning things from as well as I should have. Writing this down would have been helpful later.
Implementation & Documentation: Most of my work this week was about learning, but I should have started documenting the technical details I was picking up to make future work easier.
Testing & Debugging:
Issue 1: Cancel Button Not Working
Solution: Check that the cancel button in kitchen.html has the correct event listener and that the cancelOrder function is properly set up in the JavaScript.
Issue 2: Orders Not Being Removed
Solution: Fix the logic in the cancel_order function in app.py to ensure it updates the list of active orders when an order is canceled.
Issue 3: No Feedback to the User
Solution: Add a notification system, like a toast message, to show users when an order has been successfully canceled.
Issue 4: Code Clean-Up Made Things Break
Solution: Re-add important comments that explain complicated code in app.py and encourage the team to leave comments to help each other understand the code better.

Week 4: Writing Code for the Kitchen System
 This week, we started writing the actual code. My main task was to add a feature in app.py for kitchen staff to cancel orders. I also added a red "cancel" button in kitchen.html that was easy to find and use.
I ran into a small problem with my GitHub account because I had two different names (bams24 and Baraamsaddi), which caused some confusion.
Collaboration: The team worked really well together this week. We helped each other write and organize the code, and it made solving problems a lot quicker.
Configuration Management: I made several commits to track the new features I added and the code clean-up. This helped keep the project’s version control well-organized.
Implementation & Documentation: I documented the logic for the cancel order feature, but I could improve the clarity of the comments I left in the code.
Testing & Debugging: I manually tested the cancel button by placing and canceling orders. It worked well, but I plan to set up automated testing next week.

Week 5: Wrapping Up the Order Confirmation Feature
 One of my teammates added the basic functionality to confirm orders in app.py. This week, I expanded on that by updating index.html to show a confirmation message when an order is placed. I created a section in the HTML that checks if an order is confirmed, and if it is, it shows the details of the order.
I also used a loop to display each burger and its customizations in a clear and organized way, so users can easily review their orders.
Collaboration: I worked closely with my teammate to make sure our code was properly merged and worked together without any conflicts.
Configuration Management: I made frequent and detailed commits to track the progress of the new features.
Implementation & Documentation: I added the new functionality and documented it clearly. I made sure to leave comments in both the HTML and Python code to explain the key parts for future reference.
Testing & Debugging: I tested the order confirmation feature by placing orders and checking that the correct details were displayed. The feature worked well, but I plan to write unit tests to automate the process next week.


Week 6: Final Code Review and Wrapping Up
 In the final week, we reviewed all of the code to make sure it met the project’s goals. We also finalized our documentation and the engineering diary. I went over my commits again to make sure everything I worked on was working correctly.
Collaboration: We worked well together this week, sharing feedback and helping each other improve the code where needed.
Configuration Management: I made sure all my branches were merged properly and that the version history was clean and well-documented.
Implementation & Documentation: I updated the documentation to reflect the final state of the project, including detailed comments and descriptions of the major features I worked on.
Testing & Debugging: I manually tested all the features one last time to ensure everything was functioning correctly. I also helped add unit tests for key features, which gave us more confidence that the system was stable.

Debugging Session: Fixing Order Confirmation Issue While working on the order confirmation feature, I noticed that the confirmed orders weren’t showing up correctly. I used breakpoints to figure out that the problem was a missing check for the order_confirmed variable in the HTML. Once I fixed that, the feature worked as expected.

Reflection: 
Looking back on the project, I've learned a lot about both the technical side and working with a team. Early on, we spent a lot of time setting up tools, but we didn't plan enough for how each feature would work. More upfront planning would have saved time and made development smoother. Next time, I’ll focus on detailed planning from the start to avoid confusion later. The times when we communicated well as a team, things went much smoother. When I worked closely with teammates, we avoided issues, but working too independently sometimes slowed me down. I’ve learned that checking in with others and asking for help early on is important.
I started strong with documentation, but as the project progressed, I focused more on coding. This made it harder to track decisions later. Going forward, I’ll document throughout the project to make things easier for me and the team.
We didn’t focus on testing early enough, which led to bugs that could have been caught sooner. Testing as I go, rather than waiting until later, will save time and catch issues early in future projects. I wasted time manually looking for errors when debugging tools could have helped. Using these tools earlier would have saved me frustration. I’ll rely more on them next time to troubleshoot efficiently.
Inconsistent branch names caused confusion during merging. In the future, I’ll use clearer and more organized branch names to make it easier for me and the team to manage code. These lessons will guide me in future projects for better planning, teamwork, and development.

