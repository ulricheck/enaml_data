# -*- coding: utf-8 -*-
'''
Created on Aug 23, 2015

@author: jrm
'''

import enaml_data
enaml_data.install()

import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        from tree_view import Main

    app = QtApplication()
    view = Main()

    view.show()

    app.start()
