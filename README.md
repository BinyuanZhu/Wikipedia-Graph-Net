# Wikipedia-Graph-Net

The WikiRacer is a game where one tries to navigate to one 
Wikipedia article from another in the fewest number of clicks 
possible. This program's goal is to accomplish this task given 
the start and goal article by creating a graph and searching 
through it optimally using an A* search heuristic.

### Test Ideas
_"Cell nucleus"_ and _"Cell biology"_

## Heuristic
Because of the semantic nature of the heuristic, we have 
developed multiple heuristics in the form of ```heuristic_#``` 
where # represents an int. Currently, the default heuristic is
a cosine similarity score between the document-term matrices 
generated from the article intros. 

## How It Works
Essentially, a graph of ```Article``` classes are generated 
dynamically from the start point and the **A*** algorithm employs
a priority queue _(min-heap implementation)_ in order to 
efficiently traverse the graph and look for the desired end 
article.

## Set Up
1. Clone the repository onto your local machine.
2. Navigate to the folder
3. Set up the correct venv:
   ```
   python3 -m venv venv
   virtualenv venv
   pip install -r requirements.txt
   ```
  Make sure that you are inside the venv when you are running ```pip install```
  <br />
4. Activate the ```venv``` by running ```source venv/bin/activate```
  <br />
5. Use ```flask run``` to run the flask app and navigate to the local host
    
