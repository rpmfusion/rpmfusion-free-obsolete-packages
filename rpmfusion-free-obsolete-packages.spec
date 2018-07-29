Name:           rpmfusion-free-obsolete-packages
Version:        29
Release:        1%{?dist}
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
