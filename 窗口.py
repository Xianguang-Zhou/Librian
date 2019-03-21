import logging

import wxcef

from 環境 import 配置, 工程路徑
import 山彥


def app():
    if 配置['編寫模式']:
        url = 'file:///html/adv.html'
    elif 配置['標題畫面']:
        url = f'file:///{工程路徑}/{配置["標題畫面"]}'
    else:
        url = 'file:///html/默認標題畫面/標題.html'

    if 配置['圖標']:
        圖標 = f'{工程路徑}/{配置["圖標"]}'
    else:
        圖標 = './資源/librian.ico'

    app, 瀏覽器 = wxcef.group(title=配置['標題'], url=url, icon=圖標, size=配置['主解析度'])
    山彥.綁定(app, 標題url=url)

    return app


class 統合窗口():
    def 切換全屏(self):
        self.全屏 = not self.全屏
        if self.全屏:
            self.showFullScreen()
        else:
            self.showNormal()

    def keyPressEvent(self, event):
        keyEvent = QKeyEvent(event)
        if keyEvent.key() in (Qt.Key_Enter, 16777220):
            if QApplication.keyboardModifiers() == Qt.AltModifier:
                self.切換全屏()
