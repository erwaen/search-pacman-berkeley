# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    my_stack = Stack() # Inicializamos nuestra pila de nodos, mas abajo se describe la forma del nodo

    # Aca guardamos el estado inicial que es una tupla de la forma (x,y)
    first_state = problem.getStartState()

    # Creamos nuestro nodo que va a tener la forma de ( (x,y), [movements_to_reach_here])
    first_node = (first_state, []) # lo cual al comiento los movimientos llegar hasta ahi es vacia

    my_stack.push(first_node)

    visited_nodes = [] # Para verificar despues si el nodo fue o no visitado

    # Recorremos mientras la pila no esta vacia
    while not my_stack.isEmpty():
        current_node = my_stack.pop()
        actual_position = current_node[0] # la posicion actual que corresponde a este nodo (x,y)
        movements_to_reach_here = current_node[1] # guardamos los movimientos para llegar hasta aca

       
        # Si encontramos que este nodo pertenece a un punto de Goal, entonces reotornamos ya los movimientos
        if problem.isGoalState(actual_position):
            return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado

        # si este nodo todavia no se visito entonces que ejecute los siguiente
        if actual_position not in visited_nodes:
            visited_nodes.append(actual_position)
            successors_nodes = problem.getSuccessors(actual_position) # esta funcion nos retorna de la manera siguiente [((x,y), movement, cost)]


            # Recorremos estos nodos sucesores ( recordar que son elementos de la manera [((x,y), movement, cost)])
            for successor_node in successors_nodes:
                
                suc_pos = successor_node[0]
                suc_mov = successor_node[1]
                movements_for_this_node = movements_to_reach_here[:] # copio los movimientos anteriores para llegar a este nuevo nodo
                movements_for_this_node.append(suc_mov) # agregamso el ultimo movimiento

                #no usaremos el costo para este algortimo ya que todos son de costo 1

                new_node = (suc_pos, movements_for_this_node)
                my_stack.push(new_node)
    
    return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado


    # util.raiseNotDefined()


# Para la solucion de BFS utilizamos el mismo algortimo que DFS pero usando una Cola
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "*** YOUR CODE HERE ***"
    from util import Queue

    my_queue = Queue() # Inicializamos nuestra COLA de nodos, mas abajo se describe la forma del nodo

    # Aca guardamos el estado inicial que es una tupla de la forma (x,y)
    first_state = problem.getStartState()

    # Creamos nuestro nodo que va a tener la forma de ( (x,y), [movements_to_reach_here])
    first_node = (first_state, []) # lo cual al comiento los movimientos llegar hasta ahi es vacia

    my_queue.push(first_node)

    visited_nodes = [] # Para verificar despues si el nodo fue o no visitado

    # Recorremos mientras la cola no esta vacia
    while not my_queue.isEmpty():
        current_node = my_queue.pop()
        actual_position = current_node[0] # la posicion actual que corresponde a este nodo (x,y)
        movements_to_reach_here = current_node[1] # guardamos los movimientos para llegar hasta aca

       
        # Si encontramos que este nodo pertenece a un punto de Goal, entonces reotornamos ya los movimientos
        if problem.isGoalState(actual_position):
            return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado

        # si este nodo todavia no se visito entonces que ejecute los siguiente
        if actual_position not in visited_nodes:
            visited_nodes.append(actual_position)
            successors_nodes = problem.getSuccessors(actual_position) # esta funcion nos retorna de la manera siguiente [((x,y), movement, cost)]


            # Recorremos estos nodos sucesores ( recordar que son elementos de la manera [((x,y), movement, cost)])
            for successor_node in successors_nodes:
                
                suc_pos = successor_node[0]
                suc_mov = successor_node[1]
                movements_for_this_node = movements_to_reach_here[:] # copio los movimientos anteriores para llegar a este nuevo nodo
                movements_for_this_node.append(suc_mov) # agregamso el ultimo movimiento

                #no usaremos el costo para este algortimo ya que todos son de costo 1

                new_node = (suc_pos, movements_for_this_node)
                my_queue.push(new_node)
    
    return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado


# Para el uniformCost usamos un PriorityQueue para obtener siempre el que tiene menos costo
# y modificamos el algortimo que teniamos
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue


    my_priority_queue= PriorityQueue() # Inicializamos nuestra priorityQueue de nodos, mas abajo se describe la forma del nodo

    # Aca guardamos el estado inicial que es una tupla de la forma (x,y)
    first_state = problem.getStartState()
    costo_inicial = 0
    # Creamos nuestro nodo que va a tener la forma de ( (x,y), [movements_to_reach_here])
    first_node = (first_state, [], costo_inicial) # lo cual al comiento los movimientos llegar hasta ahi es vacia
    
    my_priority_queue.push(first_node, costo_inicial)

    visited_nodes = [] # Para verificar despues si el nodo fue o no visitado

    # Recorremos mientras la priorityQueue no esta vacia
    while not my_priority_queue.isEmpty():
        current_node = my_priority_queue.pop()
       
        actual_position = current_node[0] # la posicion actual que corresponde a este nodo (x,y)
        movements_to_reach_here = current_node[1] # guardamos los movimientos para llegar hasta aca
        node_cost = current_node[2] #Guardamos el costo para llegar hasta ese nodo
       
        # Si encontramos que este nodo pertenece a un punto de Goal, entonces reotornamos ya los movimientos
        if problem.isGoalState(actual_position):
            return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado

        # si este nodo todavia no se visito entonces que ejecute los siguiente
        if actual_position not in visited_nodes:
            visited_nodes.append(actual_position)
            successors_nodes = problem.getSuccessors(actual_position) # esta funcion nos retorna de la manera siguiente [((x,y), movement, cost)]


            # Recorremos estos nodos sucesores ( recordar que son elementos de la manera [((x,y), movement, cost)])
            for successor_node in successors_nodes:
                
                suc_pos = successor_node[0]
                suc_mov = successor_node[1]
                suc_costo = successor_node[2] # el costo para dar al siguiente paso (para el pacman siempre es 1)
             
                new_node_cost = node_cost + suc_costo # actualizamos el costo total para llegar al nuevo nodo
                movements_for_this_node = movements_to_reach_here[:] # copio los movimientos anteriores para llegar a este nuevo nodo
                movements_for_this_node.append(suc_mov) # agregamso el ultimo movimiento

                #no usaremos el costo para este algortimo ya que todos son de costo 1

                new_node = (suc_pos, movements_for_this_node, new_node_cost)
                my_priority_queue.push(new_node, new_node_cost)
    
    return movements_to_reach_here # retornamos las sdirecciones a ejecutar para llegar al resultado



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
