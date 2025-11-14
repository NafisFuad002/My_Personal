# ai code ar maddhome ami j kono (NFA) state,edge,node draw korte parbo
# ata google colab a kaj korbe

# Install graphviz if not installed
!pip install graphviz

from graphviz import Digraph
from IPython.display import Image

# Create Digraph with Left-to-Right layout
dot = Digraph(comment='NFA for a(a|b)*b', graph_attr={'rankdir':'LR'})  # LR = Left to Right

# koita node hobe ta declare korte hobe 'node_name', 'ki_nam_a_chinbo', shape
# States
dot.node('st', ' ', shape='none')          # start
dot.node('q1', 'q1', shape='circle')
dot.node('q2', 'q2', shape='circle')
dot.node('q3', 'q3', shape='circle')
dot.node('q4', 'q4', shape='doublecircle')    # final

# Transitions ['st_node', 'end_node', 'edge_connection_name']
dot.edge('st', 'q1', label=' ')
dot.edge('q1', 'q2', label='ε')   # start of loop
dot.edge('q2', 'q3', label='a')
dot.edge('q2', 'q3', label='b')
dot.edge('q3', 'q2', label='ε')   # loop back
dot.edge('q1', 'q4', label='ε')   # epsilon to move forward
dot.edge('q3', 'q4', label='ε')   # epsilon to move forward
dot.edge('q4', 'q4', label='b')   # last b

# Save PNG file
dot.render('nfa_a_aorb_star_b_RL', format='png')

# Display in Colab
Image('nfa_a_aorb_star_b_RL.png')