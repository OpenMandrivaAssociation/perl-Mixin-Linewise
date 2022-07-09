%define upstream_name    Mixin-Linewise
%define upstream_version 0.110

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Get linewise writers for strings and filenames
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Mixin::Linewise
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Mixin-Linewise-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With the Mixin::Linewise::Readers
manpage and the Mixin::Linewise::Writers manpage, you can just write a
method to handle handles, and methods for handling strings and filenames
are added for you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*
