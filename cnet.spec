Summary:	A Network Simulator
Summary(pl):	Symulator sieci
Name:		cnet
Version:	2.0.9
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.csse.uwa.edu.au/cnet/%{name}-%{version}.tgz
# Source0-md5:	593b63c809773a284bc3d655dc609298
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-longint.patch
Patch2:		%{name}-amd64fix.patch
URL:		http://www.csse.uwa.edu.au/cnet
BuildRequires:	elfutils-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define no_install_post_strip 1

%description
The cnet network simulator enables experimentation with various
data-link layer, network layer, routing and transport layer networking
protocols in networks consisting of any combination of point-to-point
links and Ethernet segments. cnet has been specifically developed for,
and is used in, undergraduate computer networking courses taken by
thousands of students worldwide since 1991. At The University of
Western Australia, cnet is used primarily in Chris McDonald's Computer
Networks (IT312) undergraduate unit.

%description
Symulator sieci cnet umo�liwia eksperymenty z r�nymi rodzajami warstw
fizycznych, sieciowych, routingi i transportowych protoko��w, w r�nych
kombinacjach link�w point-to-point, segment�w ethernet. cnet jest
tworzony i wykorzystywany w wielu kursach sieciowych pobieranych przez
tysi�ce student�w od roku 1991.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
%{__make} \
	BINDIR=%{_bindir} \
	CNETDIR=%{_datadir}/cnet \
	MANDIR=%{_mandir}/man1 \
	CFLAGS="%{rpmcflags} -fPIC" \
	ANSICC="%{__cc} -ansi" \
	LIBELFDIR="" \
	LIBELFINC=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_libdir},%{_mandir}/man1,%{_examplesdir}}
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	CNETDIR=$RPM_BUILD_ROOT%{_datadir}/cnet \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 

cp -r EXAMPLES $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE DOC
%attr(755,root,root) %{_bindir}/cnet
%{_datadir}/cnet
%{_mandir}/man1/cnet.*
%{_examplesdir}/%{name}
