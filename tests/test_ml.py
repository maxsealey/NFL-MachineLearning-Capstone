import unittest
from unittest.mock import patch
import pandas as pd

from app.ml.model import create_model


class TestMLModel(unittest.TestCase):

    @patch('app.ml.model.get_df_with_cleaned_data')
    @patch('app.ml.model.retrieve_prediction_data_script')
    def test_model_loading(self, mock_retrieve_script, mock_get_df):
        # mock retrieval and processing functions
        mock_retrieve_script.return_value = 'mock script'
        mock_get_df.return_value = pd.DataFrame({
            'qb_p': [0.1, 0.2],
            'off_p': [0.3, 0.4],
            'def_p': [0.5, 0.6],
            'playoffs': [0, 1]
        })

        model = create_model()
        self.assertIsNotNone(model)


if __name__ == '__main__':
    unittest.main()