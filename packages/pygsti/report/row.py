from __future__ import division, print_function, absolute_import, unicode_literals

#*****************************************************************
#    pyGSTi 0.9:  Copyright 2015 Sandia Corporation
#    This Software is released under the GPL license detailed
#    in the file "license.txt" in the top-level pyGSTi directory
#*****************************************************************

from .cell        import Cell
from .formatters  import formatDict as _formatDict
from .reportables import ReportableQty as _ReportableQty

class Row(object):

    def __init__(self, rowData=None, formatters=None, labels=None):
        if rowData is None:
            rowData = []
        else:
            rowData = [_ReportableQty.from_val(item) for item in rowData]
        if formatters is None:
            formatters = []
        if labels is None:
            labels = rowData

        lendiff = max(abs(len(formatters) - len(rowData)), 0)
        formatters = list(formatters) + [None] * lendiff
        
        lendiff = max(abs(len(labels) - len(rowData)), 0)
        labels = list(labels) + [None] * lendiff 

        self.cells = [Cell(item, formatter, label) 
                for item, formatter, label in 
                zip(rowData, formatters, labels)]

    def add(self, data, formatter=None, label=None):
        self.cells.append(Cell(data, formatter, label))

    def render(self, fmt, specs):
        formattedItems = []
        for cell in self.cells:
            formattedItem = cell.render(fmt, specs)
            if isinstance(formattedItem, list): #formatters can create multiple table cells by returning *lists* 
                formattedItems.extend(formattedItem)
            else:
                formattedItems.append(formattedItem)
        return formattedItems
