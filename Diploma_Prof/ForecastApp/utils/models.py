from config import MODELS_DIR, DEBUG, IMAGES_DIR, OPT_DIR
from .dates import create_df
from app_logger import logger_output
import pickle
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load_model_from_file(model_name):
    try:
        models_dir = Path(MODELS_DIR)
        if model_name == 'Вереск':
            loaded_model = pickle.load(open(models_dir / 'veresk_model', 'rb'))
        elif model_name == 'Ромашка':
            loaded_model = pickle.load(open(models_dir / 'romashka_model', 'rb'))
        else:
            loaded_model = None
            logger_output('No model selected', DEBUG, 'warning')
        return loaded_model
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')


def xgboost_image(start_date, end_date, model_name):
    file_name = ''
    try:
        loaded_model = load_model_from_file(model_name)
        df = create_df(start_date, end_date)
        predictions = pd.DataFrame(loaded_model.predict(df)).set_index(df.index)
        fig = plt.figure(figsize=(18, 12))
        ax = fig.add_subplot()
        ax.plot(predictions, color='green', label='Предсказанный ряд')
        plt.legend(loc='upper left')
        plt.title(f'Предсказания для фермы "Ромашка" (алгоритм XGBRegressor) для периода: {start_date} - {end_date}')
        plt.xticks(predictions.index, rotation=45)
        plt.grid(True)
        file_name = Path('static') / Path(IMAGES_DIR) / 'main_plot.png'
        plt.savefig(file_name)
        plt.show()
        plt.close()
        predictions.to_excel(Path('static') / Path(OPT_DIR) / 'romashka.xlsx',
                             sheet_name=f'Ромашка {start_date}-{end_date}')
        return 'img/main_plot.png', 'opt/romashka.xlsx'
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')


def arima_image(start_date, end_date, model_name):
    try:
        loaded_model = load_model_from_file(model_name)
        df = create_df('2022-01-31', end_date)
        predictions = pd.DataFrame(loaded_model.predict(len(df))).set_index(df.index)
        predictions_part = predictions.loc[(predictions.index >= start_date) & (predictions.index <= end_date)].copy()
        fig = plt.figure(figsize=(18, 12))
        ax = fig.add_subplot()
        ax.plot(predictions_part, color='green', label='Предсказанный ряд')
        plt.legend(loc='upper left')
        plt.title(f'Предсказания для фермы "Вереск" (алгоритм SARIMA) для периода: {start_date} - {end_date}')
        plt.xticks(predictions_part.index, rotation=45)
        plt.grid(True)
        file_name =  Path('static') / Path(IMAGES_DIR) / 'main_plot.png'
        plt.savefig(file_name)
        plt.show()
        plt.close()
        predictions.to_excel(Path('static') / Path(OPT_DIR) / 'veresk.xlsx',
                             sheet_name=f'Вереск {start_date}-{end_date}')
        return 'img/main_plot.png', 'opt/veresk.xlsx'
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')
