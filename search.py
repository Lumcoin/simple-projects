import time

class Node:
    
    def __init__(self, state, get_actions, act, get_cost, get_heuristic, is_goal, action=None, parent=None):
        self.state = state
        self.state_get_actions = get_actions
        self.state_act = act
        self.state_get_cost = get_cost
        self.state_get_heuristic = get_heuristic
        self.state_is_goal = is_goal
        self.action = action
        self.parent = parent
        self.cost = self.state_get_cost(action, state)
        self.heuristic = self.state_get_heuristic(state)
    
    def replace_with(self, other):
        print(f'replacing: {self}\nwith: {other}')
        self.state = other.state
        self.action = other.action
        self.parent = other.parent
        self.cost = other.cost
        self.heuristic = other.heuristic
        print(self)

    def act(self, action):
        state = self.state_act(action, self.state)
        
        return Node(state, self.state_get_actions, self.state_act,
                    self.state_get_cost, self.state_get_heuristic,
                    self.state_is_goal, action, self)

    def expand(self):
        p_actions = self.state_get_actions(self.state)
        childs = [self.act(p_action) for p_action in p_actions]

        return childs

    def is_goal(self):
        return self.state_is_goal(self.state)
    
    def get_cost(self):
        cost = self.cost

        parent = self.parent
        while parent:
            cost += parent.cost
            parent = parent.parent
        
        return cost
    
    def get_weight(self):
        return self.get_cost() + self.heuristic
    
    def get_actions(self):
        actions = [self.action]

        parent = self.parent
        while parent:
            action = parent.action
            if action is not None:
                actions.append(action)
            
            parent = parent.parent
        
        return actions[::-1]

def a_star(initial_state, get_actions, act, get_cost, get_heuristic, is_goal):
    """
    Takes:
    [action,...] actions(state): function returning all actions possible at current state
    state        act(action, state): function returning state resulting from action on state
    float        cost(action, state): function returning cost of action on state
    float        heuristic(state): function returning heuristical cost from state to goal state
    bool         is_goal(state): function reutring if current state is a goal state

    Returns:
    list of actions leading to lowest cost."""

    start_time = time.time()

    node = Node(initial_state, get_actions, act, get_cost, get_heuristic, is_goal)
    frontier = [node]  # priority queue (insert before first instance with larger cost)
    reached = []

    while frontier:
        node = frontier.pop(0)
        reached.append(node)
        
        if node.is_goal():
            print(f'time for search: {time.time() - start_time}\n')
            return node.get_actions(), node.state  # calculate goal depth
        
        for child in node.expand():
            similar_node = [r_node for r_node in reached if r_node.state == child.state]
            if similar_node:
                similar_node = similar_node[0]
                if child.get_cost() < similar_node.get_cost():
                    similar_node.replace_with(child)
                else:
                    pass  # delete child node
            else:
                child_weight = child.get_weight()
                insert_index = None
                for i, f_node in enumerate(frontier):
                    if f_node.get_weight() > child_weight:
                        insert_index = i
                        break
                if insert_index is not None:
                    frontier.insert(insert_index, child)
                else:
                    frontier.append(child)
    
    print(f'time for search: {time.time() - start_time}')
    return None, None

def alpha_beta_search(game, state):
    player = game.to_move(state)
    alpha = float('-inf')
    beta = float('inf')
    value, move = max_value(game, state, player, alpha, beta)
    return move

def max_value(game, state, player, alpha, beta):
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    
    value = float('-inf')
    for action in game.actions(state):
        value2, action2 = min_value(game, game.result(state, action), player, alpha, beta)
        if value2 > value:
            value, move = value2, action
            # pruning start ---
            alpha = max(alpha, value)
        if value >= beta:
            return (value, action)
            # pruning end   ---

    return (value, move)

def min_value(game, state, player, alpha, beta):
    if game.is_terminal(state):
        return (game.utility(state, player), None)
    
    value = float('inf')
    for action in game.actions(state):
        value2, action2 = max_value(game, game.result(state, action), player, alpha, beta)
        if value2 < value:
            value, move = value2, action
            # pruning start ---
            beta = min(beta, value)
        if value <= alpha:
            return (value, action)
            # pruning end   ---

    return (value, move)