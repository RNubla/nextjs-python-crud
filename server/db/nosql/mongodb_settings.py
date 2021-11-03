from os.path import join, dirname
from dotenv import load_dotenv
import os

dotEnv_path = join(dirname(__file__), '.env')
envornment = load_dotenv(dotEnv_path)
mongodb_env = os.environ['MONGO_DB']
