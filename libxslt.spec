#
# Conditional build:
%bcond_without	python		# don't build python binding
%bcond_without	static_libs	# don't build static library
%bcond_with	tests		# run test suite

%define		libxml2ver	1:2.6.30
Summary:	XSLT processor
Summary(pl.UTF-8):	Procesor XSLT
Summary(pt_BR.UTF-8):	Biblioteca que disponibiliza o sistema XSLT do GNOME
Name:		libxslt
Version:	1.1.28
Release:	6
License:	MIT
Group:		Libraries
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxslt/1.1/%{name}-%{version}.tar.bz2
Source0:	ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
# Source0-md5:	9667bf6f9310b957254fdcf6596600b7
Patch0:		%{name}-m4.patch
Patch1:		LFS.patch
URL:		http://xmlsoft.org/XSLT/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libxml2-devel >= %{libxml2ver}
BuildRequires:	perl-base
%if %{with python}
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-libxml2 >= %{libxml2ver}
%endif
BuildRequires:	rpm-pythonprov
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
Summary:	Python support for libxslt
Summary(pl.UTF-8):	Moduły języka Python dla biblioteki libxslt
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-libxml2 => %{libxml2ver}
%pyrequires_eq	python-modules
Obsoletes:	libxslt-python

%description -n python-%{name}
Python support for libxslt.

%description -n python-%{name} -l pl.UTF-8
Moduły języka Python dla biblioteki libxslt.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-plugins \
	%{!?with_python:--without-python}
%{__make}

%{?with_tests:%{__make} -C tests test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
# move examples to proper dir
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-python-%{version}/examples/* \
  $RPM_BUILD_ROOT%{_examplesdir}/python-%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-python-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.{py,la,a}
%endif

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright FEATURES NEWS README TODO
%attr(755,root,root) %{_libdir}/libexslt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexslt.so.0
%attr(755,root,root) %{_libdir}/libxslt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxslt.so.1
%dir %{_libdir}/libxslt-plugins

%files devel
%defattr(644,root,root,755)
%doc doc/{*.{gif,html},html}
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

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1*

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/libxsltmod.so
%{py_sitedir}/libxslt.py[co]
%{_examplesdir}/python-%{name}-%{version}
%endif
