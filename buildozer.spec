[app]
title = BM Prod
package.name = bmprod
package.domain = org.bmprod
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Fixer des versions stables pour éviter les erreurs de licence
android.api = 31
android.minapi = 21
android.sdk = 31
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
