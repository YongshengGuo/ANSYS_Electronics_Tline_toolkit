import logging
import logging.handlers
import tempfile

try:
	from Ansys.Ansoft.PluginCoreDotNet.Util import NGDesktop
except Exception: 
	pass


class DesktopHandler(logging.Handler):
	def __init__(self):
		logging.Handler.__init__(self)

	def emit(self, record):
		
		if record.levelname  == 'INFO':
			NGDesktop.AddInfoMessage(record.getMessage())
		elif record.levelname  == 'WARNING':
			NGDesktop.AddWarningMessage(record.getMessage())
		elif record.levelname  == 'ERROR':
			NGDesktop.AddErrorMessage(record.getMessage())
		elif record.levelname  == 'CRITICAL':
			NGDesktop.AddFatalMessage(record.getMessage())
		elif record.levelname  == 'DEBUG':
			NGDesktop.LogDebug(record.getMessage())
			NGDesktop.AddInfoMessage(record.getMessage())


class anstDebug(object):

	def __init__(self, szLoggerName, logLevel=logging.DEBUG, oDTop = None):
		self.oDesktop = oDTop
		self.m_logger = None
		self.m_fh = None
		self.m_logFile = ''
		logger = logging.getLogger(szLoggerName)
		logger.setLevel(logLevel)

		if self.oDesktop != None:
			tempPath = self.oDesktop.GetTempDirectory()
		else:
			tempPath = tempfile.gettempdir()

		# create the logging file handler
		self.m_logFile = tempPath+szLoggerName+".log"
		self.m_fh = logging.FileHandler(self.m_logFile,'w')

		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.m_fh.setFormatter(formatter)

		# add handler to logger object
		logger.addHandler(self.m_fh)

		if self.oDesktop != None:
			dHandler = DesktopHandler()
			logger.addHandler(dHandler)

		self.m_logger = logger
#		self.m_logger.debug('Start Logging')

	def __del__(self):
#		self.m_logger.debug('Finished')
		if self.m_fh != None:
			self.m_fh.flush()
			self.m_fh.close()
		logging.shutdown()


	def getLogger(self):
		return self.m_logger

	def GetLogFile(self):
		return self.m_logFile

	def Finish(self):
#		self.m_logger.debug('Finished Logging')
		if self.m_fh != None:
			self.m_fh.flush()
			self.m_fh.close()
		logging.shutdown()







