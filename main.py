import user_interface as ui
import logger as lg
import model



lg.logging.info('Start')
model.init_data_base('base_phone.csv')
ui.ls_menu()
