#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Template
%define	pnam	Timer
Summary:	Template::Timer - Rudimentary profiling for Template Toolkit
Summary(pl):	Template::Timer - podstawowe profilowanie dla Template Toolkitu
Name:		perl-Template-Timer
Version:	0.02
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7c988a054c71835d28ecd089c890e1be
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template::Timer provides inline timings of the template processing
throughout your code. It's an overridden version of Template::Context
that wraps the process() and include() methods.

%description -l pl
Template::Timer udostêpnia mierzenie czasu przetwarzania kodu. Jest
to przeci±¿ona wersja klasy Template::Context przechwytuj±ca metody
process() i include().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Template/*.pm
%{_mandir}/man3/*
