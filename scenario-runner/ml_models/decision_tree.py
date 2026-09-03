from tkinter import Image
import matplotlib.pyplot as plt
import six
from IPython.display import Image
from pydot import graph_from_dot_data
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
from sklearn.tree import export_graphviz, _tree

def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [feature_names[i]
                    if i != _tree.TREE_UNDEFINED else "undefined!"
                    for i in tree_.feature]
    print("def tree({}):".format(", ".join(feature_names)))
    print(tree.classes_)

    def recurse(node, depth):
        indent = "    " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, np.argmax(tree_.value[node])))

    recurse(0, 1)

def tree_to_pseudo(tree, feature_names):
    '''
    Outputs a decision tree model as if/then pseudocode

    Parameters:
    -----------
    tree: decision tree model
        The decision tree to represent as pseudocode
    feature_names: list
        The feature names of the dataset used for building the decision tree
    '''

    left = tree.tree_.children_left
    right = tree.tree_.children_right
    threshold = tree.tree_.threshold
    features = [feature_names[i] for i in tree.tree_.feature]
    value = tree.tree_.value

    def recurse(left, right, threshold, features, node, depth=0):
        indent = "  " * depth
        if (threshold[node] != -2):
            print(
            indent, "if ( " + features[node] + " <= " + str(threshold[node]) + " ) {")
            if left[node] != -1:
                recurse(left, right, threshold, features, left[node], depth + 1)
                print(
                indent, "} else {")
                if right[node] != -1:
                    recurse(left, right, threshold, features, right[node], depth + 1)
                print(
                indent, "}")
        else:
            print
            (indent, "return " + str(value[node]))

    recurse(left, right, threshold, features, 0)

def extract_rules(clf, X_train, n):
    # get the nodes which are leaves
    leaves = clf.tree_.children_left == -1
    leaves = np.arange(0, clf.tree_.node_count)[leaves]

    # loop through each leaf and figure out the data in it
    leaf_observations = np.zeros((n, len(leaves)), dtype=bool)
    rule_list = []
    #values = np.zeros(len(leaves), dtype= int)
    values = np.zeros(len(leaves), dtype=list)
    samples_no = np.zeros(len(leaves), dtype= int)
    # build a simpler tree as a nested list: [split feature, split threshold, left node, right node]
    thistree = [clf.tree_.feature.tolist()]
    thistree.append(clf.tree_.threshold.tolist())
    thistree.append(clf.tree_.children_left.tolist())
    thistree.append(clf.tree_.children_right.tolist())
    # get the decision rules for each leaf node & apply them
    for (ind, nod) in enumerate(leaves):
        # get the decision rules in numeric list form
        rules = []
        RevTraverseTree(thistree, nod, rules)
        # convert & apply to the data by sequentially &ing the rules
        thisnode = np.ones(n, dtype=bool)
        for rule in rules:
            #print("rule: {}".format(rule))
            #print(X_train[:, rule[0]])
            if rule[1] == 1:
                thisnode = np.logical_and(thisnode, X_train[:, rule[0]] > rule[2])
                #thisnode = np.logical_and(thisnode, X_train[rule[0]] > rule[2])
            else:
                thisnode = np.logical_and(thisnode, X_train[:, rule[0]] <= rule[2])
                #thisnode = np.logical_and(thisnode, X_train[rule[0]] <= rule[2])
        # get the observations that obey all the rules - they are the ones in this leaf node
        leaf_observations[:, ind] = thisnode
        # values[ind] = np.argmax(clf.tree_.value[nod])
        # samples_no[ind] = np.max(clf.tree_.value[nod])
        values[ind] = clf.tree_.value[nod]
        samples_no[ind] = np.sum(clf.tree_.value[nod])
        rule_list.append(rules)

    #sort based on class and number of samples repectively
    # zipped_items = zip(values, samples_no, rule_list, leaf_observations)
    # sorted_items = sorted(zipped_items, reverse=True)
    # values, samples_no, rule_list, leaf_observations = zip(*sorted_items)

    #print(rule_list)
    return values, samples_no, rule_list, leaf_observations

def RevTraverseTree(tree, node, rules):
    '''
    Traverase an skl decision tree from a node (presumably a leaf node)
    up to the top, building the decision rules. The rules should be
    input as an empty list, which will be modified in place. The result
    is a nested list of tuples: (feature, direction (left=-1), threshold).
    The "tree" is a nested list of simplified tree attributes:
    [split feature, split threshold, left node, right node]
    '''
    # now find the node as either a left or right child of something
    # first try to find it as a left node
    try:
        # print(tree)
        # print(tree[2])
        # print("node: {}".format(node))
        prevnode = tree[2].index(node)
        leftright = -1 #<=
    except ValueError:
        # failed, so find it as a right node - if this also causes an exception, something's really f'd up
        # print(tree)
        # print(tree[3])
        # print("node: {}".format(node))
        prevnode = tree[3].index(node)
        leftright = 1 #>
    # now let's get the rule that caused prevnode to -> node
    rules.append((tree[0][prevnode],leftright,tree[1][prevnode]))
    # if we've not yet reached the top, go up the tree one more step
    if prevnode != 0:
        RevTraverseTree(tree, prevnode, rules)

