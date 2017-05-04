%define octpkg octgpr

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Gaussian Process Regression support for Octave
Name:		octave-%{octpkg}
Version:	1.2.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The package allows interpolating and smoothing scattered multidimensional
data using Gaussian Process Regression (also known as Kriging). Projected
Gaussian Process regression is also experimentally supported.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

