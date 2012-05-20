#!/usr/bin/env python

#############################################################################
##
## OnAirScreen Analog Clock implementation
## Copyright (C) 2012 Sascha Ludwig
## All rights reserved.
##
## contains code from Riverbank Computing Limited and Nokia Corporation
## for details: see copyright notice below
##

#############################################################################
##
## Copyright (C) 2010 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt4 import QtCore, QtGui


class AnalogClock(QtGui.QWidget):
    hourHand = QtGui.QPolygon([
        QtCore.QPoint(7, 8),
        QtCore.QPoint(-7, 8),
        QtCore.QPoint(0, -50)
    ])

    minuteHand = QtGui.QPolygon([
        QtCore.QPoint(7, 8),
        QtCore.QPoint(-7, 8),
        QtCore.QPoint(0, -75)
    ])

    hourColor = QtGui.QColor(191, 191, 191, 255)
    minuteColor = QtGui.QColor(191, 191, 191, 255)
    circleColor = QtGui.QColor(255, 255, 255, 255)

    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def paintEvent(self, event):
        side = min(self.width(), self.height())
        time = QtCore.QTime.currentTime()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(AnalogClock.hourColor)

        # set hour hand length and minute hand length
        hhl = -65 #-50
        mhl = -85 #-75
        # draw hour hand
        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawRoundedRect(-4,4,8,hhl,4,4)
        painter.restore()

        painter.setPen(AnalogClock.hourColor)

        for i in range(12):
            painter.drawRoundedRect(88,-1,8,2,1,1)
            painter.rotate(30.0)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(AnalogClock.minuteColor)

        #draw minute hand
        sizefactor = 1.3
        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawRoundedRect(-4/sizefactor,4/sizefactor,8/sizefactor,mhl,4/sizefactor,4/sizefactor)
        painter.restore()

        #draw center circle
        painter.setBrush(AnalogClock.circleColor)
        painter.save()
        painter.drawEllipse(-5,-5,10,10)
        painter.restore()

        painter.setPen(AnalogClock.minuteColor)

        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = AnalogClock()
    clock.setStyleSheet("background-color:black;")
    clock.resize(500,500)
    clock.show()
    sys.exit(app.exec_())
