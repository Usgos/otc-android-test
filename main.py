from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import asyncio
import threading

class TestApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=20, spacing=12)
        self.label = Label(
            text="OTC Live AI\\nAndroid compatibility test\\n\\n"
                 "Kivy: OK\\nPython runtime: OK\\n"
                 "WebSocket test: waiting...",
            halign="center", valign="middle")
        box.add_widget(self.label)
        threading.Thread(target=self.websocket_test, daemon=True).start()
        return box

    def websocket_test(self):
        async def run():
            try:
                import websockets
                msg = "websockets: OK\\npyquotex: "
                try:
                    import pyquotex
                    msg += "OK"
                except Exception as e:
                    msg += "IMPORT ERROR: " + type(e).__name__
                self._set_status(msg)
            except Exception as e:
                self._set_status("websockets: ERROR " + repr(e))
        asyncio.run(run())

    def _set_status(self, msg):
        Clock.schedule_once(lambda dt: setattr(
            self.label, "text",
            "OTC Live AI\\nAndroid compatibility test\\n\\n"
            "Kivy: OK\\nPython runtime: OK\\n" + msg))

if __name__ == "__main__":
    TestApp().run()
