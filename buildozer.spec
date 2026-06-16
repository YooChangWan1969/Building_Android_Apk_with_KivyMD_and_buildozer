[app]
title = app_name
package.name = package_name
package.domain = com.domain_name
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.include_patterns = font/*,images/*.png
source.exclude_exts = spec,txt,json,bat,keystore
source.exclude_dirs = tests, bin, venv, __pycache__
version = 1.1.1

# requirements
requirements = python3,kivy==2.3.1,kivymd==1.2.0,sdl2_ttf,pillow,android,beautifulsoup4,soupsieve,requests==2.31.0,typing_extensions,plyer==2.1.0,pyjnius,olefile==0.47,pytz

presplash.filename = %(source.dir)s/images/presplash.png
icon.filename = %(source.dir)s/images/favicon.png
orientation = portrait,landscape
osx.python_version = 3
osx.kivy_version = 2.3.1
fullscreen = 0

# 권한 설정
android.permissions = android.permission.INTERNET, android.permission.ACCESS_NETWORK_STATE, android.permission.VIBRATE, ndroid.permission.READ_EXTERNAL_STORAGE, android.permission.WRITE_EXTERNAL_STORAGE, android.permission.FOREGROUND_SERVICE

# Android 버전 설정 (최신으로 유지)
android.api = 35
android.minapi = 24
android.sdk = 35
android.ndk = 28
android.ndk_api = 24
android.private_storage = True

# 16KB 페이지 크기 지원을 위한 핵심 설정
android.archs = arm64-v8a
android.add_linking_options = -Wl,--warn-shared-textrel

# # 16KB 페이지 크기 지원을 위한 최신 python-for-android 사용
p4a.branch = develop

# Gradle 의존성 추가 (16KB 지원 라이브러리)
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1, androidx.activity:activity:1.6.1
android.enable_androidx = True
android.add_packaging_options = "jniLibs/useLegacyPackaging=true"

# CMake 옵션 개선
android.cmake_options = -DCMAKE_POLICY_VERSION_MINIMUM=3.18, -DCMAKE_C_FLAGS="-O2 -fPIC", -DCMAKE_CXX_FLAGS="-O2 -fPIC"

# 16KB 페이지 크기를 위한 추가 플래그
android.add_gradle_options = android.bundle.enableUncompressedNativeLibs=false

# 대형 화면 지원
android.allow_backup = True
android.allow_cleartext_traffic = True

# gradle 버전 세팅
# android.gradle_version = 8.7
# android.gradle_plugin_version = 8.5.2

[buildozer]
log_level = 0
warn_on_root = 1

[android.manifest]
# 대형 화면 지원
application.resizeableActivity = true
activity.screenOrientation = unspecified

# 16KB 페이지 크기 지원
application.largeHeap = true
application.hardwareAccelerated = true

# 추가 매니페스트 속성
uses-feature.android.hardware.screen.portrait = false
uses-feature.android.hardware.screen.landscape = false
