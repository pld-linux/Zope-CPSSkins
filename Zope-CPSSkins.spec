%define		zope_subname	CPSSkins
# %%define		sub_ver	rc5
Summary:	Theme creation and management product for CMF, Plone, CPS3
Summary(pl):	Kreator i zarz±dca "skórek" dla CMF, Plone, CPS3
Name:		Zope-%{zope_subname}
Version:	2.7.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://mc.ptja.pl/%{zope_subname}%{version}.tar.gz
# Source0-md5:	2408c3693f83223922a5438756960600
URL:		http://www.medic.chalmers.se/~jmo/CPS/
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
Requires:	Zope-OrderedFolderSupportPatch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	CMF
Conflicts:	Plone

%description
CPSSkins is theme creation and management product for CMF, Plone,
CPS3.

%description -l pl
CPSSkins jest kreatorem i zarz±dc± "skórek" dla CMF, Plone, CPS3.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af Products/%{zope_subname}/{Extensions,Install,i18n,icons,skins,tests,zmi,*.py,*.png,version.txt,refresh.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc Products/%{zope_subname}/{doc/*,AUTHORS.TXT,CHANGES,CO*.TXT,CREDITS.TXT,HISTORY,INSTALL.TXT,README.TXT,UPGRADE.TXT,TODO}
%{_datadir}/%{name}
