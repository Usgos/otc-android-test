[app]
title = OTC Live AI Compatibility Test
package.name = otcliveaitest
package.domain = org.otcliveai
source.dir = .
source.include_exts = py,txt,kv
source.exclude_dirs = __pycache__,.github
version = 0.1.0
requirements = python3,kivy,pyquotex,websockets,httpx,python-dotenv,beautifulsoup4,fake-useragent,certifi,rich,pyfiglet
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 35
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True
p4a.bootstrap = sdl2
