Name:           rpmfusion-free-obsolete-packages
Version:        32
Release:        2%{?dist}
Summary:        A package to obsolete retired packages from rpmfusion-free

License:        MIT
URL:            http://rpmfusion.org
Source0:        README
BuildArch:      noarch


# Last build gnome-mplayer = 1.0.9-3.20150203svn2476.fc22
Provides: gnome-mplayer = 1.0.9-4
Obsoletes: gnome-mplayer < 1.0.9-4
Provides: gnome-mplayer-common = 1.0.9-4
Obsoletes: gnome-mplayer-common < 1.0.9-4
# Last build gmtk = 1.0.9-2.fc22
Provides: gmtk = 1.0.9-3
Obsoletes: gmtk < 1.0.9-3
# Last build dvdrip-0.98.11-15.fc27
Provides: dvdrip = 0.98.11-16
Obsoletes: dvdrip < 0.98.11-16
# Last build transcode-1.1.7-22.fc27
Provides: transcode = 1.1.7-23
Obsoletes: transcode < 1.1.7-23
# Last build DVDAuthorWizard-1.4.6-12.fc28
Provides: DVDAuthorWizard = 1.4.6-13
Obsoletes: DVDAuthorWizard < 1.4.6-13
# Last build DVDRipOMatic-0.95-15.fc28
Provides: DVDRipOMatic = 0.95-16
Obsoletes: DVDRipOMatic < 0.95-16
# Last build m2vmp2cut-0.86-8.fc28
Provides: m2vmp2cut = 0.86-9
Obsoletes: m2vmp2cut < 0.86-9
# Last build subtitleripper-0.3-11.fc28
Provides: subtitleripper = 0.3-12
Obsoletes: subtitleripper < 0.3-12
# Last build gmediafinder-1.5.1-10.694694c.fc28
Provides: gmediafinder = 1.5.1-11.694694c
Obsoletes: gmediafinder < 1.5.1-11.694694c
# Last build ffmpeg-compat-0.6.7-10.fc26
Provides: ffmpeg-compat = 0.6.7-11
Obsoletes: ffmpeg-compat < 0.6.7-11
# Last build freetype-freeworld-2.9.1-1.fc30
Provides: freetype-freeworld = 2.9.1-2
Obsoletes: freetype-freeworld < 2.9.1-2
# Last build libtxc_dxtn-1.0.1-3.gitef072983.fc27
Provides: libtxc_dxtn = 1.0.1-4
Obsoletes: libtxc_dxtn < 1.0.1-4
# Last build k9copy-3.0.3-7.fc29
Provides: k9copy = 3.0.3-8
Obsoletes: k9copy < 3.0.3-8
# Last build kplayer-0.7.2-4.fc29
Provides: kplayer = 0.7.2-5
Obsoletes: kplayer < 0.7.2-5
# Last build yle-dl-2.26-6.fc30
Provides: yle-dl = 2.26-7
Obsoletes: yle-dl < 2.26-7
# Last build gstreamer-ffmpeg-0.10.13-22.fc31
Provides: gstreamer-ffmpeg = 0.10.13-23
Obsoletes: gstreamer-ffmpeg < 0.10.13-23
# Last build gstreamer-plugins-bad-0.10.23-13.fc31
Provides: gstreamer-plugins-bad = 0.10.23-14
Obsoletes: gstreamer-plugins-bad < 0.10.23-14
# Last build gstreamer-plugins-ugly-0.10.19-33.fc31
Provides: gstreamer-plugins-ugly = 0.10.19-34
Obsoletes: gstreamer-plugins-ugly < 0.10.19-34
# Last build gxine-0.5.910-5.fc31
Provides: gxine = 0.5.910-6
Obsoletes: gxine < 0.5.910-6
# Last build python2-vlc-3.0.6109-0.4.20190508git949d19e.fc32
Provides: python2-vlc = 3.0.6109-1
Obsoletes: python2-vlc < 3.0.6109-1
# Last build wireguard-kmod-0.0.20191219-2.fc32
Provides: akmod-wireguard = 0.0.20191219-3
Obsoletes: akmod-wireguard < 0.0.20191219-3
Provides: kmod-wireguard = 0.0.20191219-3
Obsoletes: kmod-wireguard < 0.0.20191219-3
# Last build wireguard-0.0.20191219-2.fc32
Provides: wireguard-kmod-common = 0.0.20191219
Provides: wireguard = 0.0.20191219-3
Obsoletes: wireguard < 0.0.20191219-3

%description
This package exists only to obsolete other packages which need to be removed
from the RPM Fusion free for some reason.

%prep
cp -p %{SOURCE0} .

%build
# Nothing to build

%install
# Nothing to install


%files
%doc README

%changelog
* Tue Apr 14 2020 Nicolas Chauvet <kwizart@gmail.com> - 32-2
- Add missing wireguard-kmod-common

* Fri Mar 27 2020 Leigh Scott <leigh123linux@gmail.com> - 32-1
- Bump version to 32
- Add wireguard

* Wed Mar 11 2020 Leigh Scott <leigh123linux@gmail.com> - 31-3
- Add python2-vlc

* Sat Aug 24 2019 Leigh Scott <leigh123linux@gmail.com> - 31-2
- Add gxine

* Fri Aug 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 31-1
- Bump version to 31
- Add gstreamer-ffmpeg, gstreamer-plugins-bad, gstreamer-plugins-ugly

* Mon Apr 08 2019 Leigh Scott <leigh123linux@googlemail.com> - 30-1
- Bump version to 30

* Mon Apr 08 2019 Leigh Scott <leigh123linux@googlemail.com> - 29-4
- Add k9copy, kplayer and yle-dl

* Tue Dec 11 2018 Nicolas Chauvet <kwizart@gmail.com> - 29-3
- Add libtxc_dxtn

* Wed Oct 31 2018 Leigh Scott <leigh123linux@googlemail.com> - 29-2
- Add freetype-freeworld

* Sun Jul 29 2018 Nicolas Chauvet <kwizart@gmail.com> - 29-1
- Add ffmpeg-compat - rhbz#4952

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 28-4
- Add gmediafinder (rfbz #4862)

* Mon Apr 09 2018 Leigh Scott <leigh123linux@googlemail.com> - 28-3
- Add transcode, DVDAuthorWizard, DVDRipOMatic, m2vmp2cut and subtitleripper

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Nicolas Chauvet <kwizart@gmail.com> - 28-1
- Initial spec file
