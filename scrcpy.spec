%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        3.2

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}

BuildRequires:  meson gcc cmake
BuildRequires:  java-devel >= 11
BuildRequires:  libusb1-devel ffmpeg-devel

BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(libusb-1.0)

Requires:       adb

# https://github.com/Genymobile/scrcpy/blob/master/FAQ.md#issue-with-wayland
Recommends:       libdecor

%description
This application provides display and control of Android devices
connected on USB (or over TCP/IP).

%prep
%forgesetup

%build
%meson -Db_lto=true -Dprebuilt_server='%{S:1}'
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png
%{_datadir}/bash-completion/completions/%{pkgname}
%{_datadir}/zsh/site-functions/_%{pkgname}
%{_datadir}/applications/%{pkgname}*.desktop


%changelog
* Sat Mar 29 2025 Udo Seidel <udoseidel@gmx.de> 3.2-1
- Add many audio sources (#5870 [github.com], #5412 [github.com], #5670 [github.com])
- Improve/fix camera listing (#5669 [github.com])
- Add --display-ime-policy (#5703 [github.com])
- Allow controls with --no-window (#5803 [github.com], #5804 [github.com])
- Add workaround for Pico 4 Ultra (#5659 [github.com])
- Fix rotation after a recent Android 15 upgrade (#5908 [github.com])
- Fix audio capture on Android 16 (#5698 [github.com])
- Make static Linux binaries compatible with older versions (#5689 [github.com])
- Make static macOS binaries compatible with older versions (#5649 [github.com], #5697 [github.com])
- Upgrade FFmpeg to 7.1.1
- Upgrade libusb to 1.0.28
- Upgrade SDL to 2.32.2
- Various technical fixes

* Tue Dec 10 2024 Udo Seidel <udoseidel@gmx.de> 3.1-1
- Add --no-vd-destroy-content (#5615 [github.com])
- Improve gamepad support in games (#5623 [github.com], #5362 [github.com])
- Inject events to main display (#5614 [github.com], #5545 [github.com], #5605 [github.com], #5616 [github.com])
- Fix "turn screen off" on some devices (#4544 [github.com], #5274 [github.com])
- Improve cleanup reliability (#5613 [github.com], #5601 [github.com])
- Add dav1d in release builds (#5644 [github.com], #4744 [github.com])
- Upgrade SDL to 2.30.10

* Thu Dec 05 2024 Udo Seidel <udoseidel@gmx.de> 3.0.2-1
- Fix version (#5602 [github.com])

* Thu Dec 05 2024 Udo Seidel <udoseidel@gmx.de> 3.0.1-1
- Set main display power for virtual display (#5522 [github.com])
- Rollback to old --turn-screen-off method for Android 15 (#5530 [github.com])
- Do not reset TCP/IP connections (#5562 [github.com])
- Fix socket interruption on macOS (#5536 [github.com])
- Fix NullPointerException on certain devices (#5537 [github.com])
- Fix camera capture failure without retry (#5539 [github.com])
- Accept control events without display (#5542 [github.com])
- Build macOS x86_64 release (#5526 [github.com])
- Fix .tar.gz compression for release tarballs (#5581 [github.com])
- Call static binary without wrapper script (#5560 [github.com])

* Sun Nov 24 2024 Udo Seidel <udoseidel@gmx.de> 3.0-1
- Add virtual display feature (#5370, #5506, #1887, #4528, #5137)
- Launch Android app on start (#5370)
- Add OpenGL filters (#5455)
- Add --capture-orientation to replace --lock-video-orientation (which was broken on Android 14) (#4011, #4426, #5455)
- Fix --crop on Android 14 (#4162, #5387, #5455)
- Handle virtual display rotation (#5428, #5455)
- Add --angle to apply a custom rotation (#4135, #4345, #4658, #5455)
- Add --screen-off-timeout (#5447)
- Adapt "turn screen off" for Android 15 (#3927, #5418)
- Add shortcut Ctrl+Shift+click-and-move for horizontal tilt (#5317)
- Add shortcut MOD+Shift+r to reset video capture/encoding (#5432)
- Forward Alt and Super with SDK Keyboard (#5318, #5322)
- Add more details to --list-encoders output (#5416)
- Add option to disable virtual display system decorations (#5494)
- Fix --time-limit overflow on Windows (#5355)
- Fix "does not match caller's uid 2000" error (#4639, #5476)
- Accept filenames containing ':' when recording (#5487, #5499)
- Disable mouse by default if no video playback (#5410)
- Rename --display-buffer to --video-buffer (#5403, #5420)
- Listen to display changed events (#5415, #161, #1918, #4152, #5362)
- Adapt server debugging for Android >= 11 (#5346, #5466)
- Upgrade FFmpeg to 7.1 (#5332)
- Upgrade SDL to 2.30.9
- Upgrade platform-tools (adb) to 35.0.2
- Build releases via GitHub Actions (#5306, #4490)
- Release static builds for Linux and macOS (#5515, #1733, #3235, #4489, #5327)
- Various technical fixes

* Mon Sep 16 2024 Udo Seidel <udoseidel@gmx.de> 2.7-1
- Add gamepad support (#99 [github.com], #2130 [github.com], #5270 [github.com])
- Fix workarounds for ONYX devices (#5182 [github.com])
- Accept float values for --max-fps (265a15e [github.com])
- Upgrade SDL to 2.30.7 in Windows releases
-  Various technical fixes

* Thu Aug 03 2024 Udo Seidel <udoseidel@gmx.de> 2.6.1-1
- Inject finger input whenever possible (#5162 [github.com], #5163

* Thu Aug 01 2024 Udo Seidel <udoseidel@gmx.de> 2.6-1
- Add audio playback capture method (#4380, #5102)
- Add audio duplication feature (#3875, #4380, #5102)
- Add mouse secondary bindings with Shift+click (#5055, #5076)
- Rework mouse events (#5067, #5076)
- Fix "turn screen off" for Honor devices (#4823, #4943, #5109)
- Add clipboard workaround for Honor devices (#4822, #5073)
- Always apply device workarounds (#4922, #5140, #5148, #5154)
- Fix missing initialization (#5057, #5058)
- Do not report error on device disconnected (#5044)
- Upgrade SDL to 2.30.5 in Windows releases
- Various technical fixes

* Sat Jun 29 2024 Udo Seidel <udoseidel@gmx.de> 2.5-1
- Add scrcpy window without video playback (#4727 [github.com], #4793 [github.com], #4868 [github.com])
- Add a shortcut to pause/unpause display (#1632 [github.com], #4748 [github.com])
- Forward mouse hover events (#2743 [github.com], #3070 [github.com], #5039 [github.com])
- Add option to configure mouse bindings (#5022 [github.com])
- Forward all clicks by default for UHID/AOA (#5022 [github.com])
- Simplify shortcut modifiers (#4741 [github.com])
- Fix rotation shortcut for Android 14 (#4740 [github.com], #4841 [github.com])
- Fix YUV conversion for full color range (#4756 [github.com])
- Fix camera sizes listing on some devices (#4852 [github.com])
- Fix thread leak on Windows (#4973 [github.com])
- Upgrade FFmpeg to 7.0.1 in Windows releases
- Upgrade SDL to 2.30.4 in Windows releases
- Upgrade platform-tools (adb) to 35.0.0 in Windows releases
- Various technical fixes

* Sun Mar 03 2024 Udo Seidel <udoseidel@gmx.de> 2.4-1
- Add UHID keyboard and mouse support (#4473)
- Simulate tilt multitouch by pressing Shift (#4529)
- Add rotation support for non-default display (#4698)
- Improve audio player (#4572)
- Adapt to display API changes in Android 15 (#4646, #4656, #4657)
- Adapt audio workarounds to Android 14 (#4492)
- Fix clipboard for IQOO devices on Android 14 (#4492, #4589, #4703)
- Fix integer overflow for audio packet duration (#4536)
- Rework cleanup (#4649)
- Upgrade FFmpeg to 6.1.1 in Windows releases (#4713)
- Upgrade libusb to 1.0.27 in Windows releases (#4713)
- Various technical fixes

* Sat Dec 02 2023 Udo Seidel <udoseidel@gmx.de> 2.3.1-1
- Add workaround for issues on Samsung devices (#4467 [github.com])
- Fix error in a headless environment without display (#4477 [github.com])
- Fix AV1 demuxing (#4487 [github.com])
- Fix build issue on macOS (4135c41 [github.com])

* Sun Nov 26 2023 Udo Seidel <udoseidel@gmx.de> 2.3-2
- cmake, ffmpeg-devel and libusb1-devel added to build requirements 

* Sun Nov 26 2023 Udo Seidel <udoseidel@gmx.de> 2.3-1
- Add flipped display orientation (#1380 [github.com], #3819 [github.com], #4441 [github.com])
- Add recording rotation (#4441 [github.com])
- Add FLAC audio codec (#4410 [github.com])
- Add raw audio (WAV) recording (2004881 [github.com])
- Fix turn screen off for Android 14 (#3927 [github.com], #4456 [github.com])
- Fix camera issues on many devices (#4392 [github.com])
- Fix clipboard synchronization when no video (#4418 [github.com])
- Fix screen refresh on device rotation (7e3b935 [github.com])
- Fix .desktop files on Linux (#4448 [github.com])
- Upgrade SDL to 2.28.5 in Windows releases
- Various technical fixes

* Wed Nov 01 2023 Udo Seidel <udoseidel@gmx.de> 2.2-1
- back to the original versioning schema
- Add option to mirror camera (#241 [github.com], #4213 [github.com])
- Add --pause-on-exit (#4130 [github.com])
- Rename --display (deprecated) to --display-id
- Fix device disconnection detection with --no-video (#4207 [github.com])
- Accept --turn-screen-off without video playback (#4175 [github.com])
- Upgrade SDL to 2.28.4 in Windows releases
- Upgrade platform-tools to 34.0.5 (adb) in Windows releases
- Various technical fixes

* Mon Jul 17 2023 Udo Seidel <udoseidel@gmx.de> 2.1.1-1
- Ignore fold change events for other display ids (#4120)
- Fix Meizu deadlock (#4143, #4146)
- Fix possible division by zero (#4115)
- Increase attempts to start AudioRecord (#4147)

* Thu Jun 22 2023 Udo Seidel <udoseidel@gmx.de> 2.1-1
- Add --no-video to mirror audio only (#3978 [github.com])
- Add option to select the device microphone as audio source (#4044 [github.com])
- Rename --no-display to --no-playback (#4033 [github.com])
- Add --no-video-playback and --no-audio-playback (#4033 [github.com])
- Add --time-limit to automatically stop after a given delay (#3752 [github.com], #4052 [github.com])
- Add option to change the audio output buffer size (#3793 [github.com])
- Add option to kill adb on close (#205 [github.com], #2580 [github.com], #4049 [github.com])
- Support dynamic device folding (#3960 [github.com], #3979 [github.com])
- Use OpenGL 3.0+ on macOS to support trilinear filtering (#3895 [github.com])
- Add (partial) support for Android 14 (#3784 [github.com], #4074 [github.com], #4075 [github.com])
- Improve delay buffer estimation (2f9396e [github.com])
- Fix --tcpip not working in some cases (669e9a8 [github.com])
- Fix audio support for Vivo phones (#3805 [github.com], #3862 [github.com])
- Fix audio support for Honor phones (#4015 [github.com])
- Fix copy-paste on Honor Magic 5 Pro (#3885 [github.com])
- Fix audio capture starting on some Android 11+ devices (#3796 [github.com])
- Fix V4L2 regression (#3795 [github.com])
- Fix support of Nvidia Shield (#3801 [github.com])
- Fix .desktop files for Linux (#3817 [github.com])
- Fix error on device rotation while minimized on Windows (#3947 [github.com])
- Fix extra audio glitches on audio buffer underflow (#4045 [github.com])
- Automatically fix PTS for buggy device encoders (#4054 [github.com])
- Upgrade SDL to 2.28 in Windows releases (#3825 [github.com])
- Update developer documentation (#3811 [github.com])
- Various technical fixes

* Sun Mar 12 2023 Udo Seidel <udoseidel@gmx.de> 2.0-1
- Add Audio forwarding (#14, #3757)
- Add H265 and AV1 video codec support (#3713)
- Add --list-displays and --list-encoders
- Fix clicks on Chrome when --forward-on-clicks is enabled (#3635)
- Retry on spurious encoder error (#3693)
- Make --turn-screen-off work on all displays (#3716)
- Restore resizing workaround for Windows (#3640)
- Upgrade platform-tools to 34.0.1 (adb) in Windows releases
- Upgrade FFmpeg to 6.0 in Windows releases (and use a minimal build)
- Upgrade SDL to 2.26.4 in Windows releases

* Thu Dec 22 2022 Udo Seidel <udoseidel@gmx.de> 1.25-1
- Adapt copy-paste internals for Android 13 (#3497)
- Add support for high-precision scrolling (#3363, #3369)
- Add desktop entry files for Linux (#295, #296, #748, #1636, #3351)
- Add bash and zsh autocompletion for -s/--serial (#3522, #3523)
- Use current adb port (if any) for --tcpip (#3591, #3592)
- Add fallback to get display information on some devices (#3416, #3573)
- Fix click behavior when --forward-all-clicks is set (#3568, #3579)
- Fix support for non-ASCII characters in window title (#2932, #3547)
- Fix getDisplayIds() crash on some versions of Android 13 beta (#3446)
- Upgrade platform-tools to 33.0.3 (adb) in Windows releases
- Upgrade FFmpeg to 5.1.2 in Windows 64-bit releases
- Upgrade SDL to 2.26.1 in Windows releases
- Various technical fixes

* Fri Apr 29 2022 Udo Seidel <udoseidel@gmx.de> 1.24-1
- Adapt input injection for Android 13 (#3186, #3190)
- Add --no-power-on (#3148, #3210)
- Read $ANDROID_SERIAL if no selector is specified (#3111, #3113)
- Consider emulators as TCP/IP devices (-e) (#3137)
- Apply requested window size in OTG mode (#3099, #3219)
- Add specific exit code for device disconnection (#3083, #3085)
- Enable libusb support for Windows 32-bit releases (#3204, #3206)
- Upgrade libusb to 1.0.26 in Windows releases (#3206)
- Upgrade platform-tools to 33.0.1 (adb) in Windows releases (#3206)
- Upgrade SDL to 2.0.22 in Windows releases
- Upgrade FFmpeg to 5.0.1 in Windows 64-bit releases
- Improve some error messages
- Various technical fixes

* Wed Feb 23 2022 Udo Seidel <udoseidel@gmx.de> 1.23-1
- Add HID/OTG support for Windows (--otg only) (#2773, #3011)
- Add HID/OTG support for macOS (#2774, #3031)
- Improve device selection (list devices, -d, -e) (#3005)
- Downscale and retry on MediaCodec error in more cases (#2990, #3043)
- Add ZSH completion script (#3012)
- Add Bash completion script (#2930, #3048)
- Add --no-cleanup option (#1764, #3020)
- Add --printf-fps (#468, #3030)
- Print both compiled and linked version of libs on --version
- Fix FPS counter (broken in v1.22)
- Various technical refactors and fixes

* Sun Nov 14 2021 zeno <zeno@bafh.org> 1.20-3
- fix runtime dependencies
