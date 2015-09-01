""" wasatchdevice - command line application to read from a wasatch
photonics device and return data on stdout. Designed to be called from
the AnalyzeIQ product. Produces xml output on stdout.
"""

import sys
import argparse

from PyQt4 import QtGui
from PyQt4 import QtCore # required for py2exe

from wasatchanalyzeiq import wasatchxml

class WasatchDeviceApplication(object):
    """ Wrapper around application control code based on:
    https://groups.google.com/d/msg/comp.lang.python/j_tFS3uUFBY/\
        ciA7xQMe6TMJ
    Specifically, this means breaking out all of the functions from main
    into this application object so they can have a narrow interface,
    suitable for unit testing.
    """
    def __init__(self):
        super(WasatchDeviceApplication, self).__init__()
        self.parser = self.create_parser()

    def parse_args(self, argv):
        """ Handle any bad arguments, the set defaults
        """
        self.args = self.parser.parse_args([])
        return self.args

        #sys.stderr.write("Start of parse args with %s\n" % argv)
        try:
            self.args = self.parser.parse_args(argv)
            #sys.stderr.write("done parsed \n")
        except:
            sys.stderr.write("Setting default args\n")
            #sys.stderr.write("problem, re-arseing \n")
            self.args = self.parser.parse_args([])
            
        #sys.stderr.write("finished \n")

        return self.args

    def create_parser(self):
        desc = "wasatch device acquisition, xml stdout for AnalyzeIQ"
        parser = argparse.ArgumentParser(description=desc)
    
        parser.add_argument("-a", "--auto-capture", action="store_true",
            help="Automatically acquire after startup")

        parser.add_argument("-t", "--testing", action="store_true",
            help="inhibit qapplication creation and exit for unittest")
    
        return parser

    def run(self):
        """ Create the Qt application if required, execute the specific
        processing collation steps for the designated graph mode. Then
        exit with the app.exec if the unittest has not created the qt 
        application.
        """

        #print "start qapp: %s" % self.args.testing
        if not self.args.testing:
            app = QtGui.QApplication(sys.argv)

        self.form = wasatchxml.WasatchXML()

        if self.args.auto_capture:
            self.form.acquire()

        if not self.args.testing:
            sys.exit(app.exec_())

def main(argv=None): 
    """ main calls the wrapper code around the application objects with
    as little framework as possible. See:
    https://groups.google.com/d/msg/comp.lang.python/j_tFS3uUFBY/\
        ciA7xQMe6TMJ
    """
   
    if argv is None: 
        from sys import argv as sys_argv 
        argv = sys_argv 
    else:
        # Strip out the program name to match the unittest setup
        argv = argv[1:]
    
    #print "Argv processed: %s" % argv

    exit_code = 0
    try:
        wsdapp = WasatchDeviceApplication()
        wsdapp.parse_args(argv)
        wsdapp.run()
    except SystemExit, exc:
        exit_code = exc.code

    try:
        sys.stderr.write("last xml; %s\n" % wsdapp.form.last_xml_output())
        print wsdapp.form.last_xml_output()
    except:
        print "Problem executing xml output"

    sys.stderr.write("Exit with code 0")
    sys.exit(0)
    return exit_code 

if __name__ == "__main__":
    sys.exit(main(sys.argv))

