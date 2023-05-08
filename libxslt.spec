#
# Conditional build:
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module
%bcond_without	static_libs	# static library
%bcond_with	tests		# test suite

%define		libxml2ver	1:2.6.30
Summary:	XSLT processor
Summary(pl.UTF-8):	Procesor XSLT
Summary(pt_BR.UTF-8):	Biblioteca que disponibiliza o sistema XSLT do GNOME
Name:		libxslt
Version:	1.1.38
Release:	1
License:	MIT
Group:		Libraries
#Source0:	ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
Source0:	https://download.gnome.org/sources/libxslt/1.1/%{name}-%{version}.tar.xz
# Source0-md5:	7d6e43db810177ddf9818ef394027019
Patch0:		%{name}-m4.patch
Patch1:		LFS.patch
Patch2:		%{name}-libs-no-libdir.patch
URL:		http://xmlsoft.org/XSLT/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.16.3
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxml2-devel >= %{libxml2ver}
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python >= 2
BuildRequires:	python-devel >= 2
BuildRequires:	python-libxml2 >= %{libxml2ver}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-libxml2 >= %{libxml2ver}
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libgcrypt >= 1.1.42
Requires:	libxml2 >= %{libxml2ver}
Obsoletes:	libxslt1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%description -l pl.UTF-8
Biblioteka do przetwarzania XSLT.

%description -l pt_BR.UTF-8
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT. O comando xsltproc é uma interface em
linha de comandos para o mecanismo XSLT.

%package devel
Summary:	Header files for libxslt
Summary(pl.UTF-8):	Pliki nagłówkowe libxslt
Summary(pt_BR.UTF-8):	Bibliotecas, includes, etc. para incluir o mecanismo XSLT do GNOME
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.1.42
Requires:	libxml2-devel >= %{libxml2ver}
Obsoletes:	libxslt1-devel

%description devel
Header files for libxslt - XSLT processor.

%description devel -l pl.UTF-8
Pliki nagłówkowe procesora XSLT.

%description devel -l pt_BR.UTF-8
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT.

%package static
Summary:	Static libraries of libxslt
Summary(pl.UTF-8):	Biblioteki statyczne libxslt
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para incluir o mecanismo XSLT do GNOME
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries of libxslt - XSLT processor.

%description static -l pl.UTF-8
Statyczne biblioteki procesora XSLT.

%description static -l pt_BR.UTF-8
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT. Estas são as bibliotecas em sua versão
estática.

%package apidocs
Summary:	API documentation for libxslt library
Summary(pl.UTF-8):	Dokumentacja API bibliotei libxslt
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libxslt library.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotei libxslt.

%package progs
Summary:	XSLT processor
Summary(pl.UTF-8):	Procesor XSLT
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libxslt-proc

%description progs
XSLT processor.

%description progs -l pl.UTF-8
Procesor XSLT.

%package -n python-%{name}
Summary:	Python 2 support for libxslt
Summary(pl.UTF-8):	Moduły języka Python 2 dla biblioteki libxslt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libxml2 >= %{libxml2ver}
Requires:	python-modules
Obsoletes:	libxslt-python < 1.1

%description -n python-%{name}
Python 2 support for libxslt.

%description -n python-%{name} -l pl.UTF-8
Moduły języka Python 2 dla biblioteki libxslt.

%package -n python3-%{name}
Summary:	Python 3 support for libxslt
Summary(pl.UTF-8):	Moduły języka Python 3 dla biblioteki libxslt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libxml2 >= %{libxml2ver}
Requires:	python3-modules >= 1:3.2

%description -n python3-%{name}
Python 3 support for libxslt.

%description -n python3-%{name} -l pl.UTF-8
Moduły języka Python 3 dla biblioteki libxslt.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's,\$(datadir)/gtk-doc/html,%{_gtkdocdir},' \
	doc/devhelp/Makefile.am doc/EXSLT/devhelp/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{with python3}
install -d build-python3
cd build-python3
../%configure \
	PYTHON=%{__python3} \
	ac_cv_header_xlocale_h=no \
	--disable-silent-rules \
	--disable-static \
	--with-plugins

%{__make}
cd ..
%endif

install -d build
cd build
../%configure \
	ac_cv_header_xlocale_h=no \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-plugins \
	%{!?with_python2:--without-python}
%{__make}

%{?with_tests:%{__make} -C tests test}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%{__make} -C build-python3 install \
	DESTDIR=$RPM_BUILD_ROOT \
	exampledir=%{_examplesdir}/python3-%{name}-%{version}

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/*.la
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	exampledir=%{_examplesdir}/python-%{name}-%{version}

# junk (files to configure libxslt itself, not cmake export files)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmake/libxslt/{FindGcrypt,libxslt-config}.cmake

%if %{with python2}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.a
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Copyright FEATURES NEWS README.md TODO
%attr(755,root,root) %{_libdir}/libexslt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexslt.so.0
%attr(755,root,root) %{_libdir}/libxslt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxslt.so.1
%dir %{_libdir}/libxslt-plugins

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xslt-config
%attr(755,root,root) %{_libdir}/libexslt.so
%attr(755,root,root) %{_libdir}/libxslt.so
%{_libdir}/libexslt.la
%{_libdir}/libxslt.la
%attr(755,root,root) %{_libdir}/xsltConf.sh
%{_includedir}/libexslt
%{_includedir}/libxslt
%{_pkgconfigdir}/libexslt.pc
%{_pkgconfigdir}/libxslt.pc
%{_aclocaldir}/libxslt.m4
%{_mandir}/man3/libexslt.3*
%{_mandir}/man3/libxslt.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexslt.a
%{_libdir}/libxslt.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/libxslt
%{_gtkdocdir}/libexslt
%{_gtkdocdir}/libxslt

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1*

%if %{with python2}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/libxsltmod.so
%{py_sitescriptdir}/libxslt.py[co]
%{_examplesdir}/python-%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/libxsltmod.so
%{py3_sitescriptdir}/libxslt.py
%{py3_sitescriptdir}/__pycache__/libxslt.cpython-*.py[co]
%{_examplesdir}/python3-%{name}-%{version}
%endif
