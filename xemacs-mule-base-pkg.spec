Summary:	Basic Mule support, required for building with Mule
Summary(pl.UTF-8):	Podstawowa obsługa Mule, wymagana do budowania z Mule
Name:		xemacs-mule-base-pkg
%define 	srcname	mule-base
Version:	1.56
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	71ee0c546df792727c602157f561b218
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
Requires:	xemacs-apel-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic Mule support, required for building with Mule.

%description -l pl.UTF-8
Podstawowa obsługa Mule, wymagana do budowania z Mule.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/mule-base/ChangeLog
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
