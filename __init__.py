from manager import FisDataManager
from plugins import fisjson, fispy

FisDataManager.register(fispy.FisPy())
FisDataManager.register(fisjson.FisJson())
