Name:           rpmfusion-free-obsolete-packages
Version:        28
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
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Nicolas Chauvet <kwizart@gmail.com> - 28-1
- Initial spec file
