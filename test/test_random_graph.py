import random

import unittest

import igraph as ig

import igraph_steiner_tree

class GraphTest(unittest.TestCase):

    def test_random_graphs(self):
        for graph_size in [10, 100, 500]:
            graph = ig.Graph.Barabasi(graph_size, 4)
            for v in graph.vs:
                v['name'] = str(v.index)
            node_ids = random.sample(range(len(graph.vs)), 5)
            node_ids = [str(i) for i in node_ids]
            st = igraph_steiner_tree.steiner_tree(graph, node_ids)
            self.assertTrue(st.is_connected())
            self.assertTrue(st.is_tree())
            for i in node_ids:
                self.assertIsNotNone(st.vs.find(i))


if __name__ == '__main__':
    unittest.main()
