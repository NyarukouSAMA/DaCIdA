"""
Aste is analytical system test engine (аналитический движок системных тестов).
The main goal of aste is to withdraw some data from some OS and to compare
it with some signatures.
In advance we cant't know, what signatures it would be, or what part of OS data
we would take. That's why the main idea of this engine is to connect some functional
module to our program (which could do different things: from analysing of name
of some *.jpg to analysing of configurations of OS in Linux or system registry
in Windows - it depends on what functional our module implements.)

"""

from aste.processor.analytical_processor import ASTEInterface
from aste.analyser_manager import ASTEManager