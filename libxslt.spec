Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Name:		libxslt
Version:	1.0.1
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
URL:		http://xmlsoft.org/XSLT/
Requires:	libxml2 >= 2.4.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.4.1
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%package devel
Summary:	Development libraries and header files of libxslt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
Development libraries and header files of libxslt - XSLT processor.

%package static
Summary:	Static libraries of libxslt
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description static
Static libraries of libxslt - XSLT processor.

%package progs
Summary:	XSLT processor
Summary(pl):	Procesor styli XSLT
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Development/Librairies
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description progs
XSLT processor.

%description -l pl progs
Procesor styli XSLT.

%prep
%setup  -q

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/{*.{gif,html},html/*}
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xslt-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/libxslt

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsltproc
