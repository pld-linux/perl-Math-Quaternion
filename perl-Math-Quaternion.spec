#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Quaternion
Summary:	Math::Quaternion - Perl class to represent quaternions
Summary(pl):	Math::Quaternion - klasa Perla do reprezentowanai kwaternionów
Name:		perl-Math-Quaternion
Version:	0.01
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	afb5a960eb511d572a323608c42d7b11
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%{!?_without_tests:BuildRequires:	perl-Test-Simple}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(anything_fake_or_conditional)"

%description
This package lets you create and manipulate quaternions. A
quaternion is a mathematical object developed as a kind of
generalization of complex numbers, usually represented by an array
of four real numbers, and is often used to represent rotations in
three-dimensional space.

%description -l pl
Ten pakiet pozwala na tworzenie oraz wykorzystywanie kwaternionów w
obliczeniach. Kwaternion to obiekt matematyczny wymy¶lony jako rodzaj
uogólnienia liczb zespolonych, zazwyczaj reprezentowany jako tablica
czterech liczb rzeczywistych, czêsto u¿ywany do reprezentowania
obrotów w przestrzeni trójwymiarowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/Quaternion.pm
%{_mandir}/man3/*
