%include	/usr/lib/rpm/macros.python
%define		zope_subname	CPSSkins
%define		sub_ver	b2
Summary:	Theme creation and management product for CMF, Plone, CPS3
Summary(pl):	Kreator i zarz±dca "skórek" dla CMF, Plone, CPS3
Name:		Zope-%{zope_subname}
Version:	1.9
Release:	1.%{sub_ver}.1
License:	GPL
Group:		Development/Tools
Source0:	http://www.medic.chalmers.se/~jmo/CPS/%{zope_subname}%{version}%{sub_ver}.tgz
# Source0-md5:	aee05832b5d2c4ad2959666293b818f3
URL:		http://www.medic.chalmers.se/~jmo/CPS/
Requires(post,postun):	/usr/sbin/installzopeproduct
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMF
Requires:	Zope-CMFPlone
Requires:	Zope-CMFPortalContentFolder
Requires:	Zope-TranslationService
Requires:	Zope-Localizer
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

cp -af Products/%{zope_subname}/{Extensions,Install,Misc,html,i18n,icons,skins,tests,zmi,*.py,*.gif,version.txt,refresh.txt} \
    $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        /usr/sbin/installzopeproduct -d %{zope_subname}
        if [ -f /var/lock/subsys/zope ]; then
                /etc/rc.d/init.d/zope restart >&2
        fi
fi

%files
%defattr(644,root,root,755)
%doc Products/%{zope_subname}/{doc/*,AUTHORS.TXT,COPYRIGHT.TXT,CREDITS.TXT,INSTALL.TXT,README.TXT}
%{_datadir}/%{name}
