
%include	/usr/lib/rpm/macros.python

Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Summary(pt_BR):	Biblioteca que disponibiliza o sistema XSLT do Gnome
Name:		libxslt
Version:	1.0.11
Release:	1
License:	MIT
Group:		Libraries
Group(cs):	Knihovny
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://xmlsoft.org/%{name}-%{version}.tar.gz
URL:		http://xmlsoft.org/XSLT/
Requires:	libxml2 >= 2.4.14
Requires:	python-libxml2 >= 2.4.14
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2.4.14
BuildRequires:	python-libxml2 >= 2.4.14
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for XSLT processing.

%description -l pt_BR
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT. O comando xsltproc é uma interface em
linha de comandos para o mecanismo XSLT.

%package devel
Summary:	Development libraries and header files of libxslt
Summary(pt_BR):	Bibliotecas, includes, etc. para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Group(cs):	Vıvojové prostøedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Development libraries and header files of libxslt - XSLT processor.

%description -l pt_BR devel
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT.

%package static
Summary:	Static libraries of libxslt
Summary(pt_BR):	Bibliotecas estáticas para incluir o mecanismo XSLT do Gnome
Group:		Development/Libraries
Group(cs):	Vıvojové prostøedky/Knihovny
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static libraries of libxslt - XSLT processor.

%description -l pt_BR static
Esta biblioteca C permite a transformação de arquivos XML em outros
arquivos XML (ou HTML, texto, ...) usando o mecanismo padrão de
transformação dos estilos XSLT. Estas são as bibliotecas em sua versão
estática.

%package progs
Summary:	XSLT processor
Summary(pl):	Procesor XSLT
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(de):	Anwendungen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥Æ¥­¥¹¥È
Group(pl):	Aplikacje/Tekst
Group(pt):	Aplicações/Texto
Group(ru):	ğÒÉÌÏÖÅÎÉÑ/òÁÂÏÔÁ Ó ÔÅËÓÔÁÍÉ
Requires:	%{name} = %{version}

%description progs
XSLT processor.

%description -l pl progs
Procesor XSLT.

%package -n python-%{name}
Summary:	Python support for libxslt
Summary(pl):	Modu³y jêzyka Python dla biblioteki libxslt
Group:		Development/Languages/Python
Group(cs):	Vıvojové prostøedky/Programovací jazyky/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguajes/Python
Group(fr):	Development/Langues/Python
Group(ja):	³«È¯/¸À¸ì/Python
Group(pl):	Programowanie/Jêzyki/Python
Group(pt):	Desenvolvimento/Linguagens/Python
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Python
%requires_eq	python

%description -n python-%{name}
Python support for libxslt.

%description -n python-%{name} -l pl
Modu³y jêzyka Python dla biblioteki libxslt.

%prep
%setup  -q

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

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
