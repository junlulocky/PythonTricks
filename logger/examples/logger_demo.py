import sys
sys.path.append('..')
from logger import set_logger


name = 'test'
save_path = './tmp_res/res_alpha-{}'.format(name)  ## it will automatically create the folder of res_alpha-test
logger = set_logger(save_path=save_path)

something = 'something'
logger.info('best hyperparmeter: {}'.format(something))  ## save information to log