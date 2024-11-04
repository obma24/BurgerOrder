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

However, I quickly encountered a challenge: I had no prior experience connecting two different files, and I was unsure how to connect the HTML and CSS front-end with the main application. This gap in my knowledge made the task more complicated than I had anticipated. I spent a significant amount of time researching online, looking for tutorials and guides on how to connect different files. I discovered that there were multiple approaches, and the process was quite complex, involving different tools and technologies.

Some of the solutions I found required learning new programming languages or frameworks, which was initially overwhelming. After exploring several options, I realized that I needed to discuss the situation with my team. We held a meeting to talk about the different methods I had found and evaluated which one would be the most feasible for our project. Given the complexity, we decided that the best approach was to take it one step at a time. Our plan is to first establish a basic connection between the front-end and main application, then gradually add more functionality as we go along.

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
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            padding: 50px;
            margin: 0;
            color: #333;
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
During the final week of the project, I shifted my focus to intensive debugging and ensuring the system ran smoothly. This process involved close collaboration with my team and included significant code revisions in app.py and kitchen.py. Here, I'll delve deeper into the debugging sessions, detailing the specific issues encountered, the variables I monitored, and the resolutions implemented.
Issue 1: Multiple Orders Sent Individually
One of the major issues I encountered was that each item in the cart was being sent as a separate order to the kitchen. This behavior led to an overload of HTTP POST requests and cluttered the kitchen interface with numerous individual orders. The problem stemmed from the loop structure in the /place_order endpoint.
Initial Code Analysis:
for order in session['cart']:
    requests.post('http://kitchen:5001/new_order', json=order)

Debugging Observations:
Variable Observed: session['cart'] – contained all items as separate entries.
Line Impacted: The loop at for order in session['cart'].
Resolution Strategy: To resolve this, I restructured the code so that all items in the cart were grouped into a single order. This required combining the cart contents into a single payload before sending it to the kitchen service.
Updated Code:
combined_order = {
    'orders': session['cart']
}
requests.post('http://kitchen:5001/new_order', json=combined_order)

Outcome: The modification allowed all items in the cart to be processed as a single order, optimizing communication between the front end and kitchen service.
Commit Explanation: Implemented logic to group cart items and send them as a single order.
Issue 2: Order Handling in kitchen.py
The kitchen application also needed adjustments to accept the newly structured combined order payload. Initially, it was designed to handle only single-item orders:
Previous Code:
orders.append(order)

Debugging Observations:
Variable Observed: order – contained only a single burger, not a list of orders.
Behavior Noted: The kitchen view displayed individual items without recognizing group orders.
Revised Code:
for order in combined_order['orders']:
    orders.append(order)

for order in combined_order['orders']:
    orders.append(order)

Outcome: This change ensured the kitchen service could parse and display multi-item orders as a cohesive set.
Commit Explanation: Updated kitchen.py to handle batched order processing.
Debugging Variables and Observations:
Key Variables:
session['cart'] – Verified it contained the intended items during the debugging process.
combined_order – Observed to ensure it aggregated all items correctly.
HTTP Responses – Checked to confirm successful POST requests with status codes.
Observations During Testing:
Initial POST requests confirmed with status code 200 when single orders were sent.
Adjustments verified by checking the order list in the kitchen view, ensuring all items appeared under a single entry.
Error Handling Observed:
try:
    conn.request('POST', '/kitchen/orders', body=json.dumps(order), headers=headers)
    response = conn.getresponse()
    if response.status != 200:
        print(f"Kunde inte skicka beställning till köket: {response.reason}")
except Exception as e:
    print(f"Kunde inte skicka beställning till köket: {e}")

Error Insight: Handled scenarios where communication to the kitchen failed, enabling better error tracking.

Reflection: Debugging Processes and Lessons Learned
Problem-Solving and Debugging: Debugging the multi-order issue underscored the importance of understanding data flow and payload structures. I learned to analyze how variables were passed between functions and services, which improved my approach to troubleshooting.
Key Lesson: Monitoring variables like session['cart'] and implementing step-by-step adjustments provided clarity on how the program handled data internally.
Continuous Testing Insight: Testing throughout development could have identified these issues sooner. By observing variable states, particularly in HTTP responses and session data, I gained insights that will inform future projects.




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


