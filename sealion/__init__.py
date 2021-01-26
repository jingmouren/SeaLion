"""
SeaLion is a simple machine learning and data science library.

=============================================================

Designed with beginners in mind, it has rich documentation via Pydoc and algorithms that span from the most basic
to more modern approaches. It is meant to help beginners navigate it all, and the documentation not only explains t
he models and their respective functions but also what they are and when to use them. Emphasis was also put on creating
new functions to make it interesting for those who are just getting started and seasoned ml-engineers alike.

I hope you enjoy it!
- Anish Lakkapragada 2021
"""

import neural_networks
from . import cython_decision_tree_functions
from . import cython_knn
from . import cython_ensemble_learning
from . import cython_naive_bayes
from . import cython_tsne
from . import cython_unsupervised_clustering
from . import decision_trees
from . import DimensionalityReduction
from . import ensemble_learning
from . import naive_bayes
from . import nearest_neighbors
from . import regression
from . import unsupervised_clustering
from . import utils

cython_training = cython_decision_tree_functions.CythonTrainDecisionTraining
gini_impurity = cython_decision_tree_functions.gini_impurity
probabilities = cython_decision_tree_functions.probabilities
find_best_split = cython_decision_tree_functions.find_best_split
branch_data = cython_decision_tree_functions.branch_data
tuplelize = cython_decision_tree_functions.tuplelize
anti_tupelize = cython_decision_tree_functions.anti_tupelize
chunk_predict = cython_decision_tree_functions.chunk_predict
go_down_the_tree = cython_decision_tree_functions.go_down_the_tree
