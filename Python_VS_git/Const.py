# coding=utf-8

#
#    常量
#

class _const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError, "Can't rebind const(%s)" % key
        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            raise self.ConstError, "Can't unbind const(%s)" % item
        raise NameError,item

def Separate():
    print "*******************************************************************************************************************"

# import sys
# sys.modules[__name__] = _const()
