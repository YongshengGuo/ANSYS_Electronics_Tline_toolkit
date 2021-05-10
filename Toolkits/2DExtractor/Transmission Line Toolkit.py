
# updated V2.2 2021-05-10
# Fixed differential spacing error when changing width
# updated by yongsheng.guo@ansys.com
# Original author is unknown

import sys
import logging
import clr
import os
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import Application

# if 'oDesktop' in globals():
# 	tempPath = oDesktop.GetTempDirectory()
# 	sysPath = oDesktop.GetSysLibDirectory()
# else:
# 	oDesktop = None
# 	tempPath = os.environ['temp']
# 	appPath = os.path.realpath(__file__)
# 	appDir = os.path.split(appPath)[0]
# 	sysPath = os.path.abspath(os.path.join(appDir,'..\\..\\')) 
# sys.path.append(sysPath + "/Toolkits/Lib/TLine")

tempPath = os.environ['temp']
appPath = os.path.realpath(__file__)
appDir = os.path.split(appPath)[0]
sysPath = os.path.abspath(os.path.join(appDir,'..\\..\\')) 
sys.path.append(os.path.join(sysPath,r"Toolkits/Lib/TLine"))

import MainForm
import anstDebug



#oLog = anstDebug.anstDebug('TLine', logging.DEBUG, oDesktop)
oLog = anstDebug.anstDebug('TLine', logging.INFO, oDesktop)

logger = oLog.getLogger()
#logger.debug('TempDir: ' + tempPath)
#logger.debug('SysPath: ' + sysPath)

try:
	Application.EnableVisualStyles()
	form = MainForm.MainForm(oDesktop, sysPath)
	#form.SetSysPath(sysPath)
	form.SetDefaults()
	Application.Run(form)
except(e):
	pass


oLog.Finish()