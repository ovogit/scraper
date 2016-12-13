class nFile:
    def __init__( self, *args ):
        self.file_location = args[0]
        self.mode = args[1]
        self.number_of_lines_in_file = False
        self.f = False
        self.lines = []
        self.lineCount = 0

    def open( self, *args ):
        try:
            if args:
                self.f = open( self.file_location, str( args[0] ) )
            else:
                self.f = open( self.file_location, str( self.mode ) )
        except:
            print 'failed to open file'

    def readLines ( self ):
        try:
            self.open()
            self.lines = self.f.readlines()
            self.close()
            return self.lines

        except:
            print 'could not open'

    def getLineCount( self ):
        try:
            self.open()
        except:
            print 'could not open'
        try:
            lines = self.f.readlines()
            if lines == []:
                self.lineCount = 0
                return True
            else:
                for line in lines:
                    self.lineCount = self.lineCount + 1
                return True
        except:
            return False
        self.close
        return self.lineCount

    def close( self ):
        try:
            self.f.close()
        except:
            print 'failed to close'

    def write( self, *args ):
        try:
            self.open()
        except:
            print 'could not open'
        text = args[0]
        self.f.write( args[0].encode('utf-8').strip()  ) 
        return self.close
        
    def writeLine( self, *args ):
        try:
            self.open()
        except:
            print 'could not open'
        return self.close

    def contains ( self, *args ):
    #TODO
    #===========
    # [*] add regex support for searching the line
    # it currently only matches the entire line, can't match segments
    #===========
        lines = self.readLines()
        search = str(args[0])
        for line in lines:
            line = line.rstrip()
            if search == line:
                return True

    def truncate( self ):
        self.open('w')
        self.close()
        return True



