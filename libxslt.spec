%include	/usr/lib/rpm/macros.python

%define		libxml2ver	2.4.16

Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Summary(pt_BR):	Biblioteca que disponibiliza o sistema XSLT do Gnome
Name:		libxslt
Version:	1.0.12
Release:	1
License:	MIT
Group:		Libraries
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-exeext.patch
URL:		http://xmlsoft.org/XSLT/
Requires:	libxml2 >= %{libxml2ver}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= %{libxml2ver}
BuildRequires:	python-libxml2 >= %{libxml2ver}
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%description -l pl
Biblioteka do przetwarzania XSLT.

%description -l pt_BR
Esta biblioteca C permite a transforma��o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr�o de
transforma��o dos estilos XSLT. O comando xsltproc � uma interface em
linha de comandos para o mecanismo XSLT.

%package devel
Summary:	Development libraries and header files of libxslt
Summary(pt_BR):	Bibliotecas, includes, etc. para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development libraries and header files of libxslt - XSLT processor.

%description devel -l pl
Pliki nag��wkowe i biblioteki developerskie procesora XSLT.

%description devel -l pt_BR
Esta biblioteca C permite a transforma��o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr�o de
transforma��o dos estilos XSLT.

%package static
Summary:	Static libraries of libxslt
Summary(pt_BR):	Bibliotecas est�ticas para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries of libxslt - XSLT processor.

%description static -l pl
Statyczne biblioteki procesora XSLT.

%description static -l pt_BR
Esta biblioteca C permite a transforma��o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr�o de
transforma��o dos estilos XSLT. Estas s�o as bibliotecas em sua vers�o
est�tica.

%package progs
Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs
XSLT processor.

%description progs -l pl
Procesor XSLT.

%package -n python-%{name}
Summary:	Python support for libxslt
Summary(pl):	Modu�y j�zyka Python dla biblioteki libxslt
Group:		Development/Languages/Python
Requires:	python-libxml2 = %{libxml2ver}
%requires_eq	python

%description -n python-%{name}
Python support for libxslt.

%description -n python-%{name} -l pl
Modu�y j�zyka Python dla biblioteki libxslt.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
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
%{_includedir}/libexslt

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsltproc

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
