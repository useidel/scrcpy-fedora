%define         pkgname         scrcpy
%global         forgeurl        https://github.com/Genymobile/%{pkgname}
Version:        2.1

%forgemeta -i

Name:           %{pkgname}
Release:        1%{?dist}
Summary:        Display and control your Android device
License:        ASL 2.0

URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        https://github.com/Genymobile/%{pkgname}/releases/download/v%{version}/%{pkgname}-server-v%{version}

BuildRequires:  meson gcc
BuildRequires:  java-devel >= 11

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
%doc README.md DEVELOP.md FAQ.md
%{_bindir}/%{pkgname}
%{_datadir}/%{pkgname}
%{_mandir}/man1/%{pkgname}.1*
%{_datadir}/icons/hicolor/*/apps/%{pkgname}.png
%{_datadir}/bash-completion/completions/%{pkgname}
%{_datadir}/zsh/site-functions/_%{pkgname}
%{_datadir}/applications/%{pkgname}*.desktop


%changelog
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
