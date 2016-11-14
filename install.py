import os

version_mode = ?
version_name = ?
version_increase_name = ?
target = os.getcwd () + os.sep + "APK_NAME-{}-{}.{}.apk".format (version_mode,version_name,version_increase_name)
print target
target_package = "/data/local/tmp/ANDROID_PACKAGE_NAME"
os.system("adb push " + target + " " + target_package)
os.system("adb shell pm install -r " + target_package)
os.system("adb shell am start -n \"ANDROID_PACKAGE_NAME/MAIN_LAUNCHER_ACTIVITY\" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER")
os.system("adb shell am start -n \"ANDROID_PACKAGE_NAME/ACTIVITY_YOU_WANT_TO_OPEN\"")
