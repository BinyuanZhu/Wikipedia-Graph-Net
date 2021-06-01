# Wikipedia-Graph-Net

The WikiRacer is a game where one tries to navigate to one 
Wikipedia article from another in the fewest number of clicks 
possible. This program's goal is to accomplish this task given 
the start and goal article by creating a graph and searching 
through it optimally using an A* search heuristic.

## Heuristic
Because of the semantic nature of the heuristic, we have 
developed multiple heuristics in the form of ```heuristic_#``` 
where # represents an int. Currently, the default heuristic is
a cosine similarity score between the document-term matrices 
generated from the article intros. 

## How It Works
Essentially, a graph of ```Article``` classes are generated 
dynamically from the start point and the A* algorithm employs
a priority queue (min-heap implementation) in order to 
efficiently traverse the graph and look for the desired end 
article.
