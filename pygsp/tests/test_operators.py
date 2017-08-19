# -*- coding: utf-8 -*-

"""
Test suite for the operators module of the pygsp package.

"""

import unittest

import numpy as np

from pygsp import graphs, operators


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = graphs.Logo()
        cls.G.compute_fourier_basis()

        rs = np.random.RandomState(42)
        cls.signal = rs.uniform(size=cls.G.N)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_difference(self):
        for lap_type in ['combinatorial', 'normalized']:
            G = graphs.Logo(lap_type=lap_type)
            grad = operators.grad(G, self.signal)
            div = operators.div(G, grad)

            Ls = operators.div(G, operators.grad(G, self.signal))
            np.testing.assert_allclose(Ls, G.L * self.signal)

    def test_fourier_transform(self):
        f_hat = operators.gft(self.G, self.signal)
        f_star = operators.igft(self.G, f_hat)
        np.testing.assert_allclose(self.signal, f_star)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)