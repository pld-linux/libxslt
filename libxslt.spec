Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Summary(pt_BR):	Biblioteca que disponibiliza o sistema XSLT do Gnome
Name:		libxslt
Version:	1.0.8
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_debuger.patch
URL:		http://xmlsoft.org/XSLT/
Requires:	libxml2 >= 2.4.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.4.10
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%description -l pt_BR
Esta biblioteca C permite a transformaÁ„o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr„o de
transformaÁ„o dos estilos XSLT. O comando xsltproc È uma interface em
linha de comandos para o mecanismo XSLT.

%package devel
Summary:	Development libraries and header files of libxslt
Summary(pt_BR):	Bibliotecas, includes, etc. para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Development libraries and header files of libxslt - XSLT processor.

%description -l pt_BR devel
Esta biblioteca C permite a transformaÁ„o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr„o de
transformaÁ„o dos estilos XSLT.

%package static
Summary:	Static libraries of libxslt
Summary(pt_BR):	Bibliotecas est·ticas para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libraries of libxslt - XSLT processor.

%description -l pt_BR static
Esta biblioteca C permite a transformaÁ„o de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padr„o de
transformaÁ„o dos estilos XSLT. Estas s„o as bibliotecas em sua vers„o
est·tica.

%package progs
Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Development/Librairies
Group(pl):	Aplikacje/Tekst
Requires:	%{name} = %{version}

%description progs
XSLT processor.

%description -l pl progs
Procesor XSLT.

%prep
%setup  -q
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
