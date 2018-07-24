import unittest
import pandas as pd
import numpy as np
import apc

class TestFitTable(unittest.TestCase):

    def test_TA_odp(self):
        model = apc.Model()
        model.data_from_df(apc.loss_TA(), data_format='CL')
        model.fit(family='od_poisson_response', predictor='AC')
        model.fit_table()
        dev_table_Ad = model.fit_table(reference_predictor='Ad', 
                                        attach_to_self=False)
        
        self.assertTrue(np.allclose(
            model.deviance_table.astype(float).values,
            np.array([
                 [1.90301400e+06, 3.60000000e+01, 0.00000000e+00, np.nan, 
                  np.nan, np.nan, np.nan],
                 [2.26975638e+06, 4.40000000e+01, np.nan, 3.66742376e+05, 
                 8.00000000e+00, 8.67224670e-01, 5.52460650e-01],
                 [7.80786706e+06, 4.40000000e+01, np.nan, 5.90485306e+06, 
                 8.00000000e+00, 1.39630285e+01, 5.57824176e-09],
                [2.47405267e+06, 4.50000000e+01, np.nan, 5.71038670e+05, 
                 9.00000000e+00, 1.20028264e+00, 3.24889856e-01],
                [8.59757852e+06, 4.50000000e+01, np.nan, 6.69456452e+06, 
                 9.00000000e+00, 1.40714982e+01, 2.28532582e-09],
                [8.89772511e+06, 5.20000000e+01, np.nan, 6.99471110e+06, 
                 1.60000000e+01, 8.27009152e+00, 8.67290327e-08],
                [9.09618109e+06, 5.30000000e+01, np.nan, 7.19316708e+06, 
                 1.70000000e+01, 8.00445456e+00, 9.89397304e-08],
                [9.67492468e+06, 5.30000000e+01, np.nan, 7.77191068e+06, 
                 1.70000000e+01, 8.64847224e+00, 3.63679865e-08],
                [1.06994644e+07, 5.40000000e+01, np.nan, 8.79645043e+06, 
                 1.80000000e+01, 9.24475638e+00, 1.13640819e-08]
            ]), 
            equal_nan=True)
                       )
        self.assertTrue(np.allclose(
            dev_table_Ad.astype(float).values,
            np.array([
                [2.26975638e+06, 4.40000000e+01, 0.00000000e+00, np.nan, 
                 np.nan, np.nan, np.nan],
                [2.47405267e+06, 4.50000000e+01, np.nan, 2.04296293e+05, 
                 1.00000000e+00, 3.96035318e+00, 5.28199266e-02],
                [8.89772511e+06, 5.20000000e+01, np.nan, 6.62796873e+06, 
                 8.00000000e+00, 1.60606787e+01, 8.80953088e-11],
                [9.09618109e+06, 5.30000000e+01, np.nan, 6.82642471e+06, 
                 9.00000000e+00, 1.47036185e+01, 1.26508914e-10],
                [1.06994644e+07, 5.40000000e+01, np.nan, 8.42970805e+06, 
                 1.00000000e+01, 1.63412760e+01, 9.25903798e-12]
            ]), 
            equal_nan=True)
                       )
        
        
    def test_Belgian_ln_rates(self):
        model = apc.Model()
        model.data_from_df(**apc.Belgian_lung_cancer())
        model.fit(family='log_normal_rates', predictor='APC')
        model.fit_table()
        
        self.assertTrue(np.allclose(
            model.deviance_table.astype(float).values,
            np.array([
                [ -4.48541926e+01,   1.80000000e+01, np.nan,
                  np.nan,   np.nan,   7.14580741e+00],
                [ -2.89978040e+01,   3.00000000e+01,   1.58563886e+01,
                  1.20000000e+01,   7.73951199e-01,  -9.97804023e-01],
                [ -4.34535281e+01,   2.00000000e+01,   1.40066447e+00,
                  2.00000000e+00,   7.50887416e-01,   4.54647188e+00],
                [  1.26313918e+01,   2.70000000e+01,   5.74855844e+01,
                   9.00000000e+00,   1.19837754e-03,   4.66313918e+01],
                [ -2.80421983e+01,   3.20000000e+01,   1.68119943e+01,
                   1.40000000e+01,   8.33123670e-01,  -4.04219834e+00],
                [  4.76056314e+01,   3.90000000e+01,   9.24598239e+01,
                   2.10000000e+01,   1.37099871e-04,   5.76056314e+01],
                [  1.27105303e+01,   2.90000000e+01,   5.75647229e+01,
                   1.10000000e+01,   2.69265547e-03,   4.27105303e+01],
                [ -1.49167453e+01,   3.30000000e+01,   2.99374473e+01,
                   1.50000000e+01,   3.71545814e-01,   7.08325470e+00],
                [  1.65610725e+02,   4.00000000e+01,   2.10464918e+02,
                   2.20000000e+01,   1.72395120e-14,   1.73610725e+02],
                [  8.82613661e+01,   3.00000000e+01,   1.33115559e+02,
                   1.20000000e+01,   2.39611729e-09,   1.16261366e+02],
                [  4.77747017e+01,   4.10000000e+01,   9.26288943e+01,
                   2.30000000e+01,   2.20314500e-04,   5.37747017e+01],
                [  5.04233530e+01,   4.20000000e+01,   9.52775456e+01,
                   2.40000000e+01,   1.75490643e-04,   5.44233530e+01],
                [  1.65622315e+02,   4.20000000e+01,   2.10476508e+02,
                   2.40000000e+01,   3.10356942e-14,   1.69622315e+02],
                [  9.80993338e+01,   4.20000000e+01,   1.42953526e+02,
                   2.40000000e+01,   2.27337320e-08,   1.02099334e+02],
                [  1.65809402e+02,   4.30000000e+01,   2.10663595e+02,
                   2.50000000e+01,   3.95566533e-14,   1.67809402e+02]
            ]), 
            equal_nan=True)
                       )
    
    def test_Belgian_bin_dose_response(self):
        data = apc.Belgian_lung_cancer()
        dose = (data['response']/data['rate'] * 10**5).astype(int)
        model = apc.Model()
        model.data_from_df(data['response'], dose=dose, data_format='AP')
        model.fit_table('binomial_dose_response', 'APC')
        
        self.assertTrue(np.allclose(
            model.deviance_table.astype(float).values,
            np.array([
                [2.02272942e+01, 1.80000000e+01, 3.20169615e-01, np.nan, np.nan, np.nan],
                [2.55616207e+01, 3.00000000e+01, 6.97305582e-01, 5.33432652e+00,
                 1.20000000e+01, 9.45870225e-01],
                [2.14563493e+01, 2.00000000e+01, 3.70723402e-01, 1.22905512e+00,
                 2.00000000e+00, 5.40896377e-01],
                [9.91929917e+01, 2.70000000e+01, 3.49109630e-10, 7.89656975e+01,
                 9.00000000e+00, 2.59348099e-13],
                [2.65878986e+01, 3.20000000e+01, 7.37036572e-01, 6.36060439e+00,
                 1.40000000e+01, 9.56568004e-01],
                [2.53472759e+02, 3.90000000e+01, 0.00000000e+00, 2.33245465e+02,
                 2.10000000e+01, 0.00000000e+00],
                [1.00677524e+02, 2.90000000e+01, 7.61992691e-10, 8.04502302e+01,
                 1.10000000e+01, 1.20758958e-12],
                [8.55939082e+01, 3.30000000e+01, 1.48750103e-06, 6.53666140e+01,
                 1.50000000e+01, 2.94677404e-08],
                [6.39083556e+03, 4.00000000e+01, 0.00000000e+00, 6.37060827e+03,
                 2.20000000e+01, 0.00000000e+00],
                [1.21719783e+03, 3.00000000e+01, 0.00000000e+00, 1.19697053e+03,
                 1.20000000e+01, 0.00000000e+00],
                [2.54429395e+02, 4.10000000e+01, 0.00000000e+00, 2.34202101e+02,
                 2.30000000e+01, 0.00000000e+00],
                [3.08059993e+02, 4.20000000e+01, 0.00000000e+00, 2.87832698e+02,
                 2.40000000e+01, 0.00000000e+00],
                [6.39139748e+03, 4.20000000e+01, 0.00000000e+00, 6.37117019e+03,
                 2.40000000e+01, 0.00000000e+00],
                [1.61214822e+03, 4.20000000e+01, 0.00000000e+00, 1.59192092e+03,
                 2.40000000e+01, 0.00000000e+00],
                [6.50047766e+03, 4.30000000e+01, 0.00000000e+00, 6.48025037e+03,
                 2.50000000e+01, 0.00000000e+00]
            ]), 
            equal_nan=True)
                       )

    def test_Belgian_poisson_dose_response(self):
        model = apc.Model()
        model.data_from_df(**apc.Belgian_lung_cancer())
        model.fit_table('poisson_dose_response', 'APC')
        
        self.assertTrue(np.allclose(
            model.deviance_table.astype(float).sum().values,
            np.array([
                2.33052840e+04, 5.08000000e+02, 2.12588574e+00, 2.30019096e+04,
                2.38000000e+02, 2.44351741e+00
            ]), 
            equal_nan=True)
                       )
        
if __name__ == '__main__':
    unittest.main()