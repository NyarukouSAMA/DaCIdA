"""
This package gives common program's interface for
system information retrieval realisation cases.
'sysiri' package gives interface (base class), calling Withdrawal.
It can be inherited by classes, main func of which is to take some information from OS
"""

from sysanalisers.sys_handler_analyser import SysHandlerAnalyser
from sysanalisers.reg_keys_analyser import RegKeyAnalyser
from sysanalisers.sys_services_analyser import SysServicesAnalyser