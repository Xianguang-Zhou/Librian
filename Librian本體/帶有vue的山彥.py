# -*- coding: utf-8 -*-
from PySide2 import QtCore


class 帶有vue的山彥(QtCore.QObject):
    class 山彥vue:
        def __init__(self, 彥):
            self._彥 = 彥
            self._內容 = {}

        def __getattr__(self, x):
            return self._內容[x]

        def __setattr__(self, a, b):
            if a[0] == '_':
                self.__dict__[a] = b
            else:
                self._內容[a] = b
                self._彥.更新vue()

    def __init__(self, 窗口):
        super().__init__(parent = 窗口)
        self.窗口 = 窗口
        self.vue = self.山彥vue(self)
        self.vue鏈接 = None

    def vue更新(self, 內容):
        self.vue._內容 = 內容

    def 更新vue(self):
        if self.vue鏈接:
            self.vue鏈接.Call(self.vue._內容)

    @QtCore.Slot(str, result=str)
    def greet(self, name):
        return f'Hello, {name}!'

    @QtCore.Slot()
    def vue連接初始化(self):
    # def vue連接初始化(self, f):
        # self.vue鏈接 = f
        self.更新vue()

