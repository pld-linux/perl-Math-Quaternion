#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Quaternion
Summary:	Math::Quaternion - Perl class to represent quaternions
Summary(pl.UTF-8):	Math::Quaternion - klasa Perla do reprezentowania kwaternionów
Name:		perl-Math-Quaternion
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	818e88923c99053f26317acd4c61adfd
URL:		http://search.cpan.org/dist/Math-Quaternion/
%{?with_tests:BuildRequires:	perl-Test-Simple}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package lets you create and manipulate quaternions. A quaternion
is a mathematical object developed as a kind of generalization of
complex numbers, usually represented by an array of four real numbers,
and is often used to represent rotations in three-dimensional space.

%description -l pl.UTF-8
Ten pakiet pozwala na tworzenie oraz wykorzystywanie kwaternionów w
obliczeniach. Kwaternion to obiekt matematyczny wymyślony jako rodzaj
uogólnienia liczb zespolonych, zazwyczaj reprezentowany jako tablica
czterech liczb rzeczywistych, często używany do reprezentowania
obrotów w przestrzeni trójwymiarowej.

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
%doc Changes
%{perl_vendorlib}/Math/Quaternion.pm
%{_mandir}/man3/*
