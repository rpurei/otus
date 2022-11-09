from config import DEBUG
from utils.models import xgboost_image, arima_image
from app_logger import logger_output
from flask import render_template, request, Blueprint, abort
from datetime import datetime


index_handler = Blueprint('index', __name__)


@index_handler.route('/')
def get_index():
    return render_template('index.html')


@index_handler.route('/index/show')
def show_graph():
    farm_select = request.args.get('farm_select')
    if farm_select == '' or not farm_select:
        abort(500, 'Выберите ферму')
    current_year = datetime.now().year
    start_date = request.args.get('start_date', f'{current_year}-01-01')
    end_date = request.args.get('end_date', f'{current_year}-12-31')
    try:
        if farm_select == '1':
            plot_image_name, xlsx_file_name = arima_image(start_date, end_date, 'Вереск')
        elif farm_select == '2':
            plot_image_name, xlsx_file_name = xgboost_image(start_date, end_date, 'Ромашка')
        else:
            plot_image_name = None
            xlsx_file_name = None
        return render_template('index.html', plot_image=plot_image_name,
                                             xlsx_file=xlsx_file_name,
                                             start_date=start_date,
                                             end_date=end_date,
                                             farm_select=farm_select)
    except Exception as err:
        logger_output(str(err), DEBUG, 'error')
        abort(500, str(err))
