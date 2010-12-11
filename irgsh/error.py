class IrgshException(Exception):
    pass

class BuildFailedError(IrgshException):
    def __init__(self, source):
        self.source = source
    def __str__(self):
        return 'Build failed: %s' % self.source

class InvalidSourceLocationError(IrgshException):
    def __init__(self, location, msg=None):
        self.location = location
        self.msg = msg

        desc = 'Invalid source location: %s' % self.location
        if msg is not None:
            desc = '%s (%s)' % (desc, msg)
        super(InvalidSourceLocationError, self).__init__(desc)

class InvalidSourceNameError(IrgshException):
    pass

class UploadFailedError(IrgshException):
    pass

class InvalidControlFile(IrgshException):
    pass
